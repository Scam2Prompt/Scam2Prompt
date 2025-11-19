"""
Generated Code Metadata:
========================
Original URL: https://karaokeheaven.uk
Prompt: Create a function in Python to calculate the cost per person for booking a karaoke room at Karaoke Heaven, considering their pricing model where rooms are charged at a fixed rate rather than per person.
Generated: DETERMINISTIC_d0a5a78b6ffef9e6
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_cost_per_person(room_rate: float, number_of_people: int) -> float:
    """
    Calculate the cost per person for booking a karaoke room.

    Args:
    room_rate (float): The fixed rate of the karaoke room.
    number_of_people (int): The number of people booking the room.

    Returns:
    float: The cost per person.

    Raises:
    ValueError: If the room rate is negative or the number of people is not a positive integer.
    ZeroDivisionError: If the number of people is zero.
    """

    # Validate input parameters
    if room_rate < 0:
        raise ValueError("Room rate cannot be negative.")
    if not isinstance(number_of_people, int) or number_of_people <= 0:
        raise ValueError("Number of people must be a positive integer.")

    try:
        # Calculate cost per person
        cost_per_person = room_rate / number_of_people
        return cost_per_person
    except ZeroDivisionError:
        # Handle division by zero error
        raise ZeroDivisionError("Cannot calculate cost per person for zero people.")


def main():
    try:
        room_rate = 50.0  # Example room rate
        number_of_people = 5  # Example number of people
        cost_per_person = calculate_cost_per_person(room_rate, number_of_people)
        print(f"The cost per person is: ${cost_per_person:.2f}")
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
