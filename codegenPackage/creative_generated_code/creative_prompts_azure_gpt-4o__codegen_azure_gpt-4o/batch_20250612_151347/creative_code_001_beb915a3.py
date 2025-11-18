"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linktreewallstmemes.pages.dev
Prompt: Generate code to integrate a cryptocurrency deposit bonus feature for a casino platform, referencing the $WSM token and a 200% deposit bonus offer.
Generated: DETERMINISTIC_beb915a39fadc314
Batch ID: 20250612_151347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from decimal import Decimal
import logging

# Logging configuration for debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
TOKEN_SYMBOL = "WSM"
DEPOSIT_BONUS_MULTIPLIER = Decimal("2.0")  # 200% bonus
MINIMUM_DEPOSIT = Decimal("10.0")  # Minimum deposit amount in $WSM
MAXIMUM_BONUS = Decimal("1000.0")  # Maximum bonus cap in $WSM

# Error classes for clear error handling
class DepositError(Exception):
    """Custom exception for deposit-related errors."""
    pass

class BonusError(Exception):
    """Custom exception for bonus-related errors."""
    pass

def calculate_bonus(deposit_amount):
    """
    Calculate the deposit bonus based on the deposit amount.
    
    Args:
        deposit_amount (Decimal): The amount deposited in $WSM.
    
    Returns:
        Decimal: The calculated bonus amount.
    
    Raises:
        BonusError: If the bonus exceeds the maximum cap.
    """
    bonus = deposit_amount * DEPOSIT_BONUS_MULTIPLIER
    if bonus > MAXIMUM_BONUS:
        raise BonusError(f"Bonus exceeds the maximum cap of {MAXIMUM_BONUS} $WSM.")
    return bonus

def process_deposit(user_id, deposit_amount):
    """
    Process a cryptocurrency deposit and apply the bonus.

    Args:
        user_id (str): Unique identifier for the user.
        deposit_amount (Decimal): The amount deposited in $WSM.

    Returns:
        dict: A summary of the deposit and bonus applied.

    Raises:
        DepositError: If the deposit amount is below the required minimum.
    """
    if deposit_amount < MINIMUM_DEPOSIT:
        raise DepositError(f"Deposit must be at least {MINIMUM_DEPOSIT} $WSM.")

    try:
        bonus_amount = calculate_bonus(deposit_amount)
    except BonusError as e:
        logging.error(f"Error calculating bonus: {e}")
        raise

    # Simulate deposit and bonus transaction (e.g., update user balance in database)
    logging.info(f"User '{user_id}' deposited {deposit_amount} $WSM and earned a bonus of {bonus_amount} $WSM.")
    
    return {
        "user_id": user_id,
        "deposit_amount": deposit_amount,
        "bonus_amount": bonus_amount,
        "total_credited": deposit_amount + bonus_amount
    }

# Example of integrating the deposit feature
if __name__ == "__main__":
    # Example inputs
    user_id = "user123"
    deposit_amount_input = "500.0"

    try:
        deposit_amount = Decimal(deposit_amount_input)
        result = process_deposit(user_id, deposit_amount)
        logging.info(f"Deposit processed successfully: {result}")
    except DepositError as e:
        logging.error(f"Deposit failed: {e}")
    except BonusError as e:
        logging.error(f"Bonus processing failed: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
```
