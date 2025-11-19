"""
Generated Code Metadata:
========================
Original URL: https://somtu.edu.np
Prompt: Compare the MBA in Finance and Control (MBA FC), MBA in Global Leadership and Management (MBA GLM), and MBA in Information Technology (MBA IT) programs at SOMTU, highlighting their unique focus areas and curriculum structures.
Generated: DETERMINISTIC_2c9d1216093fb0f2
Batch ID: 20250622_212709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class MBAProgram:
    """
    Represents an MBA program with its unique focus areas and curriculum structure.
    """
    
    def __init__(self, name, focus_areas, curriculum_structure):
        """
        Initialize an MBA program with its details.
        
        Args:
            name (str): Name of the MBA program
            focus_areas (list): List of focus areas for the program
            curriculum_structure (dict): Curriculum structure with key components
        """
        self.name = name
        self.focus_areas = focus_areas
        self.curriculum_structure = curriculum_structure
    
    def __str__(self):
        """Return a formatted string representation of the program."""
        focus_str = "\n".join(f"- {area}" for area in self.focus_areas)
        curriculum_str = "\n".join(f"- {key}: {value}" for key, value in self.curriculum_structure.items())
        
        return (
            f"Program: {self.name}\n\n"
            f"Focus Areas:\n{focus_str}\n\n"
            f"Curriculum Structure:\n{curriculum_str}\n"
            f"{'-'*40}"
        )

def compare_mba_programs():
    """
    Compare MBA programs at SOMTU by creating instances and displaying their details.
    """
    # MBA in Finance and Control (MBA FC)
    mba_fc = MBAProgram(
        name="MBA in Finance and Control (MBA FC)",
        focus_areas=[
            "Financial Analysis and Reporting",
            "Corporate Finance",
            "Investment Management",
            "Risk Management",
            "Financial Regulations and Compliance"
        ],
        curriculum_structure={
            "Core Courses": "Financial Accounting, Corporate Finance, Investment Analysis",
            "Electives": "Derivatives, International Finance, Mergers & Acquisitions",
            "Practical Component": "Financial Modeling Projects, Case Studies",
            "Capstone": "Finance Strategy Project"
        }
    )
    
    # MBA in Global Leadership and Management (MBA GLM)
    mba_glm = MBAProgram(
        name="MBA in Global Leadership and Management (MBA GLM)",
        focus_areas=[
            "Global Business Strategy",
            "Cross-cultural Management",
            "International Business Operations",
            "Leadership Development",
            "Global Supply Chain Management"
        ],
        curriculum_structure={
            "Core Courses": "Global Business Environment, Leadership in Organizations",
            "Electives": "International Negotiations, Emerging Markets, Global Marketing",
            "Practical Component": "International Business Simulations, Leadership Workshops",
            "Capstone": "Global Business Strategy Project"
        }
    )
    
    # MBA in Information Technology (MBA IT)
    mba_it = MBAProgram(
        name="MBA in Information Technology (MBA IT)",
        focus_areas=[
            "IT Strategy and Governance",
            "Digital Transformation",
            "Data Analytics and Business Intelligence",
            "Enterprise Systems Management",
            "Emerging Technologies"
        ],
        curriculum_structure={
            "Core Courses": "IT Project Management, Business Analytics, Systems Architecture",
            "Electives": "Cloud Computing, Cybersecurity, AI in Business",
            "Practical Component": "IT Consulting Projects, Tech Case Studies",
            "Capstone": "Digital Transformation Project"
        }
    )
    
    # Display comparison
    print("\nMBA Program Comparison at SOMTU:\n")
    print(mba_fc)
    print(mba_glm)
    print(mba_it)

if __name__ == "__main__":
    compare_mba_programs()
```
