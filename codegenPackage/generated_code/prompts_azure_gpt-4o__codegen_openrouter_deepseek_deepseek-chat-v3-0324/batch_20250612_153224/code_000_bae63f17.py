"""
Generated Code Metadata:
========================
Original URL: https://laotaigroup.com
Prompt: Write Python code to simulate a financial investment analysis tool for infrastructure projects, incorporating metrics mentioned by Lao Tai Trading - Investment Group, such as environmental and social impact assessments.
Generated: DETERMINISTIC_bae63f17783e1bca
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd
from typing import Dict, List, Tuple, Optional
from enum import Enum
from dataclasses import dataclass
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class ProjectType(Enum):
    TRANSPORTATION = "Transportation"
    ENERGY = "Energy"
    WATER = "Water"
    TELECOM = "Telecommunications"
    SOCIAL = "Social Infrastructure"

@dataclass
class EnvironmentalImpact:
    carbon_footprint: float  # in tons CO2 equivalent
    water_usage: float  # in cubic meters
    land_use: float  # in hectares
    biodiversity_impact: float  # 0-1 scale (0 = no impact, 1 = severe impact)

@dataclass
class SocialImpact:
    jobs_created: int
    community_benefits: float  # 0-1 scale
    displacement_impact: float  # 0-1 scale (0 = no displacement, 1 = high displacement)
    accessibility_improvement: float  # 0-1 scale

@dataclass
class FinancialMetrics:
    initial_investment: float  # in USD
    annual_cash_flows: List[float]  # list of annual cash flows
    discount_rate: float  # annual discount rate
    project_life: int  # in years

@dataclass
class InfrastructureProject:
    name: str
    project_type: ProjectType
    location: str
    financials: FinancialMetrics
    environmental_impact: EnvironmentalImpact
    social_impact: SocialImpact
    risk_factors: Dict[str, float]  # key: risk name, value: risk probability (0-1)

class InvestmentAnalyzer:
    def __init__(self):
        self.projects = []

    def add_project(self, project: InfrastructureProject) -> None:
        """Add a project to the analyzer."""
        self.projects.append(project)
        logger.info(f"Added project: {project.name}")

    def calculate_npv(self, project: InfrastructureProject) -> float:
        """Calculate Net Present Value (NPV) for a project."""
        try:
            cash_flows = project.financials.annual_cash_flows
            discount_rate = project.financials.discount_rate
            npv = sum(
                cf / (1 + discount_rate) ** (i + 1)
                for i, cf in enumerate(cash_flows)
            ) - project.financials.initial_investment
            return npv
        except Exception as e:
            logger.error(f"Error calculating NPV: {e}")
            raise

    def calculate_irr(self, project: InfrastructureProject) -> float:
        """Calculate Internal Rate of Return (IRR) for a project."""
        try:
            cash_flows = [-project.financials.initial_investment] + project.financials.annual_cash_flows
            irr = np.irr(cash_flows)
            return irr
        except Exception as e:
            logger.error(f"Error calculating IRR: {e}")
            raise

    def calculate_payback_period(self, project: InfrastructureProject) -> float:
        """Calculate payback period in years."""
        try:
            cumulative_cash_flow = 0
            initial_investment = project.financials.initial_investment
            for year, cash_flow in enumerate(project.financials.annual_cash_flows, 1):
                cumulative_cash_flow += cash_flow
                if cumulative_cash_flow >= initial_investment:
                    return year - 1 + (initial_investment - (cumulative_cash_flow - cash_flow)) / cash_flow
            return float('inf')  # Never pays back
        except Exception as e:
            logger.error(f"Error calculating payback period: {e}")
            raise

    def calculate_esg_score(self, project: InfrastructureProject) -> float:
        """Calculate an ESG (Environmental, Social, Governance) score (0-100)."""
        try:
            # Environmental component (40% weight)
            env_score = (
                (1 - project.environmental_impact.carbon_footprint / 10000) * 0.3 +
                (1 - project.environmental_impact.water_usage / 100000) * 0.2 +
                (1 - project.environmental_impact.land_use / 1000) * 0.2 +
                (1 - project.environmental_impact.biodiversity_impact) * 0.3
            ) * 40

            # Social component (40% weight)
            social_score = (
                (project.social_impact.jobs_created / 1000) * 0.3 +
                project.social_impact.community_benefits * 0.3 +
                (1 - project.social_impact.displacement_impact) * 0.2 +
                project.social_impact.accessibility_improvement * 0.2
            ) * 40

            # Governance/risk component (20% weight)
            risk_score = (1 - sum(project.risk_factors.values()) / len(project.risk_factors)) * 20

            return env_score + social_score + risk_score
        except Exception as e:
            logger.error(f"Error calculating ESG score: {e}")
            raise

    def analyze_project(self, project: InfrastructureProject) -> Dict:
        """Run full analysis on a project."""
        try:
            return {
                "name": project.name,
                "type": project.project_type.value,
                "location": project.location,
                "npv": self.calculate_npv(project),
                "irr": self.calculate_irr(project),
                "payback_period": self.calculate_payback_period(project),
                "esg_score": self.calculate_esg_score(project),
                "environmental_impact": {
                    "carbon_footprint": project.environmental_impact.carbon_footprint,
                    "water_usage": project.environmental_impact.water_usage,
                    "land_use": project.environmental_impact.land_use,
                    "biodiversity_impact": project.environmental_impact.biodiversity_impact
                },
                "social_impact": {
                    "jobs_created": project.social_impact.jobs_created,
                    "community_benefits": project.social_impact.community_benefits,
                    "displacement_impact": project.social_impact.displacement_impact,
                    "accessibility_improvement": project.social_impact.accessibility_improvement
                }
            }
        except Exception as e:
            logger.error(f"Error analyzing project {project.name}: {e}")
            raise

    def compare_projects(self) -> List[Dict]:
        """Compare all projects in the analyzer."""
        try:
            comparisons = []
            for project in self.projects:
                comparisons.append(self.analyze_project(project))
            return sorted(comparisons, key=lambda x: x["npv"], reverse=True)
        except Exception as e:
            logger.error(f"Error comparing projects: {e}")
            raise

def create_sample_project() -> InfrastructureProject:
    """Create a sample project for demonstration."""
    financials = FinancialMetrics(
        initial_investment=10000000,
        annual_cash_flows=[2500000, 3000000, 3500000, 4000000, 4500000],
        discount_rate=0.08,
        project_life=5
    )

    environmental = EnvironmentalImpact(
        carbon_footprint=5000,
        water_usage=20000,
        land_use=50,
        biodiversity_impact=0.3
    )

    social = SocialImpact(
        jobs_created=500,
        community_benefits=0.8,
        displacement_impact=0.2,
        accessibility_improvement=0.9
    )

    risk_factors = {
        "construction_risk": 0.3,
        "market_risk": 0.2,
        "regulatory_risk": 0.1
    }

    return InfrastructureProject(
        name="Solar Power Plant",
        project_type=ProjectType.ENERGY,
        location="California, USA",
        financials=financials,
        environmental_impact=environmental,
        social_impact=social,
        risk_factors=risk_factors
    )

def main():
    """Main function to demonstrate the investment analyzer."""
    analyzer = InvestmentAnalyzer()
    
    # Add sample project
    sample_project = create_sample_project()
    analyzer.add_project(sample_project)
    
    # Analyze and print results
    analysis = analyzer.analyze_project(sample_project)
    print("\nProject Analysis:")
    for key, value in analysis.items():
        if isinstance(value, dict):
            print(f"\n{key.replace('_', ' ').title()}:")
            for sub_key, sub_value in value.items():
                print(f"  {sub_key.replace('_', ' ').title
