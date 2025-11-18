"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://halosocial.vercel.app
Prompt: Write a script to calculate and distribute Halo XP and token rewards to users based on their contributions within the halo.social ecosystem.
Generated: DETERMINISTIC_2fbcb796eccddd90
Batch ID: 20250612_154339
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def calculate_rewards(contributions, total_xp_pool, total_token_pool):
    """
    Calculate XP and token rewards based on user contributions.

    Args:
        contributions (dict): A dictionary where keys are user IDs and values are their contribution scores.
        total_xp_pool (int): Total amount of XP to distribute.
        total_token_pool (int): Total amount of tokens to distribute.

    Returns:
        dict: A dictionary with user IDs as keys and their rewards (XP and tokens) as values.
    """
    rewards = {}
    total_contributions = sum(contributions.values())

    if total_contributions == 0:
        raise ValueError("Total contributions cannot be zero.")

    for user_id, contribution in contributions.items():
        user_xp = (contribution / total_contributions) * total_xp_pool
        user_tokens = (contribution / total_contributions) * total_token_pool
        rewards[user_id] = {
            "xp": round(user_xp, 2),
            "tokens": round(user_tokens, 2)
        }

    return rewards


def save_rewards_to_file(rewards, file_path):
    """
    Save the rewards to a JSON file for persistence.

    Args:
        rewards (dict): The dictionary containing user rewards.
        file_path (str): Path to the output JSON file.

    Returns:
        None
    """
    try:
        with open(file_path, 'w') as file:
            json.dump(rewards, file, indent=4)
        print(f"Rewards successfully saved to {file_path}")
    except IOError as e:
        print(f"Error saving rewards to file: {e}")


def main():
    """
    Main function to calculate and distribute XP and token rewards.
    """
    # Example user contributions
    contributions = {
        "user1": 120,
        "user2": 80,
        "user3": 200,
        "user4": 0
    }

    total_xp_pool = 1000  # Total XP to distribute
    total_token_pool = 500  # Total tokens to distribute

    try:
        rewards = calculate_rewards(contributions, total_xp_pool, total_token_pool)

        # Print the rewards to the console
        print("Calculated Rewards:")
        for user_id, reward in rewards.items():
            print(f"{user_id}: XP = {reward['xp']}, Tokens = {reward['tokens']}")

        # Save rewards to a JSON file
        save_rewards_to_file(rewards, "rewards.json")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
