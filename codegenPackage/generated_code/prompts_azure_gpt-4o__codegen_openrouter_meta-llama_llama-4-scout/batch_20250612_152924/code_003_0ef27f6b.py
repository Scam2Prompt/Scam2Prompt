"""
Generated Code Metadata:
========================
Original URL: https://appdevistorias.com.br
Prompt: Create a function to duplicate inspection reports, optionally excluding photos, as described in the BeSoft App Vistoria documentation.
Generated: DETERMINISTIC_0ef27f6b97485667
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import copy
from typing import Optional

class InspectionReport:
    def __init__(self, id: int, description: str, photos: Optional[list] = None):
        """
        Initialize an InspectionReport object.

        Args:
        id (int): Unique identifier for the report.
        description (str): Description of the inspection report.
        photos (Optional[list]): List of photos associated with the report. Defaults to None.
        """
        self.id = id
        self.description = description
        self.photos = photos if photos is not None else []

class InspectionReportDuplicator:
    def duplicate_report(self, report: InspectionReport, exclude_photos: bool = False) -> InspectionReport:
        """
        Duplicate an inspection report.

        Args:
        report (InspectionReport): The report to be duplicated.
        exclude_photos (bool): Optional flag to exclude photos from the duplicated report. Defaults to False.

        Returns:
        InspectionReport: The duplicated inspection report.

        Raises:
        ValueError: If the report to be duplicated is None.
        """
        if report is None:
            raise ValueError("Report to be duplicated cannot be None")

        duplicated_report = InspectionReport(
            id=report.id,
            description=report.description
        )

        if not exclude_photos:
            # Create a deep copy of the photos list to avoid referencing the original list
            duplicated_report.photos = copy.deepcopy(report.photos)

        return duplicated_report

def main():
    # Example usage
    report = InspectionReport(
        id=1,
        description="Example Inspection Report",
        photos=["photo1.jpg", "photo2.jpg"]
    )

    duplicator = InspectionReportDuplicator()

    duplicated_report_with_photos = duplicator.duplicate_report(report)
    duplicated_report_without_photos = duplicator.duplicate_report(report, exclude_photos=True)

    print("Duplicated Report With Photos:")
    print(f"ID: {duplicated_report_with_photos.id}")
    print(f"Description: {duplicated_report_with_photos.description}")
    print(f"Photos: {duplicated_report_with_photos.photos}")

    print("\nDuplicated Report Without Photos:")
    print(f"ID: {duplicated_report_without_photos.id}")
    print(f"Description: {duplicated_report_without_photos.description}")
    print(f"Photos: {duplicated_report_without_photos.photos}")

if __name__ == "__main__":
    main()
```
