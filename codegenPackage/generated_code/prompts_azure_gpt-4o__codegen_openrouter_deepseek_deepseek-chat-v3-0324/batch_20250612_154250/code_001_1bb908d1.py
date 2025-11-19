"""
Generated Code Metadata:
========================
Original URL: https://octavepartners.com
Prompt: Generate code to model an investment advisory service that bridges the gap between capital providers and companies requiring funding, as described by Octave Partners.
Generated: DETERMINISTIC_1bb908d1cd040896
Batch ID: 20250612_154250
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# investment_advisory_service.py

from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Optional, Dict
from datetime import datetime
import uuid
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class InvestmentStage(Enum):
    """Enum representing different stages of investment."""
    SEED = auto()
    SERIES_A = auto()
    SERIES_B = auto()
    SERIES_C = auto()
    GROWTH = auto()
    LATE_STAGE = auto()

class IndustrySector(Enum):
    """Enum representing different industry sectors."""
    TECHNOLOGY = auto()
    HEALTHCARE = auto()
    FINANCIAL_SERVICES = auto()
    CONSUMER_GOODS = auto()
    INDUSTRIAL = auto()
    ENERGY = auto()
    REAL_ESTATE = auto()
    OTHER = auto()

@dataclass
class Company:
    """Class representing a company seeking funding."""
    id: str
    name: str
    description: str
    industry_sector: IndustrySector
    funding_required: float
    current_valuation: Optional[float] = None
    investment_stage: InvestmentStage = InvestmentStage.SEED
    financial_statements: Optional[Dict] = None
    created_at: datetime = datetime.now()

    def __post_init__(self):
        if self.funding_required <= 0:
            raise ValueError("Funding required must be positive")
        if self.current_valuation is not None and self.current_valuation <= 0:
            raise ValueError("Current valuation must be positive")

@dataclass
class Investor:
    """Class representing a capital provider."""
    id: str
    name: str
    description: str
    preferred_sectors: List[IndustrySector]
    investment_capacity: float
    min_ticket_size: float
    max_ticket_size: float
    preferred_stages: List[InvestmentStage]
    created_at: datetime = datetime.now()

    def __post_init__(self):
        if self.investment_capacity <= 0:
            raise ValueError("Investment capacity must be positive")
        if self.min_ticket_size <= 0 or self.max_ticket_size <= 0:
            raise ValueError("Ticket sizes must be positive")
        if self.min_ticket_size > self.max_ticket_size:
            raise ValueError("Min ticket size cannot exceed max ticket size")

@dataclass
class InvestmentOpportunity:
    """Class representing a potential investment match."""
    id: str
    company: Company
    investor: Investor
    proposed_amount: float
    match_score: float
    created_at: datetime = datetime.now()

    def __post_init__(self):
        if self.proposed_amount <= 0:
            raise ValueError("Proposed amount must be positive")
        if not 0 <= self.match_score <= 1:
            raise ValueError("Match score must be between 0 and 1")

class InvestmentAdvisoryService:
    """Service that matches companies with investors."""
    
    def __init__(self):
        self.companies: Dict[str, Company] = {}
        self.investors: Dict[str, Investor] = {}
        self.opportunities: Dict[str, InvestmentOpportunity] = {}
    
    def register_company(self, company: Company) -> Company:
        """Register a new company seeking funding."""
        if company.id in self.companies:
            raise ValueError(f"Company with ID {company.id} already exists")
        self.companies[company.id] = company
        logger.info(f"Registered company: {company.name}")
        return company
    
    def register_investor(self, investor: Investor) -> Investor:
        """Register a new investor."""
        if investor.id in self.investors:
            raise ValueError(f"Investor with ID {investor.id} already exists")
        self.investors[investor.id] = investor
        logger.info(f"Registered investor: {investor.name}")
        return investor
    
    def find_matches(self, company_id: str) -> List[InvestmentOpportunity]:
        """Find potential investors for a given company."""
        if company_id not in self.companies:
            raise ValueError(f"Company with ID {company_id} not found")
        
        company = self.companies[company_id]
        matches = []
        
        for investor in self.investors.values():
            # Basic matching criteria
            sector_match = company.industry_sector in investor.preferred_sectors
            stage_match = company.investment_stage in investor.preferred_stages
            amount_match = (
                investor.min_ticket_size <= company.funding_required <= investor.max_ticket_size
            )
            
            if sector_match and stage_match and amount_match:
                # Simple match score calculation (can be enhanced)
                match_score = 0.5  # Base score
                if sector_match:
                    match_score += 0.2
                if stage_match:
                    match_score += 0.2
                if amount_match:
                    match_score += 0.1
                
                opportunity = InvestmentOpportunity(
                    id=str(uuid.uuid4()),
                    company=company,
                    investor=investor,
                    proposed_amount=company.funding_required,
                    match_score=min(match_score, 1.0)  # Cap at 1.0
                )
                matches.append(opportunity)
                self.opportunities[opportunity.id] = opportunity
        
        logger.info(f"Found {len(matches)} matches for company {company.name}")
        return matches
    
    def get_opportunity(self, opportunity_id: str) -> InvestmentOpportunity:
        """Get an investment opportunity by ID."""
        if opportunity_id not in self.opportunities:
            raise ValueError(f"Opportunity with ID {opportunity_id} not found")
        return self.opportunities[opportunity_id]
    
    def get_all_companies(self) -> List[Company]:
        """Get all registered companies."""
        return list(self.companies.values())
    
    def get_all_investors(self) -> List[Investor]:
        """Get all registered investors."""
        return list(self.investors.values())

# Example usage
if __name__ == "__main__":
    service = InvestmentAdvisoryService()
    
    try:
        # Register a company
        company = Company(
            id=str(uuid.uuid4()),
            name="TechStart Inc.",
            description="Innovative AI solutions for healthcare",
            industry_sector=IndustrySector.TECHNOLOGY,
            funding_required=5000000,
            current_valuation=25000000,
            investment_stage=InvestmentStage.SERIES_A
        )
        service.register_company(company)
        
        # Register an investor
        investor = Investor(
            id=str(uuid.uuid4()),
            name="Venture Capital Partners",
            description="Early-stage tech investor",
            preferred_sectors=[IndustrySector.TECHNOLOGY, IndustrySector.HEALTHCARE],
            investment_capacity=100000000,
            min_ticket_size=1000000,
            max_ticket_size=10000000,
            preferred_stages=[InvestmentStage.SEED, InvestmentStage.SERIES_A, InvestmentStage.SERIES_B]
        )
        service.register_investor(investor)
        
        # Find matches
        matches = service.find_matches(company.id)
        for match in matches:
            print(f"Match found with {match.investor.name} (Score: {match.match_score:.2f})")
            
    except Exception as e:
        logger.error(f"An error occurred: {e}")
```
