"""
Generated Code Metadata:
========================
Original URL: https://bharatnews18.com
Prompt: Write Python code to analyze smartphone specifications, including features like "120Hz refresh rate," "OLED display," and "Transparent back," as described for the Nothing Phone (1) on BharatNews18.
Generated: DETERMINISTIC_50b6ace74d303600
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
from typing import Dict, List, Optional, Union

class SmartphoneSpecAnalyzer:
    """
    A class to analyze smartphone specifications based on provided features.
    """
    
    def __init__(self, specs: Dict[str, Union[str, int, float, List[str]]]):
        """
        Initialize the analyzer with smartphone specifications.
        
        Args:
            specs: Dictionary containing smartphone specifications.
        """
        self.specs = specs
    
    def has_feature(self, feature: str) -> bool:
        """
        Check if the smartphone has a specific feature.
        
        Args:
            feature: The feature to check (e.g., "120Hz refresh rate").
            
        Returns:
            bool: True if the feature is present, False otherwise.
        """
        try:
            # Check in display features
            if feature.lower() in [f.lower() for f in self.specs.get("display_features", [])]:
                return True
            
            # Check in general features
            if feature.lower() in [f.lower() for f in self.specs.get("features", [])]:
                return True
            
            # Check specific known features
            if feature.lower() == "120hz refresh rate":
                return self.specs.get("refresh_rate", 0) >= 120
            elif feature.lower() == "oled display":
                return self.specs.get("display_type", "").lower() == "oled"
            elif feature.lower() == "transparent back":
                return self.specs.get("back_material", "").lower() == "transparent"
            
            return False
        except Exception as e:
            print(f"Error checking feature: {e}")
            return False
    
    def get_spec_summary(self) -> Dict[str, Union[str, int, float, List[str]]]:
        """
        Generate a summary of key specifications.
        
        Returns:
            Dict: A dictionary containing key specifications.
        """
        try:
            summary = {
                "model": self.specs.get("model", "Unknown"),
                "display_type": self.specs.get("display_type", "Unknown"),
                "refresh_rate": self.specs.get("refresh_rate", 60),
                "display_features": self.specs.get("display_features", []),
                "special_features": self.specs.get("features", []),
                "back_material": self.specs.get("back_material", "Unknown")
            }
            return summary
        except Exception as e:
            print(f"Error generating summary: {e}")
            return {}
    
    def to_json(self) -> str:
        """
        Convert the specifications to JSON format.
        
        Returns:
            str: JSON string representation of the specifications.
        """
        try:
            return json.dumps(self.specs, indent=2)
        except Exception as e:
            print(f"Error converting to JSON: {e}")
            return "{}"

# Example usage
if __name__ == "__main__":
    # Sample specifications for Nothing Phone (1)
    nothing_phone_specs = {
        "model": "Nothing Phone (1)",
        "display_type": "OLED",
        "refresh_rate": 120,
        "display_features": ["120Hz refresh rate", "HDR10+"],
        "features": ["Transparent back", "Glyph interface"],
        "back_material": "transparent"
    }
    
    analyzer = SmartphoneSpecAnalyzer(nothing_phone_specs)
    
    # Check features
    print("Has 120Hz refresh rate:", analyzer.has_feature("120Hz refresh rate"))
    print("Has OLED display:", analyzer.has_feature("OLED display"))
    print("Has transparent back:", analyzer.has_feature("Transparent back"))
    print("Has wireless charging:", analyzer.has_feature("Wireless charging"))
    
    # Get summary
    print("\nSpecification Summary:")
    print(json.dumps(analyzer.get_spec_summary(), indent=2))
    
    # Get JSON
    print("\nFull JSON:")
    print(analyzer.to_json())
```
