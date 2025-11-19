"""
Generated Code Metadata:
========================
Original URL: https://metis.com.tw
Prompt: Develop a Python script to generate packaging box templates with predefined dimensions and features such as "insert bottom," "double lid," and "pizza box style," based on the options provided by Metis.
Generated: DETERMINISTIC_5e87744eb82989c2
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from typing import List, Dict

class BoxTemplateGenerator:
    """
    A class to generate packaging box templates with predefined dimensions and features.
    """

    def __init__(self, output_directory: str):
        """
        Initializes the BoxTemplateGenerator with the specified output directory.

        :param output_directory: Directory where the box templates will be saved.
        """
        self.output_directory = output_directory
        self.box_features = {
            "insert_bottom": self.create_insert_bottom,
            "double_lid": self.create_double_lid,
            "pizza_box": self.create_pizza_box
        }

        # Ensure the output directory exists
        os.makedirs(self.output_directory, exist_ok=True)

    def generate_template(self, dimensions: Dict[str, float], features: List[str]) -> None:
        """
        Generates a box template based on the provided dimensions and features.

        :param dimensions: A dictionary containing the dimensions of the box (length, width, height).
        :param features: A list of features to include in the box template.
        """
        try:
            template_content = self.create_base_template(dimensions)

            for feature in features:
                if feature in self.box_features:
                    template_content += self.box_features[feature](dimensions)
                else:
                    print(f"Warning: Feature '{feature}' is not recognized.")

            self.save_template(dimensions, template_content)

        except Exception as e:
            print(f"Error generating template: {e}")

    def create_base_template(self, dimensions: Dict[str, float]) -> str:
        """
        Creates the base template for the box.

        :param dimensions: A dictionary containing the dimensions of the box.
        :return: A string representing the base template.
        """
        return f"Base Box Template:\nDimensions: {dimensions}\n"

    def create_insert_bottom(self, dimensions: Dict[str, float]) -> str:
        """
        Creates the insert bottom feature for the box.

        :param dimensions: A dictionary containing the dimensions of the box.
        :return: A string representing the insert bottom feature.
        """
        return "Feature: Insert Bottom\n"

    def create_double_lid(self, dimensions: Dict[str, float]) -> str:
        """
        Creates the double lid feature for the box.

        :param dimensions: A dictionary containing the dimensions of the box.
        :return: A string representing the double lid feature.
        """
        return "Feature: Double Lid\n"

    def create_pizza_box(self, dimensions: Dict[str, float]) -> str:
        """
        Creates the pizza box style feature.

        :param dimensions: A dictionary containing the dimensions of the box.
        :return: A string representing the pizza box style feature.
        """
        return "Feature: Pizza Box Style\n"

    def save_template(self, dimensions: Dict[str, float], content: str) -> None:
        """
        Saves the generated box template to a file.

        :param dimensions: A dictionary containing the dimensions of the box.
        :param content: The content of the box template to save.
        """
        filename = f"box_template_{dimensions['length']}x{dimensions['width']}x{dimensions['height']}.txt"
        file_path = os.path.join(self.output_directory, filename)

        with open(file_path, 'w') as file:
            file.write(content)

        print(f"Template saved to: {file_path}")


if __name__ == "__main__":
    # Example usage
    output_dir = "box_templates"
    generator = BoxTemplateGenerator(output_directory=output_dir)

    # Define box dimensions and features
    box_dimensions = {
        "length": 12.0,
        "width": 12.0,
        "height": 2.0
    }
    box_features = ["insert_bottom", "double_lid", "pizza_box"]

    # Generate the box template
    generator.generate_template(dimensions=box_dimensions, features=box_features)
```
