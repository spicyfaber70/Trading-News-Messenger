from twilio.rest import Client
from config import Config, logger

class SMSManager:
    def __init__(self):
        try:
            self.client = Client(Config.TWILIO_SID, Config.TWILIO_AUTH_TOKEN)
        except Exception as e:
            logger.critical(f"Failed to connect to Twilio: {e}")
            self.client = None

    def send_alert(self, header: str, articles: list):
        if not self.client:
            return

        for article in articles:
            msg_body = (
                f"{header}\n"
                f"Headline: {article['title']}\n"
                f"Link: {article['url']}"
            )

            try:
                self.client.messages.create(
                    body=msg_body,
                    from_=Config.TWILIO_PHONE,
                    to=Config.USER_PHONE
                )
                logger.info(f"SMS sent successfully: {article['title'][:30]}...")
            except Exception as e:
                logger.error(f"Failed to send SMS: {e}")