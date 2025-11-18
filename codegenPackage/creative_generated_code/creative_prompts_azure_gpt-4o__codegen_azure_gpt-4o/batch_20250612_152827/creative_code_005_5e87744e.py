"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metis.com.tw
Prompt: Develop a Python script to generate packaging box templates with predefined dimensions and features such as "insert bottom," "double lid," and "pizza box style," based on the options provided by Metis.
Generated: DETERMINISTIC_5e87744eb82989c2
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import sys

# Define the BoxTemplate class to represent box specifications
class BoxTemplate:
    def __init__(self, name, width, height, depth, features):
        """
        Initialize a BoxTemplate object.

        Args:
            name (str): Name of the box template.
            width (float): Width of the box in cm.
            height (float): Height of the box in cm.
            depth (float): Depth of the box in cm.
            features (list): List of features for the box.
        """
        self.name = name
        self.width = width
        self.height = height
        self.depth = depth
        self.features = features

    def generate_template(self):
        """
        Generate a packaging box template based on dimensions and features.

        Returns:
            str: Box template information in JSON format.
        """
        template = {
            "name": self.name,
            "dimensions": {
                "width": self.width,
                "height": self.height,
                "depth": self.depth
            },
            "features": self.features
        }
        return json.dumps(template, indent=4)

# Define a function to validate input dimensions and features
def validate_input(width, height, depth, features, valid_features):
    """
    Validate the input dimensions and features.

    Args:
        width (float): Width of the box.
        height (float): Height of the box.
        depth (float): Depth of the box.
        features (list): List of features for the box.
        valid_features (list): List of valid features.

    Returns:
        bool: True if inputs are valid, False otherwise.
    """
    try:
        if width <= 0 or height <= 0 or depth <= 0:
            raise ValueError("Dimensions must be positive numbers.")
        for feature in features:
            if feature not in valid_features:
                raise ValueError(f"Invalid feature: {feature}")
        return True
    except ValueError as ve:
        print(f"Input validation error: {ve}")
        return False

# Main function to handle user input and generate box templates
def main():
    """
    Main function to generate packaging box templates based on user input.
    """
    # Predefined valid features
    valid_features = ["insert bottom", "double lid", "pizza box style"]

    try:
        # Get user input for dimensions and features
        name = input("Enter the name of the box template: ").strip()
        width = float(input("Enter the width of the box (in cm): ").strip())
        height = float(input("Enter the height of the box (in cm): ").strip())
        depth = float(input("Enter the depth of the box (in cm): ").strip())
        features = input(
            f"Enter the features for the box (comma-separated, valid options: {valid_features}): "
        ).strip().split(",")

        # Clean up features list
        features = [feature.strip() for feature in features]

        # Validate input
        if not validate_input(width, height, depth, features, valid_features):
            print("Invalid input. Exiting.")
            return

        # Create a BoxTemplate object
        box_template = BoxTemplate(name, width, height, depth, features)

        # Generate and display the box template
        print("\nGenerated Box Template:")
        print(box_template.generate_template())

    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
```
