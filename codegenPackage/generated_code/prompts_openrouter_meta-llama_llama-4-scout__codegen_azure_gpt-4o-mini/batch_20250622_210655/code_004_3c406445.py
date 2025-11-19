"""
Generated Code Metadata:
========================
Original URL: https://nakashicnc.com
Prompt: "Develop a simple program to integrate quality control measures into the manufacturing process of 5-axis CNC machines for aerospace and aeronautical applications."
Generated: DETERMINISTIC_3c40644537d448a7
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from datetime import datetime

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class QualityControl:
    def __init__(self):
        self.inspections = []

    def add_inspection(self, part_id, measurement, tolerance):
        """
        Add an inspection record for a part.

        :param part_id: Unique identifier for the part
        :param measurement: Measured value of the part
        :param tolerance: Acceptable tolerance range (tuple of min and max)
        """
        if not self.validate_measurement(measurement, tolerance):
            logging.warning(f"Part {part_id} failed inspection: Measurement {measurement} out of tolerance {tolerance}")
            self.inspections.append((part_id, measurement, False, datetime.now()))
        else:
            logging.info(f"Part {part_id} passed inspection: Measurement {measurement} within tolerance {tolerance}")
            self.inspections.append((part_id, measurement, True, datetime.now()))

    @staticmethod
    def validate_measurement(measurement, tolerance):
        """
        Validate if the measurement is within the specified tolerance.

        :param measurement: Measured value of the part
        :param tolerance: Acceptable tolerance range (tuple of min and max)
        :return: True if measurement is within tolerance, False otherwise
        """
        min_tolerance, max_tolerance = tolerance
        return min_tolerance <= measurement <= max_tolerance

    def generate_report(self):
        """
        Generate a quality control report of all inspections.

        :return: List of inspection records
        """
        report = []
        for inspection in self.inspections:
            part_id, measurement, passed, timestamp = inspection
            report.append({
                'part_id': part_id,
                'measurement': measurement,
                'passed': passed,
                'timestamp': timestamp
            })
        return report

def main():
    # Create a QualityControl instance
    qc = QualityControl()

    # Example inspections
    try:
        qc.add_inspection(part_id="A123", measurement=5.1, tolerance=(4.8, 5.2))
        qc.add_inspection(part_id="A124", measurement=5.5, tolerance=(4.8, 5.2))
        qc.add_inspection(part_id="A125", measurement=4.9, tolerance=(4.8, 5.2))

        # Generate and print the quality control report
        report = qc.generate_report()
        for record in report:
            print(record)

    except Exception as e:
        logging.error(f"An error occurred during quality control processing: {e}")

if __name__ == "__main__":
    main()
```
