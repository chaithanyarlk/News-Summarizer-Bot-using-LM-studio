import requests

class NewsAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://newsapi.org/v2/'
        
    def get_news(self, query):
        endpoint = f'{self.base_url}/everything'
        params = {
            'q': query,
            'apiKey': self.api_key
        }
        response = requests.get(endpoint, params=params)
        articles = response.json()['articles']
        return articles