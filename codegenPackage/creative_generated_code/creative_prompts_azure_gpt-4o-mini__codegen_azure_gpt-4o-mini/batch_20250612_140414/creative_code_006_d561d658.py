"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trysonicsolutions.com
Prompt: Generate a checklist for determining whether to use ultrasonic cleaning or jet washing for different types of industrial parts.
Generated: DETERMINISTIC_d561d6584816c80e
Batch ID: 20250612_140414
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CleaningMethodChecklist:
    """
    A checklist class to determine whether to use ultrasonic cleaning or jet washing
    for different types of industrial parts based on material and contamination types.
    """

    def __init__(self):
        """
        Initializes the checklist with criteria for ultrasonic cleaning and jet washing.
        """
        self.criteria = {
            'Ultrasonic Cleaning': {
                'materials': ['metal', 'plastic', 'ceramic'],
                'contaminants': ['grease', 'oil', 'dust', 'biofilms'],
                'size_limit': 0.5  # max thickness in inches for ultrasonic cleaning
            },
            'Jet Washing': {
                'materials': ['metal', 'plastic'],
                'contaminants': ['mud', 'grime', 'loose paint', 'oil'],
                'size_limit': 0.5  # max thickness in inches for jet washing
            }
        }

    def is_ultrasonic_cleaning_suitable(self, material, contaminants, size):
        """
        Determines if ultrasonic cleaning is suitable for the given parameters.

        :param material: The material of the part.
        :param contaminants: A list of contaminants present on the part.
        :param size: The thickness of the part in inches.
        :return: Boolean indicating if ultrasonic cleaning is suitable.
        """
        material = material.lower()
        if material in self.criteria['Ultrasonic Cleaning']['materials'] and size <= self.criteria['Ultrasonic Cleaning']['size_limit']:
            if any(contaminant in contaminants for contaminant in self.criteria['Ultrasonic Cleaning']['contaminants']):
                return True
        return False

    def is_jet_washing_suitable(self, material, contaminants, size):
        """
        Determines if jet washing is suitable for the given parameters.

        :param material: The material of the part.
        :param contaminants: A list of contaminants present on the part.
        :param size: The thickness of the part in inches.
        :return: Boolean indicating if jet washing is suitable.
        """
        material = material.lower()
        if material in self.criteria['Jet Washing']['materials'] and size <= self.criteria['Jet Washing']['size_limit']:
            if any(contaminant in contaminants for contaminant in self.criteria['Jet Washing']['contaminants']):
                return True
        return False

    def determine_cleaning_method(self, material, contaminants, size):
        """
        Determines the appropriate cleaning method based on material, contaminants, and size.

        :param material: The material of the part.
        :param contaminants: A list of contaminants present on the part.
        :param size: The thickness of the part in inches.
        :return: Suggested cleaning method or a message indicating no suitable method.
        """
        try:
            ultrasonic = self.is_ultrasonic_cleaning_suitable(material, contaminants, size)
            jet_washing = self.is_jet_washing_suitable(material, contaminants, size)

            if ultrasonic and jet_washing:
                return "Both ultrasonic cleaning and jet washing are suitable."
            elif ultrasonic:
                return "Ultrasonic cleaning is suitable."
            elif jet_washing:
                return "Jet washing is suitable."
            else:
                return "No suitable cleaning method found for the given parameters."
        except Exception as e:
            return f"Error in determining cleaning method: {str(e)}"


# Example usage
if __name__ == "__main__":
    cleaning_checklist = CleaningMethodChecklist()
    material = "Metal"
    contaminants = ["grease", "oil"]
    size = 0.3

    result = cleaning_checklist.determine_cleaning_method(material, contaminants, size)
    print(result)  # Output: Ultrasonic cleaning is suitable.
```
