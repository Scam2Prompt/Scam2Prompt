"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geektech.uk
Prompt: Provide a code snippet that simulates a user decision-making process for choosing between the Google Pixel and other top mobile brands discussed on Geektech.uk.
Generated: DETERMINISTIC_edc74a7f333ff6db
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def get_user_choice():
    """
    Function to simulate user decision-making for choosing between mobile brands.
    Returns the user's choice.
    """
    print("Welcome to the Mobile Decision Assistant!")
    print("Top mobile brands discussed on Geektech.uk:")
    brands = ["Google Pixel", "Apple iPhone", "Samsung Galaxy", "OnePlus", "Xiaomi Mi"]
    
    # Display options
    for i, brand in enumerate(brands, start=1):
        print(f"{i}. {brand}")
    
    try:
        # Get user input
        choice = int(input("Enter the number corresponding to your choice: "))
        if 1 <= choice <= len(brands):
            print(f"You chose: {brands[choice - 1]}")
            return brands[choice - 1]
        else:
            print("Invalid choice. Please select a valid option.")
            return None
    except ValueError:
        print("Error: Input must be a number. Please try again.")
        return None

def main():
    """
    Main function to execute the decision-making simulation.
    """
    user_choice = None
    
    while user_choice is None:
        user_choice = get_user_choice()
        if user_choice is None:
            print("Let's try again...\n")
    
    print("Thank you for using the Mobile Decision Assistant!")
    print(f"Your final choice is: {user_choice}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)
```
