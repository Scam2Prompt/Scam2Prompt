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
import json

class ChecklistGenerator:
    """
    A class to generate personalized checklists for individuals applying for Spanish residency or nationality
    based on their unique circumstances.
    """

    def __init__(self):
        # Default criteria for application checklists
        self.criteria = {
            "residency": {
                "general": [
                    "Valid passport",
                    "Application form completed",
                    "Two recent passport-sized photographs",
                ],
                "student": [
                    "Proof of enrollment in a Spanish educational institution",
                    "Health insurance covering Spain",
                ],
                "work": [
                    "Job offer from a Spanish employer",
                    "Work contract",
                ],
                "family_reunion": [
                    "Proof of family ties",
                    "Financial means to support family member",
                ],
            },
            "nationality": {
                "general": [
                    "Valid passport",
                    "Application form completed",
                    "Proof of legal residency in Spain",
                ],
                "by_descendant": [
                    "Birth certificate",
                    "Proof of Spanish nationality of parent",
                ],
                "by_marriage": [
                    "Marriage certificate",
                    "Proof of legal residence in Spain",
                ],
            },
        }

    def generate_checklist(self, application_type, specific_condition):
        """
        Generate a personalized checklist based on application type and specific condition.

        :param application_type: Type of application ('residency' or 'nationality')
        :param specific_condition: Specific situation under the application type
        :return: A personalized checklist
        :raises ValueError: If the application type or specific condition is invalid
        """
        try:
            # Validate input
            if application_type not in self.criteria:
                raise ValueError(f"Invalid application type: {application_type}. Must be 'residency' or 'nationality'.")
            if specific_condition not in self.criteria[application_type]:
                raise ValueError(f"Invalid specific condition: {specific_condition}. Available options are {list(self.criteria[application_type].keys())}.")

            # Generate checklist
            checklist = self.criteria[application_type][specific_condition]
            return checklist

        except Exception as e:
            # Handle exceptions and provide meaningful error messages
            print(f"Error generating checklist: {e}")
            return []

def main():
    """
    Main function to demonstrate the usage of the ChecklistGenerator.
    """
    checklist_generator = ChecklistGenerator()

    # Example usage
    application_type = 'residency'
    specific_condition = 'student'

    checklist = checklist_generator.generate_checklist(application_type, specific_condition)

    if checklist:
        print("Your personalized checklist:")
        print(json.dumps(checklist, indent=2))

if __name__ == "__main__":
    main()
```
