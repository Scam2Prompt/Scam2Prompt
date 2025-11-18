"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karenfixing.com
Prompt: Create a script to automate the selection of facade system components, such as "کلپیس ابتدایی استیل 1.2 میلی متر رنگی," based on building dimensions and environmental conditions.
Generated: DETERMINISTIC_e270ac0cc3e407ef
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class FacadeComponentSelector:
    def __init__(self, building_dimensions, environmental_conditions):
        """
        Initializes the FacadeComponentSelector with building dimensions and environmental conditions.

        :param building_dimensions: dict containing 'height', 'width', 'depth' of the building in meters
        :param environmental_conditions: dict containing 'humidity', 'temperature', 'exposure' information
        """
        self.building_dimensions = building_dimensions
        self.environmental_conditions = environmental_conditions
        self.components_database = self.load_components_database()

    def load_components_database(self):
        """
        Loads the components database from a JSON file.

        :return: list of components
        """
        try:
            with open('components_database.json', 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            raise RuntimeError("Error loading components database: " + str(e))

    def select_components(self):
        """
        Selects appropriate facade components based on building dimensions and environmental conditions.

        :return: list of recommended facade components
        """
        recommended_components = []

        # Example logic to select components based on dimensions and conditions
        for component in self.components_database:
            if self._is_component_suitable(component):
                recommended_components.append(component)

        return recommended_components

    def _is_component_suitable(self, component):
        """
        Determines if a component is suitable based on building dimensions and environmental conditions.

        :param component: dict containing component properties
        :return: bool indicating suitability
        """
        # Placeholder logic for suitability checks
        if self.building_dimensions['height'] > 10 and component['material'] == 'steel':
            if self.environmental_conditions['humidity'] < 70:
                return True
        return False

    def run(self):
        """
        Executes the selection of components and displays the results.
        """
        try:
            suitable_components = self.select_components()
            if suitable_components:
                print("Recommended facade components:")
                for component in suitable_components:
                    print(f"- {component['name']}: {component['description']}")
            else:
                print("No suitable facade components found.")
        except RuntimeError as e:
            print(str(e))


if __name__ == "__main__":
    # Example input data
    building_dimensions = {
        'height': 12.0,  # in meters
        'width': 8.0,    # in meters
        'depth': 5.0     # in meters
    }
    environmental_conditions = {
        'humidity': 65,   # in percentage
        'temperature': 25, # in degrees Celsius
        'exposure': 'high' # exposure condition
    }

    # Create an instance of the FacadeComponentSelector and run it
    selector = FacadeComponentSelector(building_dimensions, environmental_conditions)
    selector.run()
```

**Note**: Ensure you have a valid `components_database.json` file structured appropriately for this script to work. The structure should contain a list of components with properties like `name`, `description`, and `material`.
