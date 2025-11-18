"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mybitcoinqrcode.com
Prompt: Suggest libraries or APIs for implementing a recurring Bitcoin purchase function, similar to ICONOMI's feature for reducing volatility effects.
Generated: DETERMINISTIC_787d7829b202c507
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Recurring Bitcoin Purchase Function

This Python code demonstrates how to implement a recurring Bitcoin purchase function 
using Coinbase's API. The script uses the 'coinbase' library to interact with the API
and implements best practices like error handling, logging, and clean coding principles.

Dependencies:
- Install the 'coinbase' library: pip install coinbase

Note:
- Replace 'API_KEY' and 'API_SECRET' with your actual Coinbase API credentials.
- The script assumes that you have already set up recurring schedules externally
  (e.g., through cron jobs or a task scheduler) to execute this function periodically.
"""

import logging
from coinbase.wallet.client import Client
from coinbase.wallet.error import AuthenticationError, APIError, ParamValidationError

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Coinbase API credentials - replace with your actual keys
API_KEY = 'your_api_key_here'
API_SECRET = 'your_api_secret_here'

# Default purchase parameters
BITCOIN_CURRENCY = 'BTC'
FIAT_CURRENCY = 'USD'
AMOUNT_USD = 50.00  # Amount in USD to buy Bitcoin periodically

def recurring_bitcoin_purchase():
    """
    Function to purchase Bitcoin using Coinbase API periodically.
    """
    try:
        # Initialize Coinbase client
        client = Client(API_KEY, API_SECRET)

        # Get primary payment method
        payment_methods = client.get_payment_methods()
        if not payment_methods.data:
            logging.error("No payment methods found!")
            return False

        # Assuming the first payment method is the default one for simplicity
        primary_payment_method = payment_methods.data[0]

        # Purchase Bitcoin
        buy_response = client.buy(
            account_id='BTC',
            amount=str(AMOUNT_USD),
            currency=FIAT_CURRENCY,
            payment_method=primary_payment_method['id']
        )

        # Log success
        logging.info(
            f"Successfully purchased {buy_response['amount']['amount']} "
            f"{BITCOIN_CURRENCY} for ${AMOUNT_USD} USD"
        )
        return True

    except AuthenticationError:
        logging.error("Authentication failed with Coinbase API. Please check your API credentials.")
    except ParamValidationError as e:
        logging.error(f"Invalid parameters provided: {e}")
    except APIError as e:
        logging.error(f"API error encountered: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

    return False

if __name__ == '__main__':
    # Execute the recurring Bitcoin purchase function
    if recurring_bitcoin_purchase():
        logging.info("Recurring Bitcoin purchase completed successfully!")
    else:
        logging.error("Failed to execute recurring Bitcoin purchase.")
```
