"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://libertyaid.co
Prompt: Write a program to estimate yearly savings on auto insurance using Auto Shield+ discounts and safe driving rewards.
Generated: DETERMINISTIC_311ae1f267b6b5bf
Batch ID: 20250612_154942
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class AutoInsuranceEstimator:
    """
    A class to estimate yearly savings on auto insurance using Auto Shield+ discounts and safe driving rewards.
    """

    def __init__(self, base_premium: float):
        """
        Initializes the estimator with the base premium of the auto insurance.

        :param base_premium: The base premium amount for the automobile insurance.
        """
        if base_premium < 0:
            raise ValueError("Base premium must be a non-negative value.")
        self.base_premium = base_premium
        self.discounts = []

    def add_discount(self, discount_percentage: float):
        """
        Adds a discount to the estimator.

        :param discount_percentage: The discount percentage to be applied (0-100).
        """
        if not (0 <= discount_percentage <= 100):
            raise ValueError("Discount percentage must be between 0 and 100.")
        self.discounts.append(discount_percentage)

    def calculate_total_discount(self) -> float:
        """
        Calculates the total discount from all added discounts.

        :return: Total discount amount as a percentage.
        """
        total_discount = sum(self.discounts)
        return min(total_discount, 100)  # Cap the discount at 100%

    def estimate_yearly_savings(self) -> float:
        """
        Estimates the yearly savings on auto insurance based on discounts and base premium.

        :return: Estimated yearly savings.
        """
        total_discount = self.calculate_total_discount()
        savings = (total_discount / 100) * self.base_premium
        return savings

    def display_estimate(self):
        """
        Displays the estimated yearly savings and the details of discounts applied.
        """
        try:
            savings = self.estimate_yearly_savings()
            print(f"Base Premium: ${self.base_premium:.2f}")
            print(f"Total Discounts Applied: {self.calculate_total_discount():.2f}%")
            print(f"Estimated Yearly Savings: ${savings:.2f}")
        except Exception as e:
            print(f"Error calculating savings: {e}")


# Example usage
if __name__ == "__main__":
    try:
        estimator = AutoInsuranceEstimator(base_premium=1200.00)
        estimator.add_discount(10)  # 10% safe driving reward
        estimator.add_discount(15)  # 15% Auto Shield+ discount
        estimator.display_estimate()
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
