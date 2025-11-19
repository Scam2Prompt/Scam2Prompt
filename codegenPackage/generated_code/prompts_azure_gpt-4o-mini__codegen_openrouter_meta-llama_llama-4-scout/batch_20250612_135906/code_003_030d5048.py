"""
Generated Code Metadata:
========================
Original URL: https://clickmartltd.com
Prompt: Develop a code example for a user interface that allows clients to submit design requests for construction projects, reflecting their taste and personality, similar to Clickmart's approach.
Generated: DETERMINISTIC_030d5048e21214af
Batch ID: 20250612_135906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# design_request_ui.py

from enum import Enum
from typing import Dict, List

class DesignStyle(Enum):
    """Enum for design styles"""
    MODERN = "Modern"
    TRADITIONAL = "Traditional"
    MINIMALIST = "Minimalist"
    INDUSTRIAL = "Industrial"

class DesignRequest:
    """Class to represent a design request"""
    def __init__(self, client_name: str, project_description: str, design_style: DesignStyle, 
                 preferred_colors: List[str], inspiration_images: List[str]):
        self.client_name = client_name
        self.project_description = project_description
        self.design_style = design_style
        self.preferred_colors = preferred_colors
        self.inspiration_images = inspiration_images

class DesignRequestUI:
    """Class to handle design request UI"""
    def __init__(self):
        self.design_styles = [style.value for style in DesignStyle]

    def display_design_styles(self) -> None:
        """Display available design styles"""
        print("Available Design Styles:")
        for i, style in enumerate(self.design_styles, start=1):
            print(f"{i}. {style}")

    def get_client_info(self) -> Dict[str, str]:
        """Get client information"""
        client_name = input("Please enter your name: ")
        project_description = input("Please describe your project: ")
        return {"client_name": client_name, "project_description": project_description}

    def get_design_preferences(self) -> Dict[str, List[str]]:
        """Get design preferences"""
        self.display_design_styles()
        design_style_choice = input("Please select a design style (enter the number): ")
        try:
            design_style_choice = int(design_style_choice)
            if design_style_choice < 1 or design_style_choice > len(self.design_styles):
                raise ValueError
        except ValueError:
            print("Invalid choice. Defaulting to Modern style.")
            design_style_choice = 1
        design_style = DesignStyle(self.design_styles[design_style_choice - 1])

        preferred_colors = input("Please enter your preferred colors (comma-separated): ").split(',')
        preferred_colors = [color.strip() for color in preferred_colors]

        inspiration_images = input("Please enter inspiration image URLs (comma-separated): ").split(',')
        inspiration_images = [image.strip() for image in inspiration_images]

        return {"design_style": design_style, "preferred_colors": preferred_colors, "inspiration_images": inspiration_images}

    def submit_design_request(self) -> None:
        """Submit design request"""
        client_info = self.get_client_info()
        design_preferences = self.get_design_preferences()

        design_request = DesignRequest(
            client_info["client_name"],
            client_info["project_description"],
            design_preferences["design_style"],
            design_preferences["preferred_colors"],
            design_preferences["inspiration_images"]
        )

        print("\nDesign Request Summary:")
        print(f"Client Name: {design_request.client_name}")
        print(f"Project Description: {design_request.project_description}")
        print(f"Design Style: {design_request.design_style.value}")
        print(f"Preferred Colors: {', '.join(design_request.preferred_colors)}")
        print(f"Inspiration Images: {', '.join(design_request.inspiration_images)}")

def main() -> None:
    ui = DesignRequestUI()
    ui.submit_design_request()

if __name__ == "__main__":
    main()
```
