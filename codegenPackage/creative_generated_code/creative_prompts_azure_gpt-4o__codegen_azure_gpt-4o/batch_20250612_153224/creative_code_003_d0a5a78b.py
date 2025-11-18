"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karaokeheaven.uk
Prompt: Create a function in Python to calculate the cost per person for booking a karaoke room at Karaoke Heaven, considering their pricing model where rooms are charged at a fixed rate rather than per person.
Generated: DETERMINISTIC_d0a5a78b6ffef9e6
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_cost_per_person(room_rate: float, num_people: int) -> float:
    """
    Calculate the cost per person for booking a karaoke room.

    Parameters:
        room_rate (float): The fixed rate charged for the karaoke room.
        num_people (int): The number of people sharing the cost.

    Returns:
        float: The cost per person.

    Raises:
        ValueError: If room_rate is negative or if num_people is less than 1.
    """
    # Validate input
    if room_rate < 0:
        raise ValueError("Room rate cannot be negative.")
    if num_people < 1:
        raise ValueError("Number of people must be at least 1.")

    # Calculate the cost per person
    cost_per_person = room_rate / num_people
    return round(cost_per_person, 2)  # Round to 2 decimal places for precision


# Example usage:
try:
    room_rate = 120.00  # Fixed room rate in dollars
    num_people = 4      # Number of people sharing the cost
    cost = calculate_cost_per_person(room_rate, num_people)
    print(f"Cost per person: ${cost}")
except ValueError as e:
    print(f"Error: {e}")
```
