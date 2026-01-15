import requests
from config import Config, logger
from typing import List, Dict

class NewsManager:
    def __init__(self, company_name: str):
        self.company_name = company_name

    def get_top_articles(self, limit: int = 2) -> List[Dict[str, str]]:
        logger.info(f"Fetching news for {self.company_name}...")
        params = {
            "apiKey": Config.NEWS_API_KEY,
            "qInTitle": self.company_name,
            "sortBy": "publishedAt",
            "language": "en"
        }

        try:
            response = requests.get(Config.NEWS_ENDPOINT, params=params)
            response.raise_for_status()
            data = response.json()
            
            return data.get("articles", [])[:limit]

        except Exception as e:
            logger.error(f"Error fetching news for {self.company_name}: {e}")
            return []