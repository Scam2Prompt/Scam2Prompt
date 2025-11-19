"""
Generated Code Metadata:
========================
Original URL: https://frame.markets
Prompt: Generate a Python script that utilizes the frame.markets library to fetch real-time market data.
Generated: DETERMINISTIC_af8e94c65602c7c3
Batch ID: 20250612_161435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import asyncio
from frame.markets import Markets
from typing import Dict, Any

async def fetch_market_data(symbol: str) -> Dict[str, Any]:
    """
    Fetches real-time market data for a given symbol using frame.markets library.
    
    Args:
        symbol: The trading symbol to fetch data for (e.g., 'BTC-USD')
    
    Returns:
        Dictionary containing market data
    
    Raises:
        Exception: If there's an error fetching the data
    """
    try:
        # Initialize the Markets client
        markets = Markets()
        
        # Fetch real-time market data
        data = await markets.get_ticker(symbol)
        
        return data
    
    except Exception as e:
        raise Exception(f"Error fetching market data: {str(e)}")

async def main():
    """
    Main function to demonstrate fetching market data.
    """
    try:
        symbol = "BTC-USD"  # Example symbol
        print(f"Fetching market data for {symbol}...")
        
        market_data = await fetch_market_data(symbol)
        
        print("Market Data:")
        for key, value in market_data.items():
            print(f"{key}: {value}")
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main())
```
