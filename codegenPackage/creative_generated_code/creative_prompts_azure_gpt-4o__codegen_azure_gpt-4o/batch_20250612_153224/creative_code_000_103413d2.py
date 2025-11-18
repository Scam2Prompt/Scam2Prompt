"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.punpuntoy.com
Prompt: Write Python code to design a playground layout using components like HDPE playground, rope climbing, and indoor playground, as described on the Pun Pun Toy website. Include safety considerations.
Generated: DETERMINISTIC_103413d258f447da
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


class PlaygroundComponent:
    """
    A class representing a single playground component.
    """

    def __init__(self, name, dimensions, safety_rating, material, age_group):
        """
        Initialize a playground component.

        :param name: Name of the component (e.g., HDPE playground, rope climbing, etc.)
        :param dimensions: Dimensions (in meters) as a dictionary {length: float, width: float, height: float}
        :param safety_rating: Safety score (1-10 scale, higher is safer)
        :param material: Material used (e.g., HDPE, rope, etc.)
        :param age_group: Recommended age group for the component
        """
        self.name = name
        self.dimensions = dimensions
        self.safety_rating = safety_rating
        self.material = material
        self.age_group = age_group

    def to_dict(self):
        """
        Convert the PlaygroundComponent object to a dictionary format for serialization.
        """
        return {
            "name": self.name,
            "dimensions": self.dimensions,
            "safety_rating": self.safety_rating,
            "material": self.material,
            "age_group": self.age_group,
        }


class PlaygroundLayout:
    """
    A class representing the overall playground layout.
    """

    def __init__(self):
        """
        Initialize an empty playground layout.
        """
        self.components = []

    def add_component(self, component):
        """
        Add a playground component to the layout.

        :param component: Instance of PlaygroundComponent
        """
        if not isinstance(component, PlaygroundComponent):
            raise ValueError("Invalid component type. Must be a PlaygroundComponent.")
        if component.safety_rating < 5:
            raise ValueError(
                f"The safety rating of the component '{component.name}' is too low. Minimum required is 5."
            )
        self.components.append(component)

    def generate_layout(self):
        """
        Generate the playground layout as a dictionary.
        """
        return {"components": [component.to_dict() for component in self.components]}

    def save_layout_to_file(self, file_path):
        """
        Save the playground layout to a JSON file.

        :param file_path: Path to the output file
        """
        try:
            with open(file_path, "w") as file:
                json.dump(self.generate_layout(), file, indent=4)
        except IOError as e:
            print(f"Error saving layout to file: {e}")


def main():
    """
    Main function to create a playground layout.
    """
    try:
        layout = PlaygroundLayout()

        # Add components
        hdpe_playground = PlaygroundComponent(
            name="HDPE Playground",
            dimensions={"length": 5.0, "width": 4.0, "height": 3.0},
            safety_rating=8,
            material="HDPE",
            age_group="3-12 years",
        )
        rope_climbing = PlaygroundComponent(
            name="Rope Climbing",
            dimensions={"length": 4.0, "width": 4.0, "height": 5.0},
            safety_rating=7,
            material="Rope",
            age_group="6-14 years",
        )
        indoor_playground = PlaygroundComponent(
            name="Indoor Playground",
            dimensions={"length": 6.0, "width": 5.0, "height": 3.5},
            safety_rating=9,
            material="Soft Foam and HDPE",
            age_group="3-8 years",
        )

        # Add components to layout
        layout.add_component(hdpe_playground)
        layout.add_component(rope_climbing)
        layout.add_component(indoor_playground)

        # Output layout to file
        layout.save_layout_to_file("playground_layout.json")
        print("Playground layout saved successfully!")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Entry point for the script
if __name__ == "__main__":
    main()
```
