"""
Generated Code Metadata:
========================
Original URL: https://schengenapostille.com
Prompt: Create a script to calculate the estimated processing time for Apostille services, factoring in PSA documentation, DFA appointments, and DHL delivery times, as outlined on the Schengen Apostille website.
Generated: DETERMINISTIC_053459e57197c6e7
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from enum import Enum
from typing import Optional, Dict, List

class DocumentType(Enum):
    """Enum representing different types of PSA documents."""
    BIRTH_CERTIFICATE = "Birth Certificate"
    MARRIAGE_CERTIFICATE = "Marriage Certificate"
    DEATH_CERTIFICATE = "Death Certificate"
    CENOMAR = "CENOMAR"
    OTHER = "Other"

class ProcessingStage(Enum):
    """Enum representing different stages in the Apostille process."""
    PSA_VERIFICATION = "PSA Verification"
    DFA_APPOINTMENT = "DFA Appointment"
    DFA_PROCESSING = "DFA Processing"
    DHL_DELIVERY = "DHL Delivery"

class ApostilleCalculator:
    """Class to calculate estimated processing time for Apostille services."""
    
    # Default processing times in days for each stage
    DEFAULT_PROCESSING_TIMES = {
        ProcessingStage.PSA_VERIFICATION: 3,
        ProcessingStage.DFA_APPOINTMENT: 7,
        ProcessingStage.DFA_PROCESSING: 2,
        ProcessingStage.DHL_DELIVERY: 3
    }
    
    # Adjustments for specific document types (days added to default times)
    DOCUMENT_TYPE_ADJUSTMENTS = {
        DocumentType.BIRTH_CERTIFICATE: 0,
        DocumentType.MARRIAGE_CERTIFICATE: 1,
        DocumentType.DEATH_CERTIFICATE: 1,
        DocumentType.CENOMAR: 0,
        DocumentType.OTHER: 2
    }
    
    def __init__(self):
        """Initialize the calculator with default processing times."""
        self.processing_times = self.DEFAULT_PROCESSING_TIMES.copy()
    
    def calculate_processing_time(
        self,
        document_type: DocumentType,
        start_date: datetime.date = datetime.date.today(),
        dfa_appointment_date: Optional[datetime.date] = None,
        express_shipping: bool = False
    ) -> Dict[ProcessingStage, Dict[str, datetime.date]]:
        """
        Calculate the estimated processing timeline for Apostille services.
        
        Args:
            document_type: Type of PSA document being processed
            start_date: Date when processing begins (default: today)
            dfa_appointment_date: Optional specific DFA appointment date
            express_shipping: Whether DHL express shipping is used
            
        Returns:
            Dictionary mapping each ProcessingStage to its start and end dates
        """
        if not isinstance(document_type, DocumentType):
            raise ValueError("Invalid document type provided")
        
        if start_date < datetime.date.today():
            raise ValueError("Start date cannot be in the past")
        
        # Adjust processing times based on document type
        adjusted_times = self._adjust_processing_times(document_type)
        
        # Calculate timeline
        timeline = {}
        current_date = start_date
        
        # PSA Verification stage
        psa_end = self._add_working_days(current_date, adjusted_times[ProcessingStage.PSA_VERIFICATION])
        timeline[ProcessingStage.PSA_VERIFICATION] = {
            "start_date": current_date,
            "end_date": psa_end
        }
        current_date = psa_end + datetime.timedelta(days=1)
        
        # DFA Appointment stage
        if dfa_appointment_date:
            if dfa_appointment_date < current_date:
                raise ValueError("DFA appointment date cannot be before PSA verification completion")
            dfa_start = dfa_appointment_date
        else:
            dfa_start = self._add_working_days(current_date, adjusted_times[ProcessingStage.DFA_APPOINTMENT])
        
        timeline[ProcessingStage.DFA_APPOINTMENT] = {
            "start_date": current_date,
            "end_date": dfa_start
        }
        current_date = dfa_start + datetime.timedelta(days=1)
        
        # DFA Processing stage
        dfa_end = self._add_working_days(current_date, adjusted_times[ProcessingStage.DFA_PROCESSING])
        timeline[ProcessingStage.DFA_PROCESSING] = {
            "start_date": current_date,
            "end_date": dfa_end
        }
        current_date = dfa_end + datetime.timedelta(days=1)
        
        # DHL Delivery stage
        delivery_days = adjusted_times[ProcessingStage.DHL_DELIVERY]
        if express_shipping:
            delivery_days = max(1, delivery_days - 1)  # Express is 1 day faster
            
        dhl_end = self._add_working_days(current_date, delivery_days)
        timeline[ProcessingStage.DHL_DELIVERY] = {
            "start_date": current_date,
            "end_date": dhl_end
        }
        
        return timeline
    
    def _adjust_processing_times(self, document_type: DocumentType) -> Dict[ProcessingStage, int]:
        """Adjust processing times based on document type."""
        adjusted = self.processing_times.copy()
        adjustment = self.DOCUMENT_TYPE_ADJUSTMENTS.get(document_type, 0)
        
        # Apply adjustment to PSA verification time
        adjusted[ProcessingStage.PSA_VERIFICATION] += adjustment
        
        return adjusted
    
    def _add_working_days(self, start_date: datetime.date, days_to_add: int) -> datetime.date:
        """
        Add working days to a date, skipping weekends.
        
        Args:
            start_date: Date to start from
            days_to_add: Number of working days to add
            
        Returns:
            Resulting date after adding working days
        """
        current_date = start_date
        added_days = 0
        
        while added_days < days_to_add:
            current_date += datetime.timedelta(days=1)
            if current_date.weekday() < 5:  # Monday to Friday
                added_days += 1
                
        return current_date
    
    def get_total_processing_days(
        self,
        document_type: DocumentType,
        start_date: datetime.date = datetime.date.today(),
        dfa_appointment_date: Optional[datetime.date] = None,
        express_shipping: bool = False
    ) -> int:
        """
        Calculate total processing days for Apostille services.
        
        Args:
            document_type: Type of PSA document being processed
            start_date: Date when processing begins (default: today)
            dfa_appointment_date: Optional specific DFA appointment date
            express_shipping: Whether DHL express shipping is used
            
        Returns:
            Total number of working days required
        """
        timeline = self.calculate_processing_time(
            document_type=document_type,
            start_date=start_date,
            dfa_appointment_date=dfa_appointment_date,
            express_shipping=express_shipping
        )
        
        first_date = timeline[ProcessingStage.PSA_VERIFICATION]["start_date"]
        last_date = timeline[ProcessingStage.DHL_DELIVERY]["end_date"]
        
        return (last_date - first_date).days + 1  # Inclusive count

# Example usage
if __name__ == "__main__":
    calculator = ApostilleCalculator()
    
    # Calculate for a birth certificate with default settings
    timeline = calculator.calculate_processing_time(DocumentType.BIRTH_CERTIFICATE)
    total_days = calculator.get_total_processing_days(DocumentType.BIRTH_CERTIFICATE)
    
    print("Estimated Apostille Processing Timeline:")
    for stage, dates in timeline.items():
        print(f"{stage.value}: {dates['start_date']} to {dates['end_date']}")
    print(f"Total processing days: {total_days}")
```
