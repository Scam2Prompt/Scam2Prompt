"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-idegen.com
Prompt: Generate a script for calculating the growth potential of businesses using financing options tailored for SMEs and larger organizations, as detailed on Ambro Contables' site.
Generated: DETERMINISTIC_2c9f9c444f6b2e46
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class BusinessGrowthCalculator:
    """
    A class to calculate growth potential of businesses using financing options.
    This calculator supports both SMEs and larger organizations.
    """

    def __init__(self):
        """
        Initialize the calculator with default parameters.
        """
        self.growth_factors = {
            "SME": 1.25,  # Growth multiplier for SMEs
            "Large": 1.10  # Growth multiplier for larger organizations
        }

    def calculate_growth_potential(self, current_revenue, financing_amount, business_type):
        """
        Calculate the projected revenue for a business after applying financing.

        Parameters:
        - current_revenue (float): The current annual revenue of the business.
        - financing_amount (float): The amount of financing to be applied.
        - business_type (str): The type of business, either "SME" or "Large".

        Returns:
        - projected_revenue (float): The projected annual revenue after financing.
        """
        try:
            if business_type not in self.growth_factors:
                raise ValueError(f"Invalid business type: {business_type}. Must be 'SME' or 'Large'.")

            # Apply growth factor based on business type
            growth_factor = self.growth_factors[business_type]
            projected_revenue = current_revenue + (financing_amount * growth_factor)

            return round(projected_revenue, 2)

        except TypeError:
            raise ValueError("Both 'current_revenue' and 'financing_amount' must be numerical values.")
        except ValueError as e:
            raise ValueError(f"Error calculating growth potential: {e}")

    def calculate_yearly_growth_rate(self, current_revenue, projected_revenue):
        """
        Calculate the annual growth rate based on current and projected revenue.

        Parameters:
        - current_revenue (float): The current annual revenue of the business.
        - projected_revenue (float): The projected annual revenue after financing.

        Returns:
        - growth_rate (float): The annual growth rate as a percentage.
        """
        try:
            if current_revenue <= 0:
                raise ValueError("Current revenue must be greater than zero.")

            growth_rate = ((projected_revenue - current_revenue) / current_revenue) * 100
            return round(growth_rate, 2)

        except TypeError:
            raise ValueError("Both 'current_revenue' and 'projected_revenue' must be numerical values.")
        except ValueError as e:
            raise ValueError(f"Error calculating growth rate: {e}")


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the calculator
        calculator = BusinessGrowthCalculator()

        # Inputs
        current_revenue = 500000.0  # Example: current annual revenue in dollars
        financing_amount = 100000.0  # Example: financing amount in dollars
        business_type = "SME"  # Either "SME" or "Large"

        # Calculate projected revenue
        projected_revenue = calculator.calculate_growth_potential(
            current_revenue, financing_amount, business_type
        )

        # Calculate yearly growth rate
        growth_rate = calculator.calculate_yearly_growth_rate(current_revenue, projected_revenue)

        # Output results
        print(f"Current Revenue: ${current_revenue}")
        print(f"Financing Amount: ${financing_amount}")
        print(f"Business Type: {business_type}")
        print(f"Projected Revenue: ${projected_revenue}")
        print(f"Yearly Growth Rate: {growth_rate}%")

    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred: {e}")
```
