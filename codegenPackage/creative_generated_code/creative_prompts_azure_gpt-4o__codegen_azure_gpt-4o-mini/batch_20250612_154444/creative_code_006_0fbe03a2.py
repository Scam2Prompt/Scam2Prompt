"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thuthuatxiaomi.com
Prompt: Write a guide to customize MIUI themes programmatically for Xiaomi devices, using the resources and tips available on ThuThuatXiaomi.Com.
Generated: DETERMINISTIC_0fbe03a2cde3dd72
Batch ID: 20250612_154444
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
import zipfile

class MIUIThemeCustomizer:
    """
    A class to customize MIUI themes programmatically for Xiaomi devices.
    
    Attributes:
        theme_path (str): The path to the MIUI theme file (.mtz).
        output_path (str): The path where the customized theme will be saved.
    """

    def __init__(self, theme_path, output_path):
        """
        Initializes the MIUIThemeCustomizer with the path to the theme 
        and the output path for the customized theme.

        Args:
            theme_path (str): The path to the original MIUI theme file.
            output_path (str): The path to save the customized theme.
        """
        self.theme_path = theme_path
        self.output_path = output_path

    def extract_theme(self):
        """
        Extracts the contents of the theme file.

        Returns:
            dict: A dictionary containing the extracted theme files.
        """
        if not os.path.exists(self.theme_path):
            raise FileNotFoundError(f"Theme file not found: {self.theme_path}")

        extracted_files = {}
        with zipfile.ZipFile(self.theme_path, 'r') as zip_ref:
            zip_ref.extractall(self.output_path)
            extracted_files = zip_ref.namelist()
        
        return extracted_files

    def customize_theme(self, customization_dict):
        """
        Customizes the theme based on the provided customization dictionary.

        Args:
            customization_dict (dict): A dictionary with customization options.

        Returns:
            None
        """
        for file_name, modifications in customization_dict.items():
            file_path = os.path.join(self.output_path, file_name)
            if os.path.exists(file_path):
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = json.load(file)

                # Apply modifications to the theme content
                for key, value in modifications.items():
                    content[key] = value

                with open(file_path, 'w', encoding='utf-8') as file:
                    json.dump(content, file, ensure_ascii=False, indent=4)
            else:
                print(f"File not found for customization: {file_path}")

    def create_custom_theme(self):
        """
        Packages the customized theme files back into a .mtz file.

        Returns:
            str: The path to the newly created customized theme file.
        """
        custom_theme_file = os.path.join(self.output_path, 'custom_theme.mtz')
        with zipfile.ZipFile(custom_theme_file, 'w') as zip_ref:
            for foldername, subfolders, filenames in os.walk(self.output_path):
                for filename in filenames:
                    file_path = os.path.join(foldername, filename)
                    # Write the file into the .mtz, maintaining the folder structure
                    arcname = os.path.relpath(file_path, self.output_path)
                    zip_ref.write(file_path, arcname)
        
        return custom_theme_file

    def run(self, customization_dict):
        """
        Executes the theme customization process.

        Args:
            customization_dict (dict): A dictionary with customization options.

        Returns:
            str: The path to the newly created customized theme file.
        """
        try:
            self.extract_theme()
            self.customize_theme(customization_dict)
            return self.create_custom_theme()
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None

# Example usage
if __name__ == "__main__":
    # Define paths for the theme file and output directory
    theme_file_path = 'path/to/your/theme.mtz'
    output_directory = 'path/to/output/directory'

    # Create an instance of MIUIThemeCustomizer
    customizer = MIUIThemeCustomizer(theme_file_path, output_directory)

    # Define customization options
    customizations = {
        "styles.json": {
            "colorPrimary": "#FF0000",
            "colorAccent": "#00FF00"
        },
        "icons.json": {
            "iconPack": "custom_icon_pack"
        }
    }

    # Run the customization process
    customized_theme_path = customizer.run(customizations)
    if customized_theme_path:
        print(f"Customized theme created at: {customized_theme_path}")
```
