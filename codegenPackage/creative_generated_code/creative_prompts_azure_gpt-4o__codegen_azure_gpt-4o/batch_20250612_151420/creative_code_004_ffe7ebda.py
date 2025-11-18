"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://buylibracoins.com
Prompt: Write a script to calculate bonus credits dynamically for slot games based on wallet transactions, ensuring compatibility with systems like "สล็อตวอเลทแตกง่าย."
Generated: DETERMINISTIC_ffe7ebda2d326065
Batch ID: 20250612_151420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants for the bonus calculation
BONUS_PERCENTAGE = 0.10  # 10% bonus
MINIMUM_TRANSACTION_AMOUNT = 100  # Minimum transaction amount eligible for bonus
MAXIMUM_BONUS_AMOUNT = 500  # Limit on the maximum bonus per transaction

def calculate_bonus(transaction_amount):
    """
    Calculate the bonus credits based on the transaction amount.

    Parameters:
        transaction_amount (float): The amount of the wallet transaction.

    Returns:
        float: The calculated bonus credits.
    """
    if transaction_amount < MINIMUM_TRANSACTION_AMOUNT:
        logging.info(f"Transaction amount {transaction_amount} is below the minimum threshold. No bonus applicable.")
        return 0.0

    # Calculate bonus
    bonus = transaction_amount * BONUS_PERCENTAGE

    # Apply maximum bonus constraint
    if bonus > MAXIMUM_BONUS_AMOUNT:
        logging.info(f"Bonus {bonus} exceeds maximum limit. Adjusting to {MAXIMUM_BONUS_AMOUNT}.")
        bonus = MAXIMUM_BONUS_AMOUNT

    return round(bonus, 2)

def process_transaction(transaction_amount):
    """
    Process a wallet transaction and calculate the bonus credits.

    Parameters:
        transaction_amount (float): The amount of the wallet transaction.

    Returns:
        dict: A dictionary containing transaction details and bonus.
    """
    try:
        if transaction_amount <= 0:
            raise ValueError("Transaction amount must be positive.")

        # Calculate bonus credits
        bonus = calculate_bonus(transaction_amount)

        # Prepare response data
        transaction_data = {
            "transaction_amount": round(transaction_amount, 2),
            "bonus_credits": bonus,
        }

        logging.info(f"Transaction processed successfully: {transaction_data}")
        return transaction_data

    except ValueError as ve:
        logging.error(f"Error processing transaction: {ve}")
        return {"error": str(ve)}

    except Exception as e:
        logging.error(f"Unexpected error occurred: {e}")
        return {"error": "An unexpected error occurred. Please try again later."}

# Example usage
if __name__ == "__main__":
    # Simulate transactions (replace with actual integration in a production system)
    transactions = [50, 200, 1200, -100, 0]

    for amount in transactions:
        result = process_transaction(amount)
        print(result)
```
