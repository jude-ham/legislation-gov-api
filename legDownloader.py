import requests
import time

counter = 0
fileName = "default.fail" # if a file is created called this, something's gone seriously wrong
fileCounterInt = 1
fileCounterStr = ""
legYear = ""
legType = ""
legTypeChoice = ""
noMoreLeg = False
# response = requests.get("https://www.legislation.gov.uk/ukpga/1998/46/data.pdf")

choices = """1 for UK Public General Acts
2 for Acts of the Senedd Cymru
3 for Acts of the Scottish Parliament
4 for Acts of the Northern Ireland Assembly
Or, enter 0 to choose an alternative, using a custom argument (not recommended, untested)"""
print(choices)

legTypeChoice = input("What legislature do you want to use? ")
if legTypeChoice == "1":
    legType = "ukpga"
elif legTypeChoice == "2":
    legtype = "asc"
    print("currently very broken and untested")
elif legTypeChoice == "3":
    legtype = "asp"
    print("i've somehow broken scotland as well ffs")
elif legTypeChoice == "4":
    legtype = "nia"
    print("don't event think about complaining if this doesn't work, not got round to looking at NI yet")
else:
    legtype = input("What arugment do you want to use? ")
legYear = input("What year would you like to download? ")

# while response.status_code == 200:

while noMoreLeg == False:
    fileCounterStr = str(fileCounterInt)
    response = requests.get("https://www.legislation.gov.uk/" + legType + "/" + legYear + "/" + fileCounterStr + "/data.pdf")

    print(response.status_code)

    if response.status_code == 202:
        print("File " + legType + " " + legYear + " " + fileCounterStr + " has been requested. Please try again in at least 10 seconds.")
        exit()
    
    if response.status_code == 400:
        print("All legislation from " + legYear + " has been downloaded successfully.")
        exit()

    if response.status_code == 404:
        print("404 Error hit, program will now stop.")
        noMoreLeg = True
        exit()

    fileName = (legYear + " " + legType + " Act " + fileCounterStr + ".pdf")

    file = open(fileName, "wb")

    file.write(response.content)

    file.close()

    fileCounterInt = fileCounterInt + 1
    # counter = counter + 1