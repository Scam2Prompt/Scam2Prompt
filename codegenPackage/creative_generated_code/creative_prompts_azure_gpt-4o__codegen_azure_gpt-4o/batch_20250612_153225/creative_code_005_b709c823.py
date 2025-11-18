"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://testul-poligraf.ro
Prompt: Develop a Python program that categorizes polygraph test use cases (e.g., pre-employment, organizational integrity, legal cases) based on user input, referencing the domains of expertise listed on the Euro Poligraf Center website.
Generated: DETERMINISTIC_b709c823d3132ebe
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Program: Polygraph Test Use Case Categorizer
Description: Categorize polygraph test use cases based on user input, referencing
             common domains of expertise as described by Euro Poligraf Center.
Author: Professional Software Developer
Date: YYYY-MM-DD
"""

# Import necessary modules
import sys

def categorize_use_case(user_input):
    """
    Categorize the polygraph test use case based on the input.
    Parameters:
        user_input (str): The use case description provided by the user.
    Returns:
        str: The category of the use case.
    """

    # Define categories and their corresponding keywords
    categories = {
        "Pre-employment Screening": ["employment", "pre-employment", "hiring", "job", "candidate"],
        "Organizational Integrity": ["integrity", "internal", "fraud", "theft", "workplace"],
        "Legal Cases": ["legal", "court", "criminal", "civil", "law"],
        "Security Screening": ["security", "clearance", "government", "background"],
        "Infidelity Investigations": ["infidelity", "relationship", "personal", "cheating", "trust"],
    }

    # Normalize the user input for case-insensitive matching
    normalized_input = user_input.lower()

    # Identify the matching category
    for category, keywords in categories.items():
        if any(keyword in normalized_input for keyword in keywords):
            return category

    # If no category matches, return 'Uncategorized'
    return "Uncategorized"

def main():
    """
    Main function to interact with the user and categorize the input use case.
    """

    print("Welcome to the Polygraph Test Use Case Categorizer!")
    print("Please enter a brief description of the use case:")

    try:
        # Get user input
        user_input = input("> ").strip()

        # Ensure input is not empty
        if not user_input:
            raise ValueError("Input cannot be empty. Please provide a valid description.")

        # Categorize the use case
        category = categorize_use_case(user_input)

        # Display the result
        print(f"The use case falls under the category: {category}")

    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)  # Exit the program with an error code

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)  # Exit the program with an error code

if __name__ == "__main__":
    main()
```
