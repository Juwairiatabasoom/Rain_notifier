import requests
from twilio.rest import Client

account_sid = "AC69ac62c0118b980cb9f6eadba990e02d"
auth_token = "880f96405fa548c28c2c8082d1953823"

api_key="220d7d61a3862c538d2896da21c4ca88"
params={
"lat":13.077160,
"lon":77.592613,
"appid":api_key,
"cnt":4  #gives only 4 counts
}

response=requests.get(url="https://api.openweathermap.org/data/2.5/forecast",params=params)
response.raise_for_status()
data=response.json()

will_rain=False
condition_code=data["list"][0]["weather"][0]["id"]
for hour_data in data["list"]:
    if condition_code<700:
        will_rain=True
if will_rain:
    client=Client(account_sid,auth_token)
    message=client.messages.create(body="It might rain today,Take an ☂️ bbg ",from_="+12563803794",to="+918985988884")
    print(message.status)
