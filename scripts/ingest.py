import requests

def fetch_launches():
	url ="https://api.spacexdata.com/v4/launches" 
	try:
		response = requests.get(url)
		launches = response.json()
		return launches
	except requests.exceptions.RequestException as e:
		print(f"Error fetching data: {e}")
		return []

if __name__ == "__main__":
    data = fetch_launches()
    print(f"Fetched {len(data)} launches")
