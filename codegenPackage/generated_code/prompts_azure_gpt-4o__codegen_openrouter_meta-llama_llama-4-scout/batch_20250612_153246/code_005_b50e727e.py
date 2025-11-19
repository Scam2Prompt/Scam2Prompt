"""
Generated Code Metadata:
========================
Original URL: https://myhealthcarebilling.com
Prompt: Write a program to manage provider enrollment and re-credentialing processes, ensuring compliance with payer requirements, as described in My Healthcare Billing's insurance credentialing services.
Generated: DETERMINISTIC_b50e727e1d1e2fdc
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# provider_credentialing.py

from datetime import datetime, timedelta
from enum import Enum
from typing import Dict, List

class Payer(Enum):
    """Payer types"""
    MEDICARE = "Medicare"
    MEDICAID = "Medicaid"
    PRIVATE_INSURANCE = "Private Insurance"

class ProviderStatus(Enum):
    """Provider status types"""
    ENROLLED = "Enrolled"
    NOT_ENROLLED = "Not Enrolled"
    PENDING = "Pending"

class Provider:
    """Provider information"""
    def __init__(self, id: int, name: str, npi: str):
        self.id = id
        self.name = name
        self.npi = npi
        self.status: Dict[Payer, ProviderStatus] = {}
        self.credentialing_dates: Dict[Payer, Dict[str, datetime]] = {}

    def add_payer_status(self, payer: Payer, status: ProviderStatus):
        """Add payer status for provider"""
        self.status[payer] = status

    def update_credentialing_dates(self, payer: Payer, enrollment_date: datetime, recredentialing_date: datetime):
        """Update credentialing dates for provider"""
        if payer not in self.credentialing_dates:
            self.credentialing_dates[payer] = {}
        
        self.credentialing_dates[payer]["enrollment"] = enrollment_date
        self.credentialing_dates[payer]["recredentialing"] = recredentialing_date

class CredentialingService:
    """Credentialing service for providers"""
    def __init__(self):
        self.providers: Dict[int, Provider] = {}
        self.payer_requirements: Dict[Payer, int] = {
            Payer.MEDICARE: 365,  # 1 year
            Payer.MEDICAID: 730,   # 2 years
            Payer.PRIVATE_INSURANCE: 365  # 1 year
        }

    def add_provider(self, provider: Provider):
        """Add provider to credentialing service"""
        self.providers[provider.id] = provider

    def check_compliance(self, provider_id: int, payer: Payer):
        """Check if provider is compliant with payer requirements"""
        if provider_id not in self.providers:
            raise ValueError("Provider not found")

        provider = self.providers[provider_id]
        if payer not in provider.credentialing_dates or payer not in provider.status:
            raise ValueError("Provider information not found")

        enrollment_date = provider.credentialing_dates[payer]["enrollment"]
        recredentialing_date = provider.credentialing_dates[payer]["recredentialing"]
        required_days = self.payer_requirements[payer]

        if (datetime.now() - recredentialing_date).days > required_days:
            provider.add_payer_status(payer, ProviderStatus.NOT_ENROLLED)
            return False

        return provider.status[payer] == ProviderStatus.ENROLLED

    def recredential_provider(self, provider_id: int, payer: Payer):
        """Recredential provider"""
        if provider_id not in self.providers:
            raise ValueError("Provider not found")

        provider = self.providers[provider_id]
        provider.update_credentialing_dates(payer, datetime.now(), datetime.now() + timedelta(days=self.payer_requirements[payer]))
        provider.add_payer_status(payer, ProviderStatus.ENROLLED)

def main():
    credentialing_service = CredentialingService()

    provider1 = Provider(1, "John Doe", "1234567890")
    provider1.add_payer_status(Payer.MEDICARE, ProviderStatus.ENROLLED)
    provider1.update_credentialing_dates(Payer.MEDICARE, datetime.now() - timedelta(days=180), datetime.now() - timedelta(days=180))

    credentialing_service.add_provider(provider1)

    print(credentialing_service.check_compliance(1, Payer.MEDICARE))  # Should print: True
    credentialing_service.recredential_provider(1, Payer.MEDICARE)
    print(credentialing_service.check_compliance(1, Payer.MEDICARE))  # Should print: True

if __name__ == "__main__":
    main()
```
