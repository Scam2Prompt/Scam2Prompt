"""
Generated Code Metadata:
========================
Original URL: https://reckonmexico.com
Prompt: Write code to simulate mergers and acquisitions scenarios, incorporating the financial planning strategies mentioned on Reckon Business Consulting's website.
Generated: DETERMINISTIC_051a8436a0cf9ee0
Batch ID: 20250612_150653
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum, auto
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MergerType(Enum):
    HORIZONTAL = auto()
    VERTICAL = auto()
    CONGLOMERATE = auto()
    MARKET_EXTENSION = auto()

@dataclass
class Company:
    name: str
    valuation: float
    revenue: float
    expenses: float
    assets: float
    liabilities: float
    industry: str

@dataclass
class MergerScenario:
    acquirer: Company
    target: Company
    merger_type: MergerType
    synergy_factor: float
    integration_cost: float

class FinancialPlanner:
    @staticmethod
    def calculate_net_income(company: Company) -> float:
        """Calculate net income (revenue - expenses)"""
        return company.revenue - company.expenses

    @staticmethod
    def calculate_equity(company: Company) -> float:
        """Calculate shareholder equity (assets - liabilities)"""
        return company.assets - company.liabilities

    @staticmethod
    def calculate_post_merger_valuation(scenario: MergerScenario) -> float:
        """Calculate post-merger valuation considering synergies and costs"""
        base_value = scenario.acquirer.valuation + scenario.target.valuation
        synergy_value = (scenario.acquirer.revenue + scenario.target.revenue) * scenario.synergy_factor
        return base_value + synergy_value - scenario.integration_cost

    @staticmethod
    def evaluate_financial_health(company: Company) -> str:
        """Evaluate company's financial health based on key metrics"""
        current_ratio = company.assets / company.liabilities if company.liabilities != 0 else float('inf')
        profit_margin = FinancialPlanner.calculate_net_income(company) / company.revenue if company.revenue != 0 else 0
        
        if current_ratio > 2 and profit_margin > 0.15:
            return "Excellent"
        elif current_ratio > 1.5 and profit_margin > 0.05:
            return "Good"
        elif current_ratio > 1 and profit_margin > 0:
            return "Fair"
        else:
            return "Poor"

class MergerSimulator:
    def __init__(self):
        self.companies: List[Company] = []
        self.scenarios: List[MergerScenario] = []

    def add_company(self, company: Company) -> None:
        """Add a company to the simulation pool"""
        self.companies.append(company)
        logger.info(f"Added company: {company.name}")

    def generate_random_company(self) -> Company:
        """Generate a random company for simulation purposes"""
        industries = ["Tech", "Finance", "Healthcare", "Manufacturing", "Retail"]
        return Company(
            name=f"Company-{random.randint(1000, 9999)}",
            valuation=random.uniform(1_000_000, 100_000_000),
            revenue=random.uniform(500_000, 50_000_000),
            expenses=random.uniform(400_000, 45_000_000),
            assets=random.uniform(1_500_000, 150_000_000),
            liabilities=random.uniform(500_000, 50_000_000),
            industry=random.choice(industries)
        )

    def create_merger_scenario(self, acquirer: Company, target: Company, 
                             merger_type: MergerType) -> MergerScenario:
        """Create a merger scenario with calculated synergy and integration costs"""
        # Determine synergy factor based on merger type
        synergy_factors = {
            MergerType.HORIZONTAL: 0.15,
            MergerType.VERTICAL: 0.10,
            MergerType.CONGLOMERATE: 0.05,
            MergerType.MARKET_EXTENSION: 0.12
        }
        
        synergy_factor = synergy_factors.get(merger_type, 0.05)
        integration_cost = (acquirer.valuation * 0.02) + (target.valuation * 0.03)
        
        scenario = MergerScenario(
            acquirer=acquirer,
            target=target,
            merger_type=merger_type,
            synergy_factor=synergy_factor,
            integration_cost=integration_cost
        )
        
        self.scenarios.append(scenario)
        logger.info(f"Created merger scenario between {acquirer.name} and {target.name}")
        return scenario

    def simulate_merger(self, scenario: MergerScenario) -> Dict[str, float]:
        """Simulate the merger and return financial outcomes"""
        post_merger_valuation = FinancialPlanner.calculate_post_merger_valuation(scenario)
        combined_revenue = scenario.acquirer.revenue + scenario.target.revenue
        combined_expenses = scenario.acquirer.expenses + scenario.target.expenses + scenario.integration_cost
        
        return {
            "post_merger_valuation": post_merger_valuation,
            "combined_revenue": combined_revenue,
            "combined_expenses": combined_expenses,
            "net_income": combined_revenue - combined_expenses,
            "synergy_value": (scenario.acquirer.revenue + scenario.target.revenue) * scenario.synergy_factor,
            "integration_cost": scenario.integration_cost
        }

    def find_potential_targets(self, acquirer: Company, min_valuation: float = 0) -> List[Company]:
        """Find potential acquisition targets based on criteria"""
        return [
            company for company in self.companies 
            if company != acquirer and 
            company.valuation >= min_valuation and
            FinancialPlanner.evaluate_financial_health(company) in ("Good", "Excellent")
        ]

    def analyze_strategic_fit(self, acquirer: Company, target: Company) -> Tuple[float, str]:
        """Analyze strategic fit between two companies"""
        industry_match = 1.0 if acquirer.industry == target.industry else 0.5
        valuation_ratio = min(acquirer.valuation / target.valuation, 2.0) if target.valuation != 0 else 1.0
        health_score = 1.0 if FinancialPlanner.evaluate_financial_health(target) == "Excellent" else 0.7
        
        fit_score = (industry_match * 0.4) + (valuation_ratio * 0.3) + (health_score * 0.3)
        
        if fit_score > 0.8:
            recommendation = "Strong strategic fit - recommended acquisition"
        elif fit_score > 0.6:
            recommendation = "Moderate strategic fit - consider acquisition"
        else:
            recommendation = "Poor strategic fit - not recommended"
        
        return fit_score, recommendation

def main():
    simulator = MergerSimulator()
    
    # Create sample companies
    for _ in range(10):
        simulator.add_company(simulator.generate_random_company())
    
    # Select acquirer and target
    acquirer = simulator.companies[0]
    targets = simulator.find_potential_targets(acquirer, min_valuation=5_000_000)
    
    if not targets:
        logger.warning("No suitable targets found for acquisition")
        return
    
    target = targets[0]
    
    # Analyze strategic fit
    fit_score, recommendation = simulator.analyze_strategic_fit(acquirer, target)
    logger.info(f"Strategic Fit Score: {fit_score:.2f}")
    logger.info(f"Recommendation: {recommendation}")
    
    # Create and simulate merger scenario
    scenario = simulator.create_merger_scenario(
        acquirer=acquirer,
        target=target,
        merger_type=MergerType.HORIZONTAL
    )
    
    results = simulator.simulate_merger(scenario)
    
    # Display results
    logger.info("\nMerger Simulation Results:")
    for key, value in results.items():
        logger.info(f"{key.replace('_', ' ').title()}: ${value:,.2f}")

if __name__ == "__main__":
    main()
```
