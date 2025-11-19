"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://biogreenasia.com
Prompt: Generate a Python script to create a natural cleaning product similar to Bio Green Asia's Quick Wash liquid detergent, incorporating advanced cleaning technology and hand-soothing ingredients.
Generated: DETERMINISTIC_07d22e204455b2ea
Batch ID: 20250612_163924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to create a natural cleaning product formulation.
This script simulates the formulation of a liquid detergent with advanced cleaning technology
and hand-soothing ingredients. Note: This is a conceptual representation and does not involve
actual chemical synthesis or testing.
"""

# Import required libraries for simulation
import json

# Define the product formulation
def create_cleaning_product():
    """
    Creates a natural cleaning product formulation with advanced cleaning and hand-soothing properties.
    Returns:
        dict: A dictionary containing the ingredients and their proportions.
    """

    # Ingredients and their proportions (in percentage)
    # Note: Percentages add up to 100 for balance
    formulation = {
        "Base Ingredients": {
            "Plant-based Surfactants": 45,  # Primary cleaning agent, derived from coconut or palm oil
            "Water": 40,                   # Acts as solvent and carrier for ingredients
        },
        "Advanced Cleaning Technology": {
            "Enzymes": 5,                  # Protease and amylase enzymes to break down stains
            "Natural Solvents": 3.5,       # Citrus-based solvents for grease cutting
        },
        "Hand-Soothing Ingredients": {
            "Aloe Vera Extract": 3,        # Provides skin-soothing properties
            "Glycerin": 2,                 # Acts as a moisturizer for hands
        },
        "Preservatives": {
            "Natural Preservative": 1.5    # Ensures shelf-life without chemical additives
        }
    }

    return formulation


def validate_formulation(formulation):
    """
    Validates the product formulation to ensure percentages add up to 100.
    Args:
        formulation (dict): The product formulation dictionary.
    Returns:
        bool: True if valid, False otherwise.
    """
    total_percentage = sum(
        percentage
        for category in formulation.values()
        for percentage in category.values()
    )
    return total_percentage == 100


def save_formulation_to_file(formulation, filename="cleaning_product_formulation.json"):
    """
    Saves the formulation to a JSON file for documentation purposes.
    Args:
        formulation (dict): The product formulation dictionary.
        filename (str): The name of the file to save the formulation.
    """
    try:
        with open(filename, "w") as file:
            json.dump(formulation, file, indent=4)
        print(f"Formulation saved successfully to {filename}")
    except IOError as e:
        print(f"Error saving formulation to file: {e}")


def main():
    """
    Main function to create, validate, and save the cleaning product formulation.
    """
    # Create the formulation
    formulation = create_cleaning_product()

    # Validate the formulation
    if validate_formulation(formulation):
        print("Formulation is valid. Percentages add up to 100%.")
    else:
        print("Formulation is invalid. Please check the ingredient percentages.")
        return

    # Save the formulation to a file
    save_formulation_to_file(formulation)


if __name__ == "__main__":
    # Run the script if executed directly
    main()
```
