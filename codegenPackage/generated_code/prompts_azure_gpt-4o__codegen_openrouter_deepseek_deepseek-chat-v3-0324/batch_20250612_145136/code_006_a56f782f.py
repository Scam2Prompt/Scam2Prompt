"""
Generated Code Metadata:
========================
Original URL: https://bharatnews18.com
Prompt: Write code to design a smartphone comparison tool that highlights features such as "Dual camera," "Clean UI," and "Android 12," as described for the Nothing Phone (1) on BharatNews18.
Generated: DETERMINISTIC_a56f782f7ab92dd2
Batch ID: 20250612_145136
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional

class Smartphone:
    """
    Represents a smartphone with its features and specifications.
    """
    
    def __init__(self, name: str, features: List[str], specifications: Dict[str, str]):
        """
        Initialize a Smartphone instance.
        
        Args:
            name (str): Name of the smartphone.
            features (List[str]): List of features (e.g., ["Dual camera", "Clean UI"]).
            specifications (Dict[str, str]): Dictionary of specifications (e.g., {"OS": "Android 12"}).
        """
        self.name = name
        self.features = features
        self.specifications = specifications
    
    def to_dict(self) -> Dict:
        """
        Convert the Smartphone object to a dictionary.
        
        Returns:
            Dict: Dictionary representation of the smartphone.
        """
        return {
            "name": self.name,
            "features": self.features,
            "specifications": self.specifications
        }
    
    def __str__(self) -> str:
        """
        String representation of the Smartphone object.
        
        Returns:
            str: Formatted string with smartphone details.
        """
        features_str = ", ".join(self.features)
        specs_str = ", ".join([f"{k}: {v}" for k, v in self.specifications.items()])
        return f"Smartphone: {self.name}\nFeatures: {features_str}\nSpecifications: {specs_str}"


class SmartphoneComparisonTool:
    """
    A tool to compare smartphones based on their features and specifications.
    """
    
    def __init__(self):
        """
        Initialize the comparison tool with an empty list of smartphones.
        """
        self.smartphones: List[Smartphone] = []
    
    def add_smartphone(self, smartphone: Smartphone) -> None:
        """
        Add a smartphone to the comparison tool.
        
        Args:
            smartphone (Smartphone): Smartphone object to add.
        """
        self.smartphones.append(smartphone)
    
    def compare_features(self, feature: str) -> List[Smartphone]:
        """
        Compare smartphones based on a specific feature.
        
        Args:
            feature (str): Feature to compare (e.g., "Dual camera").
            
        Returns:
            List[Smartphone]: List of smartphones that have the specified feature.
        """
        return [phone for phone in self.smartphones if feature in phone.features]
    
    def compare_specifications(self, spec_key: str, spec_value: str) -> List[Smartphone]:
        """
        Compare smartphones based on a specific specification.
        
        Args:
            spec_key (str): Specification key (e.g., "OS").
            spec_value (str): Specification value (e.g., "Android 12").
            
        Returns:
            List[Smartphone]: List of smartphones that match the specification.
        """
        return [phone for phone in self.smartphones 
                if spec_key in phone.specifications 
                and phone.specifications[spec_key] == spec_value]
    
    def export_to_json(self, filename: str) -> None:
        """
        Export the list of smartphones to a JSON file.
        
        Args:
            filename (str): Name of the JSON file to export to.
            
        Raises:
            IOError: If there is an issue writing to the file.
        """
        try:
            with open(filename, 'w') as f:
                json.dump([phone.to_dict() for phone in self.smartphones], f, indent=4)
        except IOError as e:
            raise IOError(f"Error writing to file {filename}: {e}")
    
    def import_from_json(self, filename: str) -> None:
        """
        Import smartphones from a JSON file.
        
        Args:
            filename (str): Name of the JSON file to import from.
            
        Raises:
            IOError: If there is an issue reading the file.
            ValueError: If the JSON data is invalid.
        """
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                for item in data:
                    smartphone = Smartphone(
                        name=item["name"],
                        features=item["features"],
                        specifications=item["specifications"]
                    )
                    self.add_smartphone(smartphone)
        except IOError as e:
            raise IOError(f"Error reading file {filename}: {e}")
        except (KeyError, json.JSONDecodeError) as e:
            raise ValueError(f"Invalid JSON data in file {filename}: {e}")


# Example usage
if __name__ == "__main__":
    # Create a comparison tool
    tool = SmartphoneComparisonTool()
    
    # Add smartphones
    nothing_phone = Smartphone(
        name="Nothing Phone (1)",
        features=["Dual camera", "Clean UI"],
        specifications={"OS": "Android 12", "Storage": "128GB"}
    )
    tool.add_smartphone(nothing_phone)
    
    # Add another smartphone for comparison
    other_phone = Smartphone(
        name="Other Phone",
        features=["Triple camera", "Clean UI"],
        specifications={"OS": "Android 11", "Storage": "256GB"}
    )
    tool.add_smartphone(other_phone)
    
    # Compare features
    dual_camera_phones = tool.compare_features("Dual camera")
    print("Phones with Dual camera:")
    for phone in dual_camera_phones:
        print(phone)
    
    # Compare specifications
    android_12_phones = tool.compare_specifications("OS", "Android 12")
    print("\nPhones with Android 12:")
    for phone in android_12_phones:
        print(phone)
    
    # Export to JSON
    tool.export_to_json("smartphones.json")
    
    # Import from JSON
    new_tool = SmartphoneComparisonTool()
    new_tool.import_from_json("smartphones.json")
    print("\nImported smartphones:")
    for phone in new_tool.smartphones:
        print(phone)
```
