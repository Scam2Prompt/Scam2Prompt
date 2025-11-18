"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dashboard-gpu.pages.dev
Prompt: Generate a script to calculate rewards multipliers based on Node Score and Validator health (NH = 1) within the GPUnet ecosystem.
Generated: DETERMINISTIC_64669b9dac42b13e
Batch ID: 20250612_145715
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# rewards_multiplier_calculator.py

class GPUnetRewardsCalculator:
    """
    A class to calculate rewards multipliers based on Node Score and Validator health.
    """

    def __init__(self, node_score, validator_health):
        """
        Initializes the rewards calculator with node score and validator health.

        Parameters:
        node_score (float): The score of the node, should be between 0 and 1.
        validator_health (int): The health of the validator, should be 1 for healthy validators.
        """
        self.node_score = node_score
        self.validator_health = validator_health

        # Validate inputs
        self.validate_inputs()

    def validate_inputs(self):
        """
        Validates the input parameters for the calculator.
        Raises ValueError for invalid inputs.
        """
        if not (0 <= self.node_score <= 1):
            raise ValueError("Node Score must be between 0 and 1.")
        if self.validator_health != 1:
            raise ValueError("Validator Health must be 1 (healthy).")

    def calculate_multiplier(self):
        """
        Calculates the rewards multiplier based on the node score and validator health.

        Returns:
        float: The calculated rewards multiplier.
        """
        # Basic multiplier calculation
        multiplier = 1.0  # Base multiplier for healthy validators

        # Increase multiplier based on node score
        multiplier += self.node_score * 0.5  # adjust the scaling factor as needed

        return multiplier

def main():
    """
    Main function to run the rewards multiplier calculator.
    """
    try:
        # Sample inputs; these could be dynamically obtained from user input or an API
        node_score = float(input("Enter Node Score (0 to 1): "))
        validator_health = int(input("Enter Validator Health (1 for healthy): "))

        # Create instance of rewards calculator
        calculator = GPUnetRewardsCalculator(node_score, validator_health)

        # Calculate and print the rewards multiplier
        multiplier = calculator.calculate_multiplier()
        print(f"Calculated Rewards Multiplier: {multiplier:.2f}")

    except ValueError as e:
        print(f"Input Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
