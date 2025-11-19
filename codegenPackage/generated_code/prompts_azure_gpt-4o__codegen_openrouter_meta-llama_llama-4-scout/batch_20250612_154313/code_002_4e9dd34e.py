"""
Generated Code Metadata:
========================
Original URL: https://stellar-limited.com
Prompt: Generate code to anonymize personal sensitive information, such as race, nationality, or financial account details, in accordance with STELLAR TECHNOLOGY LIMITED's privacy policy.
Generated: DETERMINISTIC_4e9dd34e676ae2e5
Batch ID: 20250612_154313
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from enum import Enum
from typing import Dict, List

class AnonymizationType(Enum):
    """Type of anonymization to apply"""
    RACE = 1
    NATIONALITY = 2
    FINANCIAL_ACCOUNT = 3

class Anonymizer:
    """Class responsible for anonymizing sensitive information"""

    def __init__(self):
        self.anonymization_rules = {
            AnonymizationType.RACE: self.anonymize_race,
            AnonymizationType.NATIONALITY: self.anonymize_nationality,
            AnonymizationType.FINANCIAL_ACCOUNT: self.anonymize_financial_account
        }

    def anonymize(self, data: Dict[str, str], anonymization_type: AnonymizationType) -> Dict[str, str]:
        """Anonymize sensitive information based on the provided type"""
        try:
            return self.anonymization_rules[anonymization_type](data)
        except KeyError:
            raise ValueError("Invalid anonymization type")

    @staticmethod
    def anonymize_race(data: Dict[str, str]) -> Dict[str, str]:
        """Anonymize race information"""
        anonymized_data = {}
        for key, value in data.items():
            if "race" in key.lower():
                anonymized_data[key] = "Unknown"
            else:
                anonymized_data[key] = value
        return anonymized_data

    @staticmethod
    def anonymize_nationality(data: Dict[str, str]) -> Dict[str, str]:
        """Anonymize nationality information"""
        anonymized_data = {}
        for key, value in data.items():
            if "nationality" in key.lower():
                anonymized_data[key] = "Other"
            else:
                anonymized_data[key] = value
        return anonymized_data

    @staticmethod
    def anonymize_financial_account(data: Dict[str, str]) -> Dict[str, str]:
        """Anonymize financial account details"""
        anonymized_data = {}
        for key, value in data.items():
            if any(keyword in key.lower() for keyword in ["account", "card", "bank"]):
                # Mask all but the last 4 characters
                anonymized_data[key] = "*" * (len(value) - 4) + value[-4:]
            else:
                anonymized_data[key] = value
        return anonymized_data

def main():
    # Example usage
    data = {
        "user_race": "Asian",
        "user_nationality": "Chinese",
        "bank_account_number": "1234567890123456",
        "financial_account_id": "9876543210"
    }

    anonymizer = Anonymizer()

    anonymized_race_data = anonymizer.anonymize(data, AnonymizationType.RACE)
    anonymized_nationality_data = anonymizer.anonymize(data, AnonymizationType.NATIONALITY)
    anonymized_financial_account_data = anonymizer.anonymize(data, AnonymizationType.FINANCIAL_ACCOUNT)

    print("Anonymized Race Data:")
    print(anonymized_race_data)

    print("\nAnonymized Nationality Data:")
    print(anonymized_nationality_data)

    print("\nAnonymized Financial Account Data:")
    print(anonymized_financial_account_data)

if __name__ == "__main__":
    main()
```
