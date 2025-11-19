"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://armourersandbrasiers.co.uk
Prompt: Generate a Python script that utilizes the Armourers & Brasiers' Gauntlet Trust's funding criteria to evaluate potential grant applications for educational projects in Materials Science.
Generated: DETERMINISTIC_fc74a52392147b9e
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Grant Application Evaluator for Armourers & Brasiers' Gauntlet Trust

This script evaluates educational project applications for funding based 
on predefined criteria related to Materials Science.
"""

import json

# Funding criteria for evaluation
FUNDING_CRITERIA = {
    "impact_score_threshold": 7,  # Minimum required impact score (out of 10)
    "materials_science_focus": True,  # Must have a focus on Materials Science
    "budget_limit": 50000,  # Maximum budget to be eligible for funding
    "applicant_eligibility": ["university", "research_institute", "non_profit"]  # Valid applicant types
}

def evaluate_application(application):
    """
    Evaluates a grant application based on predefined funding criteria.

    Args:
        application (dict): A dictionary containing application details.

    Returns:
        dict: A dictionary containing evaluation results: 'eligible' (bool) and 'reason' (str).
    """
    try:
        # Extract application details
        impact_score = application.get("impact_score")
        focus_area = application.get("focus_area")
        budget = application.get("budget")
        applicant_type = application.get("applicant_type")

        # Check if impact score meets the threshold
        if impact_score is None or impact_score < FUNDING_CRITERIA["impact_score_threshold"]:
            return {"eligible": False, "reason": "Impact score below threshold."}

        # Check if the project is focused on Materials Science
        if focus_area is None or FUNDING_CRITERIA["materials_science_focus"] and focus_area.lower() != "materials science":
            return {"eligible": False, "reason": "Project is not focused on Materials Science."}

        # Check if budget is within the allowable limit
        if budget is None or budget > FUNDING_CRITERIA["budget_limit"]:
            return {"eligible": False, "reason": "Budget exceeds allowable limit."}

        # Check if applicant type is eligible
        if applicant_type is None or applicant_type.lower() not in FUNDING_CRITERIA["applicant_eligibility"]:
            return {"eligible": False, "reason": f"Applicant type '{applicant_type}' not eligible for funding."}

        # If all criteria are met, application is eligible
        return {"eligible": True, "reason": "Application meets all funding criteria."}

    except Exception as e:
        # Handle unexpected errors during evaluation
        return {"eligible": False, "reason": f"Error during evaluation: {str(e)}"}

def main():
    """
    Main function to handle evaluation of multiple grant applications.
    """
    # Example applications (in real-world, you may load this from a database or file)
    applications = [
        {
            "applicant_name": "University of Materials Science",
            "impact_score": 8,
            "focus_area": "Materials Science",
            "budget": 45000,
            "applicant_type": "university"
        },
        {
            "applicant_name": "Non-Profit Organization for Education",
            "impact_score": 6,
            "focus_area": "Materials Science",
            "budget": 30000,
            "applicant_type": "non_profit"
        },
        {
            "applicant_name": "Tech Startup Inc.",
            "impact_score": 9,
            "focus_area": "Materials Science",
            "budget": 60000,
            "applicant_type": "startup"
        }
    ]

    # Evaluate applications
    for app in applications:
        result = evaluate_application(app)
        print(f"Application from {app['applicant_name']} - Eligible: {result['eligible']} - Reason: {result['reason']}")

if __name__ == "__main__":
    main()
```
