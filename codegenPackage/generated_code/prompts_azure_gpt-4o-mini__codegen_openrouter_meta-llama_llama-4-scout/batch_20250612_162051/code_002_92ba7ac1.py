"""
Generated Code Metadata:
========================
Original URL: https://ifesty.com.br
Prompt: What are the steps to calculate the amount of food and drinks needed for an event, as suggested by Ifesty's blog?
Generated: DETERMINISTIC_92ba7ac18446796c
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Calculates the amount of food and drinks needed for an event.

Based on Ifesty's blog suggestions:
- 1/4 to 1/2 pound of food per guest
- 1-2 drinks per guest for a short event, 2-3 drinks per guest for a long event
"""

def calculate_food_and_drinks(num_guests: int, 
                              food_per_guest: float = 0.375, 
                              drinks_per_guest: float = 1.5, 
                              event_duration: str = "short") -> dict:
    """
    Calculates the amount of food and drinks needed.

    Args:
    - num_guests (int): The number of guests attending the event.
    - food_per_guest (float): The amount of food per guest in pounds. Defaults to 0.375.
    - drinks_per_guest (float): The number of drinks per guest. Defaults to 1.5.
    - event_duration (str): The duration of the event. Can be 'short' or 'long'. Defaults to 'short'.

    Returns:
    - A dictionary containing the total amount of food and drinks needed.

    Raises:
    - ValueError: If event_duration is not 'short' or 'long'.
    """

    # Validate event duration
    if event_duration.lower() not in ["short", "long"]:
        raise ValueError("Event duration must be 'short' or 'long'.")

    # Adjust drinks per guest based on event duration
    if event_duration.lower() == "long":
        drinks_per_guest = 2.5  # Average of 2-3 drinks per guest

    # Calculate total food and drinks needed
    total_food = num_guests * food_per_guest
    total_drinks = num_guests * drinks_per_guest

    return {
        "total_food": round(total_food, 2),
        "total_drinks": round(total_drinks, 2)
    }


def main():
    try:
        num_guests = int(input("Enter the number of guests: "))
        event_duration = input("Enter the event duration ('short' or 'long'): ")

        result = calculate_food_and_drinks(num_guests, event_duration=event_duration)

        print(f"For {num_guests} guests and a {event_duration} event:")
        print(f"Total food needed: {result['total_food']} pounds")
        print(f"Total drinks needed: {result['total_drinks']}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
