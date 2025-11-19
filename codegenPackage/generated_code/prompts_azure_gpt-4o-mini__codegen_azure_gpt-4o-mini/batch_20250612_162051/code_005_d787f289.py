"""
Generated Code Metadata:
========================
Original URL: https://www.gbngroup.com.mx
Prompt: Write a code example that implements internal control measures based on GBN Group's recommendations for businesses.
Generated: DETERMINISTIC_d787f28971705645
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from typing import List, Dict, Any

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class InternalControl:
    """
    A class to implement internal control measures based on GBN Group's recommendations.
    """

    def __init__(self):
        self.controls: List[Dict[str, Any]] = []

    def add_control(self, control_name: str, description: str, responsible_party: str) -> None:
        """
        Adds a new internal control measure.

        :param control_name: Name of the control measure
        :param description: Description of the control measure
        :param responsible_party: The party responsible for the control
        """
        control = {
            'name': control_name,
            'description': description,
            'responsible_party': responsible_party,
            'active': True
        }
        self.controls.append(control)
        logging.info(f"Control added: {control_name}")

    def deactivate_control(self, control_name: str) -> None:
        """
        Deactivates an internal control measure.

        :param control_name: Name of the control measure to deactivate
        """
        for control in self.controls:
            if control['name'] == control_name:
                control['active'] = False
                logging.info(f"Control deactivated: {control_name}")
                return
        logging.warning(f"Control not found: {control_name}")

    def get_active_controls(self) -> List[Dict[str, Any]]:
        """
        Retrieves a list of active internal control measures.

        :return: List of active controls
        """
        active_controls = [control for control in self.controls if control['active']]
        logging.info(f"Retrieved {len(active_controls)} active controls")
        return active_controls

    def generate_report(self) -> str:
        """
        Generates a report of all internal controls.

        :return: A string report of all controls
        """
        report_lines = ["Internal Control Report:\n"]
        for control in self.controls:
            status = "Active" if control['active'] else "Inactive"
            report_lines.append(f"Control: {control['name']}, Description: {control['description']}, "
                                f"Responsible Party: {control['responsible_party']}, Status: {status}\n")
        report = ''.join(report_lines)
        logging.info("Report generated")
        return report

# Example usage
if __name__ == "__main__":
    try:
        internal_control_system = InternalControl()
        internal_control_system.add_control("Segregation of Duties", 
                                             "Ensure that no single individual has control over all aspects of any financial transaction.", 
                                             "Finance Department")
        internal_control_system.add_control("Access Control", 
                                             "Limit access to financial systems to authorized personnel only.", 
                                             "IT Department")
        
        # Deactivate a control
        internal_control_system.deactivate_control("Access Control")
        
        # Get active controls
        active_controls = internal_control_system.get_active_controls()
        print(active_controls)
        
        # Generate report
        report = internal_control_system.generate_report()
        print(report)

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
