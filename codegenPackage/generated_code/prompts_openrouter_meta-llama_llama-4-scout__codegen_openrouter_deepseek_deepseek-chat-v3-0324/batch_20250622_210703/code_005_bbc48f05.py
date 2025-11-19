"""
Generated Code Metadata:
========================
Original URL: https://nzothofetcollege.co.za
Prompt: What are the differences between the Occupational Certificate: Electrician and the National N Diploma: Electrical Engineering programs at Nzotho FET College?
Generated: DETERMINISTIC_bbc48f05c7a31fba
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Program to compare Occupational Certificate: Electrician vs National N Diploma: Electrical Engineering
at Nzotho FET College.

This script outlines the key differences between the two programs.
"""

class ProgramComparison:
    """
    Class to represent and compare the two electrical programs at Nzotho FET College.
    """
    
    def __init__(self):
        self.programs = {
            "Occupational Certificate: Electrician": {
                "type": "Occupational Certificate",
                "duration": "3 years",
                "focus": "Practical electrical installation and maintenance skills",
                "certification": "QCTO accredited",
                "entry_requirements": "Grade 9 or equivalent",
                "career_path": "Qualified electrician, electrical technician",
                "assessment": "Workplace and institutional assessments",
                "theory_practice_balance": "More practical (70% practical, 30% theory)"
            },
            "National N Diploma: Electrical Engineering": {
                "type": "National Diploma",
                "duration": "3 years (N4-N6)",
                "focus": "Theoretical and technical electrical engineering knowledge",
                "certification": "DHET accredited",
                "entry_requirements": "Grade 12 with mathematics and physical science",
                "career_path": "Electrical engineer, technologist, further studies",
                "assessment": "Theoretical examinations",
                "theory_practice_balance": "More theoretical (60% theory, 40% practical)"
            }
        }
    
    def compare_programs(self):
        """
        Compare the two programs and return their differences.
        
        Returns:
            dict: A dictionary containing the comparison results.
        """
        comparison = {}
        for program_name, details in self.programs.items():
            comparison[program_name] = details
        
        return comparison

    def get_program_details(self, program_name):
        """
        Get details for a specific program.
        
        Args:
            program_name (str): Name of the program to get details for.
            
        Returns:
            dict: Program details if found, None otherwise.
        """
        return self.programs.get(program_name)

def main():
    """
    Main function to demonstrate the program comparison.
    """
    try:
        comparator = ProgramComparison()
        
        # Get comparison of all programs
        comparison = comparator.compare_programs()
        print("Program Comparison:")
        for program, details in comparison.items():
            print(f"\n{program}:")
            for key, value in details.items():
                print(f"{key.replace('_', ' ').title()}: {value}")
        
        # Example: Get details for a specific program
        print("\nExample - Getting details for Occupational Certificate:")
        electrician_details = comparator.get_program_details("Occupational Certificate: Electrician")
        if electrician_details:
            for key, value in electrician_details.items():
                print(f"{key.replace('_', ' ').title()}: {value}")
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
