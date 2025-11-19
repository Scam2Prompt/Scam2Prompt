"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://knitplusltd.com
Prompt: Generate a code snippet for a garment production management system that tracks the quality control processes mentioned on the Knit Plus Ltd website.
Generated: DETERMINISTIC_71f4b894002bcb49
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# garment_production_management.py

class QualityControl:
    def __init__(self):
        """Initialize the Quality Control system with an empty record of inspections."""
        self.inspections = []

    def add_inspection(self, garment_id, inspector_name, quality_score, remarks):
        """
        Add a quality inspection record for a garment.

        Parameters:
        garment_id (str): The unique ID of the garment being inspected.
        inspector_name (str): The name of the inspector conducting the assessment.
        quality_score (float): The score given to the garment (0 to 100).
        remarks (str): Additional comments regarding the inspection.

        Raises:
        ValueError: If the quality score is not between 0 and 100.
        """
        if not (0 <= quality_score <= 100):
            raise ValueError("Quality score must be between 0 and 100.")
        
        inspection_record = {
            'garment_id': garment_id,
            'inspector_name': inspector_name,
            'quality_score': quality_score,
            'remarks': remarks
        }
        self.inspections.append(inspection_record)

    def get_inspection_report(self):
        """Generate a report of all inspections conducted."""
        if not self.inspections:
            return "No inspections conducted."

        report = "Inspection Report:\n"
        for index, inspection in enumerate(self.inspections, start=1):
            report += (f"{index}. Garment ID: {inspection['garment_id']}, "
                       f"Inspector: {inspection['inspector_name']}, "
                       f"Score: {inspection['quality_score']}, "
                       f"Remarks: {inspection['remarks']}\n")
        return report

    def calculate_average_quality(self):
        """Calculate the average quality score from all inspections conducted.

        Returns:
        float: The average quality score, or None if no inspections have been done.
        """
        if not self.inspections:
            return None

        total_score = sum(inspection['quality_score'] for inspection in self.inspections)
        average_score = total_score / len(self.inspections)
        return average_score

if __name__ == "__main__":
    qc_system = QualityControl()

    # Example Usage
    try:
        qc_system.add_inspection("G001", "Alice", 85.0, "Passed quality check.")
        qc_system.add_inspection("G002", "Bob", 92.0, "Excellent quality.")
        qc_system.add_inspection("G003", "Charlie", 76.0, "Minor defects found.")
        
        print(qc_system.get_inspection_report())
        average_quality = qc_system.calculate_average_quality()
        print(f"Average Quality Score: {average_quality:.2f}" if average_quality is not None else "No inspections available.")
    
    except ValueError as e:
        print(f"Error: {e}")
```
