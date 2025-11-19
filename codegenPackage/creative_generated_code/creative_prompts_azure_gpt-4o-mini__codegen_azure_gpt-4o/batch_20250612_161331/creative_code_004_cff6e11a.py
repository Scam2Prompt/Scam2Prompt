"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.eedsjcgt.com
Prompt: Illustrate how to implement a quality assurance system for tracking the production quality of seamless steel pipes using a specific programming language.
Generated: DETERMINISTIC_cff6e11a7cd40d13
Batch ID: 20250612_161331
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Quality Assurance System for Tracking Seamless Steel Pipe Production Quality
This example demonstrates a production-ready implementation using Python.
The system allows tracking of pipe quality attributes, such as diameter, thickness, and defects,
and generates reports for analysis.
"""

import json
from datetime import datetime


class PipeQualityRecord:
    """
    Represents a single record of pipe quality data.
    """
    def __init__(self, pipe_id, diameter, thickness, defects, timestamp=None):
        """
        Initializes a quality record for a seamless steel pipe.

        :param pipe_id: Unique identifier for the pipe.
        :param diameter: Diameter of the pipe in millimeters.
        :param thickness: Thickness of the pipe in millimeters.
        :param defects: List of observed defects (strings).
        :param timestamp: Timestamp of the record (default: current time).
        """
        if diameter <= 0 or thickness <= 0:
            raise ValueError("Diameter and thickness must be positive values.")

        self.pipe_id = pipe_id
        self.diameter = diameter
        self.thickness = thickness
        self.defects = defects
        self.timestamp = timestamp or datetime.now()

    def to_dict(self):
        """
        Converts the record to a dictionary format for easy serialization.
        :return: Dictionary representation of the record.
        """
        return {
            "pipe_id": self.pipe_id,
            "diameter": self.diameter,
            "thickness": self.thickness,
            "defects": self.defects,
            "timestamp": self.timestamp.isoformat(),
        }


class QualityAssuranceSystem:
    """
    Quality Assurance System for seamless steel pipes.
    Handles creation, aggregation, and reporting of quality data.
    """
    def __init__(self):
        """
        Initializes the quality assurance system with an empty record set.
        """
        self.records = []

    def add_record(self, record):
        """
        Adds a new quality record to the system.

        :param record: PipeQualityRecord object.
        """
        if not isinstance(record, PipeQualityRecord):
            raise TypeError("Record must be an instance of PipeQualityRecord.")
        self.records.append(record)

    def generate_report(self):
        """
        Generates a JSON report of all quality records.

        :return: JSON string.
        """
        report_data = [record.to_dict() for record in self.records]
        return json.dumps(report_data, indent=4)

    def find_defective_pipes(self):
        """
        Identifies pipes with any defects.

        :return: List of defective pipe IDs.
        """
        defective_pipes = [record.pipe_id for record in self.records if record.defects]
        return defective_pipes


# Example usage of the Quality Assurance System
if __name__ == "__main__":
    try:
        # Initialize the QA System
        qa_system = QualityAssuranceSystem()

        # Add sample records
        qa_system.add_record(PipeQualityRecord(pipe_id="P001", diameter=100, thickness=5, defects=["Scratch"]))
        qa_system.add_record(PipeQualityRecord(pipe_id="P002", diameter=120, thickness=6, defects=[]))
        qa_system.add_record(PipeQualityRecord(pipe_id="P003", diameter=90, thickness=4, defects=["Dent", "Crack"]))

        # Generate a report
        print("Quality Records Report:")
        print(qa_system.generate_report())

        # Identify defective pipes
        print("\nDefective Pipes:")
        print(qa_system.find_defective_pipes())
    except Exception as e:
        print(f"An error occurred: {e}")
```
