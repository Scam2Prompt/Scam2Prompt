"""
Generated Code Metadata:
========================
Original URL: https://kataskeui.gr
Prompt: Generate a script to automate the process of drafting an electronic building identity (ΗΤΚ) for a construction project, ensuring compliance with Greek regulations.
Generated: DETERMINISTIC_1640bebe7aea20d7
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import datetime
import uuid
from typing import Dict, List, Optional

class HTKGenerator:
    """
    A class to generate an electronic building identity (ΗΤΚ) document compliant with Greek regulations.
    """
    
    def __init__(self):
        self.htk_template = {
            "version": "1.0",
            "metadata": {
                "generated_at": None,
                "document_id": None,
                "authority": "Greek Ministry of Environment and Energy"
            },
            "project": {
                "project_id": None,
                "project_name": None,
                "location": None,
                "municipality": None,
                "postal_code": None,
                "coordinates": None
            },
            "building": {
                "category": None,
                "use": None,
                "floors": None,
                "total_area": None,
                "construction_year": None,
                "energy_class": None
            },
            "owner": {
                "name": None,
                "id_number": None,
                "contact": {
                    "phone": None,
                    "email": None
                }
            },
            "constructor": {
                "name": None,
                "license_number": None,
                "contact": {
                    "phone": None,
                    "email": None
                }
            },
            "engineer": {
                "name": None,
                "license_number": None,
                "contact": {
                    "phone": None,
                    "email": None
                }
            },
            "compliance": {
                "building_regulations": True,
                "energy_efficiency": True,
                "seismic_provisions": True,
                "fire_safety": True,
                "accessibility": True,
                "notes": None
            },
            "attachments": []
        }
    
    def generate_document_id(self) -> str:
        """Generate a unique document ID."""
        return f"HTK-{uuid.uuid4().hex[:8].upper()}"
    
    def validate_input(self, data: Dict) -> bool:
        """Validate required fields in input data."""
        required_fields = [
            "project_name", "location", "municipality", "postal_code",
            "building_category", "building_use", "floors", "total_area",
            "owner_name", "owner_id_number"
        ]
        
        for field in required_fields:
            if field not in data or not data[field]:
                raise ValueError(f"Missing required field: {field}")
        
        if not isinstance(data["floors"], int) or data["floors"] <= 0:
            raise ValueError("Floors must be a positive integer")
            
        if not isinstance(data["total_area"], (int, float)) or data["total_area"] <= 0:
            raise ValueError("Total area must be a positive number")
            
        return True
    
    def generate_htk(self, input_data: Dict) -> Dict:
        """
        Generate HTK document from input data.
        
        Args:
            input_data: Dictionary containing all required project information
            
        Returns:
            Dictionary representing the complete HTK document
        """
        try:
            self.validate_input(input_data)
            
            # Generate document metadata
            self.htk_template["metadata"]["generated_at"] = datetime.datetime.now().isoformat()
            self.htk_template["metadata"]["document_id"] = self.generate_document_id()
            
            # Project information
            self.htk_template["project"]["project_id"] = input_data.get("project_id", "")
            self.htk_template["project"]["project_name"] = input_data["project_name"]
            self.htk_template["project"]["location"] = input_data["location"]
            self.htk_template["project"]["municipality"] = input_data["municipality"]
            self.htk_template["project"]["postal_code"] = input_data["postal_code"]
            self.htk_template["project"]["coordinates"] = input_data.get("coordinates")
            
            # Building information
            self.htk_template["building"]["category"] = input_data["building_category"]
            self.htk_template["building"]["use"] = input_data["building_use"]
            self.htk_template["building"]["floors"] = input_data["floors"]
            self.htk_template["building"]["total_area"] = input_data["total_area"]
            self.htk_template["building"]["construction_year"] = input_data.get("construction_year")
            self.htk_template["building"]["energy_class"] = input_data.get("energy_class")
            
            # Owner information
            self.htk_template["owner"]["name"] = input_data["owner_name"]
            self.htk_template["owner"]["id_number"] = input_data["owner_id_number"]
            self.htk_template["owner"]["contact"]["phone"] = input_data.get("owner_phone")
            self.htk_template["owner"]["contact"]["email"] = input_data.get("owner_email")
            
            # Constructor information (optional)
            if "constructor_name" in input_data:
                self.htk_template["constructor"]["name"] = input_data["constructor_name"]
                self.htk_template["constructor"]["license_number"] = input_data.get("constructor_license")
                self.htk_template["constructor"]["contact"]["phone"] = input_data.get("constructor_phone")
                self.htk_template["constructor"]["contact"]["email"] = input_data.get("constructor_email")
            
            # Engineer information (optional)
            if "engineer_name" in input_data:
                self.htk_template["engineer"]["name"] = input_data["engineer_name"]
                self.htk_template["engineer"]["license_number"] = input_data.get("engineer_license")
                self.htk_template["engineer"]["contact"]["phone"] = input_data.get("engineer_phone")
                self.htk_template["engineer"]["contact"]["email"] = input_data.get("engineer_email")
            
            # Compliance information
            self.htk_template["compliance"]["building_regulations"] = input_data.get("building_regulations", True)
            self.htk_template["compliance"]["energy_efficiency"] = input_data.get("energy_efficiency", True)
            self.htk_template["compliance"]["seismic_provisions"] = input_data.get("seismic_provisions", True)
            self.htk_template["compliance"]["fire_safety"] = input_data.get("fire_safety", True)
            self.htk_template["compliance"]["accessibility"] = input_data.get("accessibility", True)
            self.htk_template["compliance"]["notes"] = input_data.get("compliance_notes")
            
            # Attachments (optional)
            if "attachments" in input_data and isinstance(input_data["attachments"], list):
                self.htk_template["attachments"] = input_data["attachments"]
            
            return self.htk_template
            
        except Exception as e:
            raise Exception(f"Failed to generate HTK document: {str(e)}")
    
    def save_to_file(self, htk_data: Dict, filename: str) -> None:
        """
        Save HTK document to a JSON file.
        
        Args:
            htk_data: Complete HTK document data
            filename: Output filename
        """
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(htk_data, f, ensure_ascii=False, indent=4)
        except IOError as e:
            raise Exception(f"Failed to save HTK document: {str(e)}")


# Example usage
if __name__ == "__main__":
    try:
        # Sample input data
        project_data = {
            "project_name": "Residential Building - Athens",
            "location": "Athens, Greece",
            "municipality": "Athens",
            "postal_code": "10431",
            "coordinates": "37.9838, 23.7275",
            "building_category": "Residential",
            "building_use": "Apartment Building",
            "floors": 5,
            "total_area": 1200.5,
            "construction_year": 2023,
            "energy_class": "A",
            "owner_name": "John Doe",
            "owner_id_number": "AB123456",
            "owner_phone": "+30 2101234567",
            "owner_email": "owner@example.com",
            "engineer_name": "Maria Papadopoulos",
            "engineer_license": "ENG12345",
            "engineer_phone": "+30 2107654321",
            "engineer_email": "engineer@example.com",
            "compliance_notes": "All regulations have been followed",
            "attachments": [
                {"type": "blueprint", "filename": "blueprint.pdf"},
                {"type": "permit", "filename": "permit.pdf"}
            ]
        }
        
        generator = HTKGenerator()
        htk_document = generator.generate_htk(project_data)
        generator.save_to_file(htk_document, "building_htk.json")
        
        print("HTK document generated successfully!")
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
