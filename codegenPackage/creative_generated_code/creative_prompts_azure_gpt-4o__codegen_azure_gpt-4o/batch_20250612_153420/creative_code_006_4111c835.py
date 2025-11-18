"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mjpa.co.in
Prompt: Create a script to categorize pigments like chrome, oxide, and fluorescent pigments based on their industrial applications (e.g., inks, textiles, or coatings), using the classifications provided by M J Pigment & Additives.
Generated: DETERMINISTIC_4111c835d6f01fec
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import json

# Define the classifications provided by M J Pigment & Additives
PIGMENT_CATEGORIES = {
    "chrome": ["inks", "coatings"],
    "oxide": ["textiles", "coatings"],
    "fluorescent": ["inks", "textiles", "coatings"],
}

def categorize_pigment(pigment_name):
    """
    Categorizes pigments based on their industrial applications using predefined classifications.

    Args:
        pigment_name (str): The name of the pigment to categorize.

    Returns:
        list: A list of industrial applications for the given pigment, 
              or an error message if the pigment is not recognized.
    """
    try:
        # Match the pigment with its industrial applications
        applications = PIGMENT_CATEGORIES.get(pigment_name.lower())
        if applications:
            return applications
        else:
            return [f"Error: '{pigment_name}' is not a recognized pigment."]
    except Exception as e:
        # Handle unexpected errors
        return [f"An unexpected error occurred: {str(e)}"]

def main():
    """
    Main function to demonstrate pigment categorization.
    Accepts user input and provides categorized results based on the pigment name.
    """
    print("Welcome to the Pigment Categorization Tool!")
    print("Available pigments: chrome, oxide, fluorescent")
    
    try:
        # Prompt user for input
        pigment_name = input("Enter the name of the pigment to categorize: ").strip()
        
        # Categorize the pigment and display the results
        categories = categorize_pigment(pigment_name)
        print(f"\nCategories for '{pigment_name}':")
        for category in categories:
            print(f"- {category}")
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

# Entry point of the script
if __name__ == "__main__":
    main()
```
