"""
Generated Code Metadata:
========================
Original URL: https://trysonicsolutions.com
Prompt: "Write a technical guide on specifying the level of cleanliness required for industrial parts, including factors like surface roughness, material type, and contaminant level, and using standards and regulations like ISO 9001:2015."
Generated: DETERMINISTIC_652724339362f8e2
Batch ID: 20250622_212534
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CleanlinessSpecification:
    """
    A class to represent the cleanliness specification for industrial parts.
    """

    def __init__(self, surface_roughness: float, material_type: str, contaminant_level: str):
        """
        Initializes the cleanliness specification with the given parameters.

        :param surface_roughness: The required surface roughness in micrometers.
        :param material_type: The type of material (e.g., steel, aluminum).
        :param contaminant_level: The acceptable level of contaminants (e.g., clean, moderately clean).
        """
        self.surface_roughness = surface_roughness
        self.material_type = material_type
        self.contaminant_level = contaminant_level

    def validate(self):
        """
        Validates the cleanliness specification parameters.

        :raises ValueError: If any of the parameters are invalid.
        """
        if self.surface_roughness < 0:
            raise ValueError("Surface roughness must be a non-negative value.")
        if not self.material_type:
            raise ValueError("Material type cannot be empty.")
        if self.contaminant_level not in ['clean', 'moderately clean', 'dirty']:
            raise ValueError("Contaminant level must be one of: clean, moderately clean, dirty.")

    def to_dict(self):
        """
        Converts the cleanliness specification to a dictionary.

        :return: A dictionary representation of the cleanliness specification.
        """
        return {
            "surface_roughness": self.surface_roughness,
            "material_type": self.material_type,
            "contaminant_level": self.contaminant_level
        }

    def to_json(self):
        """
        Converts the cleanliness specification to a JSON string.

        :return: A JSON string representation of the cleanliness specification.
        """
        return json.dumps(self.to_dict(), indent=4)

def main():
    """
    Main function to demonstrate the usage of the CleanlinessSpecification class.
    """
    try:
        # Example parameters for cleanliness specification
        surface_roughness = 0.8  # in micrometers
        material_type = "steel"
        contaminant_level = "clean"

        # Create a cleanliness specification instance
        cleanliness_spec = CleanlinessSpecification(surface_roughness, material_type, contaminant_level)

        # Validate the specification
        cleanliness_spec.validate()

        # Output the specification in JSON format
        logging.info("Cleanliness Specification:")
        logging.info(cleanliness_spec.to_json())

    except ValueError as e:
        logging.error(f"Validation error: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
