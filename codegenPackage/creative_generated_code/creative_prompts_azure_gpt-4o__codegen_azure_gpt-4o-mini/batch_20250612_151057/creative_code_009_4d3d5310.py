"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sctoll.io
Prompt: Write a script to automate the customization of multi-piece floated center caps for Rolls Royce wheels, as described in Brixton Forged™'s Luxury Series.
Generated: DETERMINISTIC_4d3d5310efb75f6c
Batch ID: 20250612_151057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os

class CenterCapCustomizer:
    """
    A class to automate the customization of multi-piece floated center caps for Rolls Royce wheels.
    
    Attributes:
        template_file (str): Path to the JSON template file that contains customization options.
        output_directory (str): Directory where the customized designs will be saved.
    """

    def __init__(self, template_file, output_directory):
        """
        Initializes the CenterCapCustomizer with a template file and output directory.
        
        Args:
            template_file (str): Path to the JSON template file.
            output_directory (str): Directory for saving customized designs.
        """
        self.template_file = template_file
        self.output_directory = output_directory
        self.customization_options = self.load_template()

    def load_template(self):
        """
        Loads the customization options from the JSON template file.
        
        Returns:
            dict: A dictionary containing customization options.
        """
        try:
            with open(self.template_file, 'r') as file:
                options = json.load(file)
            return options
        except FileNotFoundError:
            raise Exception(f"Template file '{self.template_file}' not found.")
        except json.JSONDecodeError:
            raise Exception(f"Error decoding JSON from the file '{self.template_file}'.")

    def customize_center_cap(self, options):
        """
        Customizes the center cap based on provided options.
        
        Args:
            options (dict): Customization options for the center cap.
        
        Returns:
            dict: A dictionary representing the customized center cap design.
        """
        customized_cap = {}
        for key, value in options.items():
            if key in self.customization_options:
                customized_cap[key] = value
            else:
                raise ValueError(f"Invalid option '{key}' provided for customization.")
        return customized_cap

    def save_customized_cap(self, customized_cap, filename):
        """
        Saves the customized center cap to a JSON file.
        
        Args:
            customized_cap (dict): The customized center cap design.
            filename (str): The name of the file to save the design.
        """
        try:
            output_path = os.path.join(self.output_directory, filename)
            with open(output_path, 'w') as file:
                json.dump(customized_cap, file, indent=4)
            print(f"Customized center cap saved to '{output_path}'.")
        except IOError as e:
            raise Exception(f"Error saving the customized center cap: {e}")

    def run(self, customization_options, output_filename):
        """
        Runs the customization process.
        
        Args:
            customization_options (dict): User-defined customization options.
            output_filename (str): The filename to save the customized design.
        """
        try:
            customized_cap = self.customize_center_cap(customization_options)
            self.save_customized_cap(customized_cap, output_filename)
        except Exception as e:
            print(f"An error occurred: {e}")

# Example Usage
if __name__ == "__main__":
    # Specify the path to the customization template and the output directory
    template_path = 'path/to/customization_template.json'
    output_dir = 'path/to/output/directory'

    # Create an instance of the customizer
    customizer = CenterCapCustomizer(template_path, output_dir)

    # Define the customization options (example)
    user_options = {
        "finish": "Gloss Black",
        "logo": "Custom Logo",
        "ring_color": "Chrome",
        "center_color": "Matte Black"
    }

    # Run the customization process
    customizer.run(user_options, 'custom_center_cap_design.json')
```
