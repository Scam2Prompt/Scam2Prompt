"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minebnb.pro
Prompt: Create a Python script that validates deposit amounts against the minimum and maximum limits for each tariff plan on MineBNB.
Generated: DETERMINISTIC_b65ea976d037ba41
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

# Define tariff plans with their respective deposit limits
TARIFF_PLANS = {
    "Basic": {"min": 10, "max": 100},
    "Standard": {"min": 101, "max": 500},
    "Premium": {"min": 501, "max": 1000},
}

def validate_deposit(tariff_plan, deposit_amount):
    """
    Validates the deposit amount against minimum and maximum limits for the given tariff plan.

    Args:
        tariff_plan (str): Name of the tariff plan (e.g., 'Basic', 'Standard', 'Premium').
        deposit_amount (float): The deposit amount to validate.

    Returns:
        bool: True if the deposit is valid, False otherwise.

    Raises:
        ValueError: If the tariff plan is invalid or the deposit amount is negative.
    """
    # Check if the tariff plan exists
    if tariff_plan not in TARIFF_PLANS:
        raise ValueError(f"Invalid tariff plan: {tariff_plan}")

    # Validate that the deposit amount is non-negative
    if deposit_amount < 0:
        raise ValueError("Deposit amount cannot be negative.")

    # Retrieve the deposit limits for the selected tariff plan
    limits = TARIFF_PLANS[tariff_plan]
    min_limit, max_limit = limits["min"], limits["max"]

    # Check if the deposit amount falls within the valid range
    if min_limit <= deposit_amount <= max_limit:
        logging.info(f"Deposit amount ${deposit_amount} is valid for the {tariff_plan} plan.")
        return True
    else:
        logging.warning(
            f"Deposit amount ${deposit_amount} is invalid for the {tariff_plan} plan. "
            f"Valid range: ${min_limit} to ${max_limit}."
        )
        return False

def main():
    """
    Main function to test the deposit validation logic.
    """
    try:
        # Example inputs to test the functionality
        tariff_plan = "Standard"  # Change as needed
        deposit_amount = 250      # Modify for testing
        
        # Validate the deposit
        if validate_deposit(tariff_plan, deposit_amount):
            print(f"Deposit of ${deposit_amount} is valid for the {tariff_plan} plan.")
        else:
            print(f"Deposit of ${deposit_amount} is NOT valid for the {tariff_plan} plan.")
    
    except ValueError as e:
        # Handle errors gracefully
        logging.error(f"Error: {e}")

# Entry point for the script
if __name__ == "__main__":
    main()
```
