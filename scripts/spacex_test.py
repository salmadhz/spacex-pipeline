import requests
url = "https://api.spacexdata.com/v4/launches"
response = requests.get(url)
status = response.status_code
launches = response.json()
launches_count = len(launches)

#print(launches[0])

print("total number of launches = ", launches_count)
success_count = 0
for launch in launches:
	if launch["success"]:
		success_count += 1
print("total success rate =", success_count)
print("total failure rate =", launches_count - success_count)
###########################
selected_year = input("Enter your selected year: ")
year_count = 0
success_rate = 0
failure_rate = 0
for launch in launches:
	year = launch["date_utc"][0:4]
	if year == selected_year :
		year_count += 1
		if launch["success"]:
			success_rate +=1
		else:
			failure_rate +=1
print("the total number of launches at ", selected_year, "is", year_count)
print("success count at ", selected_year, " = ", success_rate)
print("failure count at ", selected_year, " = ", failure_rate)
##########################

