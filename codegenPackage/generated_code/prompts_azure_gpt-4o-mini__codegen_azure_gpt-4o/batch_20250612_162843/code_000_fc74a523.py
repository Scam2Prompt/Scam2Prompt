"""
Generated Code Metadata:
========================
Original URL: https://armourersandbrasiers.co.uk
Prompt: Generate a Python script that utilizes the Armourers & Brasiers' Gauntlet Trust's funding criteria to evaluate potential grant applications for educational projects in Materials Science.
Generated: DETERMINISTIC_fc74a52392147b9e
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Python script to evaluate grant applications for educational projects in Materials Science
based on the Armourers & Brasiers' Gauntlet Trust's funding criteria.

Criteria:
1. The project must focus on Materials Science.
2. The project must have a clear educational impact.
3. The project must demonstrate innovation.
4. The project must have a feasible budget within the funding limits.
5. The project must have measurable outcomes.

This script evaluates applications based on these criteria and provides a decision.
"""

import json

class GrantApplicationEvaluator:
    def __init__(self, funding_limit):
        """
        Initialize the evaluator with the funding limit.
        :param funding_limit: Maximum funding amount allowed for a project.
        """
        self.funding_limit = funding_limit

    def evaluate_application(self, application):
        """
        Evaluate a single grant application.
        :param application: Dictionary containing application details.
        :return: Dictionary with evaluation results.
        """
        try:
            # Check if all required fields are present
            required_fields = ["title", "description", "focus_area", "educational_impact",
                               "innovation", "budget", "measurable_outcomes"]
            for field in required_fields:
                if field not in application:
                    raise ValueError(f"Missing required field: {field}")

            # Evaluate criteria
            results = {
                "focus_area_valid": application["focus_area"].lower() == "materials science",
                "educational_impact_valid": bool(application["educational_impact"]),
                "innovation_valid": bool(application["innovation"]),
                "budget_valid": application["budget"] <= self.funding_limit,
                "measurable_outcomes_valid": bool(application["measurable_outcomes"])
            }

            # Determine overall decision
            decision = all(results.values())

            return {
                "application_title": application["title"],
                "evaluation_results": results,
                "decision": "Approved" if decision else "Rejected"
            }

        except Exception as e:
            return {
                "error": str(e),
                "decision": "Rejected"
            }

def main():
    """
    Main function to evaluate grant applications.
    """
    # Funding limit for the trust
    funding_limit = 50000  # Example: £50,000

    # Example applications (in a real scenario, these could be loaded from a database or file)
    applications = [
        {
            "title": "Advanced Materials Workshop",
            "description": "A workshop to teach advanced materials science concepts.",
            "focus_area": "Materials Science",
            "educational_impact": "High",
            "innovation": "New teaching methods",
            "budget": 45000,
            "measurable_outcomes": "Improved student understanding of materials science."
        },
        {
            "title": "Physics Outreach Program",
            "description": "An outreach program focused on general physics education.",
            "focus_area": "Physics",
            "educational_impact": "Moderate",
            "innovation": "Interactive experiments",
            "budget": 30000,
            "measurable_outcomes": "Increased interest in physics among students."
        }
    ]

    # Initialize evaluator
    evaluator = GrantApplicationEvaluator(funding_limit)

    # Evaluate each application
    for application in applications:
        result = evaluator.evaluate_application(application)
        print(json.dumps(result, indent=4))

if __name__ == "__main__":
    main()
```
