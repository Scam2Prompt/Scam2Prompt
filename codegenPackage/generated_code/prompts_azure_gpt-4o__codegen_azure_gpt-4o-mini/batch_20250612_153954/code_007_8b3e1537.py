"""
Generated Code Metadata:
========================
Original URL: https://trollercat-claim.pages.dev
Prompt: Generate a script to calculate the price increase for $TCAT tokens based on the presale stage and display the next stage price percentage change.
Generated: DETERMINISTIC_8b3e153725d0210e
Batch ID: 20250612_153954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TCATPriceCalculator:
    """
    A class to calculate the price increase of TCAT tokens based on the presale stage.
    """

    def __init__(self):
        # Define the price stages as a dictionary
        self.price_stages = {
            "Stage 1": 0.10,  # Price in USD
            "Stage 2": 0.15,
            "Stage 3": 0.20,
            "Stage 4": 0.25,
            "Stage 5": 0.30
        }
        self.stages = list(self.price_stages.keys())

    def get_current_stage(self, current_stage):
        """
        Get the current stage index based on the provided stage name.

        :param current_stage: The name of the current presale stage.
        :return: The index of the current stage or None if invalid.
        """
        try:
            return self.stages.index(current_stage)
        except ValueError:
            print(f"Error: '{current_stage}' is not a valid presale stage.")
            return None

    def calculate_price_increase(self, current_stage):
        """
        Calculate the price increase percentage to the next stage.

        :param current_stage: The name of the current presale stage.
        :return: The percentage increase to the next stage or None if invalid.
        """
        current_index = self.get_current_stage(current_stage)
        if current_index is None or current_index >= len(self.stages) - 1:
            print("Error: No next stage available or invalid current stage.")
            return None

        next_stage = self.stages[current_index + 1]
        current_price = self.price_stages[current_stage]
        next_price = self.price_stages[next_stage]

        # Calculate the percentage increase
        price_increase_percentage = ((next_price - current_price) / current_price) * 100
        return price_increase_percentage

    def display_next_stage_price_change(self, current_stage):
        """
        Display the price change percentage to the next stage.

        :param current_stage: The name of the current presale stage.
        """
        price_change = self.calculate_price_increase(current_stage)
        if price_change is not None:
            print(f"The price increase from '{current_stage}' to the next stage is: {price_change:.2f}%")

# Example usage
if __name__ == "__main__":
    calculator = TCATPriceCalculator()
    current_stage_input = input("Enter the current presale stage (e.g., 'Stage 1'): ")
    calculator.display_next_stage_price_change(current_stage_input)
```
