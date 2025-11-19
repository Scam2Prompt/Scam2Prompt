"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://novaforma.hr
Prompt: Write a Python script that automates the design process for a totem display based on the guidelines provided by Nova Forma.
Generated: DETERMINISTIC_19cd79a0f920a2b0
Batch ID: 20250612_160853
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

# Constants
CONFIG_FILE = "nova_forma_guidelines.json"
OUTPUT_DIRECTORY = "totem_designs"

# Function to load guidelines from a JSON configuration file
def load_guidelines(config_file):
    """
    Loads Nova Forma guidelines from a JSON file.
    
    :param config_file: Path to the JSON configuration file.
    :return: Dictionary containing guidelines.
    """
    try:
        with open(config_file, 'r') as file:
            guidelines = json.load(file)
        return guidelines
    except FileNotFoundError:
        raise FileNotFoundError(f"Configuration file '{config_file}' not found.")
    except json.JSONDecodeError:
        raise ValueError(f"Configuration file '{config_file}' contains invalid JSON.")

# Function to create the totem design directory
def create_output_directory(directory):
    """
    Creates an output directory for storing totem design files.
    
    :param directory: Path to the output directory.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

# Function to generate totem designs based on guidelines
def generate_totem_designs(guidelines, output_directory):
    """
    Automates the generation of totem designs based on provided guidelines.
    
    :param guidelines: Dictionary containing Nova Forma guidelines.
    :param output_directory: Path to the output directory.
    """
    for design_name, design_spec in guidelines.get("designs", {}).items():
        file_name = f"{design_name.replace(' ', '_').lower()}.txt"
        file_path = os.path.join(output_directory, file_name)
        
        try:
            with open(file_path, 'w') as file:
                file.write(f"Totem Design: {design_name}\n")
                file.write(f"Specifications:\n")
                for key, value in design_spec.items():
                    file.write(f"  - {key}: {value}\n")
        except IOError as e:
            print(f"Error writing to file '{file_path}': {e}")
        else:
            print(f"Totem design '{design_name}' generated successfully at '{file_path}'.")

# Main function
def main():
    """
    Main entry point for the script. Automates the totem design process based on Nova Forma guidelines.
    """
    try:
        # Load guidelines
        guidelines = load_guidelines(CONFIG_FILE)
        
        # Create output directory
        create_output_directory(OUTPUT_DIRECTORY)
        
        # Generate totem designs
        generate_totem_designs(guidelines, OUTPUT_DIRECTORY)
    except Exception as e:
        print(f"An error occurred: {e}")

# Execute the script
if __name__ == "__main__":
    main()
```
