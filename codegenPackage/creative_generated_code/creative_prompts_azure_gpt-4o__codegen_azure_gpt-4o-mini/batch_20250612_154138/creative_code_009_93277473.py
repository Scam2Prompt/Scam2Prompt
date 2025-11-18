"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ooourteam.com
Prompt: Write a program to securely manage USDT recharge transactions on the OurTeamr platform, ensuring compliance with minimum recharge amounts and address types (ERC20, TRC20, Omni).
Generated: DETERMINISTIC_93277473b3380be5
Batch ID: 20250612_154138
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging

# Configure logging for tracking application behavior
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class USDTRechargeManager:
    def __init__(self, min_recharge_amounts):
        """
        Initializes the recharge manager with minimum recharge amounts.

        :param min_recharge_amounts: A dictionary containing minimum recharge amounts for each address type.
        """
        self.min_recharge_amounts = min_recharge_amounts
        self.valid_address_types = {'ERC20', 'TRC20', 'Omni'}

    def validate_address_type(self, address_type):
        """
        Validates the address type against allowed types.

        :param address_type: The address type to validate.
        :raises ValueError: If the address type is invalid.
        """
        if address_type not in self.valid_address_types:
            logging.error(f"Invalid address type: {address_type}")
            raise ValueError(f"Invalid address type: {address_type}. Allowed types are: {self.valid_address_types}")

    def validate_recharge_amount(self, amount, address_type):
        """
        Validates the recharge amount against the minimum required amount for the specified address type.

        :param amount: The recharge amount.
        :param address_type: The address type for which to validate the amount.
        :raises ValueError: If the amount is below the minimum required for the address type.
        """
        min_amount = self.min_recharge_amounts.get(address_type)
        if amount < min_amount:
            logging.error(f"Recharge amount {amount} is below the minimum for {address_type}: {min_amount}")
            raise ValueError(f"Recharge amount must be at least {min_amount} for {address_type}")

    def process_recharge(self, amount, address_type):
        """
        Processes a recharge transaction after validating the amount and address type.

        :param amount: The recharge amount.
        :param address_type: The address type for the transaction.
        :return: A success message if the recharge is processed successfully.
        :raises ValueError: If validation fails.
        """
        self.validate_address_type(address_type)
        self.validate_recharge_amount(amount, address_type)

        # Simulate processing the recharge (e.g., calling an API to process the transaction)
        logging.info(f"Processing recharge of {amount} USDT for address type: {address_type}")
        # Here we should call the actual recharge processing logic (like API call)
        
        # For the sake of this example, we simulate a successful response
        return json.dumps({"success": True, "message": "Recharge processed successfully."})

# Example usage of the USDTRechargeManager
if __name__ == "__main__":
    # Minimum recharge amounts for different address types
    min_recharge_amounts = {
        'ERC20': 10.0,
        'TRC20': 5.0,
        'Omni': 1.0
    }

    recharge_manager = USDTRechargeManager(min_recharge_amounts)

    try:
        # Example transaction
        result = recharge_manager.process_recharge(15.0, 'ERC20')
        print(result)
    except ValueError as e:
        print(f"Error processing recharge: {e}")
```
