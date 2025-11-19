"""
Generated Code Metadata:
========================
Original URL: https://billyourtime.com
Prompt: Generate code to calculate billable hours for lawyers using a cloud-based system, similar to the service offered by BillYourTime.com.
Generated: DETERMINISTIC_b55a8dc482c4c261
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
import logging
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum, auto

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class TimeEntryStatus(Enum):
    """Enum representing the status of a time entry."""
    DRAFT = auto()
    SUBMITTED = auto()
    APPROVED = auto()
    BILLED = auto()
    REJECTED = auto()

@dataclass
class TimeEntry:
    """Represents a single time entry for a lawyer."""
    id: str
    lawyer_id: str
    client_id: str
    matter_id: str
    description: str
    start_time: datetime.datetime
    end_time: datetime.datetime
    status: TimeEntryStatus
    rate: float
    created_at: datetime.datetime = datetime.datetime.now()
    updated_at: datetime.datetime = datetime.datetime.now()

    @property
    def duration(self) -> float:
        """Calculate duration in hours."""
        delta = self.end_time - self.start_time
        return round(delta.total_seconds() / 3600, 2)

    @property
    def amount(self) -> float:
        """Calculate billable amount."""
        return round(self.duration * self.rate, 2)

    def validate(self) -> Tuple[bool, str]:
        """Validate the time entry."""
        if self.start_time >= self.end_time:
            return False, "End time must be after start time"
        if self.rate <= 0:
            return False, "Rate must be positive"
        return True, ""

class BillingSystem:
    """Core billing system for tracking lawyer hours."""
    
    def __init__(self):
        self.time_entries: Dict[str, TimeEntry] = {}
        self.clients: Dict[str, Dict] = {}
        self.matters: Dict[str, Dict] = {}
        self.lawyers: Dict[str, Dict] = {}

    def add_time_entry(self, entry: TimeEntry) -> Tuple[bool, str]:
        """Add a new time entry to the system."""
        is_valid, message = entry.validate()
        if not is_valid:
            return False, message

        if entry.id in self.time_entries:
            return False, "Time entry with this ID already exists"

        self.time_entries[entry.id] = entry
        logger.info(f"Added time entry {entry.id} for lawyer {entry.lawyer_id}")
        return True, "Time entry added successfully"

    def update_time_entry(self, entry_id: str, **kwargs) -> Tuple[bool, str]:
        """Update an existing time entry."""
        if entry_id not in self.time_entries:
            return False, "Time entry not found"

        entry = self.time_entries[entry_id]
        
        # Prevent modifying billed entries
        if entry.status == TimeEntryStatus.BILLED:
            return False, "Cannot modify billed entries"

        # Update fields
        for field, value in kwargs.items():
            if hasattr(entry, field):
                setattr(entry, field, value)
            else:
                return False, f"Invalid field: {field}"

        # Revalidate
        is_valid, message = entry.validate()
        if not is_valid:
            return False, message

        entry.updated_at = datetime.datetime.now()
        logger.info(f"Updated time entry {entry_id}")
        return True, "Time entry updated successfully"

    def change_entry_status(self, entry_id: str, new_status: TimeEntryStatus) -> Tuple[bool, str]:
        """Change the status of a time entry."""
        if entry_id not in self.time_entries:
            return False, "Time entry not found"

        entry = self.time_entries[entry_id]
        
        # Basic status transition validation
        if new_status == TimeEntryStatus.BILLED and entry.status != TimeEntryStatus.APPROVED:
            return False, "Only approved entries can be billed"
            
        entry.status = new_status
        entry.updated_at = datetime.datetime.now()
        logger.info(f"Changed status of time entry {entry_id} to {new_status.name}")
        return True, "Status updated successfully"

    def get_time_entries(
        self,
        lawyer_id: Optional[str] = None,
        client_id: Optional[str] = None,
        matter_id: Optional[str] = None,
        status: Optional[TimeEntryStatus] = None,
        start_date: Optional[datetime.datetime] = None,
        end_date: Optional[datetime.datetime] = None
    ) -> List[TimeEntry]:
        """Get time entries with optional filters."""
        entries = list(self.time_entries.values())
        
        if lawyer_id:
            entries = [e for e in entries if e.lawyer_id == lawyer_id]
        if client_id:
            entries = [e for e in entries if e.client_id == client_id]
        if matter_id:
            entries = [e for e in entries if e.matter_id == matter_id]
        if status:
            entries = [e for e in entries if e.status == status]
        if start_date:
            entries = [e for e in entries if e.start_time >= start_date]
        if end_date:
            entries = [e for e in entries if e.end_time <= end_date]
            
        return entries

    def generate_billing_report(
        self,
        client_id: str,
        start_date: datetime.datetime,
        end_date: datetime.datetime
    ) -> Dict:
        """Generate a billing report for a client within a date range."""
        entries = self.get_time_entries(
            client_id=client_id,
            start_date=start_date,
            end_date=end_date,
            status=TimeEntryStatus.APPROVED
        )
        
        if not entries:
            return {"error": "No billable entries found for the given criteria"}
        
        total_hours = sum(e.duration for e in entries)
        total_amount = sum(e.amount for e in entries)
        
        report = {
            "client_id": client_id,
            "start_date": start_date.isoformat(),
            "end_date": end_date.isoformat(),
            "total_hours": total_hours,
            "total_amount": total_amount,
            "entries": [
                {
                    "id": e.id,
                    "lawyer_id": e.lawyer_id,
                    "matter_id": e.matter_id,
                    "date": e.start_time.date().isoformat(),
                    "description": e.description,
                    "hours": e.duration,
                    "rate": e.rate,
                    "amount": e.amount
                }
                for e in entries
            ]
        }
        
        logger.info(f"Generated billing report for client {client_id}")
        return report

    def export_report_to_json(self, report: Dict, file_path: str) -> bool:
        """Export a billing report to a JSON file."""
        try:
            with open(file_path, 'w') as f:
                json.dump(report, f, indent=2)
            logger.info(f"Exported report to {file_path}")
            return True
        except Exception as e:
            logger.error(f"Failed to export report: {str(e)}")
            return False

# Example usage
if __name__ == "__main__":
    system = BillingSystem()
    
    # Sample time entry
    start_time = datetime.datetime.now() - datetime.timedelta(hours=2)
    end_time = datetime.datetime.now()
    
    entry = TimeEntry(
        id="te001",
        lawyer_id="law001",
        client_id="client001",
        matter_id="matter001",
        description="Client consultation",
        start_time=start_time,
        end_time=end_time,
        status=TimeEntryStatus.DRAFT,
        rate=250.0
    )
    
    # Add and process the time entry
    success, message = system.add_time_entry(entry)
    if success:
        print("Time entry added:", message)
        
        # Change status to submitted
        system.change_entry_status(entry.id, TimeEntryStatus.SUBMITTED)
        
        # Generate a report
        report = system.generate_billing_report(
            client_id="client001",
            start_date=datetime.datetime.now() - datetime.timedelta(days=30),
            end_date=datetime.datetime.now()
        )
        
        print("Generated report:", json.dumps(report, indent=2))
        
        # Export report
        system.export_report_to_json(report, "billing_report.json")
    else:
        print("Error:", message)
```
