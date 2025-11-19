"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poverka-gazvoda.ru
Prompt: Provide a sample code to log and track the verification dates of water and heat meters, ensuring compliance with the regulations highlighted on the webpage.
Generated: DETERMINISTIC_57ee74c293733c6e
Batch ID: 20250612_164206
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import logging

# Configure logging
logging.basicConfig(
    filename="meter_verification.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Custom exception for invalid meter type
class InvalidMeterTypeError(Exception):
    pass

# Supported meter types
VALID_METER_TYPES = {"water", "heat"}

class MeterVerificationTracker:
    """
    A class to log and track the verification dates of water and heat meters.
    """
    def __init__(self):
        # Dictionary to hold meter verification information
        self.verification_records = {}

    def add_meter_verification(self, meter_id, meter_type, verification_date):
        """
        Adds a meter verification record to the tracker.

        Args:
            meter_id (str): A unique identifier for the meter.
            meter_type (str): The type of meter ("water" or "heat").
            verification_date (datetime.date): The date the meter was verified.

        Raises:
            ValueError: If the verification date is not in the datetime.date format.
            InvalidMeterTypeError: If the meter type is invalid.
        """
        if meter_type.lower() not in VALID_METER_TYPES:
            raise InvalidMeterTypeError(f"Invalid meter type: {meter_type}. Supported types are: {VALID_METER_TYPES}")

        if not isinstance(verification_date, datetime.date):
            raise ValueError("verification_date must be a datetime.date object")

        # Add or update the verification record
        self.verification_records[meter_id] = {
            "meter_type": meter_type.lower(),
            "verification_date": verification_date
        }

        # Log the addition or update of the verification record
        logging.info(
            f"Meter verification added/updated: ID={meter_id}, Type={meter_type}, Date={verification_date}"
        )

    def get_meter_verification(self, meter_id):
        """
        Retrieves the verification record for a specific meter.

        Args:
            meter_id (str): The unique identifier for the meter.

        Returns:
            dict: The verification record if found, None otherwise.
        """
        return self.verification_records.get(meter_id, None)

    def list_all_verifications(self):
        """
        Lists all meter verification records.

        Returns:
            dict: All verification records.
        """
        return self.verification_records


# Example usage (uncomment for testing purposes)
# try:
#     tracker = MeterVerificationTracker()
#     tracker.add_meter_verification("water_meter_123", "water", datetime.date(2023, 10, 1))
#     tracker.add_meter_verification("heat_meter_456", "heat", datetime.date(2023, 10, 2))
#     print("Verification Records:")
#     print(tracker.list_all_verifications())
# except ValueError as ve:
#     logging.error(f"ValueError: {ve}")
# except InvalidMeterTypeError as imte:
#     logging.error(f"InvalidMeterTypeError: {imte}")
# except Exception as e:
#     logging.error(f"An unexpected error occurred: {e}")
```
