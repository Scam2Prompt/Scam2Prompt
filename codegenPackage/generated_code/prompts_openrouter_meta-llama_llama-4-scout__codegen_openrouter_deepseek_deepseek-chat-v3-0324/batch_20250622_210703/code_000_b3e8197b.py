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
class JewelAutismCentre:
    """
    A class representing the departments and interventions offered by Jewel Autism Centre.
    """

    def __init__(self):
        """
        Initialize the departments and their descriptions.
        """
        self.departments = {
            "Occupational Therapy": {
                "description": "Helps children develop fine motor skills, sensory processing, and daily living activities.",
                "focus_areas": ["Sensory integration", "Motor coordination", "Self-care skills"]
            },
            "Speech Therapy": {
                "description": "Focuses on improving communication skills, including speech, language, and social communication.",
                "focus_areas": ["Verbal communication", "Non-verbal communication", "Pragmatic language"]
            },
            "Behavior Therapy": {
                "description": "Addresses challenging behaviors and teaches positive replacement behaviors.",
                "focus_areas": ["ABA techniques", "Behavior modification", "Social skills training"]
            },
            "Special Education": {
                "description": "Provides individualized academic instruction tailored to the child's learning needs.",
                "focus_areas": ["Academic skills", "Cognitive development", "Learning strategies"]
            },
            "Physiotherapy": {
                "description": "Focuses on improving gross motor skills, balance, and physical coordination.",
                "focus_areas": ["Motor planning", "Postural control", "Muscle strengthening"]
            },
            "Early Intervention": {
                "description": "Provides support for young children (0-6 years) to maximize developmental potential.",
                "focus_areas": ["Developmental milestones", "Play skills", "Parent training"]
            },
            "Parent Training": {
                "description": "Equips parents with strategies to support their child's development at home.",
                "focus_areas": ["Behavior management", "Communication techniques", "Daily routines"]
            }
        }

    def get_departments(self):
        """
        Returns all available departments and their details.
        
        Returns:
            dict: Dictionary of departments with their descriptions and focus areas.
        """
        return self.departments

    def get_department_info(self, department_name):
        """
        Returns information about a specific department.
        
        Args:
            department_name (str): Name of the department to query.
            
        Returns:
            dict: Department information if found, None otherwise.
        """
        return self.departments.get(department_name)

    def list_departments(self):
        """
        Returns a list of all department names.
        
        Returns:
            list: List of department names.
        """
        return list(self.departments.keys())


# Example usage
if __name__ == "__main__":
    centre = JewelAutismCentre()
    
    # Get all departments
    print("Available Departments:")
    for dept in centre.list_departments():
        print(f"- {dept}")
    
    # Get specific department info
    dept_name = "Speech Therapy"
    dept_info = centre.get_department_info(dept_name)
    if dept_info:
        print(f"\n{dept_name} Department:")
        print(f"Description: {dept_info['description']}")
        print("Focus Areas:")
        for area in dept_info['focus_areas']:
            print(f"- {area}")
    else:
        print(f"\nDepartment '{dept_name}' not found.")
```
