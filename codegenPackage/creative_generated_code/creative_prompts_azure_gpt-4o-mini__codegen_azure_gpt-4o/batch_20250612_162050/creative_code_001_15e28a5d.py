"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mommymilestones.com
Prompt: Write a code snippet that generates a personalized message for a Mommaversary celebration based on user input.
Generated: DETERMINISTIC_15e28a5d72cf19de
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

def generate_mommaversary_message(name, child_name, years_as_mom):
    """
    Generates a personalized Mommaversary message.

    Args:
        name (str): The name of the mom.
        child_name (str): The name of the child.
        years_as_mom (int): The number of years the person has been a mom.

    Returns:
        str: A personalized celebration message.
    """
    try:
        # Validate input arguments
        if not name or not isinstance(name, str):
            raise ValueError("Invalid input: 'name' must be a non-empty string.")
        if not child_name or not isinstance(child_name, str):
            raise ValueError("Invalid input: 'child_name' must be a non-empty string.")
        if not isinstance(years_as_mom, int) or years_as_mom < 0:
            raise ValueError("Invalid input: 'years_as_mom' must be a non-negative integer.")
        
        # Get current date to include in the message
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        
        # Construct the personalized message
        message = (
            f"Happy Mommaversary, {name}!\n"
            f"Today, on {current_date}, we celebrate your incredible journey of {years_as_mom} year(s) as the loving mom of {child_name}.\n"
            "Thank you for all the love, care, and dedication you've shown over the years. You are truly special!"
        )
        
        return message
    except Exception as e:
        # Handle unexpected errors gracefully
        return f"An error occurred while generating the message: {e}"


# Example usage
if __name__ == "__main__":
    print("Welcome to the Mommaversary Message Generator!")
    try:
        # Collect user inputs
        mom_name = input("Enter the name of the mom: ").strip()
        child_name = input("Enter the name of the child: ").strip()
        years_as_mom = int(input("Enter the number of years as a mom: ").strip())
        
        # Generate and display the personalized message
        message = generate_mommaversary_message(mom_name, child_name, years_as_mom)
        print("\n" + message)
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
