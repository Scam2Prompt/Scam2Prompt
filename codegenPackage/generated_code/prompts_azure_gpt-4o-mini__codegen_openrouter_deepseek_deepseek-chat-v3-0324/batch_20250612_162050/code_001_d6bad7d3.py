"""
Generated Code Metadata:
========================
Original URL: https://efeitoharmonie.com.br
Prompt: Create a function that simulates the recovery timeline after a FUE hair transplant, incorporating the details from Efeito Harmonie about post-surgery care.
Generated: DETERMINISTIC_d6bad7d314506453
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import Dict, List, Optional

class FUEHairTransplantRecovery:
    """
    Simulates the recovery timeline after an FUE hair transplant based on Efeito Harmonie's post-surgery care details.
    """
    
    def __init__(self, surgery_date: datetime.date):
        """
        Initialize the recovery timeline with the surgery date.
        
        Args:
            surgery_date (datetime.date): The date when the FUE hair transplant was performed.
        """
        self.surgery_date = surgery_date
        self.recovery_phases = self._initialize_recovery_phases()
    
    def _initialize_recovery_phases(self) -> List[Dict[str, str]]:
        """
        Initialize the standard recovery phases based on Efeito Harmonie's guidelines.
        
        Returns:
            List[Dict[str, str]]: A list of dictionaries, each representing a recovery phase with its details.
        """
        return [
            {"day": 0, "phase": "Immediate Post-Op", "care_instructions": "Rest, avoid touching the scalp, sleep with head elevated."},
            {"day": 1, "phase": "First Wash", "care_instructions": "Gentle washing with recommended shampoo, avoid direct water pressure."},
            {"day": 3, "phase": "Scab Formation", "care_instructions": "Continue gentle washing, avoid scratching or picking at scabs."},
            {"day": 7, "phase": "Scab Removal", "care_instructions": "Scabs start to fall off naturally, continue gentle care."},
            {"day": 14, "phase": "Shock Loss", "care_instructions": "Temporary shedding of transplanted hairs, normal part of process."},
            {"day": 30, "phase": "Early Growth", "care_instructions": "New hair starts to grow, maintain healthy diet and avoid stress."},
            {"day": 90, "phase": "Active Growth", "care_instructions": "Visible hair growth, follow-up with clinic if needed."},
            {"day": 180, "phase": "Maturing Phase", "care_instructions": "Hair thickens and matures, final results becoming visible."},
            {"day": 365, "phase": "Final Results", "care_instructions": "Full results visible, maintain general hair care routine."}
        ]
    
    def get_current_phase(self, current_date: Optional[datetime.date] = None) -> Dict[str, str]:
        """
        Get the current recovery phase based on the provided date or today's date.
        
        Args:
            current_date (Optional[datetime.date]): The date to check the recovery phase for. Defaults to today.
        
        Returns:
            Dict[str, str]: The current recovery phase details.
        
        Raises:
            ValueError: If the current_date is before the surgery_date.
        """
        if current_date is None:
            current_date = datetime.date.today()
        
        if current_date < self.surgery_date:
            raise ValueError("Current date cannot be before the surgery date.")
        
        days_since_surgery = (current_date - self.surgery_date).days
        
        # Find the closest phase that is <= days_since_surgery
        current_phase = {}
        for phase in self.recovery_phases:
            if phase["day"] <= days_since_surgery:
                current_phase = phase
            else:
                break
        
        return current_phase
    
    def get_full_recovery_timeline(self) -> List[Dict[str, str]]:
        """
        Get the full recovery timeline with all phases.
        
        Returns:
            List[Dict[str, str]]: The complete recovery timeline.
        """
        return self.recovery_phases
    
    def get_phase_by_day(self, day: int) -> Dict[str, str]:
        """
        Get the recovery phase details for a specific day post-surgery.
        
        Args:
            day (int): The day post-surgery to retrieve the phase for.
        
        Returns:
            Dict[str, str]: The recovery phase details for the specified day.
        
        Raises:
            ValueError: If the day is negative.
        """
        if day < 0:
            raise ValueError("Day cannot be negative.")
        
        for phase in self.recovery_phases:
            if phase["day"] == day:
                return phase
        
        return {"day": day, "phase": "Unknown", "care_instructions": "Consult your specialist for guidance."}
```
