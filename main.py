# import requests module
import requests

# Making a get request
response = requests.get("https://api.github.com/")

status_code = response.status_code
print("Status Code:", status_code)

# Store JSON data in API_Data
API_Data = response.json()
print(API_Data)

# Print json data using loop
for key in API_Data:
    {print(key, ":", API_Data[key])}
