**Description:**
This project is a Python application designed to monitor a specific portfolio of stocks for volatility. Unlike standard price alerts, this system contextualizes market movement. It continuously polls stock data, and if a stock experiences volatile activity (e.g., a 5% drop), it automatically cross-references the event with the NewsAPI to find the cause. It then sends an SMS summary to me via Twilio, allowing me to be able to make decisions without constantly looking at the stocks.

**Purpose of project:**
During the JA Trading Competition where I managed to generate $8,000 in profit during a volatile market cycle (2024 US presidential elections), I realized that speed and information were my biggest assets. However, manually tracking news for every position in my personal portfolio (45.33% annual return) was inefficient. I built this tool to automate the "monitoring" phase of trading. It acts as a passive filter, ignoring normal market noise and only alerting me when a stock moves significantly enough to require my attention.

**Tech Stack:**
Language: Python
APIs: AlphaVantage (Market Data), NewsAPI (Sentiment/Context), Twilio (SMS Delivery)

**Difficulties:**
The financial data API has strict usage limits (5 calls/minute). Early versions of my code would crash or get banned for polling too fast. I had to implement a "smart sleep" mechanism and error handling logic to respect API limits while looping through the portfolio.
Initially, this was a single messy script. I refactored it into a multi-file structure (separating the Stock Manager, News Manager, and Notification system). This made the code scalable. I can now add 50 stocks to the portfolio.csv file without changing a single line of code.

**Changes for the future:**
I plan to integrate a Natural Language Processing (NLP) library to grade the news headlines (Positive/Negative) so the SMS tells me if the move is a buying opportunity or a panic sell.
Moving from SMS to a Discord Webhook to share alerts with the rest of my Programming Club members.
