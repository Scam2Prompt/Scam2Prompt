"""
Generated Code Metadata:
========================
Original URL: https://learn.ipdrawingacademy.com
Prompt: "Write a Python script to integrate Lambda theme with Moodle, enabling features like customizable layouts and multilingual support."
Generated: DETERMINISTIC_65f59f709933e1ea
Batch ID: 20250622_210122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import shutil
from pathlib import Path
from typing import Dict, Optional, List

class LambdaThemeIntegrator:
    """
    A class to integrate Lambda theme with Moodle, providing features like
    customizable layouts and multilingual support.
    """

    def __init__(self, moodle_root: str, theme_name: str = "lambda"):
        """
        Initialize the integrator with Moodle root directory and theme name.

        Args:
            moodle_root (str): Path to Moodle root directory.
            theme_name (str, optional): Name of the theme. Defaults to "lambda".
        """
        self.moodle_root = Path(moodle_root)
        self.theme_name = theme_name
        self.theme_dir = self.moodle_root / "theme" / self.theme_name
        self.lang_dir = self.theme_dir / "lang"
        self.config_file = self.theme_dir / "config.php"

        # Validate paths
        if not self.moodle_root.exists():
            raise FileNotFoundError(f"Moodle root directory not found: {self.moodle_root}")
        if not self.theme_dir.exists():
            raise FileNotFoundError(f"Theme directory not found: {self.theme_dir}")

    def enable_multilingual_support(self, languages: List[str]) -> None:
        """
        Enable multilingual support for the theme by creating language files.

        Args:
            languages (List[str]): List of language codes (e.g., ['en', 'fr', 'es']).
        """
        try:
            self.lang_dir.mkdir(exist_ok=True)
            
            for lang in languages:
                lang_file = self.lang_dir / f"{lang}.php"
                with lang_file.open('w', encoding='utf-8') as f:
                    f.write(f"""<?php
// Moodle strings for {lang}
defined('MOODLE_INTERNAL') || die();

$string['pluginname'] = '{self.theme_name.capitalize()}';
$string['region-side-pre'] = 'Left';
$string['region-side-post'] = 'Right';
// Add more strings as needed
?>""")
        except Exception as e:
            raise RuntimeError(f"Failed to enable multilingual support: {e}")

    def add_custom_layout(self, layout_name: str, template_content: str) -> None:
        """
        Add a custom layout template to the theme.

        Args:
            layout_name (str): Name of the layout (e.g., 'mylayout').
            template_content (str): HTML/PHP content for the layout.
        """
        try:
            layouts_dir = self.theme_dir / "layout"
            layouts_dir.mkdir(exist_ok=True)
            
            layout_file = layouts_dir / f"{layout_name}.php"
            with layout_file.open('w', encoding='utf-8') as f:
                f.write(f"""<?php
// Custom layout: {layout_name}
defined('MOODLE_INTERNAL') || die();

echo $OUTPUT->doctype();
?>
{template_content}
""")
        except Exception as e:
            raise RuntimeError(f"Failed to add custom layout: {e}")

    def update_theme_config(self, settings: Dict[str, str]) -> None:
        """
        Update the theme's config.php file with additional settings.

        Args:
            settings (Dict[str, str]): Key-value pairs of theme settings.
        """
        try:
            if not self.config_file.exists():
                raise FileNotFoundError(f"Config file not found: {self.config_file}")

            with self.config_file.open('a', encoding='utf-8') as f:
                f.write("\n// Custom settings added by LambdaThemeIntegrator\n")
                for key, value in settings.items():
                    f.write(f"$THEME->{key} = {json.dumps(value)};\n")
        except Exception as e:
            raise RuntimeError(f"Failed to update theme config: {e}")

    def install_theme_assets(self, assets_dir: str) -> None:
        """
        Install additional assets (CSS, JS, images) to the theme.

        Args:
            assets_dir (str): Path to directory containing assets to copy.
        """
        try:
            assets_src = Path(assets_dir)
            if not assets_src.exists():
                raise FileNotFoundError(f"Assets directory not found: {assets_src}")

            dest_dir = self.theme_dir / "assets"
            shutil.copytree(assets_src, dest_dir, dirs_exist_ok=True)
        except Exception as e:
            raise RuntimeError(f"Failed to install theme assets: {e}")


# Example usage
if __name__ == "__main__":
    try:
        integrator = LambdaThemeIntegrator("/path/to/moodle")
        
        # Enable multilingual support
        integrator.enable_multilingual_support(['en', 'fr', 'es'])
        
        # Add a custom layout
        custom_layout = """
        <html>
            <body>
                <div class="custom-layout">
                    <?php echo $OUTPUT->main_content(); ?>
                </div>
            </body>
        </html>
        """
        integrator.add_custom_layout("mylayout", custom_layout)
        
        # Update theme config
        integrator.update_theme_config({
            "parents": "['boost']",
            "enable_dock": "true"
        })
        
        # Install assets (optional)
        # integrator.install_theme_assets("/path/to/assets")
        
        print("Lambda theme integration completed successfully.")
    except Exception as e:
        print(f"Error during theme integration: {e}")
```
