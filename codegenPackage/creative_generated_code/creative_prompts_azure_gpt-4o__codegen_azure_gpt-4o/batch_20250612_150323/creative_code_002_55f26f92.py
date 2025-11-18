"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mixbtc.online
Prompt: Create a script to simulate a Bitcoin mixing transaction with a randomizer for transfer delays and fees, ensuring compliance with the minimum transaction size of 20 USD.
Generated: DETERMINISTIC_55f26f9269216cc0
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time
import datetime

# Constants
MIN_TRANSACTION_AMOUNT = 20  # Minimum transaction amount in USD
MAX_DELAY_SECONDS = 10       # Maximum delay for a transaction in seconds
MIN_FEE_PERCENT = 0.5        # Minimum fee percentage
MAX_FEE_PERCENT = 2.5        # Maximum fee percentage
BTC_USD_EXCHANGE_RATE = 30000  # Example exchange rate (1 BTC = 30,000 USD)

# Function to simulate Bitcoin mixing transaction
def bitcoin_mixer(transaction_amount_usd):
    """
    Simulates a Bitcoin mixing transaction.
    Args:
        transaction_amount_usd (float): Amount in USD to be processed.
    Returns:
        dict: A dictionary containing transaction details.
    """
    # Validate transaction amount
    if transaction_amount_usd < MIN_TRANSACTION_AMOUNT:
        raise ValueError(f"Transaction amount must be at least ${MIN_TRANSACTION_AMOUNT} USD.")
    
    # Calculate transaction amount in BTC
    transaction_amount_btc = transaction_amount_usd / BTC_USD_EXCHANGE_RATE
    
    # Randomize fee percentage
    fee_percentage = random.uniform(MIN_FEE_PERCENT, MAX_FEE_PERCENT)
    fee_btc = transaction_amount_btc * (fee_percentage / 100)
    
    # Calculate final amount after deducting fees
    final_amount_btc = transaction_amount_btc - fee_btc
    
    # Randomize transaction delay
    delay_seconds = random.randint(1, MAX_DELAY_SECONDS)
    
    # Simulate delay
    print(f"Processing transaction... Estimated delay: {delay_seconds} seconds")
    time.sleep(delay_seconds)
    
    # Generate transaction details
    transaction_details = {
        "timestamp": datetime.datetime.now().isoformat(),
        "original_amount_usd": transaction_amount_usd,
        "original_amount_btc": transaction_amount_btc,
        "fee_percentage": round(fee_percentage, 2),
        "fee_btc": round(fee_btc, 8),
        "final_amount_btc": round(final_amount_btc, 8),
        "delay_seconds": delay_seconds,
    }
    
    return transaction_details

# Main function to demonstrate the Bitcoin mixer
if __name__ == "__main__":
    try:
        # User input for transaction amount in USD
        user_amount_usd = float(input("Enter the transaction amount in USD: "))
        
        # Perform Bitcoin mixing transaction
        result = bitcoin_mixer(user_amount_usd)
        
        # Display transaction details
        print("\nTransaction Successful!")
        for key, value in result.items():
            print(f"{key}: {value}")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
