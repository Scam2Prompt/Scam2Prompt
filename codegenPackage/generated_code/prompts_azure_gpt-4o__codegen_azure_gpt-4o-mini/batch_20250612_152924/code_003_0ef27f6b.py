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
import shutil
import os
from typing import List, Optional

class InspectionReportDuplicator:
    """
    A class to handle the duplication of inspection reports.
    """

    def __init__(self, report_directory: str):
        """
        Initializes the duplicator with the directory containing inspection reports.

        :param report_directory: Path to the directory containing inspection reports.
        """
        self.report_directory = report_directory

    def duplicate_report(self, report_id: str, exclude_photos: Optional[bool] = False) -> str:
        """
        Duplicates an inspection report by its ID.

        :param report_id: The ID of the report to duplicate.
        :param exclude_photos: If True, photos will not be copied.
        :return: The path to the duplicated report.
        """
        original_report_path = os.path.join(self.report_directory, report_id)

        # Check if the original report exists
        if not os.path.exists(original_report_path):
            raise FileNotFoundError(f"Report with ID '{report_id}' does not exist.")

        # Create a new report ID for the duplicated report
        new_report_id = f"{report_id}_copy"
        new_report_path = os.path.join(self.report_directory, new_report_id)

        # Duplicate the report directory
        shutil.copytree(original_report_path, new_report_path, ignore=self._ignore_photos if exclude_photos else None)

        return new_report_path

    @staticmethod
    def _ignore_photos(dir: str, files: List[str]) -> List[str]:
        """
        Helper method to ignore photo files during duplication.

        :param dir: The directory being copied.
        :param files: The list of files in the directory.
        :return: A list of files to ignore.
        """
        # Define photo file extensions to ignore
        photo_extensions = {'.jpg', '.jpeg', '.png', '.gif'}
        return [file for file in files if os.path.splitext(file)[1].lower() in photo_extensions]

# Example usage:
# duplicator = InspectionReportDuplicator('/path/to/reports')
# try:
#     new_report_path = duplicator.duplicate_report('report_123', exclude_photos=True)
#     print(f"Report duplicated successfully: {new_report_path}")
# except Exception as e:
#     print(f"Error duplicating report: {e}")
```
