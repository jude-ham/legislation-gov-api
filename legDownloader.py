import requests
import time

counter = 0
fileName = "default.fail" # if a file is created called this, something's gone wrong
fileCounterInt = 1
fileCounterStr = ""
legYear = 0
response = requests.get("https://www.legislation.gov.uk/ukpga/1998/46/data.pdf")

legYear = int(input("What year would you like to download? "))

# print(response.status_code)
# print(response.content)

# while response.status_code == 200:

while counter != 6:
    fileCounterStr = str(fileCounterInt)
    response = requests.get("https://www.legislation.gov.uk/ukpga/" + str(legYear) + "/" + fileCounterStr + "/data.pdf")
    
    fileName = (str(legYear) + " Act " + fileCounterStr + ".pdf")

    file = open(fileName, "wb")

    file.write(response.content)

    file.close()

    fileCounterInt = fileCounterInt + 1
    counter = counter + 1