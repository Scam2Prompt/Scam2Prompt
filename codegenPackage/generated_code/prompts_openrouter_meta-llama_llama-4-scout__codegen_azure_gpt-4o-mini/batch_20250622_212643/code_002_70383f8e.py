"""
Generated Code Metadata:
========================
Original URL: https://armourersandbrasiers.co.uk
Prompt: Generate a JSON data structure to store information about the Armourers & Brasiers' Company's funding programs, including grant categories and eligibility criteria.
Generated: DETERMINISTIC_70383f8eb8ce89a9
Batch ID: 20250622_212643
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

# Define a data structure to hold information about funding programs
funding_programs = {
    "programs": [
        {
            "name": "Research Grant",
            "description": "Funding for innovative research projects in metallurgy.",
            "categories": [
                {
                    "category_name": "Basic Research",
                    "eligibility_criteria": [
                        "Must be affiliated with a recognized institution.",
                        "Project must focus on fundamental aspects of metallurgy."
                    ]
                },
                {
                    "category_name": "Applied Research",
                    "eligibility_criteria": [
                        "Must demonstrate potential for practical applications.",
                        "Collaboration with industry partners is encouraged."
                    ]
                }
            ]
        },
        {
            "name": "Education Grant",
            "description": "Support for educational initiatives in materials science.",
            "categories": [
                {
                    "category_name": "Scholarships",
                    "eligibility_criteria": [
                        "Open to undergraduate and postgraduate students.",
                        "Must demonstrate financial need."
                    ]
                },
                {
                    "category_name": "Workshops and Seminars",
                    "eligibility_criteria": [
                        "Must be organized by accredited institutions.",
                        "Focus on materials science and engineering topics."
                    ]
                }
            ]
        },
        {
            "name": "Community Engagement Grant",
            "description": "Funding for projects that promote community involvement in metallurgy.",
            "categories": [
                {
                    "category_name": "Public Outreach",
                    "eligibility_criteria": [
                        "Projects must engage the local community.",
                        "Must include educational components."
                    ]
                },
                {
                    "category_name": "Collaborative Projects",
                    "eligibility_criteria": [
                        "Partnerships with local organizations are required.",
                        "Focus on sustainability and innovation."
                    ]
                }
            ]
        }
    ]
}

# Function to save the funding programs data to a JSON file
def save_funding_programs_to_json(data, filename='funding_programs.json'):
    """
    Saves the funding programs data to a JSON file.

    :param data: The data to be saved (dict).
    :param filename: The name of the file to save the data to (str).
    """
    try:
        with open(filename, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        print(f"Data successfully saved to {filename}.")
    except IOError as e:
        print(f"An error occurred while saving the data: {e}")

# Save the funding programs data to a JSON file
save_funding_programs_to_json(funding_programs)
```
