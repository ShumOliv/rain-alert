import os
import requests
from twilio.rest import Client
# from twilio.http.http_client import TwilioHttpClient

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY")
# Twilio authentication
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

weather_params = {
    "lat": 19.075983,
    "lon": 72.877655,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
print(response.status_code)
# print(response.json())
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    # print(hour_data["weather"][0]["id"])
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
       # print("Carry your umbrella")
    #   proxy_client = TwilioHttpClient ()
    #   proxy_client.session.proxies = {'https': os.environ['https_proxy']}

       client = Client(account_sid, auth_token)
       message = client.messages.create(
           body="It's going to rain today. Remember to bring an umbrella!☂️",
           from_= os.environ.get("TWILIO_FROM"),
           to= os.environ.get"TWILIO_TO",
       )
       print(message.status)
       # print(message.body)
