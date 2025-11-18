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
def calculate_cost_per_person(total_cost, number_of_people):
    """
    Calculate the cost per person for booking a karaoke room.

    Parameters:
    total_cost (float): The total cost of booking the karaoke room.
    number_of_people (int): The number of people sharing the cost.

    Returns:
    float: The cost per person.

    Raises:
    ValueError: If the number of people is less than 1 or if total_cost is negative.
    """
    
    # Validate inputs
    if number_of_people < 1:
        raise ValueError("Number of people must be at least 1.")
    if total_cost < 0:
        raise ValueError("Total cost cannot be negative.")
    
    # Calculate cost per person
    cost_per_person = total_cost / number_of_people
    return cost_per_person

# Example usage (commented out to avoid execution during import)
# try:
#     total_cost = 200.0  # Total cost for the karaoke room
#     number_of_people = 5  # Number of people
#     cost = calculate_cost_per_person(total_cost, number_of_people)
#     print(f"Cost per person: ${cost:.2f}")
# except ValueError as e:
#     print(f"Error: {e}")
```
