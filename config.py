import os
import logging
from dotenv import load_dotenv

load_dotenv()

# log file that tracks the history of the app's execution
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app.log"), # save to file
        logging.StreamHandler()         # also print to console
    ]
)
logger = logging.getLogger(__name__)

class Config:
    STOCK_API_KEY = os.getenv("STOCK_API_KEY")
    NEWS_API_KEY = os.getenv("NEWS_API_KEY")
    TWILIO_SID = os.getenv("TWILIO_SID")
    TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
    TWILIO_PHONE = os.getenv("TWILIO_PHONE_NUMBER")
    USER_PHONE = os.getenv("MY_PERSONAL_PHONE")
    
    STOCK_ENDPOINT = "https://www.alphavantage.co/query"
    NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
    
    PORTFOLIO_FILE = "portfolio.csv"