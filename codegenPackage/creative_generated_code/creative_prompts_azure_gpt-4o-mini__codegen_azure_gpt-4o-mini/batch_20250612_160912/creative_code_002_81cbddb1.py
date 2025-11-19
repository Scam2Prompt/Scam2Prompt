"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://balajitravelsonline.com
Prompt: Write a code snippet to calculate the total cost for a family tour package from Chennai to Kodaikanal using the pricing details from Balaji Tours and Travels.
Generated: DETERMINISTIC_81cbddb1663e65db
Batch ID: 20250612_160912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TourPackage:
    """
    Class to represent a family tour package from Chennai to Kodaikanal.
    """

    def __init__(self, base_price, adult_count, child_count, discount_rate=0):
        """
        Initializes the TourPackage with pricing details.

        :param base_price: Base price per person for the tour package
        :param adult_count: Number of adults in the family
        :param child_count: Number of children in the family
        :param discount_rate: Discount rate applicable (percentage)
        """
        self.base_price = base_price
        self.adult_count = adult_count
        self.child_count = child_count
        self.discount_rate = discount_rate

    def calculate_total_cost(self):
        """
        Calculates the total cost for the family tour package.

        :return: Total cost after applying discount
        """
        try:
            if self.base_price < 0 or self.adult_count < 0 or self.child_count < 0 or self.discount_rate < 0:
                raise ValueError("Pricing details cannot be negative.")

            # Calculate total cost without discount
            total_cost = (self.adult_count + self.child_count) * self.base_price
            
            # Apply discount if applicable
            if self.discount_rate > 0:
                discount_amount = total_cost * (self.discount_rate / 100)
                total_cost -= discount_amount
            
            return total_cost

        except ValueError as ve:
            print(f"Error: {ve}")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None


# Example of usage
if __name__ == "__main__":
    # Pricing details from Balaji Tours and Travels
    base_price_per_person = 5000  # Price for one person
    number_of_adults = 2           # Number of adults
    number_of_children = 2         # Number of children
    discount = 10                  # 10% discount

    # Create a TourPackage instance
    tour_package = TourPackage(base_price_per_person, number_of_adults, number_of_children, discount)

    # Calculate total cost
    total_cost = tour_package.calculate_total_cost()
    
    if total_cost is not None:
        print(f"The total cost for the family tour package is: ₹{total_cost:.2f}")
```
