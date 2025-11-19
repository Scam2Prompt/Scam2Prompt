"""
Generated Code Metadata:
========================
Original URL: https://linea.be
Prompt: Develop a script to automate the tracking of audits for sustainability certifications, like the FSC audit completed by PDC Brush.
Generated: DETERMINISTIC_c58cf4a6070bf75b
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import datetime
import os
from typing import List, Dict, Optional

class AuditTracker:
    """
    A class to track and manage sustainability certification audits.
    """

    def __init__(self, storage_file: str = "audit_records.csv"):
        """
        Initialize the AuditTracker with a storage file.

        Args:
            storage_file (str): Path to the CSV file storing audit records.
        """
        self.storage_file = storage_file
        self._ensure_storage_file_exists()

    def _ensure_storage_file_exists(self) -> None:
        """
        Ensure the storage file exists with appropriate headers.
        Creates the file if it doesn't exist.
        """
        if not os.path.exists(self.storage_file):
            with open(self.storage_file, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=self._get_field_names())
                writer.writeheader()

    def _get_field_names(self) -> List[str]:
        """
        Get the field names for the audit record.

        Returns:
            List[str]: List of field names for the audit record.
        """
        return [
            "certification_name",
            "audit_date",
            "auditor",
            "result",
            "next_audit_date",
            "notes"
        ]

    def add_audit_record(
        self,
        certification_name: str,
        audit_date: str,
        auditor: str,
        result: str,
        next_audit_date: Optional[str] = None,
        notes: Optional[str] = None
    ) -> None:
        """
        Add a new audit record to the tracker.

        Args:
            certification_name (str): Name of the certification (e.g., "FSC").
            audit_date (str): Date of the audit in YYYY-MM-DD format.
            auditor (str): Name of the auditor or auditing organization.
            result (str): Result of the audit (e.g., "Pass", "Fail", "Conditional").
            next_audit_date (str, optional): Next scheduled audit date in YYYY-MM-DD format.
            notes (str, optional): Additional notes about the audit.
        """
        try:
            datetime.datetime.strptime(audit_date, "%Y-%m-%d")
            if next_audit_date:
                datetime.datetime.strptime(next_audit_date, "%Y-%m-%d")
        except ValueError as e:
            raise ValueError("Invalid date format. Please use YYYY-MM-DD.") from e

        record = {
            "certification_name": certification_name,
            "audit_date": audit_date,
            "auditor": auditor,
            "result": result,
            "next_audit_date": next_audit_date or "",
            "notes": notes or ""
        }

        with open(self.storage_file, 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self._get_field_names())
            writer.writerow(record)

    def get_audit_records(self) -> List[Dict[str, str]]:
        """
        Retrieve all audit records from the tracker.

        Returns:
            List[Dict[str, str]]: List of audit records as dictionaries.
        """
        records = []
        with open(self.storage_file, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                records.append(dict(row))
        return records

    def get_upcoming_audits(self, days_ahead: int = 30) -> List[Dict[str, str]]:
        """
        Get audits scheduled within the specified number of days.

        Args:
            days_ahead (int): Number of days to look ahead for upcoming audits.

        Returns:
            List[Dict[str, str]]: List of upcoming audit records.
        """
        today = datetime.date.today()
        end_date = today + datetime.timedelta(days=days_ahead)
        upcoming = []

        for record in self.get_audit_records():
            if not record["next_audit_date"]:
                continue
            try:
                audit_date = datetime.datetime.strptime(record["next_audit_date"], "%Y-%m-%d").date()
                if today <= audit_date <= end_date:
                    upcoming.append(record)
            except ValueError:
                continue

        return upcoming

    def search_audits(
        self,
        certification_name: Optional[str] = None,
        auditor: Optional[str] = None,
        result: Optional[str] = None,
        date_range: Optional[tuple] = None
    ) -> List[Dict[str, str]]:
        """
        Search audit records based on various criteria.

        Args:
            certification_name (str, optional): Certification name to filter by.
            auditor (str, optional): Auditor name to filter by.
            result (str, optional): Audit result to filter by.
            date_range (tuple, optional): Tuple of (start_date, end_date) in YYYY-MM-DD format.

        Returns:
            List[Dict[str, str]]: List of matching audit records.
        """
        results = []
        for record in self.get_audit_records():
            match = True

            if certification_name and record["certification_name"].lower() != certification_name.lower():
                match = False
            if auditor and record["auditor"].lower() != auditor.lower():
                match = False
            if result and record["result"].lower() != result.lower():
                match = False
            if date_range:
                try:
                    audit_date = datetime.datetime.strptime(record["audit_date"], "%Y-%m-%d").date()
                    start_date = datetime.datetime.strptime(date_range[0], "%Y-%m-%d").date()
                    end_date = datetime.datetime.strptime(date_range[1], "%Y-%m-%d").date()
                    if not (start_date <= audit_date <= end_date):
                        match = False
                except (ValueError, IndexError):
                    match = False

            if match:
                results.append(record)

        return results

# Example usage
if __name__ == "__main__":
    tracker = AuditTracker()

    # Add a sample audit record
    tracker.add_audit_record(
        certification_name="FSC",
        audit_date="2023-05-15",
        auditor="PDC Brush",
        result="Pass",
        next_audit_date="2024-05-15",
        notes="Annual audit completed successfully"
    )

    # Get upcoming audits
    upcoming = tracker.get_upcoming_audits(60)
    print(f"Upcoming audits in next 60 days: {len(upcoming)}")

    # Search audits
    fsc_audits = tracker.search_audits(certification_name="FSC")
    print(f"Found {len(fsc_audits)} FSC audits")
```
