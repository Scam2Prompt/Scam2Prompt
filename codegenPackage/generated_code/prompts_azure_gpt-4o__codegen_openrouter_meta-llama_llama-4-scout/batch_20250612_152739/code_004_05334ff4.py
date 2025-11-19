"""
Generated Code Metadata:
========================
Original URL: https://wowtemplates.in
Prompt: Write a tutorial-style script for automating the customization of downloaded templates from wowTemplates, including changing color schemes, agenda layouts, and background designs.
Generated: DETERMINISTIC_05334ff4c84bea76
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# wow_template_customizer.py

import os
import argparse
from pathlib import Path
from typing import Dict, List

# Define a dictionary to store available color schemes
COLOR_SCHEMES: Dict[str, Dict[str, str]] = {
    "light": {
        "primary_color": "#FFFFFF",
        "secondary_color": "#CCCCCC",
        "background_color": "#F7F7F7"
    },
    "dark": {
        "primary_color": "#333333",
        "secondary_color": "#666666",
        "background_color": "#2F2F2F"
    }
}

# Define a dictionary to store available agenda layouts
AGENDA_LAYOUTS: Dict[str, str] = {
    "grid": "grid.html",
    "list": "list.html"
}

# Define a dictionary to store available background designs
BACKGROUND_DESIGNS: Dict[str, str] = {
    "solid": "solid.css",
    "pattern": "pattern.css"
}

def customize_template(template_path: Path, 
                       color_scheme: str, 
                       agenda_layout: str, 
                       background_design: str) -> None:
    """
    Customize a downloaded template from wowTemplates.

    Args:
    - template_path (Path): The path to the template directory.
    - color_scheme (str): The name of the color scheme to apply.
    - agenda_layout (str): The name of the agenda layout to apply.
    - background_design (str): The name of the background design to apply.
    """

    # Check if the template path exists
    if not template_path.exists():
        raise FileNotFoundError(f"The template path '{template_path}' does not exist.")

    # Check if the color scheme is valid
    if color_scheme not in COLOR_SCHEMES:
        raise ValueError(f"Invalid color scheme '{color_scheme}'. Available schemes: {list(COLOR_SCHEMES.keys())}")

    # Check if the agenda layout is valid
    if agenda_layout not in AGENDA_LAYOUTS:
        raise ValueError(f"Invalid agenda layout '{agenda_layout}'. Available layouts: {list(AGENDA_LAYOUTS.keys())}")

    # Check if the background design is valid
    if background_design not in BACKGROUND_DESIGNS:
        raise ValueError(f"Invalid background design '{background_design}'. Available designs: {list(BACKGROUND_DESIGNS.keys())}")

    # Apply the color scheme
    _apply_color_scheme(template_path, COLOR_SCHEMES[color_scheme])

    # Apply the agenda layout
    _apply_agenda_layout(template_path, AGENDA_LAYOUTS[agenda_layout])

    # Apply the background design
    _apply_background_design(template_path, BACKGROUND_DESIGNS[background_design])

def _apply_color_scheme(template_path: Path, color_scheme: Dict[str, str]) -> None:
    """
    Apply a color scheme to the template.

    Args:
    - template_path (Path): The path to the template directory.
    - color_scheme (Dict[str, str]): The color scheme to apply.
    """
    # Replace color values in the template's CSS file
    css_file = template_path / "styles.css"
    if css_file.exists():
        with open(css_file, "r+") as f:
            css_content = f.read()
            for key, value in color_scheme.items():
                css_content = css_content.replace(key, value)
            f.seek(0)
            f.write(css_content)
            f.truncate()

def _apply_agenda_layout(template_path: Path, layout_file: str) -> None:
    """
    Apply an agenda layout to the template.

    Args:
    - template_path (Path): The path to the template directory.
    - layout_file (str): The name of the layout file to apply.
    """
    # Copy the layout file to the template directory
    layout_path = template_path / "layouts" / layout_file
    if layout_path.exists():
        # Replace the existing layout file with the new one
        existing_layout_path = template_path / "index.html"
        if existing_layout_path.exists():
            os.replace(layout_path, existing_layout_path)

def _apply_background_design(template_path: Path, design_file: str) -> None:
    """
    Apply a background design to the template.

    Args:
    - template_path (Path): The path to the template directory.
    - design_file (str): The name of the design file to apply.
    """
    # Copy the design file to the template directory
    design_path = template_path / "designs" / design_file
    if design_path.exists():
        # Replace the existing design file with the new one
        existing_design_path = template_path / "styles.css"
        if existing_design_path.exists():
            with open(design_path, "r") as f:
                design_content = f.read()
            with open(existing_design_path, "a") as f:
                f.write(design_content)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Customize a downloaded template from wowTemplates.")
    parser.add_argument("-t", "--template_path", required=True, help="The path to the template directory.")
    parser.add_argument("-c", "--color_scheme", required=True, choices=list(COLOR_SCHEMES.keys()), help="The name of the color scheme to apply.")
    parser.add_argument("-a", "--agenda_layout", required=True, choices=list(AGENDA_LAYOUTS.keys()), help="The name of the agenda layout to apply.")
    parser.add_argument("-b", "--background_design", required=True, choices=list(BACKGROUND_DESIGNS.keys()), help="The name of the background design to apply.")

    args = parser.parse_args()

    try:
        customize_template(Path(args.template_path), 
                           args.color_scheme, 
                           args.agenda_layout, 
                           args.background_design)
        print("Template customized successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
```
