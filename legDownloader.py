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

print("""1 for UK Public General Acts (Pre-1988 is currently untested)
2 for Acts of the Senedd Cymru (May 2020 onwards)
3 for Acts of the Scottish Parliament (1999 -  Present)
4 for Acts of the Northern Ireland Assembly (2000 - 2002, 2007 - 2016, 2020 - Present)
Or, enter 0 to choose an alternative, using a custom argument (not recommended, untested)""")

legTypeChoice = input("What legislature do you want to use? ")
if legTypeChoice == "1":
    legType = "ukpga"
elif legTypeChoice == "2":
    legType = "asc"
elif legTypeChoice == "3":
    legType = "asp"
elif legTypeChoice == "4":
    legType = "nia"
else:
    legType = input("What arugment do you want to use? ")
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
        print("Requested link - " + "https://www.legislation.gov.uk/" + legType + "/" + legYear + "/" + fileCounterStr + "/data.pdf")
        noMoreLeg = True
        exit()

    fileName = (legYear + " " + legType + " Act " + fileCounterStr + ".pdf")

    file = open(fileName, "wb")

    file.write(response.content)

    file.close()

    fileCounterInt = fileCounterInt + 1
    # counter = counter + 1