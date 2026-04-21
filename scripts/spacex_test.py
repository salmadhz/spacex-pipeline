import requests
url = "https://api.spacexdata.com/v4/launches"
response = requests.get(url)
status = response.status_code
launches = response.json()
launches_count = len(launches)
print("total number of launches = ", launches_count)
