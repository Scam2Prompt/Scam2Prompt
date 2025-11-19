"""
Generated Code Metadata:
========================
Original URL: https://poverka-gazvoda.ru
Prompt: Create a Python script that simulates the process of scheduling meter verification for water, gas, and heat meters, including fields for customer details, meter type, and verification frequency (e.g., every four years for heat meters).
Generated: DETERMINISTIC_c2d7cc55eca94373
Batch ID: 20250612_154454
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from enum import Enum
from typing import Dict

class MeterType(str, Enum):
    """Enum for meter types."""
    WATER = "water"
    GAS = "gas"
    HEAT = "heat"

class MeterVerificationScheduler:
    """Class to schedule meter verification."""

    def __init__(self):
        self.verification_frequencies = {
            MeterType.WATER: timedelta(days=365 * 5),  # every 5 years
            MeterType.GAS: timedelta(days=365 * 4),  # every 4 years
            MeterType.HEAT: timedelta(days=365 * 4),  # every 4 years
        }

    def schedule_verification(self, customer_details: Dict, meter_type: MeterType, installation_date: datetime) -> Dict:
        """
        Schedule meter verification.

        Args:
        - customer_details (Dict): Customer details.
        - meter_type (MeterType): Type of meter.
        - installation_date (datetime): Date of meter installation.

        Returns:
        - Dict: Scheduled verification details.
        """
        if meter_type not in self.verification_frequencies:
            raise ValueError("Invalid meter type")

        verification_date = installation_date + self.verification_frequencies[meter_type]
        scheduled_verification = {
            "customer_details": customer_details,
            "meter_type": meter_type,
            "installation_date": installation_date,
            "verification_date": verification_date,
        }
        return scheduled_verification

    def update_verification_date(self, scheduled_verification: Dict, new_installation_date: datetime) -> Dict:
        """
        Update verification date after meter replacement.

        Args:
        - scheduled_verification (Dict): Scheduled verification details.
        - new_installation_date (datetime): New installation date.

        Returns:
        - Dict: Updated scheduled verification details.
        """
        meter_type = scheduled_verification["meter_type"]
        verification_date = new_installation_date + self.verification_frequencies[meter_type]
        scheduled_verification["installation_date"] = new_installation_date
        scheduled_verification["verification_date"] = verification_date
        return scheduled_verification


def main():
    scheduler = MeterVerificationScheduler()

    customer_details = {
        "name": "John Doe",
        "address": "123 Main St",
    }

    installation_date = datetime(2022, 1, 1)
    meter_type = MeterType.HEAT

    try:
        scheduled_verification = scheduler.schedule_verification(customer_details, meter_type, installation_date)
        print("Scheduled Verification:")
        print(f"Customer: {scheduled_verification['customer_details']['name']}")
        print(f"Meter Type: {scheduled_verification['meter_type']}")
        print(f"Installation Date: {scheduled_verification['installation_date']}")
        print(f"Verification Date: {scheduled_verification['verification_date']}")

        new_installation_date = datetime(2024, 1, 1)
        updated_scheduled_verification = scheduler.update_verification_date(scheduled_verification, new_installation_date)
        print("\nUpdated Scheduled Verification:")
        print(f"Customer: {updated_scheduled_verification['customer_details']['name']}")
        print(f"Meter Type: {updated_scheduled_verification['meter_type']}")
        print(f"Installation Date: {updated_scheduled_verification['installation_date']}")
        print(f"Verification Date: {updated_scheduled_verification['verification_date']}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
