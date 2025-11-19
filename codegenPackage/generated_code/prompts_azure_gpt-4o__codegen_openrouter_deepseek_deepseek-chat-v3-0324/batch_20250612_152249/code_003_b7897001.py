"""
Generated Code Metadata:
========================
Original URL: https://creocollective.io
Prompt: Write code to optimize inbound lead processes for marketing campaigns, inspired by the demand generation strategies used by Creo Collective.
Generated: DETERMINISTIC_b7897001dcc31644
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from datetime import datetime
from typing import List, Dict, Optional
import logging
from abc import ABC, abstractmethod
import re
from enum import Enum

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class LeadStatus(Enum):
    NEW = "New"
    QUALIFIED = "Qualified"
    CONTACTED = "Contacted"
    CONVERTED = "Converted"
    UNQUALIFIED = "Unqualified"

class LeadSource(Enum):
    WEBSITE = "Website"
    SOCIAL = "Social Media"
    EVENT = "Event"
    REFERRAL = "Referral"
    PAID_AD = "Paid Ad"

class Lead:
    def __init__(
        self,
        email: str,
        first_name: str,
        last_name: str,
        company: str,
        source: LeadSource,
        status: LeadStatus = LeadStatus.NEW,
        timestamp: Optional[datetime] = None,
        metadata: Optional[Dict] = None
    ):
        self.email = self._validate_email(email)
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.source = source
        self.status = status
        self.timestamp = timestamp if timestamp else datetime.now()
        self.metadata = metadata if metadata else {}

    def _validate_email(self, email: str) -> str:
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email format")
        return email

    def update_status(self, new_status: LeadStatus) -> None:
        self.status = new_status
        logger.info(f"Lead {self.email} status updated to {new_status.value}")

    def add_metadata(self, key: str, value: str) -> None:
        self.metadata[key] = value
        logger.info(f"Metadata added for lead {self.email}: {key}={value}")

class LeadProcessor(ABC):
    @abstractmethod
    def process(self, lead: Lead) -> None:
        pass

class QualificationProcessor(LeadProcessor):
    def process(self, lead: Lead) -> None:
        if self._is_qualified(lead):
            lead.update_status(LeadStatus.QUALIFIED)
        else:
            lead.update_status(LeadStatus.UNQUALIFIED)

    def _is_qualified(self, lead: Lead) -> bool:
        # Basic qualification criteria
        return (
            bool(lead.company) and
            len(lead.email) > 0 and
            lead.source != LeadSource.PAID_AD  # Example rule
        )

class LeadRouter:
    def __init__(self, processors: List[LeadProcessor]):
        self.processors = processors

    def route_lead(self, lead: Lead) -> None:
        for processor in self.processors:
            try:
                processor.process(lead)
            except Exception as e:
                logger.error(f"Error processing lead {lead.email}: {str(e)}")

class CampaignAnalyzer:
    def __init__(self, leads: List[Lead]):
        self.leads = leads

    def get_conversion_rate(self) -> float:
        converted = sum(1 for lead in self.leads if lead.status == LeadStatus.CONVERTED)
        total = len(self.leads)
        return converted / total if total > 0 else 0.0

    def get_source_performance(self) -> Dict[LeadSource, float]:
        source_counts = {}
        source_conversions = {}

        for lead in self.leads:
            source_counts[lead.source] = source_counts.get(lead.source, 0) + 1
            if lead.status == LeadStatus.CONVERTED:
                source_conversions[lead.source] = source_conversions.get(lead.source, 0) + 1

        return {
            source: source_conversions.get(source, 0) / count
            for source, count in source_counts.items()
        }

class LeadStorage:
    def __init__(self, file_path: str = "leads.csv"):
        self.file_path = file_path

    def save_leads(self, leads: List[Lead]) -> None:
        try:
            df = pd.DataFrame([self._lead_to_dict(lead) for lead in leads])
            df.to_csv(self.file_path, index=False)
            logger.info(f"Successfully saved {len(leads)} leads to {self.file_path}")
        except Exception as e:
            logger.error(f"Error saving leads: {str(e)}")
            raise

    def load_leads(self) -> List[Lead]:
        try:
            df = pd.read_csv(self.file_path)
            leads = [self._dict_to_lead(row) for _, row in df.iterrows()]
            logger.info(f"Successfully loaded {len(leads)} leads from {self.file_path}")
            return leads
        except Exception as e:
            logger.error(f"Error loading leads: {str(e)}")
            raise

    def _lead_to_dict(self, lead: Lead) -> Dict:
        return {
            "email": lead.email,
            "first_name": lead.first_name,
            "last_name": lead.last_name,
            "company": lead.company,
            "source": lead.source.value,
            "status": lead.status.value,
            "timestamp": lead.timestamp.isoformat(),
            "metadata": str(lead.metadata)
        }

    def _dict_to_lead(self, data: Dict) -> Lead:
        return Lead(
            email=data["email"],
            first_name=data["first_name"],
            last_name=data["last_name"],
            company=data["company"],
            source=LeadSource(data["source"]),
            status=LeadStatus(data["status"]),
            timestamp=datetime.fromisoformat(data["timestamp"]),
            metadata=eval(data["metadata"]) if data["metadata"] else {}
        )

class LeadEnrichmentService:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def enrich_lead(self, lead: Lead) -> None:
        # Simulate API call to enrichment service
        try:
            # In a real implementation, this would call an external API
            lead.add_metadata("enriched", "true")
            lead.add_metadata("company_size", "100-500")
            lead.add_metadata("industry", "Technology")
            logger.info(f"Lead {lead.email} enriched successfully")
        except Exception as e:
            logger.error(f"Error enriching lead {lead.email}: {str(e)}")
            raise

def main():
    # Example usage
    try:
        # Create sample leads
        leads = [
            Lead(
                email="john@example.com",
                first_name="John",
                last_name="Doe",
                company="Acme Inc",
                source=LeadSource.WEBSITE
            ),
            Lead(
                email="jane@example.com",
                first_name="Jane",
                last_name="Smith",
                company="Tech Corp",
                source=LeadSource.SOCIAL
            )
        ]

        # Set up processing pipeline
        processors = [
            QualificationProcessor(),
            # Add other processors as needed
        ]
        router = LeadRouter(processors)

        # Process leads
        for lead in leads:
            router.route_lead(lead)

        # Analyze campaign performance
        analyzer = CampaignAnalyzer(leads)
        logger.info(f"Conversion rate: {analyzer.get_conversion_rate():.2%}")
        logger.info(f"Source performance: {analyzer.get_source_performance()}")

        # Store leads
        storage = LeadStorage()
        storage.save_leads(leads)

    except Exception as e:
        logger.error(f"Error in lead processing: {str(e)}")

if __name__ == "__main__":
    main()
```
