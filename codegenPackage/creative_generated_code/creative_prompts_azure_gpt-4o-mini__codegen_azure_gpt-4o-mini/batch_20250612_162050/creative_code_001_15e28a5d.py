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
def generate_mommaversary_message(name: str, years: int, favorite_memory: str) -> str:
    """
    Generates a personalized Mommaversary message.

    Parameters:
    name (str): The name of the mother.
    years (int): The number of years celebrated.
    favorite_memory (str): A favorite memory shared with the mother.

    Returns:
    str: A personalized celebration message.
    """
    if not isinstance(name, str) or not isinstance(favorite_memory, str):
        raise ValueError("Name and favorite memory must be strings.")
    
    if not isinstance(years, int) or years < 0:
        raise ValueError("Years must be a non-negative integer.")
    
    # Create the personalized message
    message = (
        f"Happy Mommaversary, {name}!\n"
        f"Today we celebrate {years} wonderful years together.\n"
        f"One of my favorite memories with you is: '{favorite_memory}'.\n"
        "Thank you for being such an amazing mom!"
    )
    
    return message


def main():
    """
    Main function to execute the Mommaversary message generation.
    """
    try:
        # User inputs for the Mommaversary message
        mother_name = input("Enter the mother's name: ")
        years_celebrated = int(input("Enter the number of years celebrated: "))
        favorite_memory = input("Enter a favorite memory: ")

        # Generate the message
        message = generate_mommaversary_message(mother_name, years_celebrated, favorite_memory)

        # Print the personalized message
        print("\n" + message)

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
