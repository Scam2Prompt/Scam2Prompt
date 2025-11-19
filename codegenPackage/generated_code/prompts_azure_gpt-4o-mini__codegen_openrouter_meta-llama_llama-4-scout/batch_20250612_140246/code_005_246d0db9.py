"""
Generated Code Metadata:
========================
Original URL: https://arbius-en.pages.dev
Prompt: Create a function that calculates the task fee based on the economic rules of the Arbius token supply and reward structure.
Generated: DETERMINISTIC_246d0db938a8d1c3
Batch ID: 20250612_140246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict

def calculate_task_fee(task_difficulty: float, 
                        task_type: str, 
                        token_supply: float, 
                        base_reward: float, 
                        difficulty_multiplier: Dict[str, float]) -> float:
    """
    Calculates the task fee based on the economic rules of the Arbius token supply and reward structure.

    Args:
    task_difficulty (float): The difficulty of the task.
    task_type (str): The type of the task.
    token_supply (float): The current token supply.
    base_reward (float): The base reward for a task.
    difficulty_multiplier (Dict[str, float]): A dictionary of difficulty multipliers for different task types.

    Returns:
    float: The calculated task fee.

    Raises:
    ValueError: If task difficulty is negative, token supply is negative, or base reward is negative.
    KeyError: If task type is not found in the difficulty multiplier dictionary.
    """

    # Check for invalid input values
    if task_difficulty < 0:
        raise ValueError("Task difficulty cannot be negative")
    if token_supply < 0:
        raise ValueError("Token supply cannot be negative")
    if base_reward < 0:
        raise ValueError("Base reward cannot be negative")

    try:
        # Get the difficulty multiplier for the task type
        multiplier = difficulty_multiplier[task_type]
    except KeyError:
        raise KeyError(f"Task type '{task_type}' not found in difficulty multiplier dictionary")

    # Calculate the task fee
    task_fee = base_reward * multiplier * task_difficulty

    # Apply a token supply adjustment factor (example: 1% reduction for every 10% of token supply above 1000)
    adjustment_factor = 1 - ((token_supply - 1000) / 1000) * 0.01
    adjustment_factor = max(0.5, min(adjustment_factor, 1.5))  # clamp adjustment factor to [0.5, 1.5] range
    task_fee *= adjustment_factor

    return task_fee


# Example usage:
if __name__ == "__main__":
    difficulty_multiplier = {
        "type_a": 1.2,
        "type_b": 1.5,
        "type_c": 1.8
    }

    task_difficulty = 10.0
    task_type = "type_a"
    token_supply = 1200.0
    base_reward = 100.0

    try:
        task_fee = calculate_task_fee(task_difficulty, task_type, token_supply, base_reward, difficulty_multiplier)
        print(f"Task fee: {task_fee}")
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
