"""
Generated Code Metadata:
========================
Original URL: https://www.geoponicsinc.com
Prompt: What are some low-maintenance, pet-friendly plants that can help purify the air in a home, and how can I care for them?
Generated: DETERMINISTIC_a9accee2efb8888c
Batch ID: 20250622_212906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Program to provide information about low-maintenance, pet-friendly plants
# that help purify the air in a home, along with care instructions.

# Import necessary modules
import json

# Define a function to get plant information
def get_pet_friendly_plants():
    """
    Returns a list of low-maintenance, pet-friendly plants that purify the air,
    along with their care instructions.
    """
    try:
        # List of plants with their care instructions
        plants = [
            {
                "name": "Areca Palm",
                "description": "A pet-friendly plant that helps purify the air.",
                "care_instructions": {
                    "light": "Bright, indirect sunlight.",
                    "water": "Keep soil moist but not soggy. Water when topsoil feels dry.",
                    "humidity": "Prefers high humidity. Mist occasionally.",
                    "temperature": "Keep in temperatures between 65°F and 75°F."
                }
            },
            {
                "name": "Calathea",
                "description": "A colorful, pet-safe plant that improves air quality.",
                "care_instructions": {
                    "light": "Low to medium indirect light.",
                    "water": "Keep soil consistently moist but avoid overwatering.",
                    "humidity": "Thrives in high humidity. Mist regularly.",
                    "temperature": "Keep in temperatures between 60°F and 80°F."
                }
            },
            {
                "name": "Parlor Palm",
                "description": "A hardy, pet-friendly plant that purifies the air.",
                "care_instructions": {
                    "light": "Low to medium indirect light.",
                    "water": "Allow topsoil to dry out between waterings.",
                    "humidity": "Prefers moderate humidity.",
                    "temperature": "Keep in temperatures between 65°F and 80°F."
                }
            },
            {
                "name": "Spider Plant",
                "description": "A resilient, pet-safe plant that removes toxins from the air.",
                "care_instructions": {
                    "light": "Bright, indirect sunlight.",
                    "water": "Water when topsoil is dry. Avoid overwatering.",
                    "humidity": "Adaptable to various humidity levels.",
                    "temperature": "Keep in temperatures between 60°F and 75°F."
                }
            }
        ]
        return plants
    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred while fetching plant information: {e}")
        return []

# Define a function to display plant information
def display_plants(plants):
    """
    Displays the list of plants and their care instructions in a readable format.
    """
    try:
        if not plants:
            print("No plant information available.")
            return

        print("Low-Maintenance, Pet-Friendly Plants That Purify the Air:\n")
        for plant in plants:
            print(f"Name: {plant['name']}")
            print(f"Description: {plant['description']}")
            print("Care Instructions:")
            for key, value in plant['care_instructions'].items():
                print(f"  {key.capitalize()}: {value}")
            print("\n")
    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred while displaying plant information: {e}")

# Main function
def main():
    """
    Main function to fetch and display plant information.
    """
    try:
        # Fetch plant information
        plants = get_pet_friendly_plants()

        # Display plant information
        display_plants(plants)
    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred in the main function: {e}")

# Entry point of the program
if __name__ == "__main__":
    main()
```
