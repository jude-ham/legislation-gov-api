import requests

response = requests.get("https://www.legislation.gov.uk/ukpga/1998/46/data.pdf")

print(response.status_code)
# print(response.content)

file = open("Act.pdf", "wb")

file.write(response.content)

file.close()

# THIS CODE WORKS
# thank fuck, change the link to the respective act's pdf to download it to the "act.pdf" file