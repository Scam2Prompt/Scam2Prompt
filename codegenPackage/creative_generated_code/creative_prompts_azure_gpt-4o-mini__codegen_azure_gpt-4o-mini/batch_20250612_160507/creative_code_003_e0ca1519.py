"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://isienvironmental.com
Prompt: Develop a code snippet that evaluates a facility's readiness for ISO 14001 certification based on the compliance audits mentioned on iSi Environmental's website.
Generated: DETERMINISTIC_e0ca1519e5993904
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Facility:
    def __init__(self, name: str):
        """
        Initializes a Facility instance with a given name.

        :param name: The name of the facility.
        """
        self.name = name
        self.compliance_audits = []

    def add_audit(self, audit_score: float):
        """
        Adds a compliance audit score to the facility.

        :param audit_score: The score of the compliance audit (0-100).
        :raises ValueError: If the audit score is not within the valid range.
        """
        if not (0 <= audit_score <= 100):
            raise ValueError("Audit score must be between 0 and 100.")
        self.compliance_audits.append(audit_score)

    def evaluate_readiness(self) -> str:
        """
        Evaluates the facility's readiness for ISO 14001 certification based on
        the average compliance audit scores.

        :return: A message indicating the readiness status.
        """
        if not self.compliance_audits:
            return "No audits conducted. Cannot evaluate readiness."

        average_score = sum(self.compliance_audits) / len(self.compliance_audits)
        
        # ISO 14001 readiness criteria
        if average_score >= 80:
            return f"{self.name} is ready for ISO 14001 certification."
        elif average_score >= 50:
            return f"{self.name} needs improvement to reach ISO 14001 certification."
        else:
            return f"{self.name} is not ready for ISO 14001 certification."

def main():
    """
    Main function to demonstrate the Facility class functionality.
    This should be the entry point of the program.
    """
    # Example facility
    facility = Facility("GreenTech Manufacturing")

    # Adding compliance audit scores
    try:
        facility.add_audit(85)
        facility.add_audit(90)
        facility.add_audit(75)
    except ValueError as e:
        print(f"Error adding audit: {e}")

    # Evaluating readiness for ISO 14001 certification
    readiness_status = facility.evaluate_readiness()
    print(readiness_status)

if __name__ == "__main__":
    main()
```
