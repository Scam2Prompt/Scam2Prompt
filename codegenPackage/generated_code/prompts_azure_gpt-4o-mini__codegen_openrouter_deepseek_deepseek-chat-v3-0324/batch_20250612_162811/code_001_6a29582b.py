"""
Generated Code Metadata:
========================
Original URL: https://alghanim-capital.com
Prompt: Generate a code snippet that simulates a wealth management portfolio, allowing users to input their financial goals and receive tailored investment recommendations based on Alghanim Capital's wealth management strategies.
Generated: DETERMINISTIC_6a29582b6b3abd2e
Batch ID: 20250612_162811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional

class InvestmentRecommendation:
    """Represents a single investment recommendation with asset details."""
    
    def __init__(self, asset_class: str, allocation: float, rationale: str):
        self.asset_class = asset_class
        self.allocation = allocation
        self.rationale = rationale
    
    def to_dict(self) -> Dict:
        """Convert recommendation to dictionary for serialization."""
        return {
            "asset_class": self.asset_class,
            "allocation": self.allocation,
            "rationale": self.rationale
        }

class WealthPortfolio:
    """Simulates a wealth management portfolio with investment strategies."""
    
    def __init__(self):
        self.risk_profiles = {
            "conservative": {
                "equities": 0.3,
                "fixed_income": 0.5,
                "alternatives": 0.2,
                "rationale": "Preservation of capital with moderate growth"
            },
            "moderate": {
                "equities": 0.5,
                "fixed_income": 0.35,
                "alternatives": 0.15,
                "rationale": "Balanced growth and income"
            },
            "aggressive": {
                "equities": 0.7,
                "fixed_income": 0.2,
                "alternatives": 0.1,
                "rationale": "Maximize long-term growth potential"
            }
        }
    
    def get_recommendations(
        self,
        risk_tolerance: str,
        time_horizon: int,
        initial_investment: float,
        financial_goal: Optional[float] = None
    ) -> List[InvestmentRecommendation]:
        """
        Generate investment recommendations based on client profile.
        
        Args:
            risk_tolerance: One of 'conservative', 'moderate', or 'aggressive'
            time_horizon: Investment period in years
            initial_investment: Initial investment amount
            financial_goal: Optional target amount for goal-based planning
            
        Returns:
            List of InvestmentRecommendation objects
            
        Raises:
            ValueError: If invalid risk tolerance is provided
        """
        if risk_tolerance not in self.risk_profiles:
            raise ValueError(f"Invalid risk tolerance. Must be one of: {list(self.risk_profiles.keys())}")
        
        profile = self.risk_profiles[risk_tolerance]
        recommendations = [
            InvestmentRecommendation(
                asset_class="Equities",
                allocation=profile["equities"],
                rationale=f"Growth potential: {profile['rationale']}"
            ),
            InvestmentRecommendation(
                asset_class="Fixed Income",
                allocation=profile["fixed_income"],
                rationale=f"Stability and income: {profile['rationale']}"
            ),
            InvestmentRecommendation(
                asset_class="Alternative Investments",
                allocation=profile["alternatives"],
                rationale=f"Diversification: {profile['rationale']}"
            )
        ]
        
        # Adjust for time horizon
        if time_horizon < 3:
            for rec in recommendations:
                if rec.asset_class == "Equities":
                    rec.allocation = max(0.1, rec.allocation - 0.2)
                elif rec.asset_class == "Fixed Income":
                    rec.allocation = min(0.7, rec.allocation + 0.2)
        
        # Goal-based adjustment
        if financial_goal and financial_goal > initial_investment:
            required_return = ((financial_goal / initial_investment) ** (1/time_horizon)) - 1
            if required_return > 0.08:  # Threshold for aggressive shift
                for rec in recommendations:
                    if rec.asset_class == "Equities":
                        rec.allocation = min(0.85, rec.allocation + 0.15)
                    elif rec.asset_class == "Fixed Income":
                        rec.allocation = max(0.1, rec.allocation - 0.15)
        
        return recommendations

def main():
    """Interactive portfolio recommendation generator."""
    print("Alghanim Capital Wealth Management Simulator")
    print("-------------------------------------------\n")
    
    portfolio = WealthPortfolio()
    
    try:
        # Get user inputs
        initial_investment = float(input("Enter your initial investment amount: $"))
        time_horizon = int(input("Enter your investment time horizon (years): "))
        risk_tolerance = input("Enter your risk tolerance (conservative/moderate/aggressive): ").lower()
        
        has_goal = input("Do you have a specific financial goal? (y/n): ").lower()
        financial_goal = None
        if has_goal == 'y':
            financial_goal = float(input("Enter your financial goal amount: $"))
        
        # Generate recommendations
        recommendations = portfolio.get_recommendations(
            risk_tolerance=risk_tolerance,
            time_horizon=time_horizon,
            initial_investment=initial_investment,
            financial_goal=financial_goal
        )
        
        # Display results
        print("\nRecommended Portfolio Allocation:")
        print("--------------------------------")
        for rec in recommendations:
            print(f"{rec.asset_class}: {rec.allocation:.0%}")
            print(f"  Rationale: {rec.rationale}\n")
        
        # Option to save results
        save = input("Would you like to save these recommendations? (y/n): ").lower()
        if save == 'y':
            filename = input("Enter filename to save (without extension): ")
            with open(f"{filename}.json", 'w') as f:
                json.dump([rec.to_dict() for rec in recommendations], f, indent=2)
            print("Recommendations saved successfully.")
    
    except ValueError as e:
        print(f"Error: {e}. Please check your inputs and try again.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
