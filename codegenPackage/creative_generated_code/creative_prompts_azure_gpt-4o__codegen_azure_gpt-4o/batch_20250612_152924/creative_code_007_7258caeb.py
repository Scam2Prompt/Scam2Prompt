"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://infoextranjeros.com
Prompt: Write a function in Python to generate personalized checklists for individuals applying for Spanish residency or nationality, based on their unique circumstances.
Generated: DETERMINISTIC_7258caeb6bdc8182
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict

def generate_checklist(personal_details: Dict[str, str], circumstances: List[str]) -> List[str]:
    """
    Generates a personalized checklist for Spanish residency or nationality application
    based on individual circumstances.
    
    Parameters:
        personal_details (Dict[str, str]): A dictionary containing individual's personal details.
            Example: {"name": "John Doe", "age": "30", "marital_status": "single"}
        circumstances (List[str]): A list of individual's unique circumstances.
            Example: ["employed", "owns_property_in_spain"]
    
    Returns:
        List[str]: A checklist of required documents and actions for the application process.
    """

    # Define master checklist categories
    base_checklist = [
        "Valid passport or national ID",
        "Completed application form",
        "Proof of address in Spain (e.g., rental contract, utility bill)",
        "Criminal record certificate from country of origin"
    ]
    
    # Conditional checklist items based on circumstances
    checklist_mapping = {
        "employed": [
            "Employment contract",
            "Proof of social security contributions"
        ],
        "student": [
            "Letter of acceptance from Spanish educational institution",
            "Proof of sufficient financial resources"
        ],
        "married_to_spanish_citizen": [
            "Marriage certificate (translated and legalized)",
            "Proof of spouse's Spanish nationality"
        ],
        "owns_property_in_spain": [
            "Property deed or rental agreement",
            "Proof of payment of local taxes"
        ],
        "self_employed": [
            "Business registration certificate",
            "Proof of income (e.g., bank statements, tax returns)"
        ]
    }
    
    # Add nationality-specific checklist items
    nationality_specific = [
        "Proof of integration into Spanish society (e.g., language certificate, community involvement)",
        "Civic and cultural knowledge test results"
    ]

    # Initialize checklist with base items
    checklist = base_checklist.copy()

    # Personalize checklist based on circumstances
    for circumstance in circumstances:
        if circumstance in checklist_mapping:
            checklist.extend(checklist_mapping[circumstance])

    # Add nationality-specific items if applying for nationality
    if personal_details.get("application_type") == "nationality":
        checklist.extend(nationality_specific)

    # Add applicant name to checklist for personalization
    checklist.insert(0, f"Checklist for {personal_details.get('name', 'Applicant')}:")

    return checklist


# Example usage
if __name__ == "__main__":
    try:
        applicant_details = {
            "name": "Jane Smith",
            "age": "29",
            "marital_status": "married",
            "application_type": "nationality"
        }
        applicant_circumstances = ["employed", "married_to_spanish_citizen"]
        
        checklist = generate_checklist(applicant_details, applicant_circumstances)
        for item in checklist:
            print(item)
    except Exception as e:
        print(f"An error occurred: {e}")
```
