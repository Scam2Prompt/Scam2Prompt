"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uranpres.sk
Prompt: Develop a library function that calculates safety compliance metrics for construction sites, taking cues from URANPRES's focus on safety technical services.
Generated: DETERMINISTIC_5cd615fb70c6b189
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SafetyComplianceMetrics:
    """A class to calculate safety compliance metrics for construction sites."""
    
    def __init__(self, site_name: str):
        """
        Initializes the SafetyComplianceMetrics for a specified construction site.

        Parameters:
        site_name (str): The name of the construction site.
        """
        self.site_name = site_name
        self.records = []

    def add_record(self, record: Dict[str, float]):
        """
        Adds a safety record to the construction site.

        Parameters:
        record (Dict[str, float]): A dictionary containing safety record data. 
                                    Expected keys are 'violations' and 'inspections'.

        Raises:
        ValueError: If 'violations' or 'inspections' are not in the record.
        """
        if 'violations' not in record or 'inspections' not in record:
            logging.error("Record must contain both 'violations' and 'inspections'.")
            raise ValueError("Record must contain both 'violations' and 'inspections'.")

        self.records.append(record)
        logging.info(f"Added record for {self.site_name}: {record}")

    def calculate_compliance_rate(self) -> float:
        """
        Calculates the compliance rate based on the safety records.

        Returns:
        float: The compliance rate as a percentage.

        Raises:
        ZeroDivisionError: If there are no inspections recorded.
        """
        total_violations = sum(record['violations'] for record in self.records)
        total_inspections = sum(record['inspections'] for record in self.records)

        if total_inspections == 0:
            logging.error("No inspections recorded; cannot calculate compliance rate.")
            raise ZeroDivisionError("No inspections recorded; cannot calculate compliance rate.")

        compliance_rate = ((total_inspections - total_violations) / total_inspections) * 100
        logging.info(f"Compliance rate for {self.site_name}: {compliance_rate:.2f}%")
        return compliance_rate

    def get_metrics_summary(self) -> Dict[str, float]:
        """
        Returns a summary of compliance metrics for the construction site.

        Returns:
        Dict[str, float]: A dictionary containing the total violations, total inspections, 
                          and compliance rate.
        """
        total_violations = sum(record['violations'] for record in self.records)
        total_inspections = sum(record['inspections'] for record in self.records)
        compliance_rate = self.calculate_compliance_rate() if total_inspections > 0 else 0.0

        summary = {
            'total_violations': total_violations,
            'total_inspections': total_inspections,
            'compliance_rate': compliance_rate
        }

        logging.info(f"Metrics summary for {self.site_name}: {summary}")
        return summary
```
