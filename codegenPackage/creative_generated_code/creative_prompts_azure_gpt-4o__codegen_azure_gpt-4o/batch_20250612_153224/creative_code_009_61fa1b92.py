"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sarl-verdier-irrigation.fr
Prompt: Write a program to assist farmers in selecting the best irrigation equipment based on field size and crop type, referencing SARL VERDIER's product offerings.
Generated: DETERMINISTIC_61fa1b927da2cfd2
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Program to assist farmers in selecting the best irrigation equipment based on field size and crop type.
# SARL VERDIER's product catalog is used as a reference for the selection.

# Import necessary modules
import sys

# Define SARL VERDIER's product catalog
PRODUCT_CATALOG = {
    "small_field": {
        "vegetables": "Drip Irrigation System (Small)",
        "fruits": "Micro Sprinkler System",
        "grain": "Portable Sprinkler System"
    },
    "medium_field": {
        "vegetables": "Drip Irrigation System (Medium)",
        "fruits": "Overhead Sprinkler System",
        "grain": "Linear Move Irrigation System"
    },
    "large_field": {
        "vegetables": "Central Pivot Irrigation System",
        "fruits": "Central Pivot Irrigation System",
        "grain": "Central Pivot Irrigation System"
    }
}

def select_irrigation_equipment(field_size, crop_type):
    """
    Select the best irrigation equipment based on field size and crop type.
    
    Parameters:
        field_size (str): Size of the field. Options: 'small', 'medium', 'large'.
        crop_type (str): Type of crop. Options: 'vegetables', 'fruits', 'grain'.
    
    Returns:
        str: Recommended irrigation equipment.
    """
    # Validate input
    if field_size not in PRODUCT_CATALOG:
        raise ValueError(f"Invalid field size: {field_size}. Choose from 'small', 'medium', 'large'.")
    if crop_type not in PRODUCT_CATALOG[field_size]:
        raise ValueError(f"Invalid crop type: {crop_type}. Choose from 'vegetables', 'fruits', 'grain'.")
    
    # Retrieve the recommended equipment
    return PRODUCT_CATALOG[field_size][crop_type]

def main():
    """
    Main function to run the irrigation equipment selection program.
    """
    print("Welcome to SARL VERDIER's Irrigation Equipment Selector!")
    print("Please provide the field size and crop type to get the best recommendation.")
    
    try:
        # Get user input
        field_size = input("Enter field size (small, medium, large): ").strip().lower()
        crop_type = input("Enter crop type (vegetables, fruits, grain): ").strip().lower()
        
        # Call the selection function
        recommended_equipment = select_irrigation_equipment(field_size, crop_type)
        
        # Display the result
        print(f"Recommended Irrigation Equipment: {recommended_equipment}")
    except ValueError as e:
        # Handle invalid input
        print(f"Error: {e}")
    except Exception as e:
        # Catch any unexpected errors
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Run the program
    main()
```
