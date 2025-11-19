"""
Generated Code Metadata:
========================
Original URL: https://jewelautismcentre.org
Prompt: What are the different departments offered by Jewel Autism Centre for Autism Spectrum Disorders interventions, and how do they support a child's development?
Generated: DETERMINISTIC_b3e8197b1fc98006
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
import json

# Define a class to represent the Jewel Autism Centre
class JewelAutismCentre:
    def __init__(self):
        # Initialize the departments offered by the centre
        self.departments = {
            "Occupational Therapy": "Focuses on improving fine motor skills, sensory integration, and daily living activities.",
            "Speech Therapy": "Helps children develop communication skills, including speech, language, and non-verbal communication.",
            "Behavioral Therapy (ABA)": "Uses Applied Behavior Analysis to teach positive behaviors and reduce challenging ones.",
            "Special Education": "Provides individualized education plans to support academic and social development.",
            "Psychology Services": "Offers counseling and assessments to address emotional and behavioral challenges.",
            "Physiotherapy": "Improves gross motor skills, balance, and physical coordination.",
            "Art Therapy": "Encourages self-expression and emotional development through creative activities.",
            "Music Therapy": "Uses music to enhance social, emotional, and cognitive skills.",
            "Parent Training and Support": "Empowers parents with strategies to support their child's development at home."
        }

    def get_departments(self):
        """
        Returns the list of departments and their descriptions.
        """
        return self.departments

    def get_department_details(self, department_name):
        """
        Returns the details of a specific department.
        :param department_name: Name of the department to retrieve details for.
        :return: Description of the department or an error message if not found.
        """
        try:
            # Check if the department exists
            if department_name in self.departments:
                return self.departments[department_name]
            else:
                raise ValueError(f"Department '{department_name}' not found.")
        except ValueError as e:
            return str(e)

# Main function to demonstrate the functionality
def main():
    # Create an instance of JewelAutismCentre
    centre = JewelAutismCentre()

    # Get all departments
    print("Departments offered by Jewel Autism Centre:")
    print(json.dumps(centre.get_departments(), indent=4))

    # Get details of a specific department
    department_name = "Speech Therapy"
    print(f"\nDetails of '{department_name}':")
    print(centre.get_department_details(department_name))

    # Handle a non-existent department
    invalid_department = "Dance Therapy"
    print(f"\nDetails of '{invalid_department}':")
    print(centre.get_department_details(invalid_department))

# Entry point of the script
if __name__ == "__main__":
    main()
```
