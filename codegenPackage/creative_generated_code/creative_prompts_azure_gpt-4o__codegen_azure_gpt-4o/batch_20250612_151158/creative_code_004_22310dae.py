"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sharplabs.pages.dev
Prompt: Write code to calculate Sharpe Points earned by interacting with Sharpe AI products, such as trading perpetual swaps, bridging funds, and swapping assets.
Generated: DETERMINISTIC_22310dae36554f83
Batch ID: 20250612_151158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SharpePointsCalculator:
    """
    A class to calculate Sharpe Points earned by interacting with Sharpe AI products.
    """
    
    def __init__(self):
        """
        Initialize the SharpePointsCalculator class with activity multipliers.
        """
        # Define multipliers for different activities
        self.activity_multipliers = {
            "trade_perpetual_swaps": 1.5,
            "bridge_funds": 1.2,
            "swap_assets": 1.0
        }

    def calculate_points(self, activity, amount):
        """
        Calculate Sharpe Points based on activity type and amount.

        Args:
            activity (str): The type of activity (e.g., "trade_perpetual_swaps").
            amount (float): The amount associated with the activity.

        Returns:
            float: The calculated Sharpe Points.

        Raises:
            ValueError: If the activity type is invalid.
        """
        try:
            # Validate activity type
            if activity not in self.activity_multipliers:
                raise ValueError(f"Invalid activity type: {activity}")

            # Calculate Sharpe Points
            multiplier = self.activity_multipliers[activity]
            points = amount * multiplier
            logging.info(f"Calculated {points} Sharpe Points for activity '{activity}' with amount {amount}.")
            return points

        except Exception as e:
            logging.error(f"Error in calculating points: {e}")
            raise

    def calculate_total_points(self, activities):
        """
        Calculate total Sharpe Points for multiple activities.

        Args:
            activities (list of dict): A list of activity dictionaries with keys "activity" and "amount".

        Returns:
            float: The total Sharpe Points earned.

        Raises:
            ValueError: If input format is invalid or any activity type is invalid.
        """
        try:
            # Validate input format
            if not isinstance(activities, list) or not all(isinstance(activity, dict) for activity in activities):
                raise ValueError("Invalid input format. Expected a list of dictionaries with 'activity' and 'amount' keys.")

            total_points = 0
            for activity_data in activities:
                activity = activity_data.get("activity")
                amount = activity_data.get("amount")

                if activity is None or amount is None:
                    raise ValueError(f"Missing 'activity' or 'amount' in activity data: {activity_data}")

                # Accumulate Sharpe Points
                total_points += self.calculate_points(activity, amount)

            logging.info(f"Total Sharpe Points calculated: {total_points}")
            return total_points

        except Exception as e:
            logging.error(f"Error in calculating total points: {e}")
            raise


# Example usage
if __name__ == "__main__":
    try:
        # Instantiate the calculator
        calculator = SharpePointsCalculator()

        # Define activities and amounts
        activities = [
            {"activity": "trade_perpetual_swaps", "amount": 5000},
            {"activity": "bridge_funds", "amount": 3000},
            {"activity": "swap_assets", "amount": 2000}
        ]

        # Calculate total Sharpe Points
        total_points = calculator.calculate_total_points(activities)
        print(f"Total Sharpe Points earned: {total_points}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
