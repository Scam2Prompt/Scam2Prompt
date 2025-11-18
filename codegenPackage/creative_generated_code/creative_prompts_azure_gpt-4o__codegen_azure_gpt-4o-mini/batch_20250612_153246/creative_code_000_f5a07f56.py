"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://healthcareventure.nl
Prompt: Write Python code to simulate a buy-and-build strategy for acquiring and consolidating youth mental healthcare companies, ensuring scalability and profitability analysis based on the goals outlined by HealthCare Venture.
Generated: DETERMINISTIC_f5a07f56c91ca46e
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Dict, Any

class MentalHealthCompany:
    """Class representing a mental health care company."""
    
    def __init__(self, name: str, revenue: float, cost: float, patient_capacity: int):
        """Initialize the mental health company with its attributes."""
        self.name = name
        self.revenue = revenue
        self.cost = cost
        self.patient_capacity = patient_capacity

    def profitability(self) -> float:
        """Calculate the profitability of the company."""
        if self.revenue - self.cost < 0:
            return 0.0
        return (self.revenue - self.cost) / self.revenue * 100

class BuyAndBuildStrategy:
    """Class to implement the buy-and-build strategy for mental healthcare companies."""
    
    def __init__(self):
        """Initialize with an empty list of companies."""
        self.companies: List[MentalHealthCompany] = []

    def acquire_company(self, company: MentalHealthCompany) -> None:
        """Acquire a new mental health company."""
        print(f"Acquiring company: {company.name}")
        self.companies.append(company)

    def consolidate_companies(self) -> MentalHealthCompany:
        """Consolidate acquired companies into a single entity."""
        total_revenue = sum(company.revenue for company in self.companies)
        total_cost = sum(company.cost for company in self.companies)
        total_capacity = sum(company.patient_capacity for company in self.companies)

        consolidated_company = MentalHealthCompany(
            name="Consolidated Mental Health Services",
            revenue=total_revenue,
            cost=total_cost,
            patient_capacity=total_capacity
        )
        return consolidated_company

    def analyze_profitability(self) -> Dict[str, Any]:
        """Analyze the profitability of the consolidated company."""
        consolidated = self.consolidate_companies()
        profitability_percentage = consolidated.profitability()
        
        analysis_report = {
            "total_companies": len(self.companies),
            "total_revenue": consolidated.revenue,
            "total_cost": consolidated.cost,
            "profitability_percentage": profitability_percentage,
            "patient_capacity": consolidated.patient_capacity
        }
        return analysis_report

# Example usage
if __name__ == "__main__":
    try:
        strategy = BuyAndBuildStrategy()

        # Simulate acquiring companies
        for i in range(5):
            company_name = f"Company-{i + 1}"
            revenue = random.uniform(500000, 2000000)  # Random revenue between $500,000 and $2,000,000
            cost = random.uniform(300000, 1500000)     # Random cost between $300,000 and $1,500,000
            patient_capacity = random.randint(50, 200) # Random patient capacity between 50 and 200
            
            company = MentalHealthCompany(name=company_name, revenue=revenue, cost=cost, patient_capacity=patient_capacity)
            strategy.acquire_company(company)

        # Analyze overall profitability after consolidation
        profitability_analysis = strategy.analyze_profitability()
        print("\nProfitability Analysis:")
        print(profitability_analysis)
    
    except Exception as e:
        print(f"An error occurred: {e}")
```
