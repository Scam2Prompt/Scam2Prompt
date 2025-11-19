"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rexas-de.web.app
Prompt: What are the key features of the Rexas Launchpad for launching token sales, and how can I integrate it into my project?
Generated: DETERMINISTIC_de124a14a7ce6d8b
Batch ID: 20250612_155436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# rexas_launchpad.py

class RexasLaunchpad:
    """
    A class to represent the Rexas Launchpad for launching token sales.
    """

    def __init__(self, project_name, token_symbol, sale_start, sale_end, target_amount):
        """
        Initializes the RexasLaunchpad instance.

        :param project_name: Name of the project for the token sale.
        :param token_symbol: Symbol of the token being sold.
        :param sale_start: Start date and time of the token sale (ISO format).
        :param sale_end: End date and time of the token sale (ISO format).
        :param target_amount: The target amount to be raised during the token sale.
        """
        
        self.project_name = project_name
        self.token_symbol = token_symbol
        self.sale_start = self.validate_date(sale_start)
        self.sale_end = self.validate_date(sale_end)
        self.target_amount = target_amount
        self.funds_raised = 0

    @staticmethod
    def validate_date(date_str):
        """
        Validates the date string format.

        :param date_str: The date string to validate.
        :return: A datetime object if valid.
        :raises ValueError: If the date string is not in the correct format.
        """
        from datetime import datetime

        try:
            return datetime.fromisoformat(date_str)
        except ValueError:
            raise ValueError("Date must be in ISO format (YYYY-MM-DDTHH:MM:SS)")

    def start_sale(self):
        """
        Starts the token sale if the current time is within the sale period.
        """
        from datetime import datetime

        current_time = datetime.now()
        if current_time < self.sale_start:
            raise Exception("Token sale has not started yet.")
        if current_time > self.sale_end:
            raise Exception("Token sale has already ended.")

        print(f"Token sale for {self.project_name} has started!")

    def contribute(self, amount):
        """
        Allows users to contribute to the token sale.

        :param amount: The amount of funds the user wishes to contribute.
        :raises ValueError: If the contribution amount is invalid.
        :raises Exception: If the funding goal has been reached or sale is not active.
        """
        if amount <= 0:
            raise ValueError("Contribution amount must be greater than zero.")

        if self.funds_raised >= self.target_amount:
            raise Exception("Funding goal has already been reached.")

        if self.sale_start > datetime.now() or self.sale_end < datetime.now():
            raise Exception("Token sale is not currently active.")

        self.funds_raised += amount
        print(f"Contributed {amount} to the sale. Total raised: {self.funds_raised}")

    def get_status(self):
        """
        Returns the current status of the token sale.

        :return: A dictionary containing project name, amount raised, and funding goal.
        """
        return {
            'project_name': self.project_name,
            'funds_raised': self.funds_raised,
            'target_amount': self.target_amount,
            'sale_active': self.sale_start <= datetime.now() <= self.sale_end
        }
```

### Usage Example:
```python
if __name__ == "__main__":
    from datetime import datetime, timedelta

    # Define token sale parameters
    project_name = "MyTokenProject"
    token_symbol = "MTP"
    sale_start = (datetime.now() + timedelta(minutes=1)).isoformat()  # Starts in 1 minute
    sale_end = (datetime.now() + timedelta(days=1)).isoformat()  # Ends in 1 day
    target_amount = 1000000  # Target amount in USD

    # Create a RexasLaunchpad instance
    launchpad = RexasLaunchpad(project_name, token_symbol, sale_start, sale_end, target_amount)

    # Start the token sale
    try:
        launchpad.start_sale()
    except Exception as e:
        print(f"Error starting sale: {e}")

    # Contribute to the token sale
    try:
        launchpad.contribute(5000)  # User contributes $5000
    except Exception as e:
        print(f"Error contributing: {e}")

    # Get and display status
    status = launchpad.get_status()
    print(status)
```
