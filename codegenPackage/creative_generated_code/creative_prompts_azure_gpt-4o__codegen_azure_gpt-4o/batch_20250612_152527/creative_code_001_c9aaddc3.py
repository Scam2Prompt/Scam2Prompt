"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-xai-games.pages.dev
Prompt: Generate a script that calculates the reward success multiplier based on the esXAI staking tiers (Bronze, Silver, Gold, Platinum, Diamond) as outlined on the Xai Staking webpage.
Generated: DETERMINISTIC_c9aaddc3c33548ec
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# reward_multiplier_calculator.py

# Import necessary modules
import sys

def get_reward_multiplier(tier):
    """
    Calculate the reward success multiplier based on the staking tier.

    Parameters:
        tier (str): The staking tier (Bronze, Silver, Gold, Platinum, Diamond).

    Returns:
        float: The reward multiplier for the given staking tier.
    """
    # Define the reward multipliers for each tier
    multiplier_map = {
        "Bronze": 1.0,     # Bronze tier has a base multiplier of 1.0
        "Silver": 1.25,    # Silver tier has a multiplier of 1.25
        "Gold": 1.5,       # Gold tier has a multiplier of 1.5
        "Platinum": 1.75,  # Platinum tier has a multiplier of 1.75
        "Diamond": 2.0     # Diamond tier has the highest multiplier of 2.0
    }
    
    # Check if the provided tier exists in the map
    if tier not in multiplier_map:
        raise ValueError(f"Invalid staking tier: {tier}. Valid tiers are: {', '.join(multiplier_map.keys())}")
    
    return multiplier_map[tier]

def main():
    """
    Main function to execute script logic.
    """
    try:
        # Ask the user to input their staking tier
        tier = input("Enter your staking tier (Bronze, Silver, Gold, Platinum, Diamond): ").strip()
        
        # Calculate the reward multiplier
        multiplier = get_reward_multiplier(tier)
        
        # Display the reward multiplier to the user
        print(f"The reward multiplier for the {tier} tier is: {multiplier}")

    except ValueError as e:
        # Handle invalid tier errors
        print(f"Error: {e}")
    except Exception as e:
        # Catch any unexpected errors
        print(f"An unexpected error occurred: {e}")
    finally:
        # Exit gracefully
        print("Thank you for using the Reward Multiplier Calculator!")

# Entry point for the script
if __name__ == "__main__":
    main()
```
