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
import json

class FacilityReadinessEvaluator:
    """
    A class to evaluate a facility's readiness for ISO 14001 certification
    based on compliance audit data.
    """
    
    def __init__(self, audit_data):
        """
        Initializes the evaluator with audit data.

        Parameters:
        - audit_data (list of dict): Each dict represents an audit with criteria and its compliance status.
        """
        self.audit_data = audit_data

    def evaluate_readiness(self):
        """
        Evaluates the readiness of the facility based on audit data.

        Returns:
        - dict: A summary of readiness, including overall compliance percentage
                and a list of non-compliant criteria.
        """
        if not self.audit_data:
            raise ValueError("Audit data is empty. Cannot evaluate readiness.")
        
        total_criteria = len(self.audit_data)
        if total_criteria == 0:
            raise ValueError("No criteria found in audit data.")
        
        compliant_count = 0
        non_compliant_criteria = []

        for audit in self.audit_data:
            criteria = audit.get('criteria')
            compliance_status = audit.get('compliant', False)

            # Validate data structure
            if criteria is None:
                raise ValueError("Invalid audit data: 'criteria' field is missing.")
            
            # Count compliant criteria and track non-compliant ones
            if compliance_status:
                compliant_count += 1
            else:
                non_compliant_criteria.append(criteria)

        compliance_percentage = (compliant_count / total_criteria) * 100

        return {
            "compliance_percentage": round(compliance_percentage, 2),
            "non_compliant_criteria": non_compliant_criteria
        }


if __name__ == "__main__":
    # Example audit data
    audit_data_json = """
    [
        {"criteria": "Environmental Policy Adherence", "compliant": true},
        {"criteria": "Waste Management Compliance", "compliant": false},
        {"criteria": "Energy Efficiency Standards", "compliant": true},
        {"criteria": "Legal and Regulatory Requirements", "compliant": false}
    ]
    """

    # Load audit data (simulating input from an external source like a database or JSON file)
    try:
        audit_data = json.loads(audit_data_json)
    except json.JSONDecodeError as e:
        print(f"Error loading audit data: {e}")
        exit(1)

    # Instantiate the readiness evaluator and evaluate readiness
    try:
        evaluator = FacilityReadinessEvaluator(audit_data)
        readiness_summary = evaluator.evaluate_readiness()

        # Display the results
        print("Facility ISO 14001 Readiness Evaluation:")
        print(f"Compliance Percentage: {readiness_summary['compliance_percentage']}%")
        print("Non-Compliant Criteria:")
        for criteria in readiness_summary['non_compliant_criteria']:
            print(f"- {criteria}")
    except ValueError as e:
        print(f"Error evaluating readiness: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
