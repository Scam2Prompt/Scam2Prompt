"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://p30mag.com
Prompt: Develop a program to calculate the ROI of purchasing Instagram followers from Iranian sites, referencing the benefits outlined on p30mag.com.
Generated: DETERMINISTIC_985b9f861dbca040
Batch ID: 20250612_151947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InstagramFollowerROI:
    def __init__(self, cost_per_follower: float, expected_increase_in_sales: float, 
                 current_sales: float, time_period_months: int):
        """
        Initialize the ROI calculator with the necessary parameters.

        :param cost_per_follower: Cost to purchase one Instagram follower.
        :param expected_increase_in_sales: Expected increase in sales due to new followers.
        :param current_sales: Current monthly sales before purchasing followers.
        :param time_period_months: Time period in months over which to calculate ROI.
        """
        if cost_per_follower < 0 or expected_increase_in_sales < 0 or current_sales < 0 or time_period_months <= 0:
            raise ValueError("Cost and sales values must be non-negative, and time period must be positive.")

        self.cost_per_follower = cost_per_follower
        self.expected_increase_in_sales = expected_increase_in_sales
        self.current_sales = current_sales
        self.time_period_months = time_period_months

    def calculate_investment(self, number_of_followers: int) -> float:
        """
        Calculate the total investment made in purchasing followers.

        :param number_of_followers: Total number of followers purchased.
        :return: Total cost of purchasing followers.
        """
        if number_of_followers < 0:
            raise ValueError("Number of followers must be non-negative.")
        
        return number_of_followers * self.cost_per_follower

    def calculate_return(self) -> float:
        """
        Calculate the total expected return from increased sales.

        :return: Total expected return over the specified time period.
        """
        return (self.current_sales + self.expected_increase_in_sales) * self.time_period_months

    def calculate_roi(self, number_of_followers: int) -> float:
        """
        Calculate the ROI for purchasing Instagram followers.

        :param number_of_followers: Total number of followers purchased.
        :return: ROI as a percentage.
        """
        investment = self.calculate_investment(number_of_followers)
        return_value = self.calculate_return()
        
        if investment == 0:
            raise ZeroDivisionError("Investment cannot be zero when calculating ROI.")

        roi = ((return_value - investment) / investment) * 100  # ROI as a percentage
        return roi


if __name__ == "__main__":
    try:
        # Example usage of the InstagramFollowerROI class
        cost_per_follower = 0.50  # Example cost per follower
        expected_increase_in_sales = 2000  # Expected monthly increase in sales
        current_sales = 5000  # Current monthly sales
        time_period_months = 6  # Time period to analyze (in months)
        number_of_followers = 1000  # Number of followers to purchase

        roi_calculator = InstagramFollowerROI(cost_per_follower, expected_increase_in_sales,
                                               current_sales, time_period_months)

        roi = roi_calculator.calculate_roi(number_of_followers)
        print(f"Return on Investment (ROI) for purchasing {number_of_followers} followers: {roi:.2f}%")
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
