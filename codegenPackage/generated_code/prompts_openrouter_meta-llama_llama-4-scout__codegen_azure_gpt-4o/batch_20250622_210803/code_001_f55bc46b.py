"""
Generated Code Metadata:
========================
Original URL: https://eternallaunch.pages.dev
Prompt: Generate a Python code snippet to calculate the boost for a participant in the $EAI public sale based on their position in the allowlist and the provided boost levels.
Generated: DETERMINISTIC_f55bc46ba9c68dab
Batch ID: 20250622_210803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Python code to calculate the boost for a participant in the $EAI public sale

def calculate_boost(position, boost_levels):
    """
    Calculate the boost for a participant based on their position in the allowlist.

    Args:
        position (int): The position of the participant in the allowlist (1-based index).
        boost_levels (dict): A dictionary mapping position ranges to boost percentages.
                             Example: { (1, 100): 20, (101, 500): 15, (501, 1000): 10 }

    Returns:
        float: The boost percentage for the participant.
    Raises:
        ValueError: If the position is invalid or not covered by the boost levels.
    """
    if position <= 0:
        raise ValueError("Position must be a positive integer.")

    for range_tuple, boost in boost_levels.items():
        start, end = range_tuple
        if start <= position <= end:
            return boost

    raise ValueError("Position not covered by the provided boost levels.")


# Example usage
if __name__ == "__main__":
    try:
        # Define boost levels as a dictionary
        boost_levels = {
            (1, 100): 20,    # 20% boost for positions 1 to 100
            (101, 500): 15,  # 15% boost for positions 101 to 500
            (501, 1000): 10  # 10% boost for positions 501 to 1000
        }

        # Participant's position in the allowlist
        participant_position = 250

        # Calculate the boost
        boost = calculate_boost(participant_position, boost_levels)
        print(f"Participant at position {participant_position} receives a {boost}% boost.")
    except ValueError as e:
        print(f"Error: {e}")
```
