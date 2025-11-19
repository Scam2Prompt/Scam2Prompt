"""
Generated Code Metadata:
========================
Original URL: https://trysonicsolutions.com
Prompt: Generate a checklist for determining whether to use ultrasonic cleaning or jet washing for different types of industrial parts.
Generated: DETERMINISTIC_d561d6584816c80e
Batch ID: 20250612_140414
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CleaningChecklist:
    """
    A class to determine the appropriate cleaning method for industrial parts.
    """

    def __init__(self):
        # Define the criteria for ultrasonic cleaning and jet washing
        self.criteria = {
            "ultrasonic": {
                "material": ["metal", "plastic"],
                "contamination": ["grease", "oil", "dirt"],
                "size": "small",
                "delicate": True
            },
            "jet_washing": {
                "material": ["metal", "ceramic"],
                "contamination": ["mud", "heavy dirt"],
                "size": "large",
                "delicate": False
            }
        }

    def determine_cleaning_method(self, material, contamination, size, delicate):
        """
        Determine the appropriate cleaning method based on the provided criteria.

        :param material: The material of the part (str)
        :param contamination: The type of contamination (str)
        :param size: The size of the part (str)
        :param delicate: Whether the part is delicate (bool)
        :return: Recommended cleaning method (str)
        """
        try:
            # Check for ultrasonic cleaning suitability
            if (material in self.criteria["ultrasonic"]["material"] and
                    contamination in self.criteria["ultrasonic"]["contamination"] and
                    size == self.criteria["ultrasonic"]["size"] and
                    delicate == self.criteria["ultrasonic"]["delicate"]):
                return "Recommended cleaning method: Ultrasonic Cleaning"

            # Check for jet washing suitability
            if (material in self.criteria["jet_washing"]["material"] and
                    contamination in self.criteria["jet_washing"]["contamination"] and
                    size == self.criteria["jet_washing"]["size"] and
                    delicate == self.criteria["jet_washing"]["delicate"]):
                return "Recommended cleaning method: Jet Washing"

            return "No suitable cleaning method found for the given criteria."

        except Exception as e:
            return f"Error determining cleaning method: {str(e)}"


# Example usage
if __name__ == "__main__":
    checklist = CleaningChecklist()
    
    # Example part details
    material = "metal"
    contamination = "grease"
    size = "small"
    delicate = True

    # Get the recommended cleaning method
    result = checklist.determine_cleaning_method(material, contamination, size, delicate)
    print(result)
```
