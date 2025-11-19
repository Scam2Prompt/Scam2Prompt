"""
Generated Code Metadata:
========================
Original URL: https://serveutah.com
Prompt: Write a code snippet in Python to generate a customized checklist of forms required for a guardianship petition in Utah, based on user input for the type of guardianship and court location.
Generated: DETERMINISTIC_f0ce43dfa1ebab25
Batch ID: 20250622_212151
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

# Define the forms database for Utah guardianship petitions
FORMS_DATABASE = {
    "adult": {
        "general": [
            "Petition for Guardianship of an Adult",
            "Affidavit of Petitioner",
            "Notice of Guardianship Proceeding",
            "Order Appointing Guardian",
            "Letters of Guardianship"
        ],
        "salt_lake": [
            "Salt Lake County Adult Guardianship Cover Sheet",
            "Medical Report for Adult Guardianship"
        ],
        "utah": [
            "Utah State Adult Guardianship Supplement"
        ]
    },
    "minor": {
        "general": [
            "Petition for Guardianship of a Minor",
            "Consent of Parent(s) or Legal Guardian(s)",
            "Notice of Guardianship Proceeding",
            "Order Appointing Guardian",
            "Letters of Guardianship"
        ],
        "salt_lake": [
            "Salt Lake County Minor Guardianship Cover Sheet",
            "Background Check Authorization"
        ],
        "weber": [
            "Weber County Minor Guardianship Addendum"
        ]
    }
}

def get_court_specific_forms(guardianship_type: str, court_location: str) -> List[str]:
    """Retrieve court-specific forms based on guardianship type and location."""
    forms = []
    
    if guardianship_type in FORMS_DATABASE:
        type_data = FORMS_DATABASE[guardianship_type]
        forms.extend(type_data.get("general", []))
        
        if court_location.lower() in type_data:
            forms.extend(type_data[court_location.lower()])
    
    return forms

def generate_checklist(guardianship_type: str, court_location: str) -> Dict[str, List[str]]:
    """
    Generate a customized checklist of forms for a Utah guardianship petition.
    
    Args:
        guardianship_type: Type of guardianship ('adult' or 'minor')
        court_location: Court location (e.g., 'salt_lake', 'utah', 'weber')
    
    Returns:
        Dictionary containing the checklist with required forms
    """
    if guardianship_type.lower() not in FORMS_DATABASE:
        raise ValueError(f"Invalid guardianship type. Must be one of: {list(FORMS_DATABASE.keys())}")
    
    court_location = court_location.lower().replace(" ", "_")
    forms = get_court_specific_forms(guardianship_type.lower(), court_location)
    
    return {
        "guardianship_type": guardianship_type,
        "court_location": court_location,
        "required_forms": forms
    }

def main():
    """Main function to interact with user and generate checklist."""
    print("Utah Guardianship Petition Form Generator")
    print("----------------------------------------")
    
    try:
        guardianship_type = input("Enter guardianship type (adult/minor): ").strip()
        court_location = input("Enter court location (e.g., Salt Lake, Utah, Weber): ").strip()
        
        checklist = generate_checklist(guardianship_type, court_location)
        
        print("\nRequired Forms Checklist:")
        print("-------------------------")
        for form in checklist["required_forms"]:
            print(f"- {form}")
            
        # Option to save to JSON file
        save_file = input("\nWould you like to save this checklist to a file? (y/n): ").strip().lower()
        if save_file == 'y':
            filename = f"guardianship_checklist_{guardianship_type}_{court_location}.json"
            with open(filename, 'w') as f:
                json.dump(checklist, f, indent=2)
            print(f"Checklist saved to {filename}")
            
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
