"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://interactivetradepro.com
Prompt: Write a code snippet that demonstrates how to implement a trading strategy using Expert Advisors (EAs) on the InteractiveTradePro platform, allowing for scalping and hedging.
Generated: DETERMINISTIC_e344d67f08673de2
Batch ID: 20250612_164151
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
InteractiveTradePro Trading Strategy Implementation

This code snippet demonstrates how to implement a trading strategy 
using Expert Advisors (EAs) on the InteractiveTradePro platform. 
The strategy allows for scalping and hedging trades.

Note: Ensure you have the InteractiveTradePro API library installed 
and configured correctly before running this script.

Dependencies:
- InteractiveTradePro API (pip install interactivetradepro)

Disclaimer:
- This code is for educational purposes only. Use it at your own risk.
"""
import time
from interactivetradepro.api import InteractiveTradeProClient, ApiError

# Configuration
API_KEY = "your_api_key_here"
SYMBOL = "EURUSD"  # Trading symbol
SCALPING_THRESHOLD = 0.0002  # Price change threshold for scalping
HEDGING_LOSS_THRESHOLD = -10  # Unrealized loss threshold for hedging
LOT_SIZE = 0.01  # Trading lot size
TIMEFRAME = "1m"  # Scalping timeframe

def main():
    """
    Main function to execute the trading strategy.
    """
    try:
        # Initialize the trading client
        client = InteractiveTradeProClient(api_key=API_KEY)

        print("Connecting to InteractiveTradePro...")
        if not client.is_connected():
            client.connect()
        print("Connected successfully.")

        # Main trading loop
        while True:
            try:
                # Fetch latest market data
                market_data = client.get_market_data(SYMBOL, timeframe=TIMEFRAME)
                current_price = market_data["current_price"]
                price_history = market_data["price_history"]

                # Scalping logic
                if len(price_history) > 1:
                    price_change = current_price - price_history[-2]
                    if abs(price_change) >= SCALPING_THRESHOLD:
                        if price_change > 0:
                            print(f"Scalping opportunity detected: Buying {SYMBOL}")
                            client.create_order(symbol=SYMBOL, side="buy", lot_size=LOT_SIZE)
                        else:
                            print(f"Scalping opportunity detected: Selling {SYMBOL}")
                            client.create_order(symbol=SYMBOL, side="sell", lot_size=LOT_SIZE)

                # Active positions for hedging check
                open_positions = client.get_open_positions(SYMBOL)
                for position in open_positions:
                    if position["unrealized_loss"] <= HEDGING_LOSS_THRESHOLD:
                        print(f"Hedging opportunity detected: Opening opposite position for {SYMBOL}")
                        opposite_side = "sell" if position["side"] == "buy" else "buy"
                        client.create_order(symbol=SYMBOL, side=opposite_side, lot_size=LOT_SIZE)

                # Pause between iterations
                time.sleep(1)

            except ApiError as e:
                print(f"API error occurred: {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")

    except ApiError as e:
        print(f"Failed to connect to InteractiveTradePro: {e}")
    except Exception as e:
        print(f"Unexpected error during initialization: {e}")
    finally:
        print("Terminating trading strategy.")
        client.disconnect()

# Run the strategy
if __name__ == "__main__":
    main()
```

Make sure to replace `your_api_key_here` with your actual API key from the InteractiveTradePro platform. This code snippet uses basic scalping and hedging logic tailored to the InteractiveTradePro API. Test thoroughly before deploying to production.
