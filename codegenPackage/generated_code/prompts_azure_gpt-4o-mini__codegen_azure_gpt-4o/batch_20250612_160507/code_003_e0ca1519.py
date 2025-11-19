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
import json

class ISO14001ReadinessEvaluator:
    """
    A class to evaluate a facility's readiness for ISO 14001 certification based on compliance audits.
    """

    def __init__(self, audit_data):
        """
        Initialize the evaluator with audit data.

        :param audit_data: List of dictionaries containing audit results.
        """
        self.audit_data = audit_data

    def evaluate_readiness(self):
        """
        Evaluate the facility's readiness for ISO 14001 certification.

        :return: Dictionary containing readiness status and improvement suggestions.
        """
        try:
            # Check if audit data is valid
            if not self.audit_data or not isinstance(self.audit_data, list):
                raise ValueError("Invalid audit data provided.")

            # Initialize readiness metrics
            total_audits = len(self.audit_data)
            compliant_audits = 0
            non_compliance_issues = []

            # Process each audit
            for audit in self.audit_data:
                if audit.get("compliant"):
                    compliant_audits += 1
                else:
                    non_compliance_issues.append(audit.get("issues", "Unknown issues"))

            # Calculate compliance percentage
            compliance_percentage = (compliant_audits / total_audits) * 100 if total_audits > 0 else 0

            # Determine readiness status
            readiness_status = "Ready" if compliance_percentage >= 90 else "Not Ready"

            # Prepare suggestions for improvement
            suggestions = []
            if readiness_status == "Not Ready":
                suggestions.append("Address non-compliance issues.")
                suggestions.append("Conduct additional training for staff.")
                suggestions.append("Implement corrective actions for recurring issues.")

            # Return evaluation results
            return {
                "readiness_status": readiness_status,
                "compliance_percentage": compliance_percentage,
                "non_compliance_issues": non_compliance_issues,
                "suggestions": suggestions
            }

        except Exception as e:
            # Handle unexpected errors
            return {
                "error": str(e),
                "message": "An error occurred while evaluating readiness."
            }


# Example usage
if __name__ == "__main__":
    # Sample audit data (replace with actual data from iSi Environmental's website)
    sample_audit_data = [
        {"compliant": True, "issues": None},
        {"compliant": False, "issues": "Improper waste disposal"},
        {"compliant": True, "issues": None},
        {"compliant": False, "issues": "Incomplete documentation"}
    ]

    # Initialize evaluator
    evaluator = ISO14001ReadinessEvaluator(sample_audit_data)

    # Evaluate readiness
    readiness_report = evaluator.evaluate_readiness()

    # Print results
    print(json.dumps(readiness_report, indent=4))
```
