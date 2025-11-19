"""
Generated Code Metadata:
========================
Original URL: https://isienvironmental.com
Prompt: Develop a code snippet that evaluates a facility's readiness for ISO 14001 certification based on the compliance audits mentioned on iSi Environmental's website.
Generated: DETERMINISTIC_e0ca1519e5993904
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Facility:
    def __init__(self, name, audits):
        """
        Initializes a Facility instance.

        :param name: str - The name of the facility.
        :param audits: list of dict - A list of compliance audits with their results.
        """
        self.name = name
        self.audits = audits

    def evaluate_readiness(self):
        """
        Evaluates the facility's readiness for ISO 14001 certification based on compliance audits.

        :return: str - Readiness status message.
        """
        if not self.audits:
            return f"{self.name} has no audits conducted. Cannot evaluate readiness."

        compliant_audits = [audit for audit in self.audits if audit.get('compliant', False)]
        total_audits = len(self.audits)

        # Calculate compliance percentage
        compliance_percentage = (len(compliant_audits) / total_audits) * 100

        # Determine readiness based on compliance percentage
        if compliance_percentage >= 80:
            return f"{self.name} is ready for ISO 14001 certification with a compliance rate of {compliance_percentage:.2f}%."
        else:
            return f"{self.name} is not ready for ISO 14001 certification. Compliance rate is {compliance_percentage:.2f}%."

def main():
    """
    Main function to demonstrate the facility readiness evaluation.
    """
    # Example audits data
    audits_data = [
        {'audit_id': 1, 'compliant': True},
        {'audit_id': 2, 'compliant': False},
        {'audit_id': 3, 'compliant': True},
        {'audit_id': 4, 'compliant': True},
    ]

    # Create a Facility instance
    facility = Facility("iSi Environmental Facility", audits_data)

    # Evaluate readiness
    readiness_status = facility.evaluate_readiness()
    print(readiness_status)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
