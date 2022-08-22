import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

iss_position(longitude, latitude)

print(iss_position)


# https://www.latlong.net/Show-Latitude-Longitude.html

#print(response.status_code)

#if response.status_code != 200:
    #raise Exception("Bad response from ISS API")

#if response.status_code == 404:
    #raise Exception("That resource not exist.")
#elif response.status_code == 401:
    #raise Exception("you are not authorized to access this data.")

