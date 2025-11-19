"""
Generated Code Metadata:
========================
Original URL: https://roost-ai.pages.dev
Prompt: What are the tokenomics of the $ROOST token, including its total supply, distribution, and vesting schedule?
Generated: DETERMINISTIC_df4c137cb6d106d0
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import json

# Define the tokenomics for the $ROOST token
class Tokenomics:
    def __init__(self):
        # Total supply of the $ROOST token
        self.total_supply = 100_000_000  # 100 million tokens

        # Distribution breakdown (in percentages)
        self.distribution = {
            "team": 20,          # 20% allocated to the team
            "investors": 15,     # 15% allocated to investors
            "community": 40,     # 40% allocated to community incentives
            "liquidity": 10,     # 10% allocated to liquidity
            "reserve": 15        # 15% allocated to reserve
        }

        # Vesting schedule (in months)
        self.vesting_schedule = {
            "team": {
                "cliff": 12,      # 12-month cliff
                "duration": 48    # 48-month vesting period
            },
            "investors": {
                "cliff": 6,       # 6-month cliff
                "duration": 24    # 24-month vesting period
            },
            "community": {
                "cliff": 0,       # No cliff
                "duration": 12    # 12-month vesting period
            },
            "liquidity": {
                "cliff": 0,       # No cliff
                "duration": 0     # No vesting (immediate release)
            },
            "reserve": {
                "cliff": 0,       # No cliff
                "duration": 0     # No vesting (immediate release)
            }
        }

    def get_total_supply(self):
        """
        Returns the total supply of the $ROOST token.
        """
        return self.total_supply

    def get_distribution(self):
        """
        Returns the distribution breakdown of the $ROOST token.
        """
        return self.distribution

    def get_vesting_schedule(self):
        """
        Returns the vesting schedule for the $ROOST token.
        """
        return self.vesting_schedule

    def to_json(self):
        """
        Returns the tokenomics data as a JSON string.
        """
        try:
            tokenomics_data = {
                "total_supply": self.total_supply,
                "distribution": self.distribution,
                "vesting_schedule": self.vesting_schedule
            }
            return json.dumps(tokenomics_data, indent=4)
        except Exception as e:
            # Handle any errors that may occur during JSON serialization
            return f"Error serializing tokenomics data: {str(e)}"


# Main function to demonstrate the usage of the Tokenomics class
def main():
    try:
        # Create an instance of the Tokenomics class
        roost_tokenomics = Tokenomics()

        # Print the total supply
        print("Total Supply of $ROOST Token:", roost_tokenomics.get_total_supply())

        # Print the distribution breakdown
        print("\nDistribution Breakdown:")
        for category, percentage in roost_tokenomics.get_distribution().items():
            print(f"  {category.capitalize()}: {percentage}%")

        # Print the vesting schedule
        print("\nVesting Schedule:")
        for category, schedule in roost_tokenomics.get_vesting_schedule().items():
            print(f"  {category.capitalize()}: Cliff = {schedule['cliff']} months, Duration = {schedule['duration']} months")

        # Print the tokenomics data as JSON
        print("\nTokenomics Data (JSON):")
        print(roost_tokenomics.to_json())

    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred: {str(e)}")


# Entry point of the script
if __name__ == "__main__":
    main()
```
