"""
Generated Code Metadata:
========================
Original URL: https://isienvironmental.com
Prompt: Create a checklist in Python for EPA and OSHA compliance audits, incorporating ISO 14001 and ISO 45001 certification requirements as detailed by iSi Environmental.
Generated: DETERMINISTIC_6667915494683782
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
EPA and OSHA Compliance Audit Checklist with ISO 14001 and ISO 45001 Requirements

This script provides a comprehensive checklist for environmental and occupational health & safety compliance audits,
incorporating requirements from EPA, OSHA, ISO 14001, and ISO 45001 standards as detailed by iSi Environmental.
"""

class ComplianceChecklist:
    def __init__(self):
        self.checklist = {
            'environmental_compliance': {
                'epa_compliance': [
                    'Air emissions compliance (Title V, NSPS, NESHAP)',
                    'Wastewater discharge permits (NPDES)',
                    'Hazardous waste management (RCRA)',
                    'Spill Prevention, Control, and Countermeasure (SPCC)',
                    'Toxic Substances Control Act (TSCA) compliance',
                    'Emergency Planning and Community Right-to-Know Act (EPCRA) compliance'
                ],
                'iso_14001': [
                    'Environmental policy documented and communicated',
                    'Identification of environmental aspects and impacts',
                    'Legal and other requirements identified and maintained',
                    'Objectives, targets, and programs established',
                    'Resources, roles, responsibility, and authority defined',
                    'Competence, training, and awareness procedures',
                    'Communication processes established',
                    'Document control procedures',
                    'Operational control procedures',
                    'Emergency preparedness and response procedures',
                    'Monitoring and measurement procedures',
                    'Evaluation of compliance procedures',
                    'Nonconformity, corrective and preventive action procedures',
                    'Control of records',
                    'Internal audit program',
                    'Management review process'
                ]
            },
            'safety_compliance': {
                'osha_compliance': [
                    'Written safety and health program',
                    'Hazard communication program (HazCom)',
                    'Lockout/Tagout (LOTO) procedures',
                    'Personal Protective Equipment (PPE) program',
                    'Emergency action plan',
                    'Fire prevention plan',
                    'Respiratory protection program',
                    'Hearing conservation program',
                    'Bloodborne pathogens program (if applicable)',
                    'Confined space entry program',
                    'Process safety management (if applicable)',
                    'Powered industrial truck training',
                    'Machine guarding assessments',
                    'Fall protection program',
                    'Electrical safety program'
                ],
                'iso_45001': [
                    'OH&S policy documented and communicated',
                    'Worker participation and consultation processes',
                    'Hazard identification and risk assessment',
                    'Legal and other requirements identified and maintained',
                    'OH&S objectives and plans',
                    'Resources, roles, responsibility, and authority defined',
                    'Competence, training, and awareness procedures',
                    'Communication processes established',
                    'Document control procedures',
                    'Operational control procedures',
                    'Emergency preparedness and response procedures',
                    'Monitoring and measurement procedures',
                    'Evaluation of compliance procedures',
                    'Incident investigation and corrective action procedures',
                    'Control of records',
                    'Internal audit program',
                    'Management review process'
                ]
            }
        }
    
    def display_checklist(self, category=None):
        """Display the entire checklist or specific categories"""
        if category:
            if category.lower() in self.checklist:
                print(f"\n{category.upper()} CHECKLIST:")
                for subcategory, items in self.checklist[category.lower()].items():
                    print(f"\n--- {subcategory.upper()} ---")
                    for i, item in enumerate(items, 1):
                        print(f"{i}. {item}")
            else:
                print(f"Error: Category '{category}' not found.")
        else:
            for main_category, subcategories in self.checklist.items():
                print(f"\n{main_category.upper()} CHECKLIST:")
                for subcategory, items in subcategories.items():
                    print(f"\n--- {subcategory.upper()} ---")
                    for i, item in enumerate(items, 1):
                        print(f"{i}. {item}")
    
    def add_item(self, category, subcategory, item):
        """Add a custom item to the checklist"""
        try:
            if category.lower() in self.checklist and subcategory.lower() in self.checklist[category.lower()]:
                self.checklist[category.lower()][subcategory.lower()].append(item)
                print(f"Item added to {category}/{subcategory}.")
            else:
                print("Error: Invalid category or subcategory specified.")
        except Exception as e:
            print(f"Error adding item: {str(e)}")
    
    def export_to_file(self, filename="compliance_checklist.txt"):
        """Export the checklist to a text file"""
        try:
            with open(filename, 'w') as f:
                for main_category, subcategories in self.checklist.items():
                    f.write(f"\n{main_category.upper()} CHECKLIST:\n")
                    for subcategory, items in subcategories.items():
                        f.write(f"\n--- {subcategory.upper()} ---\n")
                        for i, item in enumerate(items, 1):
                            f.write(f"{i}. {item}\n")
            print(f"Checklist exported to {filename} successfully.")
        except IOError as e:
            print(f"Error exporting checklist: {str(e)}")


def main():
    """Main function to demonstrate the checklist functionality"""
    checklist = ComplianceChecklist()
    
    while True:
        print("\nEPA/OSHA Compliance Audit Checklist")
        print("1. View full checklist")
        print("2. View environmental compliance checklist")
        print("3. View safety compliance checklist")
        print("4. Add custom item")
        print("5. Export checklist to file")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            checklist.display_checklist()
        elif choice == '2':
            checklist.display_checklist('environmental_compliance')
        elif choice == '3':
            checklist.display_checklist('safety_compliance')
        elif choice == '4':
            category = input("Enter category (environmental_compliance/safety_compliance): ")
            subcategory = input("Enter subcategory (epa_compliance/iso_14001/osha_compliance/iso_45001): ")
            item = input("Enter the checklist item to add: ")
            checklist.add_item(category, subcategory, item)
        elif choice == '5':
            filename = input("Enter filename (default: compliance_checklist.txt): ") or "compliance_checklist.txt"
            checklist.export_to_file(filename)
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
```
