"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hyperblox.vercel.app
Prompt: Generate code to calculate and apply point multipliers for earning HPB Tokens during the HPB Hunt campaign, referencing Nexo's reward system.
Generated: DETERMINISTIC_9dc38d6b9ee00ee6
Batch ID: 20250612_153925
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class HPBHunt:
    """
    A class to calculate and apply point multipliers for earning HPB Tokens during the HPB Hunt campaign.
    """

    def __init__(self, base_points):
        """
        Initializes the HPBHunt instance with a base point value.

        :param base_points: The initial number of points earned.
        """
        if base_points < 0:
            raise ValueError("Base points must be a non-negative integer.")
        self.base_points = base_points
        self.multipliers = []

    def add_multiplier(self, multiplier):
        """
        Adds a point multiplier to the list of multipliers.

        :param multiplier: A float representing the multiplier to be added.
        :raises ValueError: If the multiplier is less than or equal to zero.
        """
        if multiplier <= 0:
            raise ValueError("Multiplier must be greater than zero.")
        self.multipliers.append(multiplier)

    def calculate_total_points(self):
        """
        Calculates the total points earned after applying all multipliers.

        :return: Total points as a float after applying multipliers.
        """
        total_points = self.base_points
        for multiplier in self.multipliers:
            total_points *= multiplier
        return total_points

    def apply_rewards(self):
        """
        Applies the calculated rewards based on the total points.

        :return: A formatted string representing the earned HPB Tokens.
        """
        try:
            total_points = self.calculate_total_points()
            return f"Earning HPB Tokens: {total_points:.2f}"
        except Exception as e:
            return f"Error calculating rewards: {str(e)}"


if __name__ == "__main__":
    try:
        # Initialize the HPB Hunt with base points.
        hpb_hunt = HPBHunt(base_points=100)

        # Add point multipliers for the campaign.
        hpb_hunt.add_multiplier(1.5)  # 50% increase
        hpb_hunt.add_multiplier(2.0)   # 100% increase

        # Calculate and print the total HPB Tokens earned.
        print(hpb_hunt.apply_rewards())

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
