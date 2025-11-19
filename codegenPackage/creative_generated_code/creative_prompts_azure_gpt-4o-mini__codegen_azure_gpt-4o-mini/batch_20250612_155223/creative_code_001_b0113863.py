"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mgel.com.br
Prompt: Write a code snippet that integrates with a compliance management library to ensure adherence to environmental responsibilities in construction projects.
Generated: DETERMINISTIC_b01138635c47f07d
Batch ID: 20250612_155223
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from compliance_management_library import ComplianceManager, ComplianceError

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EnvironmentalComplianceChecker:
    def __init__(self, project_id):
        """
        Initialize the compliance checker for a specific construction project.

        :param project_id: Unique identifier for the construction project.
        """
        self.project_id = project_id
        self.compliance_manager = ComplianceManager()

    def check_compliance(self):
        """
        Check the environmental compliance status of the construction project.

        :return: True if compliant, raises an exception if not compliant.
        """
        try:
            logging.info(f"Checking compliance for project ID: {self.project_id}")
            compliance_status = self.compliance_manager.get_compliance_status(self.project_id)

            if compliance_status.is_compliant:
                logging.info("Project is compliant with environmental responsibilities.")
                return True
            else:
                logging.warning("Project is not compliant with environmental responsibilities.")
                return False

        except ComplianceError as e:
            logging.error(f"Error while checking compliance: {e}")
            raise

    def remediate_compliance_issues(self):
        """
        Remediate any compliance issues identified in the project.

        :return: None
        """
        try:
            logging.info(f"Remediating compliance issues for project ID: {self.project_id}")
            remediation_actions = self.compliance_manager.get_remediation_actions(self.project_id)

            for action in remediation_actions:
                self.compliance_manager.execute_remediation_action(action)
                logging.info(f"Executed remediation action: {action}")

            logging.info("All compliance issues remediated successfully.")

        except ComplianceError as e:
            logging.error(f"Error while remediating compliance issues: {e}")
            raise


if __name__ == "__main__":
    # Example usage
    project_id = "12345"  # Replace with actual project ID
    compliance_checker = EnvironmentalComplianceChecker(project_id)

    if compliance_checker.check_compliance():
        logging.info("No further action needed.")
    else:
        compliance_checker.remediate_compliance_issues()
```
