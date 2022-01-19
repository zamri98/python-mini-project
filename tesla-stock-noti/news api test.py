import requests

news_endpoint="https://newsapi.org/v2/everything"
news_api_key=""


news_param={

    "q":"Tesla",
    "apiKey":news_api_key,

}

response=requests.get(news_endpoint,params=news_param)
print(response.json())
