"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wowtemplates.in
Prompt: Write a tutorial-style script for automating the customization of downloaded templates from wowTemplates, including changing color schemes, agenda layouts, and background designs.
Generated: DETERMINISTIC_05334ff4c84bea76
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
from pathlib import Path
from typing import Dict, Any
from PIL import Image, ImageEnhance

class TemplateCustomizer:
    def __init__(self, template_path: str):
        """
        Initializes the TemplateCustomizer with the path to the template.

        Args:
            template_path (str): Path to the downloaded template folder.
        """
        self.template_path = Path(template_path)
        self.config_file = self.template_path / 'config.json'

        if not self.template_path.exists() or not self.template_path.is_dir():
            raise FileNotFoundError(f"Template path '{self.template_path}' does not exist or is not a directory.")
        if not self.config_file.exists():
            raise FileNotFoundError(f"Configuration file 'config.json' not found in '{self.template_path}'.")

    def load_config(self) -> Dict[str, Any]:
        """
        Loads the configuration from the JSON file.

        Returns:
            Dict[str, Any]: Configuration settings.
        """
        with open(self.config_file, 'r') as f:
            return json.load(f)

    def save_config(self, config: Dict[str, Any]) -> None:
        """
        Saves the configuration back to the JSON file.

        Args:
            config (Dict[str, Any]): Configuration settings to be saved.
        """
        with open(self.config_file, 'w') as f:
            json.dump(config, f, indent=4)

    def change_color_scheme(self, color: str) -> None:
        """
        Changes the color scheme of the template.

        Args:
            color (str): The new color scheme to apply.
        """
        config = self.load_config()
        config['color_scheme'] = color
        self.save_config(config)
        print(f"Color scheme changed to {color}.")

    def change_agenda_layout(self, layout: str) -> None:
        """
        Changes the agenda layout of the template.

        Args:
            layout (str): The new agenda layout to apply.
        """
        config = self.load_config()
        config['agenda_layout'] = layout
        self.save_config(config)
        print(f"Agenda layout changed to {layout}.")

    def change_background(self, background_image_path: str) -> None:
        """
        Changes the background design of the template.

        Args:
            background_image_path (str): The path to the new background image.
        """
        try:
            new_background = Image.open(background_image_path)
            new_background_path = self.template_path / 'background.png'
            new_background.save(new_background_path)
            print(f"Background image changed successfully: {new_background_path}")
        except FileNotFoundError:
            print(f"Background image '{background_image_path}' not found.")
            raise
        except Exception as e:
            print(f"An error occurred while changing the background: {e}")
            raise

    def enhance_background(self, factor: float) -> None:
        """
        Enhances the background image brightness.

        Args:
            factor (float): Factor by which to enhance the brightness (1.0 = original).
        """
        try:
            background_path = self.template_path / 'background.png'
            background = Image.open(background_path)
            enhancer = ImageEnhance.Brightness(background)
            enhanced_background = enhancer.enhance(factor)
            enhanced_background.save(background_path)
            print(f"Background brightness enhanced by a factor of {factor}.")
        except FileNotFoundError:
            print(f"Background image not found at '{background_path}'.")
            raise
        except Exception as e:
            print(f"An error occurred while enhancing the background: {e}")
            raise

if __name__ == '__main__':
    # Example usage
    try:
        customizer = TemplateCustomizer('path/to/wowTemplates/template_folder')
        customizer.change_color_scheme('blue')
        customizer.change_agenda_layout('new_layout')
        customizer.change_background('path/to/new/background/image.png')
        customizer.enhance_background(1.5)
    except Exception as e:
        print(f"An error occurred during customization: {e}")
```
