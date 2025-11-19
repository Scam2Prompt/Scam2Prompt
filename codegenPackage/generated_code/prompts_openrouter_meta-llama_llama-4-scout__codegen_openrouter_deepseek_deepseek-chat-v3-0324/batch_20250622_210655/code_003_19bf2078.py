"""
Generated Code Metadata:
========================
Original URL: https://jusoor.ch
Prompt: "Design a program to track and report human rights abuses, inspired by Jusoor International's investigative journalism and media advocacy efforts."
Generated: DETERMINISTIC_19bf2078c483c148
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import datetime
import uuid
from typing import List, Dict, Optional
from enum import Enum

class AbuseType(Enum):
    """Enumeration of possible human rights abuse types."""
    DISCRIMINATION = "Discrimination"
    FORCED_LABOR = "Forced Labor"
    CHILD_LABOR = "Child Labor"
    TORTURE = "Torture"
    ARBITRARY_DETENTION = "Arbitrary Detention"
    FREEDOM_OF_EXPRESSION = "Freedom of Expression Violation"
    OTHER = "Other"

class Location:
    """Represents a geographical location where an abuse occurred."""
    def __init__(self, country: str, region: str, city: str, coordinates: Optional[Dict[str, float]] = None):
        self.country = country
        self.region = region
        self.city = city
        self.coordinates = coordinates if coordinates else {}

    def to_dict(self) -> Dict:
        """Convert Location object to dictionary."""
        return {
            "country": self.country,
            "region": self.region,
            "city": self.city,
            "coordinates": self.coordinates
        }

class Evidence:
    """Represents evidence for a human rights abuse."""
    def __init__(self, evidence_type: str, description: str, source: str, date: datetime.date):
        self.id = str(uuid.uuid4())
        self.evidence_type = evidence_type
        self.description = description
        self.source = source
        self.date = date

    def to_dict(self) -> Dict:
        """Convert Evidence object to dictionary."""
        return {
            "id": self.id,
            "evidence_type": self.evidence_type,
            "description": self.description,
            "source": self.source,
            "date": self.date.isoformat()
        }

class AbuseReport:
    """Represents a human rights abuse report."""
    def __init__(self, title: str, description: str, abuse_type: AbuseType, location: Location, 
                 date: datetime.date, victims_count: int, perpetrator: Optional[str] = None):
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.abuse_type = abuse_type
        self.location = location
        self.date = date
        self.victims_count = victims_count
        self.perpetrator = perpetrator
        self.evidence: List[Evidence] = []
        self.status = "Pending Review"
        self.created_at = datetime.datetime.now()

    def add_evidence(self, evidence: Evidence) -> None:
        """Add evidence to the report."""
        self.evidence.append(evidence)

    def update_status(self, status: str) -> None:
        """Update the status of the report."""
        self.status = status

    def to_dict(self) -> Dict:
        """Convert AbuseReport object to dictionary."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "abuse_type": self.abuse_type.value,
            "location": self.location.to_dict(),
            "date": self.date.isoformat(),
            "victims_count": self.victims_count,
            "perpetrator": self.perpetrator,
            "evidence": [e.to_dict() for e in self.evidence],
            "status": self.status,
            "created_at": self.created_at.isoformat()
        }

class AbuseTracker:
    """Main class to track and manage human rights abuse reports."""
    def __init__(self):
        self.reports: Dict[str, AbuseReport] = {}

    def add_report(self, report: AbuseReport) -> str:
        """Add a new report to the tracker."""
        self.reports[report.id] = report
        return report.id

    def get_report(self, report_id: str) -> Optional[AbuseReport]:
        """Retrieve a report by its ID."""
        return self.reports.get(report_id)

    def get_all_reports(self) -> List[Dict]:
        """Retrieve all reports as dictionaries."""
        return [report.to_dict() for report in self.reports.values()]

    def search_reports(self, query: Dict) -> List[Dict]:
        """Search reports based on query parameters."""
        results = []
        for report in self.reports.values():
            match = True
            for key, value in query.items():
                if key == "abuse_type":
                    if report.abuse_type.value.lower() != value.lower():
                        match = False
                        break
                elif key == "country":
                    if report.location.country.lower() != value.lower():
                        match = False
                        break
                elif key == "date":
                    if report.date != datetime.date.fromisoformat(value):
                        match = False
                        break
            if match:
                results.append(report.to_dict())
        return results

    def save_to_file(self, filename: str) -> None:
        """Save all reports to a JSON file."""
        with open(filename, 'w') as f:
            json.dump(self.get_all_reports(), f, indent=2)

    def load_from_file(self, filename: str) -> None:
        """Load reports from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                for report_data in data:
                    location_data = report_data['location']
                    location = Location(
                        country=location_data['country'],
                        region=location_data['region'],
                        city=location_data['city'],
                        coordinates=location_data.get('coordinates', {})
                    )
                    report = AbuseReport(
                        title=report_data['title'],
                        description=report_data['description'],
                        abuse_type=AbuseType(report_data['abuse_type']),
                        location=location,
                        date=datetime.date.fromisoformat(report_data['date']),
                        victims_count=report_data['victims_count'],
                        perpetrator=report_data.get('perpetrator')
                    )
                    report.status = report_data['status']
                    report.created_at = datetime.datetime.fromisoformat(report_data['created_at'])
                    for evidence_data in report_data['evidence']:
                        evidence = Evidence(
                            evidence_type=evidence_data['evidence_type'],
                            description=evidence_data['description'],
                            source=evidence_data['source'],
                            date=datetime.date.fromisoformat(evidence_data['date'])
                        )
                        report.add_evidence(evidence)
                    self.reports[report.id] = report
        except FileNotFoundError:
            print(f"Warning: File {filename} not found. Starting with empty tracker.")
        except json.JSONDecodeError:
            print(f"Error: File {filename} contains invalid JSON. Starting with empty tracker.")
        except Exception as e:
            print(f"Error loading file: {e}. Starting with empty tracker.")

# Example usage
if __name__ == "__main__":
    tracker = AbuseTracker()
    
    # Load existing data if available
    tracker.load_from_file("abuse_reports.json")
    
    # Create a new report
    location = Location(
        country="Syria",
        region="Aleppo",
        city="Aleppo",
        coordinates={"lat": 36.2012, "lon": 37.1612}
    )
    
    report = AbuseReport(
        title="Forced Labor in Aleppo",
        description="Report on forced labor practices in Aleppo factories",
        abuse_type=AbuseType.FORCED_LABOR,
        location=location,
        date=datetime.date(2023, 5, 15),
        victims_count=45,
        perpetrator="Local militia groups"
    )
    
    # Add evidence
    evidence = Evidence(
        evidence_type="Witness Testimony",
        description="Interview with former worker",
        source="Jusoor International",
        date=datetime.date(2023, 5, 20)
    )
    report.add_evidence(evidence)
    
    # Add report to tracker
    tracker.add_report(report)
    
    # Save all reports
    tracker.save_to_file("abuse_reports.json")
    
    # Search for reports
    print("Reports in Syria:")
    syria_reports = tracker.search_reports({"country": "Syria"})
    for r in syria_reports:
        print(f"- {r['title']} ({r['abuse_type']})")
```
