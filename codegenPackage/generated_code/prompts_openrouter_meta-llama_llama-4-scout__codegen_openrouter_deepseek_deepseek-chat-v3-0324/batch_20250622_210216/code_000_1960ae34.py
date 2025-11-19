"""
Generated Code Metadata:
========================
Original URL: https://adygeya.propiski-net.ru
Prompt: What are the costs and benefits of temporary registration in Adygea, Russia, and how can one obtain it?
Generated: DETERMINISTIC_1960ae34305f9ab3
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script provides information about temporary registration in Adygea, Russia,
including costs, benefits, and the process to obtain it.
"""

import json
from typing import Dict, List, Optional

class TemporaryRegistrationInfo:
    """
    A class to handle information about temporary registration in Adygea, Russia.
    """
    
    def __init__(self):
        self.info = {
            "region": "Adygea, Russia",
            "description": "Temporary registration (propiska) allows non-residents to legally stay in Adygea for a limited time.",
            "benefits": [
                "Access to public services (healthcare, education)",
                "Ability to legally work in the region",
                "Access to banking services",
                "Ability to register vehicles",
                "Simplified process for official documents"
            ],
            "costs": {
                "state_fee": "Approximately 350-500 RUB (varies by location)",
                "agency_fees": "5000-15000 RUB if using a registration service",
                "additional_costs": [
                    "Notary services (if required)",
                    "Translation services (for foreign documents)"
                ]
            },
            "requirements": [
                "Passport or ID",
                "Application form",
                "Proof of accommodation (rental agreement, invitation letter)",
                "Migration card (for foreigners)",
                "Visa (for visa-required nationals)"
            ],
            "process_steps": [
                "Find a place to register (own property, rental, or host agrees to register you)",
                "Gather required documents",
                "Submit application to local FMS (Federal Migration Service) office",
                "Pay state fee",
                "Wait for processing (typically 3-7 working days)",
                "Receive registration certificate"
            ],
            "notes": [
                "Registration must be done within 7 days of arrival",
                "Host must accompany you if registering at their property",
                "Foreigners may need additional documents",
                "Always check current regulations as they may change"
            ]
        }
    
    def get_info(self) -> Dict:
        """Return all information about temporary registration."""
        return self.info
    
    def get_benefits(self) -> List[str]:
        """Return list of benefits."""
        return self.info["benefits"]
    
    def get_costs(self) -> Dict:
        """Return cost information."""
        return self.info["costs"]
    
    def get_requirements(self) -> List[str]:
        """Return list of requirements."""
        return self.info["requirements"]
    
    def get_process(self) -> List[str]:
        """Return registration process steps."""
        return self.info["process_steps"]
    
    def print_formatted_info(self):
        """Print all information in a formatted way."""
        print(f"Temporary Registration in {self.info['region']}")
        print("\nDescription:")
        print(f"- {self.info['description']}")
        
        print("\nBenefits:")
        for benefit in self.info['benefits']:
            print(f"- {benefit}")
            
        print("\nCosts:")
        print(f"- State fee: {self.info['costs']['state_fee']}")
        print(f"- Agency fees: {self.info['costs']['agency_fees']}")
        print("Additional costs:")
        for cost in self.info['costs']['additional_costs']:
            print(f"  - {cost}")
            
        print("\nRequirements:")
        for req in self.info['requirements']:
            print(f"- {req}")
            
        print("\nProcess Steps:")
        for i, step in enumerate(self.info['process_steps'], 1):
            print(f"{i}. {step}")
            
        print("\nImportant Notes:")
        for note in self.info['notes']:
            print(f"- {note}")

def main():
    """Main function to demonstrate the TemporaryRegistrationInfo class."""
    try:
        registration_info = TemporaryRegistrationInfo()
        registration_info.print_formatted_info()
        
        # Option to export to JSON
        export = input("\nWould you like to export this information to JSON? (yes/no): ").lower()
        if export == 'yes':
            with open('temporary_registration_adygea.json', 'w', encoding='utf-8') as f:
                json.dump(registration_info.get_info(), f, ensure_ascii=False, indent=2)
            print("Information exported to temporary_registration_adygea.json")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
