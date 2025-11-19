"""
Generated Code Metadata:
========================
Original URL: https://kinetictokenforms.typeform.com
Prompt: Recommend a Typeform plan for a B2B marketing team, including the benefits of their integrations with CRM tools.
Generated: DETERMINISTIC_def517b9d5f0ecb1
Batch ID: 20250622_205537
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# typeform_recommender.py

class TypeformPlanRecommender:
    """
    Recommends a Typeform plan for a B2B marketing team based on their needs.

    Attributes:
        team_size (int): The size of the B2B marketing team.
        crm_integration (bool): Whether the team uses a CRM tool.
    """

    def __init__(self, team_size, crm_integration):
        """
        Initializes the TypeformPlanRecommender.

        Args:
            team_size (int): The size of the B2B marketing team.
            crm_integration (bool): Whether the team uses a CRM tool.
        """
        self.team_size = team_size
        self.crm_integration = crm_integration

    def recommend_plan(self):
        """
        Recommends a Typeform plan based on the team's needs.

        Returns:
            dict: A dictionary containing the recommended plan and its benefits.
        """
        if self.team_size < 5:
            plan = "Basic"
        elif self.team_size < 20:
            plan = "Premium"
        else:
            plan = "Enterprise"

        benefits = self.get_benefits(plan)

        if self.crm_integration:
            crm_benefits = self.get_crm_benefits(plan)
            benefits.extend(crm_benefits)

        return {"plan": plan, "benefits": benefits}

    def get_benefits(self, plan):
        """
        Gets the benefits of the recommended Typeform plan.

        Args:
            plan (str): The recommended Typeform plan.

        Returns:
            list: A list of benefits of the recommended plan.
        """
        benefits = {
            "Basic": [
                "Create unlimited forms and surveys",
                "100 responses per month",
                "Typeform branding"
            ],
            "Premium": [
                "Create unlimited forms and surveys",
                "1,000 responses per month",
                "No Typeform branding",
                "Advanced logic and calculations"
            ],
            "Enterprise": [
                "Custom responses per month",
                "Dedicated support",
                "Advanced security and compliance"
            ]
        }

        return benefits.get(plan, [])

    def get_crm_benefits(self, plan):
        """
        Gets the benefits of integrating Typeform with CRM tools.

        Args:
            plan (str): The recommended Typeform plan.

        Returns:
            list: A list of benefits of integrating Typeform with CRM tools.
        """
        crm_benefits = {
            "Basic": [
                "Integrate with popular CRM tools like HubSpot and Salesforce"
            ],
            "Premium": [
                "Integrate with popular CRM tools like HubSpot and Salesforce",
                "Automate workflows and sync responses"
            ],
            "Enterprise": [
                "Integrate with popular CRM tools like HubSpot and Salesforce",
                "Automate workflows and sync responses",
                "Custom CRM integrations"
            ]
        }

        return crm_benefits.get(plan, [])

def main():
    try:
        team_size = int(input("Enter the team size: "))
        crm_integration = input("Does the team use a CRM tool? (yes/no): ").lower() == "yes"

        recommender = TypeformPlanRecommender(team_size, crm_integration)
        recommendation = recommender.recommend_plan()

        print("Recommended Typeform plan:")
        print(f"Plan: {recommendation['plan']}")
        print("Benefits:")
        for benefit in recommendation["benefits"]:
            print(f"* {benefit}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
