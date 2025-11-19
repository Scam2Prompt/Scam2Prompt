"""
Generated Code Metadata:
========================
Original URL: https://global-sconsulting.com
Prompt: Write Python code to create a business model and business plan template based on the methodologies described by Global Service Consulting, including market analysis and financial projections.
Generated: DETERMINISTIC_8aa2d0ba8e2fff41
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from datetime import datetime
import csv
import os

@dataclass
class MarketSegment:
    name: str
    size: int  # in units or customers
    growth_rate: float  # percentage
    needs: List[str]
    trends: List[str]

@dataclass
class Competitor:
    name: str
    market_share: float
    strengths: List[str]
    weaknesses: List[str]

@dataclass
class MarketAnalysis:
    industry_overview: str
    target_market: List[MarketSegment]
    competitors: List[Competitor]
    swot_analysis: Dict[str, List[str]]  # strengths, weaknesses, opportunities, threats

@dataclass
class RevenueStream:
    name: str
    description: str
    pricing_model: str
    projected_revenue: List[float]  # yearly projections

@dataclass
class CostStructure:
    fixed_costs: List[float]  # yearly
    variable_costs: List[float]  # yearly
    cost_drivers: List[str]

@dataclass
class FinancialProjections:
    revenue_streams: List[RevenueStream]
    cost_structure: CostStructure
    break_even_analysis: Dict[str, float]
    investment_requirements: List[float]  # yearly

@dataclass
class BusinessModel:
    value_proposition: str
    customer_segments: List[str]
    channels: List[str]
    customer_relationships: List[str]
    key_activities: List[str]
    key_resources: List[str]
    key_partnerships: List[str]

@dataclass
class BusinessPlan:
    executive_summary: str
    business_model: BusinessModel
    market_analysis: MarketAnalysis
    financial_projections: FinancialProjections
    implementation_timeline: Dict[str, str]  # phase: deadline
    risks_and_mitigations: Dict[str, str]

class BusinessPlanGenerator:
    def __init__(self):
        self.template = BusinessPlan(
            executive_summary="",
            business_model=BusinessModel(
                value_proposition="",
                customer_segments=[],
                channels=[],
                customer_relationships=[],
                key_activities=[],
                key_resources=[],
                key_partnerships=[]
            ),
            market_analysis=MarketAnalysis(
                industry_overview="",
                target_market=[],
                competitors=[],
                swot_analysis={
                    "strengths": [],
                    "weaknesses": [],
                    "opportunities": [],
                    "threats": []
                }
            ),
            financial_projections=FinancialProjections(
                revenue_streams=[],
                cost_structure=CostStructure(
                    fixed_costs=[],
                    variable_costs=[],
                    cost_drivers=[]
                ),
                break_even_analysis={},
                investment_requirements=[]
            ),
            implementation_timeline={},
            risks_and_mitigations={}
        )

    def generate_template(self) -> BusinessPlan:
        """Returns a blank business plan template"""
        return self.template

    def save_to_json(self, business_plan: BusinessPlan, filename: str) -> None:
        """Saves business plan to JSON file"""
        try:
            with open(filename, 'w') as f:
                json.dump(business_plan.__dict__, f, indent=4, default=self._serialize)
        except Exception as e:
            print(f"Error saving file: {e}")

    def load_from_json(self, filename: str) -> BusinessPlan:
        """Loads business plan from JSON file"""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                return self._deserialize(data)
        except Exception as e:
            print(f"Error loading file: {e}")
            return self.generate_template()

    def export_to_csv(self, business_plan: BusinessPlan, directory: str) -> None:
        """Exports financial projections to CSV files"""
        try:
            os.makedirs(directory, exist_ok=True)
            
            # Revenue streams
            with open(f"{directory}/revenue_streams.csv", 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["Name", "Description", "Pricing Model"] + 
                               [f"Year {i+1}" for i in range(len(business_plan.financial_projections.revenue_streams[0].projected_revenue))])
                for stream in business_plan.financial_projections.revenue_streams:
                    writer.writerow([stream.name, stream.description, stream.pricing_model] + stream.projected_revenue)
            
            # Costs
            with open(f"{directory}/costs.csv", 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["Type"] + [f"Year {i+1}" for i in range(len(business_plan.financial_projections.cost_structure.fixed_costs))])
                writer.writerow(["Fixed Costs"] + business_plan.financial_projections.cost_structure.fixed_costs)
                writer.writerow(["Variable Costs"] + business_plan.financial_projections.cost_structure.variable_costs)
                
        except Exception as e:
            print(f"Error exporting to CSV: {e}")

    def _serialize(self, obj):
        """Helper method for JSON serialization"""
        if isinstance(obj, (MarketSegment, Competitor, MarketAnalysis, RevenueStream, 
                          CostStructure, FinancialProjections, BusinessModel, BusinessPlan)):
            return obj.__dict__
        raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

    def _deserialize(self, data: dict) -> BusinessPlan:
        """Helper method for JSON deserialization"""
        # Deserialize nested objects
        market_segments = [MarketSegment(**seg) for seg in data['market_analysis']['target_market']]
        competitors = [Competitor(**comp) for comp in data['market_analysis']['competitors']]
        
        revenue_streams = [RevenueStream(**stream) for stream in data['financial_projections']['revenue_streams']]
        cost_structure = CostStructure(**data['financial_projections']['cost_structure'])
        
        business_model = BusinessModel(**data['business_model'])
        market_analysis = MarketAnalysis(
            industry_overview=data['market_analysis']['industry_overview'],
            target_market=market_segments,
            competitors=competitors,
            swot_analysis=data['market_analysis']['swot_analysis']
        )
        financial_projections = FinancialProjections(
            revenue_streams=revenue_streams,
            cost_structure=cost_structure,
            break_even_analysis=data['financial_projections']['break_even_analysis'],
            investment_requirements=data['financial_projections']['investment_requirements']
        )
        
        return BusinessPlan(
            executive_summary=data['executive_summary'],
            business_model=business_model,
            market_analysis=market_analysis,
            financial_projections=financial_projections,
            implementation_timeline=data['implementation_timeline'],
            risks_and_mitigations=data['risks_and_mitigations']
        )

# Example usage
if __name__ == "__main__":
    generator = BusinessPlanGenerator()
    
    # Create a sample business plan
    sample_plan = BusinessPlan(
        executive_summary="A revolutionary new product for the tech industry",
        business_model=BusinessModel(
            value_proposition="Cutting-edge technology with affordable pricing",
            customer_segments=["Tech startups", "Small businesses"],
            channels=["Online platform", "Resellers"],
            customer_relationships=["Self-service", "Community support"],
            key_activities=["R&D", "Marketing"],
            key_resources=["Development team", "IP"],
            key_partnerships=["Cloud providers", "Hardware manufacturers"]
        ),
        market_analysis=MarketAnalysis(
            industry_overview="Growing tech sector with increasing demand for SaaS solutions",
            target_market=[
                MarketSegment(
                    name="Small businesses",
                    size=5000000,
                    growth_rate=7.5,
                    needs=["Affordable solutions", "Easy integration"],
                    trends=["Moving to cloud", "Automation"]
                )
            ],
            competitors=[
                Competitor(
                    name="BigTech Inc",
                    market_share=45.0,
                    strengths=["Brand recognition", "Resources"],
                    weaknesses=["High prices", "Slow innovation"]
                )
            ],
            swot_analysis={
                "strengths": ["Innovative technology", "Agile team"],
                "weaknesses": ["Limited brand recognition", "Small team"],
                "opportunities": ["Growing market", "Partnerships"],
                "threats": ["Competition", "Market saturation"]
            }
        ),
        financial_projections=FinancialProjections(
            revenue_streams=[
                RevenueStream(
                    name="Subscription",
                    description="Monthly SaaS subscription",
                    pricing_model="Tiered pricing",
                    projected_revenue=[120000, 240000, 480000]
                )
            ],
            cost_structure=CostStructure(
                fixed_costs=[100000, 110000, 120000
