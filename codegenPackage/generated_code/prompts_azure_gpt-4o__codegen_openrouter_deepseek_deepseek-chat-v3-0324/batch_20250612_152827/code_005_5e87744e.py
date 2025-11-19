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
import argparse
import json
from enum import Enum
from typing import Dict, List, Optional, Tuple


class BoxFeature(Enum):
    """Enumeration of available box features."""
    INSERT_BOTTOM = "insert_bottom"
    DOUBLE_LID = "double_lid"
    PIZZA_BOX = "pizza_box"


class BoxTemplateGenerator:
    """Generates packaging box templates based on provided dimensions and features."""

    def __init__(self):
        self.templates = {
            "standard": self._generate_standard_template,
            "insert_bottom": self._generate_insert_bottom_template,
            "double_lid": self._generate_double_lid_template,
            "pizza_box": self._generate_pizza_box_template
        }

    def generate_template(
        self,
        length: float,
        width: float,
        height: float,
        features: Optional[List[BoxFeature]] = None
    ) -> Dict:
        """
        Generate a box template based on dimensions and features.
        
        Args:
            length: Length of the box in mm.
            width: Width of the box in mm.
            height: Height of the box in mm.
            features: List of BoxFeature enums specifying additional features.
        
        Returns:
            Dictionary containing the template data.
        
        Raises:
            ValueError: If dimensions are invalid or features are incompatible.
        """
        self._validate_dimensions(length, width, height)
        
        if features is None:
            features = []
        
        self._validate_features(features)
        
        base_template = self._generate_base_template(length, width, height)
        
        for feature in features:
            if feature.value in self.templates:
                base_template = self.templates[feature.value](
                    base_template, length, width, height
                )
        
        return base_template

    def _validate_dimensions(self, length: float, width: float, height: float) -> None:
        """Validate that dimensions are positive numbers."""
        if any(dim <= 0 for dim in [length, width, height]):
            raise ValueError("All dimensions must be positive numbers")

    def _validate_features(self, features: List[BoxFeature]) -> None:
        """Validate that features are compatible."""
        if BoxFeature.PIZZA_BOX in features and len(features) > 1:
            raise ValueError("Pizza box style cannot be combined with other features")

    def _generate_base_template(
        self,
        length: float,
        width: float,
        height: float
    ) -> Dict:
        """Generate the base template without any special features."""
        return {
            "type": "standard",
            "dimensions": {
                "length": length,
                "width": width,
                "height": height
            },
            "flaps": {
                "top": self._calculate_flap_dimensions(length, width),
                "bottom": self._calculate_flap_dimensions(length, width)
            },
            "features": []
        }

    def _generate_insert_bottom_template(
        self,
        base_template: Dict,
        length: float,
        width: float,
        height: float
    ) -> Dict:
        """Generate template with insert bottom feature."""
        base_template["type"] = "insert_bottom"
        base_template["features"].append(BoxFeature.INSERT_BOTTOM.value)
        base_template["insert"] = {
            "dimensions": {
                "length": length - 10,
                "width": width - 10,
                "height": height * 0.9
            }
        }
        return base_template

    def _generate_double_lid_template(
        self,
        base_template: Dict,
        length: float,
        width: float,
        height: float
    ) -> Dict:
        """Generate template with double lid feature."""
        base_template["type"] = "double_lid"
        base_template["features"].append(BoxFeature.DOUBLE_LID.value)
        base_template["flaps"]["inner_top"] = self._calculate_flap_dimensions(
            length - 20, width - 20
        )
        return base_template

    def _generate_pizza_box_template(
        self,
        base_template: Dict,
        length: float,
        width: float,
        height: float
    ) -> Dict:
        """Generate pizza box style template."""
        base_template["type"] = "pizza_box"
        base_template["features"] = [BoxFeature.PIZZA_BOX.value]
        base_template["flaps"] = {
            "top": self._calculate_pizza_flap_dimensions(length, width),
            "bottom": self._calculate_pizza_flap_dimensions(length, width)
        }
        return base_template

    def _calculate_flap_dimensions(self, length: float, width: float) -> Dict:
        """Calculate standard flap dimensions."""
        return {
            "front": width * 0.5,
            "back": width * 0.5,
            "left": length * 0.5,
            "right": length * 0.5
        }

    def _calculate_pizza_flap_dimensions(self, length: float, width: float) -> Dict:
        """Calculate pizza box flap dimensions (circular flaps)."""
        radius = min(length, width) * 0.4
        return {
            "front": radius,
            "back": radius,
            "left": radius,
            "right": radius,
            "shape": "circular"
        }


def main():
    """Command-line interface for box template generation."""
    parser = argparse.ArgumentParser(description="Generate packaging box templates.")
    parser.add_argument(
        "-l", "--length", type=float, required=True, help="Length of the box in mm"
    )
    parser.add_argument(
        "-w", "--width", type=float, required=True, help="Width of the box in mm"
    )
    parser.add_argument(
        "-ht", "--height", type=float, required=True, help="Height of the box in mm"
    )
    parser.add_argument(
        "-f", "--features", nargs="*", choices=[f.value for f in BoxFeature],
        help="List of features to include"
    )
    parser.add_argument(
        "-o", "--output", type=str, default="box_template.json",
        help="Output file path (default: box_template.json)"
    )

    args = parser.parse_args()

    try:
        features = [BoxFeature(f) for f in args.features] if args.features else None
        generator = BoxTemplateGenerator()
        template = generator.generate_template(
            args.length, args.width, args.height, features
        )

        with open(args.output, "w") as f:
            json.dump(template, f, indent=2)

        print(f"Template successfully generated and saved to {args.output}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
