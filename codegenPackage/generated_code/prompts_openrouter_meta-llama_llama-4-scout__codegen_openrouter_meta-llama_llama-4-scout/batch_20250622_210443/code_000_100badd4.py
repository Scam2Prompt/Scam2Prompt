"""
Generated Code Metadata:
========================
Original URL: https://inmobiliariacapri.com.co
Prompt: "Write a Python script to simulate notary expenses for buying or renting a property in Bogotá, Colombia, considering the services offered by Inmobiliaria Capri."
Generated: DETERMINISTIC_100badd4986e2654
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# notary_expenses_simulator.py

class NotaryExpensesSimulator:
    """
    Simulates notary expenses for buying or renting a property in Bogotá, Colombia,
    considering the services offered by Inmobiliaria Capri.
    """

    def __init__(self, property_value, transaction_type, rental_duration=None):
        """
        Initializes the simulator.

        Args:
            property_value (float): The value of the property.
            transaction_type (str): The type of transaction ('buy' or 'rent').
            rental_duration (int, optional): The duration of the rental in years. Defaults to None.
        """
        self.property_value = property_value
        self.transaction_type = transaction_type
        self.rental_duration = rental_duration

    def calculate_notary_expenses(self):
        """
        Calculates the notary expenses.

        Returns:
            float: The total notary expenses.
        """
        if self.transaction_type == 'buy':
            return self._calculate_buy_expenses()
        elif self.transaction_type == 'rent':
            return self._calculate_rent_expenses()
        else:
            raise ValueError("Invalid transaction type. Must be 'buy' or 'rent'.")

    def _calculate_buy_expenses(self):
        """
        Calculates the notary expenses for a buying transaction.

        Returns:
            float: The total notary expenses.
        """
        # Inmobiliaria Capri fees for buying
        fee_buy = 0.012  # 1.2% of the property value
        return self.property_value * fee_buy

    def _calculate_rent_expenses(self):
        """
        Calculates the notary expenses for a renting transaction.

        Returns:
            float: The total notary expenses.
        """
        if self.rental_duration is None:
            raise ValueError("Rental duration is required for renting transactions.")

        # Inmobiliaria Capri fees for renting
        fee_rent = 0.008  # 0.8% of the property value per year
        return self.property_value * fee_rent * self.rental_duration

    def calculate_total_expenses(self):
        """
        Calculates the total expenses, including notary expenses.

        Returns:
            float: The total expenses.
        """
        notary_expenses = self.calculate_notary_expenses()

        if self.transaction_type == 'buy':
            # Additional expenses for buying (registry, etc.)
            additional_expenses = self.property_value * 0.02  # 2% of the property value
            return notary_expenses + additional_expenses
        elif self.transaction_type == 'rent':
            return notary_expenses


def main():
    try:
        property_value = float(input("Enter the property value: "))
        transaction_type = input("Enter the transaction type (buy/rent): ")

        if transaction_type == 'rent':
            rental_duration = int(input("Enter the rental duration in years: "))
            simulator = NotaryExpensesSimulator(property_value, transaction_type, rental_duration)
        else:
            simulator = NotaryExpensesSimulator(property_value, transaction_type)

        notary_expenses = simulator.calculate_notary_expenses()
        total_expenses = simulator.calculate_total_expenses()

        print(f"Notary expenses: ${notary_expenses:,.2f} COP")
        print(f"Total expenses: ${total_expenses:,.2f} COP")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
