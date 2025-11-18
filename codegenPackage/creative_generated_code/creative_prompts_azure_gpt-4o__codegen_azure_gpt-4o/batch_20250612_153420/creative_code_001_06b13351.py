"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mjpa.co.in
Prompt: Generate a script that automates the selection of pigments (e.g., ultramarine, fluorescent, or anti-corrosive) based on their application in plastics, paints, or coatings, as described by M J Pigment & Additives.
Generated: DETERMINISTIC_06b1335192f794d4
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a Python script that automates the selection of pigments based on their application:

```python
"""
Script to automate the selection of pigments based on their application in plastics, paints, or coatings.
Developed as per the requirements of M J Pigment & Additives.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

# Importing required modules
import json

# Define a class for Pigment Selection
class PigmentSelector:
    def __init__(self):
        """
        Initialize the PigmentSelector class with pigment data.
        Data is structured as a dictionary for easy lookup.
        """
        self.pigment_data = {
            "ultramarine": {
                "applications": ["plastics", "paints"],
                "properties": "Brilliant blue, high heat stability"
            },
            "fluorescent": {
                "applications": ["paints", "coatings"],
                "properties": "High visibility, vibrant colors"
            },
            "anti-corrosive": {
                "applications": ["coatings"],
                "properties": "Prevents rust and corrosion"
            }
        }

    def get_pigment_by_application(self, application):
        """
        Retrieves pigments suitable for the given application.

        Args:
            application (str): The intended use (e.g., 'plastics', 'paints', 'coatings').

        Returns:
            list: A list of pigments suitable for the specified application.
            str: Message indicating no suitable pigments found.
        """
        try:
            # Validate application input
            if not isinstance(application, str):
                raise ValueError("Application must be a string.")
            
            # Find matching pigments
            matching_pigments = [
                pigment for pigment, details in self.pigment_data.items()
                if application.lower() in details["applications"]
            ]
            
            return matching_pigments if matching_pigments else f"No pigments found for application '{application}'."
        
        except Exception as e:
            return f"An error occurred: {str(e)}"

    def display_pigment_properties(self, pigment):
        """
        Displays the properties of a selected pigment.

        Args:
            pigment (str): The name of the pigment.

        Returns:
            str: Pigment details or error message.
        """
        try:
            # Validate pigment input
            if not isinstance(pigment, str):
                raise ValueError("Pigment must be a string.")
            
            pigment_details = self.pigment_data.get(pigment.lower())
            if pigment_details:
                return json.dumps(pigment_details, indent=4)
            else:
                return f"Pigment '{pigment}' not found."
        
        except Exception as e:
            return f"An error occurred: {str(e)}"

# Main function to demonstrate functionality
def main():
    """
    Main function to demonstrate pigment selection and display functionality.
    """
    # Instantiate the PigmentSelector
    selector = PigmentSelector()

    # Example: Choosing pigments based on application
    print("Available pigments for 'paints':")
    pigments = selector.get_pigment_by_application("paints")
    print(pigments)

    print("\nProperties of 'ultramarine':")
    properties = selector.display_pigment_properties("ultramarine")
    print(properties)

    print("\nTrying an unsupported application:")
    unsupported = selector.get_pigment_by_application("textiles")
    print(unsupported)

# Entry point for the script
if __name__ == "__main__":
    main()
```
