import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "9dd8cc04ac69fc0192627ab16edfe5fd"

account_sid = "AC80dd328dbf4091255e435780d9a5a24a"
auth_token = "5f05f95dfb9eefece75706eba2af8d06"

parameters = {
    "lat": 19.957343,
    "lon": 73.837058,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

weather_slice = weather_data["hourly"][:24]
print(weather_slice)

will_rain = False
for hour_data in weather_slice:
    condition = hour_data["weather"][0]["id"]
    if int(condition) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It's going to rain today, Remember to bring an umbrella",
            from_='+18624658730',
            to='+917559197084'
        )
    print(message.status)
