"""
Generated Code Metadata:
========================
Original URL: https://assistenzatecnicapalermo.it
Prompt: Provide an example of code for managing GDPR-compliant data protection protocols for businesses, referencing the privacy-focused services mentioned on Assistenza Tecnica Palermo's site.
Generated: DETERMINISTIC_bc88059300ed39f2
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# gdpr_compliance.py

import logging
from enum import Enum
from typing import Dict, List

# Set up logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ConsentStatus(Enum):
    """Enum for consent status"""
    GIVEN = 1
    WITHDRAWN = 2
    UNKNOWN = 3

class DataSubject:
    """Class representing a data subject"""
    def __init__(self, id: int, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email
        self.consent_status: Dict[str, ConsentStatus] = {}

    def update_consent(self, purpose: str, status: ConsentStatus):
        """Update consent status for a specific purpose"""
        self.consent_status[purpose] = status

class GDPRComplianceManager:
    """Class managing GDPR compliance"""
    def __init__(self):
        self.data_subjects: Dict[int, DataSubject] = {}
        self.purposes: List[str] = []

    def add_data_subject(self, data_subject: DataSubject):
        """Add a data subject to the registry"""
        self.data_subjects[data_subject.id] = data_subject

    def add_purpose(self, purpose: str):
        """Add a purpose for data processing"""
        self.purposes.append(purpose)

    def get_data_subject(self, id: int) -> DataSubject:
        """Retrieve a data subject by ID"""
        return self.data_subjects.get(id)

    def update_consent(self, id: int, purpose: str, status: ConsentStatus):
        """Update consent status for a data subject and purpose"""
        data_subject = self.get_data_subject(id)
        if data_subject:
            data_subject.update_consent(purpose, status)
        else:
            logger.error(f"Data subject with ID {id} not found")

    def notify_data_subjects(self, purpose: str):
        """Notify data subjects about data processing for a specific purpose"""
        for data_subject in self.data_subjects.values():
            if purpose in data_subject.consent_status:
                if data_subject.consent_status[purpose] == ConsentStatus.GIVEN:
                    # Send notification to data subject
                    logger.info(f"Notifying data subject {data_subject.name} about purpose {purpose}")
                else:
                    logger.info(f"Skipping data subject {data_subject.name} due to withdrawn consent")

def main():
    # Create a GDPR compliance manager
    gdpr_manager = GDPRComplianceManager()

    # Add purposes for data processing
    gdpr_manager.add_purpose("Marketing")
    gdpr_manager.add_purpose("Analytics")

    # Create data subjects
    data_subject1 = DataSubject(1, "John Doe", "john.doe@example.com")
    data_subject2 = DataSubject(2, "Jane Doe", "jane.doe@example.com")

    # Add data subjects to the registry
    gdpr_manager.add_data_subject(data_subject1)
    gdpr_manager.add_data_subject(data_subject2)

    # Update consent status
    gdpr_manager.update_consent(1, "Marketing", ConsentStatus.GIVEN)
    gdpr_manager.update_consent(2, "Marketing", ConsentStatus.WITHDRAWN)

    # Notify data subjects about data processing
    gdpr_manager.notify_data_subjects("Marketing")

if __name__ == "__main__":
    main()
```
