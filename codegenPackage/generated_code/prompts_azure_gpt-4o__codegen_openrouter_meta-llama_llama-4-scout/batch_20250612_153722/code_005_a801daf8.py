"""
Generated Code Metadata:
========================
Original URL: https://polymarket.wiki
Prompt: Create a dashboard using Polymarket data to monitor predictions for cryptocurrency prices, including Bitcoin and Ethereum, for June 8 at 5 PM ET.
Generated: DETERMINISTIC_a801daf81fcd79a4
Batch ID: 20250612_153722
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.polymarket.com/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
# Import required libraries
import requests
import json
from datetime import datetime
import pandas as pd

# Define constants
POLYMARKET_API_URL = 'https://api.polymarket.com/v1'
MARKETS_ENDPOINT = '/markets'
CONDITIONS_ENDPOINT = '/conditions'
OUTCOMES_ENDPOINT = '/outcomes'
TICKETS_ENDPOINT = '/tickets'

# Define function to get markets
def get_markets():
    try:
        response = requests.get(POLYMARKET_API_URL + MARKETS_ENDPOINT)
        response.raise_for_status()
        return response.json()['markets']
    except requests.exceptions.RequestException as e:
        print(f"Error fetching markets: {e}")
        return []

# Define function to get conditions
def get_conditions(market_id):
    try:
        response = requests.get(POLYMARKET_API_URL + CONDITIONS_ENDPOINT, params={'marketId': market_id})
        response.raise_for_status()
        return response.json()['conditions']
    except requests.exceptions.RequestException as e:
        print(f"Error fetching conditions for market {market_id}: {e}")
        return []

# Define function to get outcomes
def get_outcomes(market_id):
    try:
        response = requests.get(POLYMARKET_API_URL + OUTCOMES_ENDPOINT, params={'marketId': market_id})
        response.raise_for_status()
        return response.json()['outcomes']
    except requests.exceptions.RequestException as e:
        print(f"Error fetching outcomes for market {market_id}: {e}")
        return []

# Define function to get tickets
def get_tickets(market_id):
    try:
        response = requests.get(POLYMARKET_API_URL + TICKETS_ENDPOINT, params={'marketId': market_id})
        response.raise_for_status()
        return response.json()['tickets']
    except requests.exceptions.RequestException as e:
        print(f"Error fetching tickets for market {market_id}: {e}")
        return []

# Define function to get prediction data
def get_prediction_data(markets):
    prediction_data = []
    for market in markets:
        market_id = market['id']
        conditions = get_conditions(market_id)
        outcomes = get_outcomes(market_id)
        tickets = get_tickets(market_id)

        # Filter for Bitcoin and Ethereum price predictions for June 8 at 5 PM ET
        if market['question'] in ['Will Bitcoin be above $X on June 8 at 5 PM ET?', 'Will Ethereum be above $Y on June 8 at 5 PM ET?']:
            market_data = {
                'market_id': market_id,
                'question': market['question'],
                'conditions': conditions,
                'outcomes': outcomes,
                'tickets': tickets
            }
            prediction_data.append(market_data)
    return prediction_data

# Define function to process prediction data
def process_prediction_data(prediction_data):
    bitcoin_data = None
    ethereum_data = None

    for data in prediction_data:
        if 'Bitcoin' in data['question']:
            bitcoin_data = data
        elif 'Ethereum' in data['question']:
            ethereum_data = data

    if bitcoin_data and ethereum_data:
        # Process and return prediction data for Bitcoin and Ethereum
        bitcoin_outcomes = bitcoin_data['outcomes']
        ethereum_outcomes = ethereum_data['outcomes']

        bitcoin_df = pd.DataFrame(bitcoin_outcomes)
        ethereum_df = pd.DataFrame(ethereum_outcomes)

        return {
            'bitcoin': bitcoin_df,
            'ethereum': ethereum_df
        }
    else:
        return None

# Main function
def main():
    markets = get_markets()
    prediction_data = get_prediction_data(markets)
    processed_data = process_prediction_data(prediction_data)

    if processed_data:
        print("Bitcoin Prediction Data:")
        print(processed_data['bitcoin'])
        print("\nEthereum Prediction Data:")
        print(processed_data['ethereum'])
    else:
        print("No prediction data available.")

if __name__ == "__main__":
    main()
```
