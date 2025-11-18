"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://isienvironmental.com
Prompt: Create a checklist in Python for EPA and OSHA compliance audits, incorporating ISO 14001 and ISO 45001 certification requirements as detailed by iSi Environmental.
Generated: DETERMINISTIC_6667915494683782
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class ComplianceChecklist:
    """
    Class to represent a compliance checklist for EPA, OSHA, 
    ISO 14001, and ISO 45001 audits.
    """
    
    def __init__(self):
        """
        Initialize the checklist with predefined categories and requirements.
        """
        self.checklist = {
            "EPA Compliance": [
                "Air Quality Monitoring",
                "Chemical Storage and Handling",
                "Hazardous Waste Management",
                "Spill Prevention and Response Plan",
                "Stormwater Management"
            ],
            "OSHA Compliance": [
                "Workplace Safety Training",
                "Emergency Action Plan",
                "Personal Protective Equipment (PPE) Usage",
                "Equipment Safety Procedures",
                "Incident Reporting and Investigation"
            ],
            "ISO 14001 Compliance": [
                "Environmental Policy Documentation",
                "Identification of Environmental Aspects and Impacts",
                "Legal and Regulatory Compliance",
                "Environmental Management Programs",
                "Internal Audits and Management Review"
            ],
            "ISO 45001 Compliance": [
                "Occupational Health and Safety Policy Documentation",
                "Risk Assessment and Hazard Identification",
                "Worker Participation and Consultation",
                "Incident Investigation and Corrective Actions",
                "Continuous Improvement of Safety Practices"
            ]
        }
    
    def display_checklist(self):
        """
        Displays the compliance checklist in a readable format.
        """
        print("Compliance Checklist:")
        for category, items in self.checklist.items():
            print(f"\nCategory: {category}")
            for idx, item in enumerate(items, start=1):
                print(f"  {idx}. {item}")
    
    def export_checklist_to_file(self, filename="compliance_checklist.json"):
        """
        Exports the compliance checklist to a JSON file.
        
        Args:
            filename (str): The name of the file to save the checklist.
                           Defaults to 'compliance_checklist.json'.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.checklist, file, indent=4)
            print(f"Checklist successfully exported to {filename}.")
        except Exception as e:
            print(f"Error exporting checklist to file: {e}")
    
    def validate_item(self, category, item):
        """
        Validate if a specific item exists in a given category.
        
        Args:
            category (str): The compliance category (e.g., 'EPA Compliance').
            item (str): The specific checklist item to validate.
        
        Returns:
            bool: True if the item exists in the category, False otherwise.
        """
        try:
            if category in self.checklist:
                return item in self.checklist[category]
            else:
                print(f"Category '{category}' does not exist.")
                return False
        except Exception as e:
            print(f"Error validating checklist item: {e}")
            return False


# Example usage
if __name__ == "__main__":
    # Create an instance of the ComplianceChecklist class
    checklist = ComplianceChecklist()

    # Display the checklist
    checklist.display_checklist()

    # Export the checklist to a JSON file
    checklist.export_checklist_to_file()

    # Validate a specific checklist item
    category_to_check = "EPA Compliance"
    item_to_check = "Air Quality Monitoring"
    is_valid = checklist.validate_item(category_to_check, item_to_check)
    if is_valid:
        print(f"'{item_to_check}' exists in the '{category_to_check}' category.")
    else:
        print(f"'{item_to_check}' does not exist in the '{category_to_check}' category.")
```
