"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://biinance.online
Prompt: Write a function to calculate hosting plan costs and savings based on Hostinger's "Save 90%" offer for website hosting.
Generated: DETERMINISTIC_ca5c89905630f8f2
Batch ID: 20250612_150615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class HostingPlan:
    def __init__(self, original_price: float, discount_percentage: float):
        """
        Initialize a HostingPlan instance.

        :param original_price: The original price of the hosting plan.
        :param discount_percentage: The percentage discount being offered.
        """
        if original_price < 0:
            raise ValueError("Original price must be non-negative.")
        if discount_percentage < 0 or discount_percentage > 100:
            raise ValueError("Discount percentage must be between 0 and 100.")
        
        self.original_price = original_price
        self.discount_percentage = discount_percentage

    def calculate_discounted_price(self) -> float:
        """
        Calculate the discounted price after applying the discount.

        :return: The price after discount.
        """
        discount_amount = (self.original_price * self.discount_percentage) / 100
        discounted_price = self.original_price - discount_amount
        return discounted_price

    def calculate_savings(self) -> float:
        """
        Calculate the total savings based on the discount.

        :return: The amount saved due to the discount.
        """
        savings = (self.original_price * self.discount_percentage) / 100
        return savings

    def display_cost_details(self) -> None:
        """
        Display the original price, discounted price, and savings.
        """
        try:
            discounted_price = self.calculate_discounted_price()
            savings = self.calculate_savings()
            
            print(f"Original Price: ${self.original_price:.2f}")
            print(f"Discounted Price: ${discounted_price:.2f}")
            print(f"Savings: ${savings:.2f}")
        except Exception as e:
            print(f"An error occurred while calculating costs: {e}")


# Example Usage
if __name__ == "__main__":
    try:
        # Set original price and discount percentage for the hosting plan
        original_price = 100.0  # Example original price
        discount_percentage = 90  # Save 90%

        plan = HostingPlan(original_price, discount_percentage)
        plan.display_cost_details()
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
