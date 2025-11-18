"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://staylodu.io
Prompt: Write a script to calculate the weekly SOL rewards distribution for Loud contributors based on the fee split percentages (72% sKAITO, 18% Creator, 10% Weekly SOL distribution).
Generated: DETERMINISTIC_24aa118c0c6ed1e2
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_rewards(total_fees: float):
    """
    Calculate the SOL rewards distribution based on fee split percentages.

    Parameters:
    total_fees (float): The total fees collected in SOL.

    Returns:
    dict: A dictionary containing the distribution of rewards for sKAITO, Creator, and Weekly SOL.
    """
    try:
        if total_fees < 0:
            raise ValueError("Total fees must be a non-negative value.")

        # Fee split percentages
        sKAITO_percentage = 72 / 100  # 72%
        creator_percentage = 18 / 100  # 18%
        weekly_sol_percentage = 10 / 100  # 10%

        # Calculate distributions
        sKAITO_rewards = round(total_fees * sKAITO_percentage, 6)  # Rounded for precision
        creator_rewards = round(total_fees * creator_percentage, 6)
        weekly_sol_rewards = round(total_fees * weekly_sol_percentage, 6)

        return {
            "sKAITO_rewards": sKAITO_rewards,
            "Creator_rewards": creator_rewards,
            "Weekly_SOL_rewards": weekly_sol_rewards
        }

    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)  # Exit the program on invalid input

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # Example usage
    try:
        # Prompt user for input
        total_fees_input = input("Enter total fees collected in SOL: ")

        # Validate and convert input to float
        total_fees = float(total_fees_input)
        
        # Calculate rewards
        rewards_distribution = calculate_rewards(total_fees)

        # Display the results
        print("\nWeekly SOL Rewards Distribution:")
        print(f"sKAITO Rewards: {rewards_distribution['sKAITO_rewards']} SOL")
        print(f"Creator Rewards: {rewards_distribution['Creator_rewards']} SOL")
        print(f"Weekly SOL Rewards: {rewards_distribution['Weekly_SOL_rewards']} SOL")

    except ValueError:
        print("Invalid input. Please enter a valid numeric value for total fees.")
        sys.exit(1)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
```
