"""
Generated Code Metadata:
========================
Original URL: https://lexuscertifications.com
Prompt: "Create a sample business plan for implementing an ISO 45001 Occupational Health and Safety Management System."
Generated: DETERMINISTIC_3ea3caab10cb3293
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
ISO 45001 Business Plan Generator
This script generates a sample business plan for implementing an ISO 45001 Occupational Health and Safety Management System.
The plan includes key sections such as objectives, scope, resources, timeline, and risk management.
"""

import json

def generate_iso_45001_business_plan(company_name, industry, start_date, end_date):
    """
    Generates a sample business plan for ISO 45001 implementation.

    Args:
        company_name (str): Name of the company.
        industry (str): Industry type (e.g., manufacturing, construction).
        start_date (str): Start date of the implementation (YYYY-MM-DD).
        end_date (str): End date of the implementation (YYYY-MM-DD).

    Returns:
        dict: A structured business plan.
    """
    try:
        # Validate input dates
        if start_date >= end_date:
            raise ValueError("Start date must be earlier than end date.")

        # Business plan structure
        business_plan = {
            "Company Name": company_name,
            "Industry": industry,
            "ISO 45001 Implementation Plan": {
                "Objectives": [
                    "Enhance workplace safety and reduce risks.",
                    "Ensure compliance with legal and regulatory requirements.",
                    "Promote a culture of health and safety within the organization."
                ],
                "Scope": "Implementation of ISO 45001 across all departments and facilities.",
                "Resources": {
                    "Personnel": [
                        "Project Manager",
                        "Health and Safety Officer",
                        "Department Representatives"
                    ],
                    "Budget": "Estimated budget of $50,000 for training, audits, and certification.",
                    "Tools": [
                        "Risk assessment software",
                        "Incident reporting system",
                        "Training materials"
                    ]
                },
                "Timeline": {
                    "Start Date": start_date,
                    "End Date": end_date,
                    "Milestones": [
                        {"Phase": "Planning", "Deadline": "1 month from start date"},
                        {"Phase": "Risk Assessment", "Deadline": "2 months from start date"},
                        {"Phase": "Training", "Deadline": "3 months from start date"},
                        {"Phase": "Implementation", "Deadline": "4 months from start date"},
                        {"Phase": "Audit and Certification", "Deadline": "5 months from start date"}
                    ]
                },
                "Risk Management": {
                    "Potential Risks": [
                        "Resistance to change from employees.",
                        "Budget overruns.",
                        "Delays in implementation."
                    ],
                    "Mitigation Strategies": [
                        "Conduct awareness sessions to address resistance.",
                        "Monitor expenses closely and adjust budget as needed.",
                        "Develop contingency plans for delays."
                    ]
                }
            }
        }

        return business_plan

    except ValueError as ve:
        print(f"Error: {ve}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


def save_business_plan_to_file(business_plan, file_name):
    """
    Saves the business plan to a JSON file.

    Args:
        business_plan (dict): The business plan to save.
        file_name (str): Name of the file to save the plan.

    Returns:
        bool: True if the file was saved successfully, False otherwise.
    """
    try:
        with open(file_name, 'w') as file:
            json.dump(business_plan, file, indent=4)
        print(f"Business plan saved successfully to {file_name}.")
        return True
    except Exception as e:
        print(f"Failed to save business plan: {e}")
        return False


# Example usage
if __name__ == "__main__":
    # Generate a sample business plan
    company_name = "ABC Corp"
    industry = "Manufacturing"
    start_date = "2023-01-01"
    end_date = "2023-06-01"

    business_plan = generate_iso_45001_business_plan(company_name, industry, start_date, end_date)

    if business_plan:
        # Save the business plan to a file
        save_business_plan_to_file(business_plan, "iso_45001_business_plan.json")
```
