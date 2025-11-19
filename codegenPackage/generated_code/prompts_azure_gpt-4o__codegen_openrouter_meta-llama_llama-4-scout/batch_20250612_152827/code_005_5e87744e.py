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
from dataclasses import dataclass
from enum import Enum
from typing import Optional

class BoxStyle(Enum):
    """Predefined box styles."""
    INSERT_BOTTOM = "insert_bottom"
    DOUBLE_LID = "double_lid"
    PIZZA_BOX = "pizza_box"

@dataclass
class BoxDimensions:
    """Box dimensions."""
    length: float
    width: float
    height: float

@dataclass
class BoxTemplate:
    """Box template with dimensions and features."""
    dimensions: BoxDimensions
    style: BoxStyle
    insert_bottom: bool = False
    double_lid: bool = False

def generate_box_template(dimensions: BoxDimensions, style: BoxStyle, 
                          insert_bottom: bool = False, double_lid: bool = False) -> BoxTemplate:
    """
    Generate a box template with predefined dimensions and features.

    Args:
    - dimensions (BoxDimensions): Box dimensions.
    - style (BoxStyle): Box style.
    - insert_bottom (bool): Whether to include an insert bottom. Defaults to False.
    - double_lid (bool): Whether to include a double lid. Defaults to False.

    Returns:
    - BoxTemplate: Box template with dimensions and features.
    """
    return BoxTemplate(dimensions, style, insert_bottom, double_lid)

def create_box_template_from_args(args: argparse.Namespace) -> BoxTemplate:
    """
    Create a box template from command line arguments.

    Args:
    - args (argparse.Namespace): Command line arguments.

    Returns:
    - BoxTemplate: Box template with dimensions and features.
    """
    try:
        dimensions = BoxDimensions(
            length=float(args.length),
            width=float(args.width),
            height=float(args.height)
        )
        style = BoxStyle(args.style)
    except ValueError as e:
        print(f"Invalid argument: {e}")
        return None

    return generate_box_template(
        dimensions,
        style,
        insert_bottom=args.insert_bottom,
        double_lid=args.double_lid
    )

def print_box_template(template: BoxTemplate) -> None:
    """
    Print a box template.

    Args:
    - template (BoxTemplate): Box template with dimensions and features.
    """
    print("Box Template:")
    print(f"  Dimensions: {template.dimensions.length} x {template.dimensions.width} x {template.dimensions.height}")
    print(f"  Style: {template.style.value}")
    print(f"  Insert Bottom: {template.insert_bottom}")
    print(f"  Double Lid: {template.double_lid}")

def main() -> None:
    parser = argparse.ArgumentParser(description="Generate packaging box templates.")
    parser.add_argument("--length", type=float, required=True, help="Box length.")
    parser.add_argument("--width", type=float, required=True, help="Box width.")
    parser.add_argument("--height", type=float, required=True, help="Box height.")
    parser.add_argument("--style", type=str, required=True, choices=[style.value for style in BoxStyle], help="Box style.")
    parser.add_argument("--insert-bottom", action="store_true", help="Include an insert bottom.")
    parser.add_argument("--double-lid", action="store_true", help="Include a double lid.")

    args = parser.parse_args()
    template = create_box_template_from_args(args)

    if template:
        print_box_template(template)

if __name__ == "__main__":
    main()
```
