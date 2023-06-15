import requests
from twilio.rest import Client
OWN_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
MY_LAT = 42.697708
MY_LONG = 23.321867
api_key = "69f04e4613056b159c2761a9d9e664d2"
account_sid = "AC5e38c72883a39c7777692be00c4782bd"
auth_token = "6adfd2eb4edae33f8c82f47adb928676"

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "exclude": "current,daily,minutely"
}
response = requests.get(OWN_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
will_rain = False

for hour_data in weather_slice:
    condition_code = int(hour_data["weather"][0]["id"])
    if condition_code < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body = "it's going to rain today. remember to bring an umbrella",
        from_ = "+13613106464",
        to = "+201003349095"
    )
    print(message.status)

