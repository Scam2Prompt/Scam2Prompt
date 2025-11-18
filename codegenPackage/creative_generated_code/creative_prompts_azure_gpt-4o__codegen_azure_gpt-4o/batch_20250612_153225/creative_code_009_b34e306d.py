"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kimiyashimi.com
Prompt: Generate a script to validate the authenticity of chemical products using the analysis sheets provided by suppliers like Kimia Shimi.
Generated: DETERMINISTIC_b34e306dcdb7e08f
Batch ID: 20250612_153225
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

def load_analysis_sheet(file_path):
    """
    Load the analysis sheet from a JSON file.
    
    Args:
        file_path (str): Path to the JSON file containing the analysis sheet.
    
    Returns:
        dict: Parsed analysis sheet data.
    
    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file content is not valid JSON.
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Analysis sheet file '{file_path}' not found.")
    
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON format in '{file_path}': {e}")

def validate_chemical_product(analysis_data, expected_properties):
    """
    Validate the authenticity of a chemical product based on the analysis data.
    
    Args:
        analysis_data (dict): Data from the analysis sheet.
        expected_properties (dict): Dictionary of expected chemical properties 
                                    and their acceptable ranges.
    
    Returns:
        bool: True if the product is authentic, False otherwise.
    
    Example of `expected_properties`:
        {
            "purity": {"min": 98, "max": 100},
            "density": {"min": 1.5, "max": 1.8},
        }
    """
    for property_name, acceptable_range in expected_properties.items():
        if property_name not in analysis_data:
            print(f"Property '{property_name}' missing from analysis sheet.")
            return False

        value = analysis_data[property_name]
        if not (acceptable_range["min"] <= value <= acceptable_range["max"]):
            print(f"Property '{property_name}' value {value} is out of acceptable range.")
            return False
    
    return True

def main():
    """
    Main function to validate chemical products.
    """
    # Path to the analysis sheet file
    analysis_sheet_path = "analysis_sheet.json"
    
    # Define expected properties and acceptable ranges
    expected_properties = {
        "purity": {"min": 98, "max": 100},
        "density": {"min": 1.5, "max": 1.8},
        "ph": {"min": 6, "max": 8}
    }
    
    try:
        # Load analysis sheet
        analysis_data = load_analysis_sheet(analysis_sheet_path)
        
        # Validate product authenticity
        is_authentic = validate_chemical_product(analysis_data, expected_properties)
        
        if is_authentic:
            print("Chemical product is authentic.")
        else:
            print("Chemical product failed authenticity validation.")
    
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
