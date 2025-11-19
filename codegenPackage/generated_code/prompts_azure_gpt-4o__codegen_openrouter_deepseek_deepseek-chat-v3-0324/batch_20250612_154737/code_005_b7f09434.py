"""
Generated Code Metadata:
========================
Original URL: https://landoparafusos.blogspot.com
Prompt: Provide a Python script to automate the selection of fasteners like "Parafuso Cabeça de Martelo" and "Porcas" based on the material type of the roof structure in a solar energy project.
Generated: DETERMINISTIC_b7f09434b602123d
Batch ID: 20250612_154737
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from enum import Enum

class MaterialType(Enum):
    WOOD = "wood"
    METAL = "metal"
    CONCRETE = "concrete"

class FastenerType(Enum):
    HAMMER_HEAD_SCREW = "Parafuso Cabeça de Martelo"
    NUT = "Porcas"
    ANCHOR_BOLT = "Parafuso de Âncora"
    LAG_SCREW = "Parafuso de Fixação"

class FastenerSelector:
    """
    A class to select appropriate fasteners based on roof material type.
    """
    
    # Mapping of material types to recommended fasteners
    MATERIAL_TO_FASTENER = {
        MaterialType.WOOD: [FastenerType.HAMMER_HEAD_SCREW, FastenerType.LAG_SCREW],
        MaterialType.METAL: [FastenerType.NUT, FastenerType.HAMMER_HEAD_SCREW],
        MaterialType.CONCRETE: [FastenerType.ANCHOR_BOLT, FastenerType.NUT]
    }
    
    @staticmethod
    def get_fasteners(material_type):
        """
        Get recommended fasteners for the given material type.
        
        Args:
            material_type (MaterialType): The type of material
            
        Returns:
            list: List of recommended FastenerType enums
            
        Raises:
            ValueError: If material_type is not a valid MaterialType
        """
        if not isinstance(material_type, MaterialType):
            raise ValueError("Invalid material type. Must be a MaterialType enum.")
            
        return FastenerSelector.MATERIAL_TO_FASTENER.get(material_type, [])

def load_config(config_file="fastener_config.json"):
    """
    Load configuration from JSON file.
    
    Args:
        config_file (str): Path to configuration file
        
    Returns:
        dict: Configuration data
        
    Raises:
        FileNotFoundError: If config file doesn't exist
        json.JSONDecodeError: If config file is invalid JSON
    """
    try:
        with open(config_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"Configuration file {config_file} not found.")
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"Invalid JSON in configuration file: {e.msg}", e.doc, e.pos)

def save_selection(project_name, material_type, fasteners, output_file="fastener_selections.json"):
    """
    Save fastener selection to a JSON file.
    
    Args:
        project_name (str): Name of the solar project
        material_type (str): Material type used
        fasteners (list): List of selected fasteners
        output_file (str): Path to output file
        
    Raises:
        IOError: If there's an error writing to the file
    """
    try:
        data = {
            "project_name": project_name,
            "material_type": material_type,
            "fasteners": [f.value for f in fasteners],
            "timestamp": datetime.datetime.now().isoformat()
        }
        
        # Read existing data if file exists
        existing_data = []
        try:
            with open(output_file, 'r', encoding='utf-8') as f:
                existing_data = json.load(f)
                if not isinstance(existing_data, list):
                    existing_data = []
        except (FileNotFoundError, json.JSONDecodeError):
            pass
            
        existing_data.append(data)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(existing_data, f, indent=4, ensure_ascii=False)
            
    except IOError as e:
        raise IOError(f"Error saving selection: {str(e)}")

def main():
    import argparse
    import datetime
    
    parser = argparse.ArgumentParser(description="Solar Project Fastener Selector")
    parser.add_argument("project_name", help="Name of the solar project")
    parser.add_argument("material", help="Roof material type (wood, metal, concrete)")
    parser.add_argument("--config", default="fastener_config.json", help="Path to configuration file")
    parser.add_argument("--output", default="fastener_selections.json", help="Output file path")
    
    args = parser.parse_args()
    
    try:
        # Load any additional configuration
        config = load_config(args.config)
        
        # Convert input material to enum
        try:
            material_type = MaterialType(args.material.lower())
        except ValueError:
            raise ValueError(f"Invalid material type: {args.material}. Must be one of: {[m.value for m in MaterialType]}")
        
        # Get recommended fasteners
        fasteners = FastenerSelector.get_fasteners(material_type)
        
        if not fasteners:
            print(f"No fasteners found for material type: {material_type.value}")
            return
            
        print(f"Recommended fasteners for {material_type.value}:")
        for fastener in fasteners:
            print(f"- {fastener.value}")
            
        # Save selection
        save_selection(args.project_name, material_type.value, fasteners, args.output)
        print(f"Selection saved to {args.output}")
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return 1
        
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())
```
