"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kataskeui.gr
Prompt: Suggest a library or tool to assist in supervising daily construction activities, with features for tracking progress and compliance with issued permits in Greece.
Generated: DETERMINISTIC_8aed71e765c22cbc
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Construction Supervision Management System

This script is a basic implementation of a library for tracking daily construction activities.
It includes features for managing tasks, tracking progress, and ensuring compliance with permits.
The implementation is designed for production use with proper error handling and documentation.

Dependencies:
- pandas: For data handling (install with `pip install pandas`)
"""

import pandas as pd

class ConstructionActivityTracker:
    """
    A class to manage construction activities, track progress, and ensure compliance with permits.
    """

    def __init__(self):
        """Initialize the tracker with an empty DataFrame."""
        self.activities = pd.DataFrame(columns=["date", "activity", "progress", "compliance"])

    def add_activity(self, date: str, activity: str, progress: float, compliance: bool):
        """
        Add a new construction activity to the tracker.

        Parameters:
        date (str): The date of the activity (format: YYYY-MM-DD).
        activity (str): Description of the activity.
        progress (float): Progress percentage (0 to 100).
        compliance (bool): Whether the activity complies with issued permits.

        Raises:
        ValueError: If progress is not between 0 and 100 or the date format is incorrect.
        """
        if not (0 <= progress <= 100):
            raise ValueError("Progress must be between 0 and 100.")
        
        # Validate date format
        try:
            pd.to_datetime(date)
        except ValueError as e:
            raise ValueError("Date format must be YYYY-MM-DD.") from e
        
        # Add the activity
        self.activities = self.activities.append(
            {"date": date, "activity": activity, "progress": progress, "compliance": compliance},
            ignore_index=True
        )

    def get_progress_report(self):
        """
        Generate a report of all activities with their progress and compliance status.

        Returns:
        DataFrame: A DataFrame containing the progress report.
        """
        return self.activities

    def check_compliance(self):
        """
        Check overall compliance of all activities.

        Returns:
        bool: True if all activities are compliant, False otherwise.
        """
        return self.activities['compliance'].all()

# Example usage
if __name__ == "__main__":
    tracker = ConstructionActivityTracker()
    
    try:
        tracker.add_activity("2023-10-01", "Excavation", 50.0, True)
        tracker.add_activity("2023-10-02", "Foundation", 30.0, False)  # Non-compliant activity
        tracker.add_activity("2023-10-03", "Framing", 10.0, True)

        print("Progress Report:")
        print(tracker.get_progress_report())

        is_compliant = tracker.check_compliance()
        print(f"Overall Compliance: {'Compliant' if is_compliant else 'Non-Compliant'}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
