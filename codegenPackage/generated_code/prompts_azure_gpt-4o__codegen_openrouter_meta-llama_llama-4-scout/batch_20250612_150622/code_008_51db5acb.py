"""
Generated Code Metadata:
========================
Original URL: https://webs-bigtime.pages.dev
Prompt: Develop a program to calculate bonus rolls for crafting items in Big Time, ensuring accurate probabilities based on user input.
Generated: DETERMINISTIC_51db5acbc0c96375
Batch ID: 20250612_150622
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

def calculate_bonus_rolls(base_chance: float, num_rolls: int, target_chance: float) -> dict:
    """
    Calculate the probability of achieving a target chance with a given number of bonus rolls.

    Args:
    - base_chance (float): The base chance of success for a single roll (between 0 and 1).
    - num_rolls (int): The number of bonus rolls available.
    - target_chance (float): The target chance of success (between 0 and 1).

    Returns:
    - dict: A dictionary containing the probability of achieving the target chance and the number of rolls required.
    """

    # Validate input values
    if not (0 <= base_chance <= 1):
        raise ValueError("Base chance must be between 0 and 1")
    if num_rolls < 0:
        raise ValueError("Number of rolls must be non-negative")
    if not (0 <= target_chance <= 1):
        raise ValueError("Target chance must be between 0 and 1")

    # Calculate the probability of failure for a single roll
    fail_chance = 1 - base_chance

    # Calculate the probability of failure for all rolls
    prob_fail_all = fail_chance ** (num_rolls + 1)

    # Calculate the probability of success for at least one roll
    prob_succeed_at_least_one = 1 - prob_fail_all

    # Calculate the probability of achieving the target chance
    prob_target_chance = min(prob_succeed_at_least_one, target_chance)

    return {
        "probability": prob_target_chance,
        "num_rolls": num_rolls,
        "base_chance": base_chance,
        "target_chance": target_chance,
    }


def simulate_crafting(base_chance: float, num_rolls: int, target_chance: float, num_simulations: int = 10000) -> dict:
    """
    Simulate crafting with bonus rolls to estimate the actual probability of achieving a target chance.

    Args:
    - base_chance (float): The base chance of success for a single roll (between 0 and 1).
    - num_rolls (int): The number of bonus rolls available.
    - target_chance (float): The target chance of success (between 0 and 1).
    - num_simulations (int): The number of simulations to run (default: 10000).

    Returns:
    - dict: A dictionary containing the estimated probability of achieving the target chance and the number of rolls required.
    """

    successes = 0

    for _ in range(num_simulations):
        rolls = [random.random() < base_chance for _ in range(num_rolls + 1)]
        if any(rolls):
            successes += 1

    estimated_prob = successes / num_simulations

    return {
        "estimated_probability": estimated_prob,
        "num_rolls": num_rolls,
        "base_chance": base_chance,
        "target_chance": target_chance,
    }


def main():
    try:
        base_chance = float(input("Enter the base chance of success (between 0 and 1): "))
        num_rolls = int(input("Enter the number of bonus rolls: "))
        target_chance = float(input("Enter the target chance of success (between 0 and 1): "))

        result = calculate_bonus_rolls(base_chance, num_rolls, target_chance)
        print("Calculated Probability:")
        print(f"Probability: {result['probability']:.4f}")
        print(f"Number of Rolls: {result['num_rolls']}")
        print(f"Base Chance: {result['base_chance']:.4f}")
        print(f"Target Chance: {result['target_chance']:.4f}")

        simulated_result = simulate_crafting(base_chance, num_rolls, target_chance)
        print("\nSimulated Probability:")
        print(f"Estimated Probability: {simulated_result['estimated_probability']:.4f}")
        print(f"Number of Rolls: {simulated_result['num_rolls']}")
        print(f"Base Chance: {simulated_result['base_chance']:.4f}")
        print(f"Target Chance: {simulated_result['target_chance']:.4f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
