import requests

news_endpoint="https://newsapi.org/v2/everything"
news_api_key="676a89cdd1024aff80b4b0f0e01b45f2"


news_param={

    "q":"Tesla",
    "apiKey":news_api_key,

}

response=requests.get(news_endpoint,params=news_param)
print(response.json())
