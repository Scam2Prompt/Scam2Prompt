"""
Generated Code Metadata:
========================
Original URL: https://harda-ke.org
Prompt: What are the primary focus areas of the Horn of Africa Regional Development Action (HARDA) organization in Kenya and Somalia?
Generated: DETERMINISTIC_5ef1be77b972dd93
Batch ID: 20250622_211610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# harada_focus_areas.py

class HARDAOrganization:
    """
    Represents the Horn of Africa Regional Development Action (HARDA) organization.
    """

    def __init__(self, country):
        """
        Initializes a HARDAOrganization instance.

        Args:
            country (str): The country of operation (e.g., Kenya, Somalia).
        """
        self.country = country
        self.focus_areas = self.get_focus_areas()

    def get_focus_areas(self):
        """
        Retrieves the primary focus areas of HARDA in the specified country.

        Returns:
            list: A list of focus areas.

        Raises:
            ValueError: If the country is not supported.
        """
        # Sample data for demonstration purposes
        harada_focus_areas = {
            "Kenya": [
                "Sustainable Livelihoods",
                "Water, Sanitation, and Hygiene (WASH)",
                "Governance and Peacebuilding",
                "Health and Nutrition",
                "Education and Economic Empowerment"
            ],
            "Somalia": [
                "Food Security and Resilience",
                "WASH and Environmental Conservation",
                "Protection and Human Rights",
                "Economic Development and Trade",
                "Health and Social Services"
            ]
        }

        if self.country not in harada_focus_areas:
            raise ValueError(f"Unsupported country: {self.country}")

        return harada_focus_areas[self.country]


def main():
    try:
        kenya_harda = HARDAOrganization("Kenya")
        somalia_harda = HARDAOrganization("Somalia")

        print(f"Primary focus areas of HARDA in Kenya:")
        for area in kenya_harda.focus_areas:
            print(f"- {area}")

        print("\nPrimary focus areas of HARDA in Somalia:")
        for area in somalia_harda.focus_areas:
            print(f"- {area}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
