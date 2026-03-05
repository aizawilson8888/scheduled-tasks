import requests
import os
from twilio.rest import Client

OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "f59c744d21e08efe39d377c7f0ea7ae5"
account_sid = os.environ.get("ACC_SID")
auth_token = os.environ.get("AUTH_TOKEN")

weather_params = {
    "lat": "39.006779",
    "lon": "-76.779137",
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data)

weather_id = weather_data["list"][0]["weather"][0]["id"]

will_rain = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        content_sid='HX612f9001845268c94ae17fbbd2ac91a4',
        to='whatsapp:+639192802432'
    )
    print(message.status)
