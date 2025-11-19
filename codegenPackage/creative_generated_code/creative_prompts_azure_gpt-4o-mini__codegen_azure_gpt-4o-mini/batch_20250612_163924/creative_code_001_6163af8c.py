"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://passandbrazzz.blogspot.com
Prompt: Write a function that calculates the total cost of purchasing a commercial property, using the example of a lighting store priced at R$ 350.000 in São Paulo.
Generated: DETERMINISTIC_6163af8c7e744c00
Batch ID: 20250612_163924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class PropertyPurchase:
    def __init__(self, price: float, tax_rate: float = 0.02, additional_fees: float = 5000.0):
        """
        Initializes the PropertyPurchase instance.

        :param price: The base price of the property.
        :param tax_rate: The tax rate applied to the property purchase.
        :param additional_fees: Any additional fees incurred during the purchase.
        """
        self.price = price
        self.tax_rate = tax_rate
        self.additional_fees = additional_fees

    def calculate_total_cost(self) -> float:
        """
        Calculates the total cost of purchasing the property including taxes and additional fees.

        :return: The total cost as a float.
        """
        try:
            # Calculate taxes based on the price
            taxes = self.price * self.tax_rate
            # Calculate total cost
            total_cost = self.price + taxes + self.additional_fees
            return total_cost
        except Exception as e:
            print(f"An error occurred while calculating the total cost: {e}")
            return 0.0


def main():
    # Example property: a lighting store in São Paulo priced at R$ 350,000
    property_price = 350000.0

    # Create an instance of PropertyPurchase
    purchase = PropertyPurchase(price=property_price)

    # Calculate total cost
    total_cost = purchase.calculate_total_cost()

    # Display the total cost
    print(f"The total cost of purchasing the property is: R$ {total_cost:.2f}")


if __name__ == "__main__":
    main()
```
