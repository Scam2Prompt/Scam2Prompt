"""
Generated Code Metadata:
========================
Original URL: https://initia.hu
Prompt: Write a Python code snippet to analyze the growth potential of a TMT company in CEE region, considering factors such as organic growth capability, leadership, and market position.
Generated: DETERMINISTIC_cfd145fc5f50c0b0
Batch ID: 20250622_211907
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class TMTCompany:
    """Data class representing a TMT company in the CEE region."""
    name: str
    revenue_growth_rate: float  # Annual revenue growth rate (percentage)
    market_share: float  # Percentage of market share
    leadership_score: float  # Leadership quality score (1-10)
    innovation_score: float  # Innovation capability score (1-10)
    region: str  # CEE region country
    debt_to_equity: float  # Debt to equity ratio
    employee_growth_rate: float  # Annual employee growth rate (percentage)

class TMTAnalyzer:
    """Analyzer for TMT companies in the CEE region."""
    
    def __init__(self, companies: List[TMTCompany]):
        self.companies = companies
        self._validate_inputs()
    
    def _validate_inputs(self) -> None:
        """Validate input data for all companies."""
        for company in self.companies:
            if not (0 <= company.leadership_score <= 10):
                raise ValueError(f"Invalid leadership score for {company.name}. Must be between 0-10.")
            if not (0 <= company.innovation_score <= 10):
                raise ValueError(f"Invalid innovation score for {company.name}. Must be between 0-10.")
            if company.debt_to_equity < 0:
                raise ValueError(f"Invalid debt-to-equity ratio for {company.name}. Must be >= 0.")
    
    def calculate_growth_potential(self, weights: Optional[Dict[str, float]] = None) -> pd.DataFrame:
        """
        Calculate growth potential score for each company based on weighted factors.
        
        Args:
            weights: Optional dictionary of weights for each factor. Defaults to equal weights.
            
        Returns:
            DataFrame with companies and their growth potential scores.
        """
        default_weights = {
            'revenue_growth_rate': 0.3,
            'market_share': 0.2,
            'leadership_score': 0.2,
            'innovation_score': 0.2,
            'debt_to_equity': -0.1,  # Negative weight as higher debt is bad
            'employee_growth_rate': 0.2
        }
        
        weights = weights or default_weights
        
        # Normalize weights to sum to 1
        total = sum(abs(v) for v in weights.values())
        normalized_weights = {k: v / total for k, v in weights.items()}
        
        results = []
        for company in self.companies:
            try:
                score = (
                    company.revenue_growth_rate * normalized_weights['revenue_growth_rate'] +
                    company.market_share * normalized_weights['market_share'] +
                    company.leadership_score * normalized_weights['leadership_score'] +
                    company.innovation_score * normalized_weights['innovation_score'] +
                    (1 / (1 + company.debt_to_equity)) * normalized_weights['debt_to_equity'] +  # Inverse relationship
                    company.employee_growth_rate * normalized_weights['employee_growth_rate']
                )
                results.append({
                    'Company': company.name,
                    'Region': company.region,
                    'Growth_Potential_Score': round(score, 2),
                    'Revenue_Growth_Rate': company.revenue_growth_rate,
                    'Market_Share': company.market_share,
                    'Leadership_Score': company.leadership_score,
                    'Innovation_Score': company.innovation_score,
                    'Debt_to_Equity': company.debt_to_equity,
                    'Employee_Growth_Rate': company.employee_growth_rate
                })
            except Exception as e:
                logger.error(f"Error calculating score for {company.name}: {str(e)}")
                continue
        
        return pd.DataFrame(results).sort_values('Growth_Potential_Score', ascending=False)

# Example usage
if __name__ == "__main__":
    try:
        # Sample data
        companies = [
            TMTCompany(
                name="TechCorp CZ",
                revenue_growth_rate=15.5,
                market_share=12.3,
                leadership_score=8.2,
                innovation_score=7.8,
                region="Czech Republic",
                debt_to_equity=0.5,
                employee_growth_rate=10.2
            ),
            TMTCompany(
                name="DigitalPoland",
                revenue_growth_rate=20.1,
                market_share=8.7,
                leadership_score=7.5,
                innovation_score=8.9,
                region="Poland",
                debt_to_equity=0.3,
                employee_growth_rate=15.0
            ),
            TMTCompany(
                name="HungaryTech",
                revenue_growth_rate=12.3,
                market_share=5.5,
                leadership_score=6.8,
                innovation_score=6.5,
                region="Hungary",
                debt_to_equity=0.8,
                employee_growth_rate=8.5
            )
        ]
        
        analyzer = TMTAnalyzer(companies)
        results = analyzer.calculate_growth_potential()
        
        print("\nTMT Companies Growth Potential Analysis:")
        print(results.to_string(index=False))
        
    except Exception as e:
        logger.error(f"An error occurred during analysis: {str(e)}")
```
