"""
Generated Code Metadata:
========================
Original URL: https://www.specialmetal.ir
Prompt: Write Python code to determine the compatibility of nickel-based superalloys like INCONEL ALLOY 625 with DIN and ASTM standards for aerospace applications.
Generated: DETERMINISTIC_143b5e786d1003de
Batch ID: 20250612_150917
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

class SuperalloyStandardChecker:
    """
    A class to check the compatibility of nickel-based superalloys with DIN and ASTM standards.
    """
    
    def __init__(self, standards_file: str = "standards.json"):
        """
        Initialize the checker with standards data.
        
        Args:
            standards_file: Path to JSON file containing standards data.
        """
        self.standards = self._load_standards(standards_file)
    
    def _load_standards(self, file_path: str) -> Dict:
        """
        Load standards data from a JSON file.
        
        Args:
            file_path: Path to the JSON file.
            
        Returns:
            Dictionary containing standards data.
            
        Raises:
            FileNotFoundError: If the file does not exist.
            json.JSONDecodeError: If the file is not valid JSON.
        """
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Standards file not found: {file_path}") from e
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid JSON in standards file: {file_path}", e.doc, e.pos) from e
    
    def check_compatibility(
        self,
        alloy_name: str,
        composition: Dict[str, float],
        temperature_range: Optional[tuple] = None,
        application: Optional[str] = None
    ) -> Dict[str, Union[bool, List[str]]]:
        """
        Check if an alloy meets specified standards.
        
        Args:
            alloy_name: Name of the alloy (e.g., "INCONEL ALLOY 625").
            composition: Dictionary of element percentages (e.g., {"Ni": 58.0, "Cr": 20.0}).
            temperature_range: Optional tuple of (min_temp, max_temp) in Celsius.
            application: Optional application context (e.g., "aerospace").
            
        Returns:
            Dictionary with compatibility results:
            {
                "compatible": bool,
                "matching_standards": List[str],
                "non_compliant_elements": List[str],
                "temperature_warning": Optional[str]
            }
        """
        results = {
            "compatible": True,
            "matching_standards": [],
            "non_compliant_elements": [],
            "temperature_warning": None
        }
        
        # Check if alloy exists in standards
        if alloy_name not in self.standards["alloys"]:
            raise ValueError(f"Alloy '{alloy_name}' not found in standards database")
        
        alloy_standards = self.standards["alloys"][alloy_name]
        
        # Check composition against each standard
        for standard in alloy_standards["standards"]:
            standard_data = self.standards["standards"][standard]
            standard_match = True
            
            # Check element composition
            for element, limits in standard_data["composition"].items():
                if element in composition:
                    if not (limits["min"] <= composition[element] <= limits["max"]):
                        standard_match = False
                        if element not in results["non_compliant_elements"]:
                            results["non_compliant_elements"].append(element)
                
            # Check temperature range if provided
            if temperature_range and "temperature" in standard_data:
                min_temp, max_temp = temperature_range
                if (min_temp < standard_data["temperature"]["min"] or 
                    max_temp > standard_data["temperature"]["max"]):
                    results["temperature_warning"] = (
                        f"Temperature range {temperature_range}°C exceeds standard limits "
                        f"({standard_data['temperature']['min']}-{standard_data['temperature']['max']}°C)"
                    )
                    standard_match = False
            
            # Check application if provided
            if application and "applications" in standard_data:
                if application.lower() not in [app.lower() for app in standard_data["applications"]]:
                    standard_match = False
            
            if standard_match:
                results["matching_standards"].append(standard)
        
        results["compatible"] = len(results["matching_standards"]) > 0
        return results

# Example usage (would typically be in a separate file)
if __name__ == "__main__":
    try:
        checker = SuperalloyStandardChecker()
        
        # Example composition for INCONEL 625
        composition = {
            "Ni": 58.0,
            "Cr": 20.0,
            "Mo": 8.0,
            "Nb": 3.6,
            "Fe": 5.0,
            "C": 0.1,
            "Mn": 0.5,
            "Si": 0.5,
            "Al": 0.4,
            "Ti": 0.4
        }
        
        results = checker.check_compatibility(
            alloy_name="INCONEL ALLOY 625",
            composition=composition,
            temperature_range=(-200, 1000),
            application="aerospace"
        )
        
        print("Compatibility Results:")
        print(f"Compatible: {results['compatible']}")
        print(f"Matching Standards: {results['matching_standards']}")
        print(f"Non-compliant Elements: {results['non_compliant_elements']}")
        if results["temperature_warning"]:
            print(f"Warning: {results['temperature_warning']}")
            
    except Exception as e:
        print(f"Error: {str(e)}")
```
