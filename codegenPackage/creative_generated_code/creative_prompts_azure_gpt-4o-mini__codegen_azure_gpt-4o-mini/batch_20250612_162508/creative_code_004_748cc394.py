"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://longhuigolf.com
Prompt: Create a function that calculates the cost of custom golf grips, taking into account the variables mentioned on the Longhui Golf site, such as logo and shipping.
Generated: DETERMINISTIC_748cc394f0c2280e
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class GolfGripCalculator:
    """
    A class to calculate the total cost of custom golf grips based on various parameters.
    """

    BASE_PRICE_PER_GRIP = 10.00  # Base price for a single custom golf grip
    LOGO_COST = 2.50              # Additional cost for adding a logo
    SHIPPING_COST = 5.00          # Flat shipping cost

    def __init__(self, number_of_grips: int, logo: bool, expedited_shipping: bool):
        """
        Initializes the GolfGripCalculator with the number of grips, logo option, and shipping preference.

        :param number_of_grips: Number of custom golf grips to order
        :param logo: Boolean indicating if a logo is required
        :param expedited_shipping: Boolean indicating if expedited shipping is selected
        """
        if number_of_grips <= 0:
            raise ValueError("Number of grips must be a positive integer.")
        
        self.number_of_grips = number_of_grips
        self.logo = logo
        self.expedited_shipping = expedited_shipping

    def calculate_cost(self) -> float:
        """
        Calculates the total cost of the custom golf grips.

        :return: Total cost as a float
        """
        try:
            total_cost = self.number_of_grips * self.BASE_PRICE_PER_GRIP
            
            # Add logo cost if applicable
            if self.logo:
                total_cost += self.LOGO_COST
            
            # Add shipping cost
            total_cost += self.SHIPPING_COST
            
            # Add expedited shipping cost if necessary
            if self.expedited_shipping:
                total_cost += 10.00  # Additional cost for expedited shipping
            
            return total_cost
        except Exception as e:
            raise RuntimeError("An error occurred while calculating the cost.") from e

# Example usage:
if __name__ == "__main__":
    try:
        grip_calculator = GolfGripCalculator(number_of_grips=5, logo=True, expedited_shipping=False)
        total_cost = grip_calculator.calculate_cost()
        print(f"The total cost for custom golf grips is: ${total_cost:.2f}")
    except Exception as e:
        print(f"Error: {str(e)}")
```
