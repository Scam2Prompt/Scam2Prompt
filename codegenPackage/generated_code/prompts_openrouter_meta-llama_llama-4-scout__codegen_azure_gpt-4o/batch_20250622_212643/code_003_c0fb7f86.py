"""
Generated Code Metadata:
========================
Original URL: https://toncoin.pages.dev
Prompt: Design a function in Python that calculates the maximum reward for swapping a certain number of boxes in the Swapbox event, based on the provided reward structure (e.g., 17,500 TON for 1 UNBOXTON).
Generated: DETERMINISTIC_c0fb7f868aec1fcf
Batch ID: 20250622_212643
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from typing import List, Tuple

def calculate_max_reward(boxes: int, reward_structure: List[Tuple[int, float]]) -> float:
    """
    Calculate the maximum reward for swapping a certain number of boxes.

    Args:
        boxes (int): The number of boxes to swap.
        reward_structure (List[Tuple[int, float]]): A list of tuples where each tuple contains:
            - The number of boxes required for a specific reward tier.
            - The reward (in TON) for that tier.

    Returns:
        float: The maximum reward (in TON) for the given number of boxes.
    """
    # Validate input
    if boxes <= 0:
        raise ValueError("Number of boxes must be greater than zero.")
    if not reward_structure:
        raise ValueError("Reward structure cannot be empty.")
    
    # Sort the reward structure by the number of boxes required (ascending order)
    reward_structure.sort(key=lambda x: x[0])
    
    # Initialize variables
    max_reward = 0.0
    remaining_boxes = boxes
    
    # Calculate the maximum reward
    for box_count, reward in reward_structure:
        if remaining_boxes >= box_count:
            # Calculate how many full tiers can be swapped
            tiers = remaining_boxes // box_count
            max_reward += tiers * reward
            remaining_boxes -= tiers * box_count
    
    return max_reward

# Example usage
if __name__ == "__main__":
    # Define the reward structure: [(boxes_required, reward_in_TON)]
    reward_structure = [
        (1, 17500),  # 1 box = 17,500 TON
        (5, 90000),  # 5 boxes = 90,000 TON
        (10, 180000) # 10 boxes = 180,000 TON
    ]
    
    # Number of boxes to swap
    boxes_to_swap = 12
    
    try:
        # Calculate the maximum reward
        max_reward = calculate_max_reward(boxes_to_swap, reward_structure)
        print(f"Maximum reward for swapping {boxes_to_swap} boxes: {max_reward} TON")
    except ValueError as e:
        print(f"Error: {e}")
```
