"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dre-8x7.pages.dev
Prompt: Generate code to implement a tiered presale system where contributors receive different amounts of DRE tokens based on their FTM contributions (e.g., 250, 500, 1000, 2000, 3000 FTM).
Generated: DETERMINISTIC_fe2d046aede10b7f
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the implementation of a tiered presale system in Python:

```python
class TieredPresaleSystem:
    """
    A class to implement a tiered presale system where contributors receive DRE tokens
    based on their FTM contributions.
    """
    
    def __init__(self):
        """
        Initialize the presale system with predefined tiers and their respective reward rates.
        """
        # Define the tiers with minimum FTM contributions and corresponding DRE reward rates
        self.tiers = {
            250: 500,   # Tier 1: Min 250 FTM = 500 DRE tokens rewarded
            500: 1100,  # Tier 2: Min 500 FTM = 1100 DRE tokens rewarded
            1000: 2500, # Tier 3: Min 1000 FTM = 2500 DRE tokens rewarded
            2000: 6000, # Tier 4: Min 2000 FTM = 6000 DRE tokens rewarded
            3000: 10000 # Tier 5: Min 3000 FTM = 10000 DRE tokens rewarded
        }
    
    def calculate_rewards(self, ftm_contribution):
        """
        Calculate the number of DRE tokens a user qualifies for based on their FTM contribution.

        :param ftm_contribution: Integer, the amount of FTM tokens contributed by the user.
        :return: Integer, the number of DRE tokens the user qualifies for.
        :raises ValueError: If the contribution is less than the minimum tier requirement.
        """
        if not isinstance(ftm_contribution, (int, float)) or ftm_contribution < 250:
            raise ValueError("FTM contribution must be at least 250 and a valid number.")

        # Sort tiers in descending order to find the highest matching tier
        for tier in sorted(self.tiers.keys(), reverse=True):
            if ftm_contribution >= tier:
                return self.tiers[tier]

        # If no tier matches, this shouldn't normally happen due to validation above
        raise ValueError("No matching tier found for the given contribution.")

    def run_presale(self):
        """
        Run the presale system to accept contributions and calculate rewards.
        """
        print("Welcome to the DRE Token Presale!")
        try:
            # Get user input for FTM contribution
            ftm_contribution = float(input("Enter your FTM contribution: "))
            reward = self.calculate_rewards(ftm_contribution)
            print(f"Thank you for your contribution of {ftm_contribution} FTM.")
            print(f"You qualify for {reward} DRE tokens!")
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


# Main entry point
if __name__ == "__main__":
    # Create an instance of the presale system and run it
    presale = TieredPresaleSystem()
    presale.run_presale()
```

This Python code implements a tiered presale system based on the request. It uses a dictionary to define contribution tiers and their respective reward rates, includes error handling for invalid inputs, and adheres to best practices.
