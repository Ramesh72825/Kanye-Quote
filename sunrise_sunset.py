import requests
from datetime import datetime


MY_LAT = 26.976368
MY_LNG = 75.750252

def is_iss_overhead():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_lat = float(data["iss_position"]["latitude"])
    iss_lng = float(data["iss_position"]["longtitude"])

    if MY_LAT-5 <= iss_lat <= MY_LAT+5 and MY_LNG-5 <=iss_lng <= MY_LNG+5:
        return True

def is_night():

    parameters = {
        "lat" : MY_LAT,
        "lng" : MY_LNG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

