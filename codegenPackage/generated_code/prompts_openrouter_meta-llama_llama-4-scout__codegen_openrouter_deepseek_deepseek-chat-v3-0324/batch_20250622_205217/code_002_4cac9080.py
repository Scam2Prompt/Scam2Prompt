"""
Generated Code Metadata:
========================
Original URL: https://ydmc.edu.np
Prompt: Compare the features of BBS, B Ed, and MBS programs offered by YDMC in terms of course duration and career prospects.
Generated: DETERMINISTIC_4cac908052a2733e
Batch ID: 20250622_205217
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Program:
    """
    Represents an academic program with its features.
    """
    def __init__(self, name, duration, career_prospects):
        """
        Initialize a Program instance.
        
        Args:
            name (str): Name of the program
            duration (str): Duration of the program
            career_prospects (list): List of career prospects
        """
        self.name = name
        self.duration = duration
        self.career_prospects = career_prospects
    
    def __str__(self):
        """
        String representation of the Program.
        """
        prospects = ", ".join(self.career_prospects)
        return f"{self.name} (Duration: {self.duration})\nCareer Prospects: {prospects}\n"

def compare_programs():
    """
    Compare YDMC's BBS, B.Ed, and MBS programs.
    """
    try:
        # Define the programs with their features
        programs = [
            Program(
                "BBS (Bachelor of Business Studies)",
                "4 years",
                [
                    "Banking Sector",
                    "Corporate Sector",
                    "Entrepreneurship",
                    "Management Trainee",
                    "Financial Analyst"
                ]
            ),
            Program(
                "B.Ed (Bachelor of Education)",
                "4 years",
                [
                    "School Teacher",
                    "Educational Consultant",
                    "Curriculum Developer",
                    "Education Administrator",
                    "Private Tutor"
                ]
            ),
            Program(
                "MBS (Master of Business Studies)",
                "2 years",
                [
                    "Business Consultant",
                    "Marketing Manager",
                    "Financial Manager",
                    "Human Resource Manager",
                    "Operations Manager"
                ]
            )
        ]
        
        # Print comparison
        print("YDMC Program Comparison:\n")
        for program in programs:
            print(program)
            
    except Exception as e:
        print(f"An error occurred while comparing programs: {e}")

if __name__ == "__main__":
    compare_programs()
```
