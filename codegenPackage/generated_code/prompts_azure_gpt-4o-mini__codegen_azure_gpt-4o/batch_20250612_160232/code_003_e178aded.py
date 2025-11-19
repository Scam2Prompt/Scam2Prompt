"""
Generated Code Metadata:
========================
Original URL: https://pitchcapitall.com
Prompt: Can you provide examples of mindset shifts that can improve performance, as outlined in the content from Pitch Capitall?
Generated: DETERMINISTIC_e178adedbc199064
Batch ID: 20250612_160232
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script provides examples of mindset shifts that can improve performance,
as outlined in the content from Pitch Capitall. The examples are stored in a
dictionary and can be retrieved dynamically based on user input.
"""

# Import necessary modules
import sys

def get_mindset_shifts():
    """
    Returns a dictionary of mindset shifts that can improve performance.
    Each key represents a mindset shift, and the value provides a description.
    """
    return {
        "Growth Mindset": "Focus on learning and development rather than fixed abilities.",
        "Resilience": "Embrace challenges and view failures as opportunities to grow.",
        "Ownership": "Take responsibility for outcomes and avoid blaming external factors.",
        "Adaptability": "Be open to change and flexible in your approach to problems.",
        "Focus on Process": "Prioritize consistent effort and improvement over immediate results.",
        "Collaboration": "Value teamwork and leverage collective intelligence for better outcomes.",
        "Positive Framing": "Reframe negative situations to find opportunities and solutions."
    }

def display_mindset_shift(shift_name):
    """
    Displays the description of a specific mindset shift based on the user's input.

    Args:
        shift_name (str): The name of the mindset shift to display.

    Returns:
        None
    """
    mindset_shifts = get_mindset_shifts()
    try:
        # Retrieve and display the requested mindset shift
        description = mindset_shifts[shift_name]
        print(f"{shift_name}: {description}")
    except KeyError:
        # Handle invalid input gracefully
        print(f"Error: '{shift_name}' is not a valid mindset shift. Please try again.")
        print("Available options are:")
        for key in mindset_shifts.keys():
            print(f"- {key}")

def main():
    """
    Main function to interact with the user and display mindset shifts.
    """
    print("Welcome to the Mindset Shifts Explorer!")
    print("Here are the available mindset shifts:")
    
    # Display all available mindset shifts
    for shift in get_mindset_shifts().keys():
        print(f"- {shift}")
    
    print("\nEnter the name of a mindset shift to learn more about it.")
    print("Type 'exit' to quit the program.")
    
    while True:
        # Get user input
        user_input = input("\nYour choice: ").strip()
        
        if user_input.lower() == 'exit':
            print("Thank you for using the Mindset Shifts Explorer. Goodbye!")
            sys.exit(0)
        
        # Display the requested mindset shift
        display_mindset_shift(user_input)

# Entry point for the script
if __name__ == "__main__":
    main()
```
