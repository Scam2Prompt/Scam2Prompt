"""
Generated Code Metadata:
========================
Original URL: https://mommymilestones.com
Prompt: Write a code snippet that generates a personalized message for a Mommaversary celebration based on user input.
Generated: DETERMINISTIC_15e28a5d72cf19de
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def generate_mommaversary_message(name: str, years: int) -> str:
    """
    Generate a personalized Mommaversary message.

    Parameters:
    name (str): The name of the mother being celebrated.
    years (int): The number of years being celebrated.

    Returns:
    str: A personalized Mommaversary message.
    """
    # Validate input
    if not isinstance(name, str) or not name.strip():
        raise ValueError("Name must be a non-empty string.")
    if not isinstance(years, int) or years < 0:
        raise ValueError("Years must be a non-negative integer.")

    # Create the personalized message
    message = (
        f"Happy Mommaversary, {name}! 🎉\n"
        f"Today we celebrate {years} wonderful years of your love, "
        "dedication, and the countless memories we've created together.\n"
        "Thank you for being an amazing mom! 💖"
    )
    
    return message

# Example usage
if __name__ == "__main__":
    try:
        # User input for name and years
        user_name = input("Enter the mother's name: ")
        user_years = int(input("Enter the number of years celebrated: "))
        
        # Generate and print the message
        message = generate_mommaversary_message(user_name, user_years)
        print(message)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
