"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://azterdex.com
Prompt: How can I implement a non-custodial trading strategy using Aster's decentralized perpetual contracts?
Generated: DETERMINISTIC_7ded7e89f5cdb80b
Batch ID: 20250612_163133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python implementation of a non-custodial trading strategy using Aster's decentralized perpetual contracts. This code assumes you already have access to Aster's SDK or API library.

```python
import aster_sdk  # Hypothetical Aster SDK for interacting with their decentralized contracts
from decimal import Decimal

# Configuration: Replace with your actual API keys, wallet details, and parameters
ASTER_API_KEY = "your-api-key"
WALLET_PRIVATE_KEY = "your-wallet-private-key"
TRADING_PAIR = "BTC-USDT"  # Example trading pair
LEVERAGE = 5  # Define leverage for the perpetual contract
TRADE_AMOUNT = Decimal("0.01")  # Amount of BTC to trade
TAKE_PROFIT_PERCENTAGE = Decimal("5.0")  # Percentage profit target
STOP_LOSS_PERCENTAGE = Decimal("2.0")  # Percentage loss target

def initialize_aster_client(api_key, private_key):
    """
    Initialize the Aster client using API key and private key for the wallet.
    """
    try:
        return aster_sdk.Client(api_key=api_key, private_key=private_key)
    except Exception as e:
        raise RuntimeError(f"Error initializing Aster client: {str(e)}")

def calculate_prices(entry_price, take_profit_percentage, stop_loss_percentage):
    """
    Calculate take-profit and stop-loss prices based on entry price and percentages.
    """
    take_profit_price = entry_price * (1 + take_profit_percentage / 100)
    stop_loss_price = entry_price * (1 - stop_loss_percentage / 100)
    return take_profit_price, stop_loss_price

def execute_trade(client, trading_pair, trade_amount, leverage):
    """
    Open a leveraged position on the specified trading pair.
    """
    try:
        # Fetch current market price
        market_price = client.get_market_price(trading_pair)

        # Calculate take-profit and stop-loss prices
        take_profit_price, stop_loss_price = calculate_prices(
            entry_price=market_price,
            take_profit_percentage=TAKE_PROFIT_PERCENTAGE,
            stop_loss_percentage=STOP_LOSS_PERCENTAGE,
        )

        # Open a leveraged position
        position = client.open_position(
            pair=trading_pair,
            amount=trade_amount,
            leverage=leverage,
            take_profit=take_profit_price,
            stop_loss=stop_loss_price,
        )

        print(f"Position opened successfully: {position}")
        return position
    except Exception as e:
        print(f"Error executing trade: {str(e)}")
        return None

def main():
    """
    Main function to execute the trading strategy.
    """
    print("Initializing Aster client...")
    try:
        # Initialize the client
        client = initialize_aster_client(api_key=ASTER_API_KEY, private_key=WALLET_PRIVATE_KEY)

        print("Executing trade...")
        # Execute the trade
        position = execute_trade(
            client=client,
            trading_pair=TRADING_PAIR,
            trade_amount=TRADE_AMOUNT,
            leverage=LEVERAGE,
        )

        if position:
            print("Trading strategy executed successfully!")
        else:
            print("Failed to execute trading strategy.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```

### Notes:
- Replace `aster_sdk` with the actual SDK or API library provided by Aster.
- Update the constants (`ASTER_API_KEY`, `WALLET_PRIVATE_KEY`, etc.) with your actual credentials and trading parameters.
- Ensure you have installed the relevant SDK or API library and dependencies before running the script.
