import requests
from config import Config, logger
from typing import Optional, Tuple

class StockManager:
    def __init__(self, symbol: str):
        self.symbol = symbol

    def get_price_change(self) -> Tuple[float, Optional[str]]:
        params = {
            "function": "TIME_SERIES_DAILY",
            "symbol": self.symbol,
            "apikey": Config.STOCK_API_KEY
        }

        try:
            response = requests.get(Config.STOCK_ENDPOINT, params=params)
            response.raise_for_status()
            data = response.json()
            
            # API limit check (AlphaVantage returns this key on error)
            if "Note" in data:
                logger.warning(f"API Limit Reached for {self.symbol}. Skipping.")
                return 0.0, None

            daily_data = data.get("Time Series (Daily)")
            if not daily_data:
                logger.error(f"No data found for {self.symbol}")
                return 0.0, None

            data_list = [value for (key, value) in daily_data.items()]
            
            # math
            yesterday_close = float(data_list[0]["4. close"])
            day_before_close = float(data_list[1]["4. close"])

            difference = yesterday_close - day_before_close
            percent_diff = (difference / yesterday_close) * 100
            
            emoji = "📈" if difference > 0 else "📉"
            
            logger.info(f"{self.symbol}: Checked. Movement: {round(percent_diff, 2)}%")
            return round(percent_diff, 2), emoji

        except Exception as e:
            logger.error(f"Error fetching stock data for {self.symbol}: {e}")
            return 0.0, None