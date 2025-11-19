"""
Generated Code Metadata:
========================
Original URL: https://amirinternationalcharity.org
Prompt: Recommend a suitable CRM (Customer Relationship Management) system for a charity organization like Amir International Charity Organization to manage donor relationships, volunteer engagement, and program coordination.
Generated: DETERMINISTIC_e9e09021f1e5ef65
Batch ID: 20250622_210348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# crm_recommender.py

class CRMSystem:
    """Base class for CRM systems."""

    def __init__(self, name):
        """
        Initialize a CRM system.

        Args:
            name (str): Name of the CRM system.
        """
        self.name = name

    def get_features(self):
        """Get features of the CRM system."""
        pass


class Salesforce(CRMSystem):
    """Salesforce CRM system."""

    def __init__(self):
        super().__init__("Salesforce")

    def get_features(self):
        """
        Get features of Salesforce CRM system.

        Returns:
            list: Features of Salesforce CRM system.
        """
        return [
            "Donor management",
            "Volunteer engagement",
            "Program coordination",
            "Grant management",
            "Reporting and analytics",
        ]


class ZohoCRM(CRMSystem):
    """Zoho CRM system."""

    def __init__(self):
        super().__init__("Zoho CRM")

    def get_features(self):
        """
        Get features of Zoho CRM system.

        Returns:
            list: Features of Zoho CRM system.
        """
        return [
            "Donor management",
            "Volunteer engagement",
            "Program coordination",
            "Marketing automation",
            "Reporting and analytics",
        ]


class HubSpot(CRMSystem):
    """HubSpot CRM system."""

    def __init__(self):
        super().__init__("HubSpot")

    def get_features(self):
        """
        Get features of HubSpot CRM system.

        Returns:
            list: Features of HubSpot CRM system.
        """
        return [
            "Donor management",
            "Volunteer engagement",
            "Program coordination",
            "Marketing automation",
            "Sales automation",
            "Reporting and analytics",
        ]


def recommend_crm(charity_type, budget):
    """
    Recommend a suitable CRM system for a charity organization.

    Args:
        charity_type (str): Type of charity organization.
        budget (float): Budget of the charity organization.

    Returns:
        CRMSystem: Recommended CRM system.

    Raises:
        ValueError: If charity type or budget is invalid.
    """
    if charity_type not in ["local", "international"]:
        raise ValueError("Invalid charity type")

    if budget < 0:
        raise ValueError("Invalid budget")

    crm_systems = {
        "local": [Salesforce(), ZohoCRM()],
        "international": [Salesforce(), HubSpot()],
    }

    recommended_crm = None
    for crm in crm_systems[charity_type]:
        if budget >= 10000 and crm.name == "Salesforce":
            recommended_crm = crm
            break
        elif budget >= 5000 and crm.name == "HubSpot":
            recommended_crm = crm
            break
        elif budget >= 1000 and crm.name == "Zoho CRM":
            recommended_crm = crm
            break

    if recommended_crm is None:
        recommended_crm = crm_systems[charity_type][0]

    return recommended_crm


def main():
    charity_type = "international"
    budget = 15000

    try:
        recommended_crm = recommend_crm(charity_type, budget)
        print(f"Recommended CRM system: {recommended_crm.name}")
        print("Features:")
        for feature in recommended_crm.get_features():
            print(f"- {feature}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
