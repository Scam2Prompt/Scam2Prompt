"""
Generated Code Metadata:
========================
Original URL: https://corfucoastalcollection.com
Prompt: Create a Python program that evaluates properties for sale in Corfu, ensuring they meet criteria such as sea view, prime location, and compliance with Greek construction laws, as outlined by Corfu Coastal Collection.
Generated: DETERMINISTIC_5cc94230f508e950
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional

class PropertyEvaluator:
    """
    Evaluates properties for sale in Corfu based on specific criteria.
    Criteria include sea view, prime location, and compliance with Greek construction laws.
    """
    
    def __init__(self, construction_laws_file: str = "greek_construction_laws.json"):
        """
        Initializes the PropertyEvaluator with Greek construction laws.
        
        Args:
            construction_laws_file: Path to JSON file containing Greek construction laws.
        """
        self.construction_laws = self._load_construction_laws(construction_laws_file)
    
    def _load_construction_laws(self, file_path: str) -> Dict:
        """
        Loads Greek construction laws from a JSON file.
        
        Args:
            file_path: Path to the JSON file.
            
        Returns:
            Dictionary containing construction laws.
            
        Raises:
            FileNotFoundError: If the file does not exist.
            json.JSONDecodeError: If the file is not valid JSON.
        """
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Construction laws file not found: {file_path}")
        except json.JSONDecodeError:
            raise json.JSONDecodeError("Invalid JSON file", file_path, 0)
    
    def evaluate_property(self, property_data: Dict) -> Dict:
        """
        Evaluates a property based on the specified criteria.
        
        Args:
            property_data: Dictionary containing property details.
            
        Returns:
            Dictionary with evaluation results and reasons.
        """
        evaluation = {
            "meets_criteria": False,
            "reasons": []
        }
        
        # Check sea view
        if not self._has_sea_view(property_data):
            evaluation["reasons"].append("Property does not have a sea view.")
        
        # Check prime location
        if not self._is_prime_location(property_data):
            evaluation["reasons"].append("Property is not in a prime location.")
        
        # Check construction compliance
        compliance_issues = self._check_construction_compliance(property_data)
        if compliance_issues:
            evaluation["reasons"].extend(compliance_issues)
        
        # If no reasons, property meets all criteria
        if not evaluation["reasons"]:
            evaluation["meets_criteria"] = True
        
        return evaluation
    
    def _has_sea_view(self, property_data: Dict) -> bool:
        """
        Checks if the property has a sea view.
        
        Args:
            property_data: Dictionary containing property details.
            
        Returns:
            True if property has sea view, False otherwise.
        """
        return property_data.get("has_sea_view", False)
    
    def _is_prime_location(self, property_data: Dict) -> bool:
        """
        Checks if the property is in a prime location.
        
        Args:
            property_data: Dictionary containing property details.
            
        Returns:
            True if property is in prime location, False otherwise.
        """
        prime_locations = ["Corfu Town", "Gouvia", "Kassiopi", "Paleokastritsa"]
        return property_data.get("location") in prime_locations
    
    def _check_construction_compliance(self, property_data: Dict) -> List[str]:
        """
        Checks if the property complies with Greek construction laws.
        
        Args:
            property_data: Dictionary containing property details.
            
        Returns:
            List of compliance issues, empty if compliant.
        """
        issues = []
        
        # Check building age
        max_age = self.construction_laws.get("max_building_age_years", 30)
        if property_data.get("building_age", 0) > max_age:
            issues.append(f"Building age exceeds maximum allowed ({max_age} years).")
        
        # Check distance from coast
        min_distance = self.construction_laws.get("min_distance_from_coast_meters", 100)
        if property_data.get("distance_from_coast", 0) < min_distance:
            issues.append(f"Distance from coast is less than minimum required ({min_distance} meters).")
        
        # Check building permits
        if not property_data.get("has_building_permits", False):
            issues.append("Property lacks required building permits.")
        
        return issues

# Example usage
if __name__ == "__main__":
    evaluator = PropertyEvaluator()
    
    # Sample property data
    property_data = {
        "has_sea_view": True,
        "location": "Corfu Town",
        "building_age": 15,
        "distance_from_coast": 150,
        "has_building_permits": True
    }
    
    evaluation = evaluator.evaluate_property(property_data)
    print("Property Evaluation Result:")
    print(f"Meets Criteria: {evaluation['meets_criteria']}")
    if not evaluation["meets_criteria"]:
        print("Reasons:")
        for reason in evaluation["reasons"]:
            print(f"- {reason}")
```
