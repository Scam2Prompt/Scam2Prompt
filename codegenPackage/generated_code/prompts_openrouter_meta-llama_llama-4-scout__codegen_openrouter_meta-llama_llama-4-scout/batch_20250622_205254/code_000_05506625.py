"""
Generated Code Metadata:
========================
Original URL: https://curve.fr
Prompt: Write a Python script to facilitate domain name transactions, including calculating the total cost of purchasing a domain name like curve.fr, considering the sale price and annual renewal fees.
Generated: DETERMINISTIC_05506625a954056c
Batch ID: 20250622_205254
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# domain_transaction.py

class Domain:
    def __init__(self, name, sale_price, annual_renewal_fee):
        """
        Initialize a Domain object.

        Args:
            name (str): The domain name.
            sale_price (float): The sale price of the domain.
            annual_renewal_fee (float): The annual renewal fee of the domain.
        """
        self.name = name
        self.sale_price = sale_price
        self.annual_renewal_fee = annual_renewal_fee

    def calculate_total_cost(self, years):
        """
        Calculate the total cost of purchasing and renewing the domain.

        Args:
            years (int): The number of years to calculate the total cost for.

        Returns:
            float: The total cost.

        Raises:
            ValueError: If the number of years is less than 1.
        """
        if years < 1:
            raise ValueError("Number of years must be 1 or more")

        # Calculate the total cost as the sale price plus the renewal fees for the given number of years
        total_cost = self.sale_price + (self.annual_renewal_fee * years)
        return total_cost


class DomainTransaction:
    def __init__(self):
        """
        Initialize a DomainTransaction object.
        """
        self.domains = {}

    def add_domain(self, domain):
        """
        Add a domain to the transaction.

        Args:
            domain (Domain): The domain to add.
        """
        self.domains[domain.name] = domain

    def calculate_total_transaction_cost(self, years):
        """
        Calculate the total cost of all domains in the transaction.

        Args:
            years (int): The number of years to calculate the total cost for.

        Returns:
            float: The total cost.

        Raises:
            ValueError: If the number of years is less than 1.
        """
        if years < 1:
            raise ValueError("Number of years must be 1 or more")

        total_cost = 0
        for domain in self.domains.values():
            total_cost += domain.calculate_total_cost(years)
        return total_cost


def main():
    try:
        # Create a domain transaction
        transaction = DomainTransaction()

        # Create a domain
        curve_fr = Domain("curve.fr", 1000.0, 20.0)
        transaction.add_domain(curve_fr)

        # Calculate the total cost for 5 years
        years = 5
        total_cost = transaction.calculate_total_transaction_cost(years)

        print(f"The total cost of purchasing curve.fr for {years} years is: ${total_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
