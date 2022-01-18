import requests
import os
from twilio.rest import Client


api_key="yor_api_key"
Owm_endpoint="https://api.openweathermap.org/data/2.5/onecall"

account_sid = "account_ssid"
auth_token = "auth_token"



weather_params={

    "lat":2.967008,
    "lon":101.490715,
    "exclude":"current,minutely,daily",
    "appid":api_key,


}
response= requests.get(Owm_endpoint,params=weather_params)
response.raise_for_status()
data=response.json()
hourly=data["hourly"][0:12]


weather_hour_list=[]

will_rain= False

for x in hourly:
    weather_id=x["weather"][0]["id"]
    weather_hour_list.append(weather_id)
    if int(weather_id) < 700:
        will_rain=True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="Bring Umbrella",
        from_="sender no from twilio",
        to="your phone number"
    )

    print(message.status)










