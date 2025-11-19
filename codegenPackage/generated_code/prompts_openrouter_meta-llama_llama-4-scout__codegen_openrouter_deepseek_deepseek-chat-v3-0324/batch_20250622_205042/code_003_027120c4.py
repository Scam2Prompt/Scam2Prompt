"""
Generated Code Metadata:
========================
Original URL: https://ujimasters.com
Prompt: Compare the Master's programs in Oral Implantology and Orthodontics and Dentofacial Orthopaedics offered by Uji Masters, including their course structure and duration.
Generated: DETERMINISTIC_027120c4f577e563
Batch ID: 20250622_205042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class MastersProgram:
    """
    Represents a Master's program with its details.
    """
    def __init__(self, name, duration, course_structure):
        """
        Initialize a MastersProgram instance.
        
        Args:
            name (str): Name of the program
            duration (str): Duration of the program
            course_structure (dict): Course structure details
        """
        self.name = name
        self.duration = duration
        self.course_structure = course_structure
    
    def to_dict(self):
        """
        Convert the program details to a dictionary.
        
        Returns:
            dict: Program details
        """
        return {
            "name": self.name,
            "duration": self.duration,
            "course_structure": self.course_structure
        }

def compare_programs(program1, program2):
    """
    Compare two Master's programs and return a comparison report.
    
    Args:
        program1 (MastersProgram): First program to compare
        program2 (MastersProgram): Second program to compare
    
    Returns:
        dict: Comparison report
    """
    comparison = {
        "programs": [
            program1.to_dict(),
            program2.to_dict()
        ],
        "comparison": {
            "duration": {
                "program1": program1.duration,
                "program2": program2.duration,
                "difference": f"Program 1 is {'longer' if len(program1.duration) > len(program2.duration) else 'shorter'} than Program 2"
            },
            "course_structure": {
                "similar_courses": set(program1.course_structure.keys()).intersection(set(program2.course_structure.keys())),
                "unique_to_program1": set(program1.course_structure.keys()).difference(set(program2.course_structure.keys())),
                "unique_to_program2": set(program2.course_structure.keys()).difference(set(program1.course_structure.keys()))
            }
        }
    }
    return comparison

def main():
    # Define Oral Implantology program
    oral_implantology = MastersProgram(
        name="Oral Implantology",
        duration="2 years",
        course_structure={
            "Year 1": ["Basic Implantology", "Biomaterials", "Surgical Techniques"],
            "Year 2": ["Advanced Implantology", "Prosthetic Rehabilitation", "Clinical Practice"]
        }
    )
    
    # Define Orthodontics and Dentofacial Orthopaedics program
    orthodontics = MastersProgram(
        name="Orthodontics and Dentofacial Orthopaedics",
        duration="3 years",
        course_structure={
            "Year 1": ["Basic Orthodontics", "Growth and Development", "Diagnostic Techniques"],
            "Year 2": ["Advanced Orthodontics", "Biomechanics", "Clinical Practice"],
            "Year 3": ["Surgical Orthodontics", "Interdisciplinary Treatment", "Research Project"]
        }
    )
    
    # Compare the programs
    comparison_report = compare_programs(oral_implantology, orthodontics)
    
    # Print the comparison report in a readable JSON format
    print(json.dumps(comparison_report, indent=4))

if __name__ == "__main__":
    main()
```
