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
def generate_mommaversary_message():
    """
    Generates a personalized Mommaversary message based on user input.
    
    Returns:
        str: A personalized Mommaversary message.
    """
    try:
        # Get user input
        name = input("Enter the mom's name: ").strip()
        years = input("Enter the number of years being celebrated: ").strip()
        child_name = input("Enter the child's name: ").strip()
        favorite_thing = input("Enter mom's favorite thing (e.g., hobby, food, etc.): ").strip()
        
        # Validate input
        if not name or not years or not child_name or not favorite_thing:
            raise ValueError("All fields are required.")
        
        if not years.isdigit() or int(years) <= 0:
            raise ValueError("Years must be a positive integer.")
        
        years = int(years)
        
        # Generate message
        message = (
            f"Happy {years} year{'s' if years > 1 else ''} Mommaversary, {name}!\n\n"
            f"Wishing you a day as wonderful as you are! {child_name} is so lucky "
            f"to have you as their mom. May your day be filled with lots of "
            f"{favorite_thing} and love. Here's to many more years of amazing motherhood!\n\n"
            f"With love,\n{child_name}"
        )
        
        return message
    
    except ValueError as e:
        return f"Error: {str(e)}. Please try again."
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}. Please try again."


if __name__ == "__main__":
    print("\nWelcome to the Mommaversary Message Generator!\n")
    message = generate_mommaversary_message()
    print("\nHere's your personalized Mommaversary message:\n")
    print(message)
```
