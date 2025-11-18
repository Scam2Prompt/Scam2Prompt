"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://codes-bigtime.pages.dev
Prompt: Write a script to calculate bonus rolls during item crafting in Big Time, displaying probabilities and potential rewards.
Generated: DETERMINISTIC_009c6944c719aac3
Batch ID: 20250612_151003
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

def calculate_bonus_rolls(base_chance, num_rolls, potential_rewards):
    """
    Calculate bonus rolls during item crafting in Big Time.
    
    :param base_chance: float - Base percentage chance of a bonus roll (0-100).
    :param num_rolls: int - Number of crafting attempts.
    :param potential_rewards: list - List of potential rewards for bonus rolls.
    :return: dict - Summary containing probabilities and results.
    """
    # Validate inputs
    if not (0 <= base_chance <= 100):
        raise ValueError("Base chance must be between 0 and 100.")
    if num_rolls <= 0:
        raise ValueError("Number of rolls must be greater than 0.")
    if len(potential_rewards) == 0:
        raise ValueError("Potential rewards list cannot be empty.")
    
    # Convert base chance to a decimal probability
    base_probability = base_chance / 100.0
    
    # Initialize result tracking
    successful_rolls = 0
    rewards = []

    # Perform crafting attempts
    for _ in range(num_rolls):
        # Simulate a random roll
        if random.random() <= base_probability:
            successful_rolls += 1
            # Randomly select a reward from the potential rewards
            rewards.append(random.choice(potential_rewards))
    
    # Calculate probabilities
    roll_probability = base_probability
    success_rate = (successful_rolls / num_rolls) * 100

    # Return summary of results
    return {
        "base_probability": roll_probability,
        "success_rate": success_rate,
        "successful_rolls": successful_rolls,
        "rewards": rewards
    }

def main():
    """
    Main function to execute the bonus roll calculation.
    """
    # Example inputs
    base_chance = 25.0  # 25% chance for a bonus roll
    num_rolls = 10  # Number of crafting attempts
    potential_rewards = ["Rare Gem", "Epic Weapon", "Legendary Armor", "Gold Coins"]
    
    try:
        # Calculate bonus rolls
        result = calculate_bonus_rolls(base_chance, num_rolls, potential_rewards)
        
        # Display the results
        print("Bonus Roll Calculation Results:")
        print(f"Base Probability: {result['base_probability'] * 100}%")
        print(f"Success Rate: {result['success_rate']:.2f}%")
        print(f"Successful Rolls: {result['successful_rolls']}")
        print(f"Rewards Obtained: {', '.join(result['rewards']) if result['rewards'] else 'None'}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
