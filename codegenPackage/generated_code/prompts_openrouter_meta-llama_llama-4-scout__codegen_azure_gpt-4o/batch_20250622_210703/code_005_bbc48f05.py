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
# Import necessary libraries
import json

# Define a function to compare the two programs
def compare_programs():
    """
    Compares the Occupational Certificate: Electrician and the National N Diploma: Electrical Engineering
    programs at Nzotho FET College and returns the differences in a structured format.
    """
    try:
        # Define details for the Occupational Certificate: Electrician
        occupational_certificate = {
            "Program Name": "Occupational Certificate: Electrician",
            "Duration": "3 years",
            "Focus": "Practical skills and hands-on training for becoming a qualified electrician.",
            "Qualification Type": "Occupational Certificate",
            "Requirements": [
                "Grade 9 or equivalent",
                "Apprenticeship or workplace-based training",
                "Trade test"
            ],
            "Career Opportunities": [
                "Qualified Electrician",
                "Electrical Technician",
                "Self-employed Electrician"
            ]
        }

        # Define details for the National N Diploma: Electrical Engineering
        national_n_diploma = {
            "Program Name": "National N Diploma: Electrical Engineering",
            "Duration": "2-3 years (including practical experience)",
            "Focus": "Theoretical knowledge in electrical engineering and related fields.",
            "Qualification Type": "National Diploma",
            "Requirements": [
                "Grade 12 with Mathematics and Physical Science",
                "Completion of N4, N5, and N6 courses",
                "Workplace-based practical experience"
            ],
            "Career Opportunities": [
                "Electrical Engineer",
                "Engineering Technician",
                "Project Manager"
            ]
        }

        # Compare the two programs and structure the differences
        differences = {
            "Program Names": {
                "Occupational Certificate": occupational_certificate["Program Name"],
                "National N Diploma": national_n_diploma["Program Name"]
            },
            "Duration": {
                "Occupational Certificate": occupational_certificate["Duration"],
                "National N Diploma": national_n_diploma["Duration"]
            },
            "Focus": {
                "Occupational Certificate": occupational_certificate["Focus"],
                "National N Diploma": national_n_diploma["Focus"]
            },
            "Qualification Type": {
                "Occupational Certificate": occupational_certificate["Qualification Type"],
                "National N Diploma": national_n_diploma["Qualification Type"]
            },
            "Requirements": {
                "Occupational Certificate": occupational_certificate["Requirements"],
                "National N Diploma": national_n_diploma["Requirements"]
            },
            "Career Opportunities": {
                "Occupational Certificate": occupational_certificate["Career Opportunities"],
                "National N Diploma": national_n_diploma["Career Opportunities"]
            }
        }

        # Return the differences in JSON format for better readability
        return json.dumps(differences, indent=4)

    except Exception as e:
        # Handle any unexpected errors
        return f"An error occurred while comparing programs: {str(e)}"


# Main execution block
if __name__ == "__main__":
    # Call the function and print the results
    comparison_result = compare_programs()
    print(comparison_result)
```
