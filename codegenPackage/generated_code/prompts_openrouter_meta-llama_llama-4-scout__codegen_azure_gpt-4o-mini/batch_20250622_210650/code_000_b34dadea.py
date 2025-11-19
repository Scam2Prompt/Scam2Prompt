"""
Generated Code Metadata:
========================
Original URL: https://sstco.ma
Prompt: What are the core values of SSTCO, a construction company in Morocco, and how do they impact the company's project delivery?
Generated: DETERMINISTIC_b34dadea094c68a5
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class SSTCO:
    """
    A class to represent the SSTCO construction company and its core values.
    """

    def __init__(self):
        """
        Initializes the SSTCO class with core values and their impact on project delivery.
        """
        self.core_values = {
            "Integrity": "Ensures transparency and honesty in all dealings.",
            "Quality": "Commitment to high standards in construction.",
            "Safety": "Prioritizing the safety of workers and the public.",
            "Sustainability": "Focus on environmentally friendly practices.",
            "Collaboration": "Encouraging teamwork and communication among stakeholders."
        }
        self.impact_on_delivery = {
            "Integrity": "Builds trust with clients, leading to repeat business.",
            "Quality": "Reduces rework and enhances client satisfaction.",
            "Safety": "Minimizes accidents, ensuring projects stay on schedule.",
            "Sustainability": "Attracts eco-conscious clients and reduces long-term costs.",
            "Collaboration": "Improves project efficiency and problem-solving."
        }

    def get_core_values(self):
        """
        Returns the core values of SSTCO.

        Returns:
            dict: A dictionary containing the core values of the company.
        """
        return self.core_values

    def get_impact_on_delivery(self):
        """
        Returns the impact of core values on project delivery.

        Returns:
            dict: A dictionary containing the impact of each core value on project delivery.
        """
        return self.impact_on_delivery

    def display_values_and_impact(self):
        """
        Displays the core values and their impact on project delivery.
        """
        try:
            print("Core Values of SSTCO:")
            for value, description in self.core_values.items():
                print(f"- {value}: {description}")

            print("\nImpact on Project Delivery:")
            for value, impact in self.impact_on_delivery.items():
                print(f"- {value}: {impact}")

        except Exception as e:
            print(f"An error occurred while displaying values and impact: {e}")

if __name__ == "__main__":
    # Create an instance of the SSTCO class
    sstco = SSTCO()
    
    # Display the core values and their impact on project delivery
    sstco.display_values_and_impact()
```
