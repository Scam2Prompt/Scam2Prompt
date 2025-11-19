"""
Generated Code Metadata:
========================
Original URL: https://auqualhairservices.com
Prompt: Generate a Python script to calculate the estimated recovery time for hair transplant procedures based on the session durations provided by Auqual Hair Services.
Generated: DETERMINISTIC_96bf066e9ecf1176
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
from typing import Optional, Dict

class HairTransplantRecoveryCalculator:
    """
    A class to calculate the estimated recovery time for hair transplant procedures
    based on session durations provided by Auqual Hair Services.
    """
    
    # Recovery time multipliers based on session duration (in hours)
    RECOVERY_MULTIPLIERS = {
        'FUE': 1.5,  # Follicular Unit Extraction
        'FUT': 2.0,  # Follicular Unit Transplantation
        'DHI': 1.8   # Direct Hair Implantation
    }
    
    # Base recovery days for each procedure type
    BASE_RECOVERY_DAYS = {
        'FUE': 7,
        'FUT': 14,
        'DHI': 10
    }
    
    def __init__(self):
        """Initialize the recovery calculator."""
        pass
    
    def calculate_recovery_time(
        self,
        procedure_type: str,
        session_duration_hours: float,
        procedure_date: Optional[datetime.date] = None
    ) -> Dict[str, str]:
        """
        Calculate the estimated recovery time for a hair transplant procedure.
        
        Args:
            procedure_type: Type of procedure (FUE, FUT, or DHI)
            session_duration_hours: Duration of the procedure session in hours
            procedure_date: Optional date of the procedure (defaults to today)
            
        Returns:
            Dictionary containing:
                - 'recovery_days': Estimated recovery days
                - 'full_recovery_date': Estimated full recovery date
                - 'procedure_type': The input procedure type
                - 'session_duration': The input session duration
                
        Raises:
            ValueError: If invalid procedure type or negative session duration
        """
        # Validate inputs
        procedure_type = procedure_type.upper()
        if procedure_type not in self.RECOVERY_MULTIPLIERS:
            raise ValueError(f"Invalid procedure type: {procedure_type}. Must be one of {list(self.RECOVERY_MULTIPLIERS.keys())}")
        
        if session_duration_hours < 0:
            raise ValueError("Session duration cannot be negative")
            
        # Set default procedure date to today if not provided
        if procedure_date is None:
            procedure_date = datetime.date.today()
            
        # Calculate recovery days
        multiplier = self.RECOVERY_MULTIPLIERS[procedure_type]
        base_days = self.BASE_RECOVERY_DAYS[procedure_type]
        
        recovery_days = base_days + (session_duration_hours * multiplier)
        recovery_days = int(round(recovery_days))  # Round to nearest whole day
        
        # Calculate full recovery date
        full_recovery_date = procedure_date + datetime.timedelta(days=recovery_days)
        
        return {
            'recovery_days': recovery_days,
            'full_recovery_date': full_recovery_date.strftime('%Y-%m-%d'),
            'procedure_type': procedure_type,
            'session_duration': f"{session_duration_hours} hours"
        }


def main():
    """Example usage of the HairTransplantRecoveryCalculator."""
    calculator = HairTransplantRecoveryCalculator()
    
    try:
        # Example calculation
        result = calculator.calculate_recovery_time(
            procedure_type='FUE',
            session_duration_hours=6.5,
            procedure_date=datetime.date(2023, 11, 15)
        )
        
        print("Hair Transplant Recovery Estimation")
        print("----------------------------------")
        print(f"Procedure Type: {result['procedure_type']}")
        print(f"Session Duration: {result['session_duration']}")
        print(f"Estimated Recovery Days: {result['recovery_days']}")
        print(f"Full Recovery Date: {result['full_recovery_date']}")
        
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
