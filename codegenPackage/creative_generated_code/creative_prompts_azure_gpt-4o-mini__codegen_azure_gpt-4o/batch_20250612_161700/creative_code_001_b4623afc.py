"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://olavovieira.com.br
Prompt: How can I implement a property evaluation system that incorporates judicial and extra-judicial appraisal methods as described by Olavo Vieira?
Generated: DETERMINISTIC_b4623afcaacfccfa
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a clean and production-ready Python implementation of a property evaluation system incorporating judicial and extra-judicial appraisal methods. 

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

class PropertyEvaluationSystem:
    """
    A system to evaluate property values using judicial and extra-judicial appraisal methods.
    """

    def __init__(self):
        """
        Initializes the property evaluation system.
        """
        self.properties = {}

    def add_property(self, property_id, description, judicial_value, extra_judicial_value):
        """
        Adds a new property to the system.

        Args:
            property_id (str): Unique identifier for the property.
            description (str): Description of the property.
            judicial_value (float): Appraised value using judicial methods.
            extra_judicial_value (float): Appraised value using extra-judicial methods.

        Raises:
            ValueError: If judicial or extra-judicial values are not positive.
        """
        if judicial_value <= 0 or extra_judicial_value <= 0:
            raise ValueError("Appraised values must be positive numbers.")

        self.properties[property_id] = {
            "description": description,
            "judicial_value": judicial_value,
            "extra_judicial_value": extra_judicial_value,
        }
        logging.info(f"Property '{property_id}' added successfully.")

    def evaluate_property(self, property_id):
        """
        Evaluates the property value by combining judicial and extra-judicial methods.

        Args:
            property_id (str): Unique identifier for the property.

        Returns:
            float: Combined property value.

        Raises:
            KeyError: If the property ID does not exist.
        """
        if property_id not in self.properties:
            raise KeyError(f"Property with ID '{property_id}' not found.")

        judicial_value = self.properties[property_id]["judicial_value"]
        extra_judicial_value = self.properties[property_id]["extra_judicial_value"]

        # Compute combined value (weighted average as an example)
        combined_value = (judicial_value * 0.6) + (extra_judicial_value * 0.4)

        logging.info(
            f"Property '{property_id}' evaluated successfully. Combined value: {combined_value:.2f}"
        )
        return combined_value

    def list_properties(self):
        """
        Lists all properties in the system.

        Returns:
            dict: Dictionary containing all properties and their details.
        """
        return self.properties


# Example usage
if __name__ == "__main__":
    try:
        # Instantiate the system
        system = PropertyEvaluationSystem()

        # Add properties
        system.add_property(
            property_id="P001",
            description="Luxury apartment in downtown.",
            judicial_value=500000.0,
            extra_judicial_value=450000.0,
        )
        system.add_property(
            property_id="P002",
            description="Beachfront villa.",
            judicial_value=750000.0,
            extra_judicial_value=800000.0,
        )

        # Evaluate properties
        value_p001 = system.evaluate_property("P001")
        value_p002 = system.evaluate_property("P002")

        # List all properties
        all_properties = system.list_properties()
        logging.info(f"All properties: {all_properties}")

    except (ValueError, KeyError) as e:
        logging.error(e)
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
```

This code provides a robust, scalable property evaluation system using judicial and extra-judicial appraisal methods. Adjustments can be made for more advanced algorithms or integrations as needed.
