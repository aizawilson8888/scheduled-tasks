import requests
import os
from twilio.rest import Client

OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("API_KEY")
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
        content_sid='HX3e73c0a6db6fa4e840bd1466d9555a3f',
        to='whatsapp:+639192802432'
    )
    print(message.status)
