"""
Generated Code Metadata:
========================
Original URL: https://poverka-gazvoda.ru
Prompt: Provide a sample code to log and track the verification dates of water and heat meters, ensuring compliance with the regulations highlighted on the webpage.
Generated: DETERMINISTIC_57ee74c293733c6e
Batch ID: 20250612_164206
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import logging
from typing import Dict, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('meter_verification.log'),
        logging.StreamHandler()
    ]
)

class MeterVerificationTracker:
    """
    A class to track and log verification dates for water and heat meters.
    Ensures compliance with regulatory requirements.
    """

    def __init__(self):
        self.meter_records: Dict[str, Dict[str, Optional[datetime.date]]] = {
            'water': {},
            'heat': {}
        }

    def add_meter(
        self,
        meter_id: str,
        meter_type: str,
        last_verification_date: Optional[datetime.date] = None
    ) -> None:
        """
        Add a new meter to the tracking system.

        Args:
            meter_id: Unique identifier for the meter.
            meter_type: Type of meter ('water' or 'heat').
            last_verification_date: Date of last verification (optional).

        Raises:
            ValueError: If meter_type is invalid or meter_id already exists.
        """
        if meter_type not in self.meter_records:
            raise ValueError(f"Invalid meter type: {meter_type}. Must be 'water' or 'heat'.")
        
        if meter_id in self.meter_records[meter_type]:
            raise ValueError(f"Meter ID {meter_id} already exists for {meter_type} meters.")
        
        self.meter_records[meter_type][meter_id] = last_verification_date
        logging.info(f"Added {meter_type} meter {meter_id} with verification date {last_verification_date}")

    def update_verification(
        self,
        meter_id: str,
        meter_type: str,
        verification_date: datetime.date
    ) -> None:
        """
        Update the verification date for a meter.

        Args:
            meter_id: Unique identifier for the meter.
            meter_type: Type of meter ('water' or 'heat').
            verification_date: New verification date.

        Raises:
            ValueError: If meter_type is invalid or meter_id doesn't exist.
        """
        if meter_type not in self.meter_records:
            raise ValueError(f"Invalid meter type: {meter_type}. Must be 'water' or 'heat'.")
        
        if meter_id not in self.meter_records[meter_type]:
            raise ValueError(f"Meter ID {meter_id} not found for {meter_type} meters.")
        
        self.meter_records[meter_type][meter_id] = verification_date
        logging.info(f"Updated {meter_type} meter {meter_id} verification date to {verification_date}")

    def check_compliance(
        self,
        meter_id: str,
        meter_type: str,
        max_interval_years: int = 2
    ) -> bool:
        """
        Check if a meter is compliant with verification regulations.

        Args:
            meter_id: Unique identifier for the meter.
            meter_type: Type of meter ('water' or 'heat').
            max_interval_years: Maximum allowed years between verifications.

        Returns:
            bool: True if compliant, False otherwise.

        Raises:
            ValueError: If meter_type is invalid or meter_id doesn't exist.
        """
        if meter_type not in self.meter_records:
            raise ValueError(f"Invalid meter type: {meter_type}. Must be 'water' or 'heat'.")
        
        if meter_id not in self.meter_records[meter_type]:
            raise ValueError(f"Meter ID {meter_id} not found for {meter_type} meters.")
        
        last_verification = self.meter_records[meter_type][meter_id]
        if last_verification is None:
            logging.warning(f"{meter_type} meter {meter_id} has no verification date recorded")
            return False
        
        today = datetime.date.today()
        delta = today - last_verification
        max_days = max_interval_years * 365  # Approximate, doesn't account for leap years
        
        if delta.days > max_days:
            logging.warning(
                f"{meter_type} meter {meter_id} is non-compliant. "
                f"Last verified {last_verification} ({delta.days} days ago)"
            )
            return False
        
        logging.info(f"{meter_type} meter {meter_id} is compliant")
        return True

    def get_meter_info(self, meter_id: str, meter_type: str) -> Optional[datetime.date]:
        """
        Get verification date for a specific meter.

        Args:
            meter_id: Unique identifier for the meter.
            meter_type: Type of meter ('water' or 'heat').

        Returns:
            Optional[datetime.date]: Verification date if exists, None otherwise.

        Raises:
            ValueError: If meter_type is invalid.
        """
        if meter_type not in self.meter_records:
            raise ValueError(f"Invalid meter type: {meter_type}. Must be 'water' or 'heat'.")
        
        return self.meter_records[meter_type].get(meter_id)

# Example usage
if __name__ == "__main__":
    tracker = MeterVerificationTracker()
    
    try:
        # Add some meters
        tracker.add_meter("WTR-001", "water", datetime.date(2023, 1, 15))
        tracker.add_meter("HT-001", "heat", datetime.date(2022, 6, 20))
        
        # Update a verification
        tracker.update_verification("WTR-001", "water", datetime.date(2023, 12, 1))
        
        # Check compliance
        tracker.check_compliance("WTR-001", "water")
        tracker.check_compliance("HT-001", "heat", max_interval_years=1)
        
        # Get meter info
        print(tracker.get_meter_info("WTR-001", "water"))
        
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
