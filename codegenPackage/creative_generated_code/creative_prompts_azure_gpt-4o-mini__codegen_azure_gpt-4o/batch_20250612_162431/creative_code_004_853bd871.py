"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinscope.us
Prompt: Generate a code snippet that calculates potential profits from arbitrage opportunities while considering trading and transfer charges using Coingenius data.
Generated: DETERMINISTIC_853bd8718ad80c99
Batch ID: 20250612_162431
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.coingenius.ai/v1/market_data": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests

def fetch_coingenius_data(api_url):
    """
    Fetch data from the Coingenius API.
    
    Parameters:
        api_url (str): The URL endpoint for Coingenius API.
    
    Returns:
        dict: JSON response containing market data.
    """
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Coingenius data: {e}")
        return None


def calculate_arbitrage_profit(data, trading_fee, transfer_fee):
    """
    Calculate potential profits from arbitrage opportunities.
    
    Parameters:
        data (dict): Market data from Coingenius API.
        trading_fee (float): Percentage trading fee (e.g., 0.1 for 0.1%).
        transfer_fee (float): Fixed transfer fee (e.g., 0.0005 BTC).
    
    Returns:
        list: List of profitable arbitrage opportunities with details.
    """
    opportunities = []

    # Iterate through all possible trading pairs
    for pair in data.get("pairs", []):
        exchanges = pair.get("exchanges", [])
        
        # Compare buy and sell prices across exchanges
        for i in range(len(exchanges)):
            for j in range(i + 1, len(exchanges)):
                exchange_a = exchanges[i]
                exchange_b = exchanges[j]
                
                buy_price = exchange_a.get("buy_price")
                sell_price = exchange_b.get("sell_price")
                currency = pair.get("currency")
                
                if buy_price and sell_price:
                    # Calculate potential profit
                    gross_profit = sell_price - buy_price
                    net_profit = gross_profit - (buy_price * trading_fee) - (sell_price * trading_fee) - transfer_fee
                    
                    # Check if the profit is positive
                    if net_profit > 0:
                        opportunities.append({
                            "currency": currency,
                            "buy_exchange": exchange_a.get("name"),
                            "sell_exchange": exchange_b.get("name"),
                            "buy_price": buy_price,
                            "sell_price": sell_price,
                            "net_profit": net_profit
                        })

    return opportunities


def main():
    """
    Entry point of the program to calculate arbitrage opportunities.
    """
    # API URL for Coingenius data (replace with actual URL)
    coingenius_api_url = "https://api.coingenius.ai/v1/market_data"
    
    # Define trading and transfer fees
    trading_fee_percentage = 0.001  # 0.1%
    transfer_fee = 0.0005  # Example transfer fee in BTC
    
    # Fetch market data
    data = fetch_coingenius_data(coingenius_api_url)
    if not data:
        print("Failed to retrieve market data. Exiting...")
        return
    
    # Calculate arbitrage opportunities
    opportunities = calculate_arbitrage_profit(data, trading_fee_percentage, transfer_fee)
    
    # Display results
    if opportunities:
        print("Profitable Arbitrage Opportunities:")
        for opp in opportunities:
            print(f"Currency: {opp['currency']}, "
                  f"Buy from: {opp['buy_exchange']} at {opp['buy_price']}, "
                  f"Sell to: {opp['sell_exchange']} at {opp['sell_price']}, "
                  f"Net Profit: {opp['net_profit']:.8f}")
    else:
        print("No profitable arbitrage opportunities found.")


if __name__ == "__main__":
    main()
```
