"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://infoextranjeros.com
Prompt: How can I set up a business in Spain while ensuring all legal aspects related to foreign investment are properly managed?
Generated: DETERMINISTIC_304a5db60118f7e7
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BusinessSetupSpain:
    """
    A class to manage the setup of a business in Spain, ensuring compliance 
    with legal aspects related to foreign investment.
    """

    def __init__(self, business_name: str, owner_name: str, investment_amount: float):
        """
        Initializes the BusinessSetupSpain class with necessary details.

        :param business_name: Name of the business to be set up
        :param owner_name: Name of the business owner
        :param investment_amount: Amount of money being invested into the business
        """
        self.business_name = business_name
        self.owner_name = owner_name
        self.investment_amount = investment_amount

    def validate_investment(self):
        """
        Validates the investment amount to ensure it meets minimum requirements.

        :raises ValueError: If the investment amount is below the minimum threshold.
        """
        minimum_investment = 3000  # Example minimum investment requirement in EUR
        if self.investment_amount < minimum_investment:
            raise ValueError(f"Investment amount must be at least {minimum_investment} EUR.")

    def register_business(self):
        """
        Simulates the process of registering the business in Spain.
        """
        try:
            self.validate_investment()
            print(f"Registering business '{self.business_name}' owned by '{self.owner_name}' with an investment of {self.investment_amount} EUR.")
            # Simulated registration logic; replace with actual registration code
            print("Business registration successful.")
        except ValueError as ve:
            print(f"Error during business registration: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def obtain_nif(self):
        """
        Simulates obtaining a Tax Identification Number (NIF) required in Spain.
        """
        try:
            print(f"Obtaining NIF for business '{self.business_name}'...")
            # Simulated process for obtaining NIF; replace with actual logic
            print("NIF obtained successfully.")
        except Exception as e:
            print(f"Error obtaining NIF: {e}")

    def setup_business(self):
        """
        Sets up the business by executing required steps in order.
        """
        self.register_business()
        self.obtain_nif()

# Example usage:
if __name__ == "__main__":
    try:
        business = BusinessSetupSpain(business_name="My Spanish Business", owner_name="John Doe", investment_amount=5000)
        business.setup_business()
    except Exception as e:
        print(f"Failed to set up the business: {e}")
```
