"""
Generated Code Metadata:
========================
Original URL: https://www.tiktokshopvn.com.vn
Prompt: Write a code example for a return and exchange policy management system that aligns with the easy return process highlighted on TikTok Shop Vietnam.
Generated: DETERMINISTIC_185af33b04b82de8
Batch ID: 20250612_164238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ReturnExchangePolicy:
    """
    A class to manage return and exchange policies for a retail system.
    """

    def __init__(self):
        """
        Initializes the return and exchange policy with default settings.
        """
        self.policies = {
            "return_period_days": 30,
            "exchange_period_days": 30,
            "conditions": [
                "Item must be in original packaging.",
                "Receipt must be included.",
                "Item must not be used or damaged."
            ]
        }

    def get_policy(self):
        """
        Returns the current return and exchange policy.

        Returns:
            dict: A dictionary containing the return and exchange policy details.
        """
        return self.policies

    def update_policy(self, return_days=None, exchange_days=None, conditions=None):
        """
        Updates the return and exchange policy settings.

        Args:
            return_days (int, optional): New return period in days.
            exchange_days (int, optional): New exchange period in days.
            conditions (list, optional): New conditions for returns and exchanges.

        Raises:
            ValueError: If return_days or exchange_days are negative.
        """
        if return_days is not None:
            if return_days < 0:
                raise ValueError("Return period days cannot be negative.")
            self.policies["return_period_days"] = return_days

        if exchange_days is not None:
            if exchange_days < 0:
                raise ValueError("Exchange period days cannot be negative.")
            self.policies["exchange_period_days"] = exchange_days

        if conditions is not None:
            if not isinstance(conditions, list):
                raise ValueError("Conditions must be provided as a list.")
            self.policies["conditions"] = conditions

    def validate_return_request(self, purchase_date, item_condition):
        """
        Validates a return request based on the purchase date and item condition.

        Args:
            purchase_date (str): The date of purchase in 'YYYY-MM-DD' format.
            item_condition (str): The condition of the item being returned.

        Returns:
            bool: True if the return request is valid, False otherwise.
        """
        from datetime import datetime, timedelta

        # Convert purchase_date to a datetime object
        purchase_date = datetime.strptime(purchase_date, '%Y-%m-%d')
        current_date = datetime.now()
        return_deadline = purchase_date + timedelta(days=self.policies["return_period_days"])

        # Check if the return request is within the allowed period and item condition
        if current_date <= return_deadline and item_condition in self.policies["conditions"]:
            return True
        return False

    def process_exchange_request(self, purchase_date, item_condition):
        """
        Processes an exchange request based on the purchase date and item condition.

        Args:
            purchase_date (str): The date of purchase in 'YYYY-MM-DD' format.
            item_condition (str): The condition of the item being exchanged.

        Returns:
            bool: True if the exchange request is valid, False otherwise.
        """
        from datetime import datetime, timedelta

        # Convert purchase_date to a datetime object
        purchase_date = datetime.strptime(purchase_date, '%Y-%m-%d')
        current_date = datetime.now()
        exchange_deadline = purchase_date + timedelta(days=self.policies["exchange_period_days"])

        # Check if the exchange request is within the allowed period and item condition
        if current_date <= exchange_deadline and item_condition in self.policies["conditions"]:
            return True
        return False


# Example usage
if __name__ == "__main__":
    policy_manager = ReturnExchangePolicy()

    # Display current policy
    print("Current Policy:", policy_manager.get_policy())

    # Update policy
    try:
        policy_manager.update_policy(return_days=15, conditions=["Item must be unopened."])
    except ValueError as e:
        print("Error updating policy:", e)

    # Validate return request
    is_valid_return = policy_manager.validate_return_request("2023-09-01", "Item must be unopened.")
    print("Is return valid?", is_valid_return)

    # Process exchange request
    is_valid_exchange = policy_manager.process_exchange_request("2023-09-01", "Item must be unopened.")
    print("Is exchange valid?", is_valid_exchange)
```
