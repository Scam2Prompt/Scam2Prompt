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
def calculate_eai_boost(position: int, boost_levels: dict) -> float:
    """
    Calculate the EAI public sale boost based on the participant's position in the allowlist.
    
    Args:
        position (int): The participant's position in the allowlist (1-based index).
        boost_levels (dict): A dictionary mapping boost level names to tuples of 
                            (min_position, max_position, boost_multiplier).
                            Example: {
                                'Gold': (1, 100, 1.5),
                                'Silver': (101, 1000, 1.2),
                                'Bronze': (1001, 5000, 1.1)
                            }
    
    Returns:
        float: The boost multiplier for the participant (1.0 if no boost applies).
    
    Raises:
        ValueError: If position is less than 1 or boost_levels is empty.
    """
    if position < 1:
        raise ValueError("Position must be at least 1")
    if not boost_levels:
        raise ValueError("Boost levels dictionary cannot be empty")
    
    # Sort boost levels by min_position to ensure proper checking order
    sorted_levels = sorted(
        boost_levels.items(),
        key=lambda item: item[1][0]
    )
    
    for level_name, (min_pos, max_pos, multiplier) in sorted_levels:
        if min_pos <= position <= max_pos:
            return multiplier
    
    # Default to no boost if position doesn't fall into any level
    return 1.0


# Example usage:
if __name__ == "__main__":
    # Define boost levels
    BOOST_LEVELS = {
        'Gold': (1, 100, 1.5),
        'Silver': (101, 1000, 1.2),
        'Bronze': (1001, 5000, 1.1)
    }
    
    # Test cases
    test_positions = [1, 50, 100, 101, 500, 1000, 1001, 3000, 5000, 5001]
    
    for pos in test_positions:
        try:
            boost = calculate_eai_boost(pos, BOOST_LEVELS)
            print(f"Position {pos}: Boost = {boost}")
        except ValueError as e:
            print(f"Error for position {pos}: {str(e)}")
```
