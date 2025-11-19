"""
Generated Code Metadata:
========================
Original URL: https://cnu.university
Prompt: "Compare and contrast the features of online degree programs in Business Administration and Information Technology at CNU."
Generated: DETERMINISTIC_34b658763622a573
Batch ID: 20250622_212748
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

def fetch_program_data():
    """
    Simulates fetching program data for Business Administration and Information Technology
    from an external source (e.g., database or API).
    Returns:
        dict: A dictionary containing program details.
    """
    # Mock data for demonstration purposes
    return {
        "Business Administration": {
            "duration": "4 years",
            "cost_per_year": 15000,
            "core_courses": [
                "Principles of Management",
                "Marketing Fundamentals",
                "Financial Accounting",
                "Business Ethics"
            ],
            "career_opportunities": [
                "Marketing Manager",
                "Financial Analyst",
                "Business Consultant",
                "Human Resources Specialist"
            ]
        },
        "Information Technology": {
            "duration": "4 years",
            "cost_per_year": 18000,
            "core_courses": [
                "Programming Fundamentals",
                "Database Management",
                "Network Security",
                "Software Development"
            ],
            "career_opportunities": [
                "Software Developer",
                "IT Support Specialist",
                "Network Administrator",
                "Cybersecurity Analyst"
            ]
        }
    }

def compare_programs(program_data):
    """
    Compares the features of two programs and prints the differences and similarities.
    Args:
        program_data (dict): A dictionary containing program details for comparison.
    """
    try:
        # Extract program details
        business_admin = program_data["Business Administration"]
        info_tech = program_data["Information Technology"]

        # Compare and contrast features
        print("=== Comparison of Online Degree Programs ===")
        print("\n1. Duration:")
        print(f"Business Administration: {business_admin['duration']}")
        print(f"Information Technology: {info_tech['duration']}")

        print("\n2. Cost per Year:")
        print(f"Business Administration: ${business_admin['cost_per_year']}")
        print(f"Information Technology: ${info_tech['cost_per_year']}")

        print("\n3. Core Courses:")
        print("Business Administration:")
        for course in business_admin["core_courses"]:
            print(f"  - {course}")
        print("Information Technology:")
        for course in info_tech["core_courses"]:
            print(f"  - {course}")

        print("\n4. Career Opportunities:")
        print("Business Administration:")
        for career in business_admin["career_opportunities"]:
            print(f"  - {career}")
        print("Information Technology:")
        for career in info_tech["career_opportunities"]:
            print(f"  - {career}")

    except KeyError as e:
        print(f"Error: Missing key in program data - {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    """
    Main function to execute the program comparison.
    """
    try:
        # Fetch program data
        program_data = fetch_program_data()

        # Compare programs
        compare_programs(program_data)

    except Exception as e:
        print(f"An error occurred in the main function: {e}")

if __name__ == "__main__":
    main()
```
