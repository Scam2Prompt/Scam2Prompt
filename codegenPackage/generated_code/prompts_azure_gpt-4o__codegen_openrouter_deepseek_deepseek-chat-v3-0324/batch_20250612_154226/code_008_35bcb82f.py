"""
Generated Code Metadata:
========================
Original URL: https://claimlink.io
Prompt: Create a script to filter and categorize legal leads by case type (e.g., car accidents, bicycle accidents) and client readiness, as described by ClaimLink Legal Solutions.
Generated: DETERMINISTIC_35bcb82f1746fb55
Batch ID: 20250612_154226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
from enum import Enum
from typing import List, Dict, Optional
from dataclasses import dataclass
from datetime import datetime
import logging

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('legal_leads_processor.log'),
        logging.StreamHandler()
    ]
)

class CaseType(Enum):
    """Enumeration of possible case types."""
    CAR_ACCIDENT = "Car Accident"
    BICYCLE_ACCIDENT = "Bicycle Accident"
    SLIP_FALL = "Slip and Fall"
    WORK_INJURY = "Work Injury"
    MEDICAL_MALPRACTICE = "Medical Malpractice"
    OTHER = "Other"

class ReadinessLevel(Enum):
    """Enumeration of client readiness levels."""
    READY_TO_SIGN = "Ready to Sign"
    NEEDS_FOLLOW_UP = "Needs Follow-up"
    INFORMATION_GATHERING = "Information Gathering"
    NOT_INTERESTED = "Not Interested"

@dataclass
class LegalLead:
    """Data class representing a legal lead."""
    lead_id: str
    name: str
    contact_info: str
    case_type: CaseType
    readiness: ReadinessLevel
    incident_date: Optional[datetime] = None
    notes: Optional[str] = None

class LegalLeadProcessor:
    """Processor for filtering and categorizing legal leads."""
    
    def __init__(self):
        self.leads: List[LegalLead] = []
    
    def load_leads_from_csv(self, file_path: str) -> None:
        """Load leads from a CSV file.
        
        Args:
            file_path: Path to the CSV file containing lead data.
            
        Raises:
            FileNotFoundError: If the file does not exist.
            ValueError: If the file is malformed.
        """
        try:
            with open(file_path, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        lead = self._parse_lead_row(row)
                        self.leads.append(lead)
                    except (ValueError, KeyError) as e:
                        logging.warning(f"Skipping malformed row: {row}. Error: {e}")
        except FileNotFoundError:
            logging.error(f"File not found: {file_path}")
            raise
        except Exception as e:
            logging.error(f"Error reading file: {e}")
            raise ValueError(f"Failed to read file: {file_path}") from e
    
    def _parse_lead_row(self, row: Dict[str, str]) -> LegalLead:
        """Parse a single row from the CSV into a LegalLead object.
        
        Args:
            row: Dictionary representing a single row from the CSV.
            
        Returns:
            LegalLead: Parsed lead object.
            
        Raises:
            ValueError: If required fields are missing or invalid.
        """
        try:
            incident_date = (
                datetime.strptime(row['incident_date'], '%Y-%m-%d')
                if 'incident_date' in row and row['incident_date'] else None
            )
            
            return LegalLead(
                lead_id=row['lead_id'],
                name=row['name'],
                contact_info=row['contact_info'],
                case_type=CaseType(row['case_type']),
                readiness=ReadinessLevel(row['readiness']),
                incident_date=incident_date,
                notes=row.get('notes', None)
            )
        except KeyError as e:
            raise ValueError(f"Missing required field: {e}") from e
        except ValueError as e:
            raise ValueError(f"Invalid field value: {e}") from e
    
    def filter_leads(
        self,
        case_types: Optional[List[CaseType]] = None,
        readiness_levels: Optional[List[ReadinessLevel]] = None,
        min_incident_date: Optional[datetime] = None,
        max_incident_date: Optional[datetime] = None
    ) -> List[LegalLead]:
        """Filter leads based on specified criteria.
        
        Args:
            case_types: List of case types to include. If None, all case types are included.
            readiness_levels: List of readiness levels to include. If None, all levels are included.
            min_incident_date: Minimum incident date to include. If None, no minimum date filter.
            max_incident_date: Maximum incident date to include. If None, no maximum date filter.
            
        Returns:
            List of filtered LegalLead objects.
        """
        filtered_leads = self.leads.copy()
        
        if case_types is not None:
            filtered_leads = [lead for lead in filtered_leads if lead.case_type in case_types]
        
        if readiness_levels is not None:
            filtered_leads = [lead for lead in filtered_leads if lead.readiness in readiness_levels]
        
        if min_incident_date is not None:
            filtered_leads = [
                lead for lead in filtered_leads
                if lead.incident_date and lead.incident_date >= min_incident_date
            ]
        
        if max_incident_date is not None:
            filtered_leads = [
                lead for lead in filtered_leads
                if lead.incident_date and lead.incident_date <= max_incident_date
            ]
        
        return filtered_leads
    
    def categorize_leads(self) -> Dict[str, Dict[str, List[LegalLead]]]:
        """Categorize leads by case type and readiness level.
        
        Returns:
            Dictionary with case types as top-level keys and readiness levels as second-level keys,
            containing lists of leads for each category.
        """
        categorized = {}
        
        for case_type in CaseType:
            case_leads = [lead for lead in self.leads if lead.case_type == case_type]
            readiness_dict = {}
            
            for readiness in ReadinessLevel:
                readiness_dict[readiness.value] = [
                    lead for lead in case_leads if lead.readiness == readiness
                ]
            
            categorized[case_type.value] = readiness_dict
        
        return categorized
    
    def export_to_csv(self, file_path: str, leads: List[LegalLead]) -> None:
        """Export leads to a CSV file.
        
        Args:
            file_path: Path to save the CSV file.
            leads: List of leads to export.
            
        Raises:
            IOError: If there's an error writing to the file.
        """
        try:
            with open(file_path, mode='w', encoding='utf-8', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=[
                    'lead_id', 'name', 'contact_info', 'case_type', 'readiness',
                    'incident_date', 'notes'
                ])
                writer.writeheader()
                
                for lead in leads:
                    writer.writerow({
                        'lead_id': lead.lead_id,
                        'name': lead.name,
                        'contact_info': lead.contact_info,
                        'case_type': lead.case_type.value,
                        'readiness': lead.readiness.value,
                        'incident_date': lead.incident_date.strftime('%Y-%m-%d') if lead.incident_date else '',
                        'notes': lead.notes or ''
                    })
        except IOError as e:
            logging.error(f"Error writing to file {file_path}: {e}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        processor = LegalLeadProcessor()
        
        # Load leads from CSV
        processor.load_leads_from_csv('legal_leads.csv')
        
        # Filter for car accident leads ready to sign
        filtered_leads = processor.filter_leads(
            case_types=[CaseType.CAR_ACCIDENT],
            readiness_levels=[ReadinessLevel.READY_TO_SIGN]
        )
        
        # Export filtered leads
        processor.export_to_csv('filtered_leads.csv', filtered_leads)
        
        # Get categorized leads
        categorized = processor.categorize_leads()
        logging.info(f"Found {len(filtered_leads)} car accident leads ready to sign")
        
    except Exception as e:
        logging.error(f"An error occurred: {e}", exc_info=True)
```
