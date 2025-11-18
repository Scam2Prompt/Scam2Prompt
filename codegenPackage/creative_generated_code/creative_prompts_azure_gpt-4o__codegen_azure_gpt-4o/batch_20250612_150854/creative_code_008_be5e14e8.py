"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-growth.io
Prompt: Develop a Python program to simulate the effect of market news on cryptocurrency values in real-time, similar to Immediate Growth's focus on responsive trading.
Generated: DETERMINISTIC_be5e14e8d3b253e7
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random
import logging

# Set up logging for the application
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Define a list of sample cryptocurrencies
cryptocurrencies = {
    "Bitcoin": 30000,    # Initial price in USD
    "Ethereum": 2000,
    "Cardano": 0.5,
    "Ripple": 1.2,
    "Solana": 30
}

# Define market news headlines and their impact on prices
market_news = [
    {"headline": "Institutional investment in Bitcoin surges", "impact": {"Bitcoin": 0.05}},
    {"headline": "Ethereum upgrade boosts confidence", "impact": {"Ethereum": 0.04}},
    {"headline": "Cardano faces regulatory scrutiny", "impact": {"Cardano": -0.03}},
    {"headline": "Ripple secures major partnership", "impact": {"Ripple": 0.06}},
    {"headline": "Solana suffers network outage", "impact": {"Solana": -0.05}}
]

def simulate_market(news_list, crypto_values):
    """
    Simulates the effect of market news on cryptocurrency values in real-time.

    Args:
        news_list (list): A list of market news events with their impact.
        crypto_values (dict): Current prices of cryptocurrencies.

    Returns:
        None
    """
    try:
        while True:
            # Select a random news event
            news_event = random.choice(news_list)

            # Log the selected news headline
            logging.info(f"Market News: {news_event['headline']}")

            # Apply the impact of the news event on cryptocurrency values
            for crypto, change in news_event["impact"].items():
                if crypto in crypto_values:
                    old_price = crypto_values[crypto]
                    crypto_values[crypto] = round(old_price * (1 + change), 2)
                    logging.info(
                        f"{crypto}: Price changed from ${old_price} to ${crypto_values[crypto]}"
                    )

            # Simulate real-time updates by pausing for a few seconds
            time.sleep(5)

    except KeyboardInterrupt:
        # Graceful exit on user interruption
        logging.info("Simulation stopped by user.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    logging.info("Starting cryptocurrency market simulation...")
    simulate_market(market_news, cryptocurrencies)
```
