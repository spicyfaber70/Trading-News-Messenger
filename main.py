import os
import requests
from twilio.rest import Client
 
STOCK = "MP"
COMPANY = "MP Materials"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}

news_params = {
    "apiKey": NEWS_API_KEY,
    "qInTitle": COMPANY
}

news_response = requests.get(NEWS_ENDPOINT, params=news_params)
articles = news_response.json()["articles"] # <- dict format
stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = stock_response.json()["Time Series (Daily)"] # <- dict format

#stripping away dates
data_list = [value for (key, value) in data.items()]

#yesterday's stock data
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

#day before yesterday's stock data for comparison
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
gain_loss = None
if difference > 0:
    gain_loss = "📈"
else:
    gain_loss = "📉"

diff_percent = round((difference / float(yesterday_closing_price)) * 100)

if abs(diff_percent) > 1:
    x_articles = articles[:1]
    print(x_articles)

    final_articles = [f"{STOCK}: {gain_loss}{diff_percent}% \nHeadline: {article['title']}. \nDescription: {article['description']}. \nURL: {article['url']}" for article in x_articles]

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    for article in final_articles:
        message = client.messages.create(
            body=article,
            from_=os.environ.get("TWILIO_PHONE_NUMBER"),
            to=os.environ.get("MY_PERSONAL_PHONE")
        )