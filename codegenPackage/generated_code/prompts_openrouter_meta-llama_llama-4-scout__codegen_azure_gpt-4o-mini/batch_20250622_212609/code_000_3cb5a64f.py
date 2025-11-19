"""
Generated Code Metadata:
========================
Original URL: https://currency-connect.com
Prompt: Write a Python code snippet to calculate the cost savings of using a specialized currency exchange service like Currency Connect for international payments, compared to traditional bank conversion rates.
Generated: DETERMINISTIC_3cb5a64f80802ffa
Batch ID: 20250622_212609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CurrencyExchangeService:
    """
    A class to represent a currency exchange service for calculating cost savings
    compared to traditional bank conversion rates.
    """

    def __init__(self, bank_rate: float, service_rate: float):
        """
        Initializes the CurrencyExchangeService with bank and service rates.

        :param bank_rate: The conversion rate offered by the traditional bank.
        :param service_rate: The conversion rate offered by the specialized service.
        """
        if bank_rate <= 0 or service_rate <= 0:
            raise ValueError("Rates must be positive values.")
        
        self.bank_rate = bank_rate
        self.service_rate = service_rate

    def calculate_cost(self, amount: float) -> dict:
        """
        Calculates the cost of currency conversion using both bank and service rates.

        :param amount: The amount of money to be converted.
        :return: A dictionary containing the costs for both methods and the savings.
        """
        if amount <= 0:
            raise ValueError("Amount must be a positive value.")

        # Calculate costs
        bank_cost = amount * self.bank_rate
        service_cost = amount * self.service_rate
        savings = bank_cost - service_cost

        return {
            "bank_cost": bank_cost,
            "service_cost": service_cost,
            "savings": savings
        }


def main():
    """
    Main function to demonstrate the cost savings calculation.
    """
    try:
        # Example rates (these would be fetched from a reliable source in a real application)
        bank_conversion_rate = 1.2  # Example bank conversion rate
        service_conversion_rate = 1.1  # Example service conversion rate
        amount_to_convert = 1000  # Amount in the base currency

        # Create an instance of CurrencyExchangeService
        exchange_service = CurrencyExchangeService(bank_conversion_rate, service_conversion_rate)

        # Calculate costs and savings
        result = exchange_service.calculate_cost(amount_to_convert)

        # Display the results
        print(f"Bank Cost: ${result['bank_cost']:.2f}")
        print(f"Service Cost: ${result['service_cost']:.2f}")
        print(f"Savings: ${result['savings']:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
