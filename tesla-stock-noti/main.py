
import requests
from twilio.rest import Client
from datetime import datetime



STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


######stock api key and api endpoint #############################################
api_key=""
stock_endpoint="https://www.alphavantage.co/query"
########news api key and endpoint############################################
news_endpoint="https://newsapi.org/v2/everything"
news_api_key=""
######twitlio api key and api endpoint #################################
twilio_sid=""
twilio_auth_key=""
#############################################################################


news_param={

    "qInTitle":COMPANY_NAME,
    "apiKey":news_api_key,

}

stock_param={

    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "apikey":api_key,


}

response=requests.get(stock_endpoint,params=stock_param)
data=response.json()["Time Series (Daily)"]


#convert the daily stock data in the list
datalist=[ value for (key,value) in data.items() ]

#grab data from yesterday closing data
yesterday_data = datalist[0]
yesterday_closing_data= yesterday_data["4. close"]

#grab 2 days before closing data
daybefore_data = datalist[1]
daybefore_closing_data= daybefore_data["4. close"]

difference = abs(float(yesterday_closing_data)-float(daybefore_closing_data))

#difference in percentage

diff_percent = (difference/float(yesterday_closing_data)) *100
print(daybefore_closing_data)
print(yesterday_closing_data)
#print(difference)
print(diff_percent)
###################################################################################################



############### if the stock below or higher 5 % do sent us message about news regarding tesla
if diff_percent > 5 :
    response=requests.get(news_endpoint,params=news_param)
    data_article=response.json()["articles"][0:4]
    print(data_article)

    formatted_article_list=[f"headline:{article['title']}.\nBrief {article['description']}" for article in data_article ]
    print(formatted_article_list)

    client = Client(twilio_sid, twilio_auth_key)
    for x in formatted_article_list:

        message = client.messages.create(
            body= x,
            from_="twilio no",
            to="your number"
        )


