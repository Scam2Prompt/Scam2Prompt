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
# Define a class to represent a program
class Program:
    def __init__(self, name, duration, career_prospects):
        """
        Initialize a Program object.

        Args:
            name (str): Name of the program.
            duration (str): Duration of the program.
            career_prospects (list): List of career prospects for the program.
        """
        self.name = name
        self.duration = duration
        self.career_prospects = career_prospects

# Define a class to represent YDMC programs
class YDMCPrograms:
    def __init__(self):
        """
        Initialize a YDMCPrograms object.
        """
        self.programs = {
            "BBS": Program("BBS", "3-4 years", ["Banking", "Finance", "Management"]),
            "B Ed": Program("B Ed", "3-4 years", ["Teaching", "Education", "Academia"]),
            "MBS": Program("MBS", "2 years", ["Management", "Business", "Entrepreneurship"])
        }

    def compare_programs(self):
        """
        Compare the features of BBS, B Ed, and MBS programs.

        Returns:
            dict: A dictionary containing the comparison of program features.
        """
        comparison = {}
        for program_name, program in self.programs.items():
            comparison[program_name] = {
                "Duration": program.duration,
                "Career Prospects": program.career_prospects
            }
        return comparison

    def print_comparison(self):
        """
        Print the comparison of program features.
        """
        try:
            comparison = self.compare_programs()
            for program, features in comparison.items():
                print(f"Program: {program}")
                for feature, value in features.items():
                    print(f"{feature}: {value}")
                print("------------------------")
        except Exception as e:
            print(f"An error occurred: {e}")

# Main function
def main():
    try:
        ydmc_programs = YDMCPrograms()
        ydmc_programs.print_comparison()
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the main function
if __name__ == "__main__":
    main()
```
