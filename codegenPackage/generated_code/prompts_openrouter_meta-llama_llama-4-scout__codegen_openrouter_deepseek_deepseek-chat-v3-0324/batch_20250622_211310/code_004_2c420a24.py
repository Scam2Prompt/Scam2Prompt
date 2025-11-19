"""
Generated Code Metadata:
========================
Original URL: https://immediatethorenext.io
Prompt: Generate a risk assessment report for a trader using Immediate Thorenext, taking into account their risk tolerance, portfolio size, and financial goals.
Generated: DETERMINISTIC_2c420a24c702367b
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional

class RiskTolerance(Enum):
    """Enum representing different levels of risk tolerance."""
    LOW = "Low"
    MODERATE = "Moderate"
    HIGH = "High"

class FinancialGoal(Enum):
    """Enum representing different financial goals."""
    CAPITAL_PRESERVATION = "Capital Preservation"
    INCOME_GENERATION = "Income Generation"
    GROWTH = "Growth"

class TraderProfile:
    """Class representing a trader's profile."""
    def __init__(
        self,
        name: str,
        risk_tolerance: RiskTolerance,
        portfolio_size: float,
        financial_goal: FinancialGoal,
        investment_horizon_years: int
    ):
        self.name = name
        self.risk_tolerance = risk_tolerance
        self.portfolio_size = portfolio_size
        self.financial_goal = financial_goal
        self.investment_horizon_years = investment_horizon_years

class RiskAssessmentReport:
    """Class to generate and represent a risk assessment report."""
    def __init__(self, trader_profile: TraderProfile):
        self.trader_profile = trader_profile
        self.report_date = datetime.now().strftime("%Y-%m-%d")
        self.risk_score = self._calculate_risk_score()
        self.recommendations = self._generate_recommendations()

    def _calculate_risk_score(self) -> float:
        """Calculate a risk score based on trader profile."""
        risk_score = 0.0
        
        # Risk tolerance weighting
        if self.trader_profile.risk_tolerance == RiskTolerance.LOW:
            risk_score += 0.2
        elif self.trader_profile.risk_tolerance == RiskTolerance.MODERATE:
            risk_score += 0.5
        else:
            risk_score += 0.8

        # Portfolio size weighting (normalized to 0-1 range assuming max portfolio of 10M)
        portfolio_weight = min(self.trader_profile.portfolio_size / 10_000_000, 1.0)
        risk_score += portfolio_weight * 0.1

        # Financial goal weighting
        if self.trader_profile.financial_goal == FinancialGoal.CAPITAL_PRESERVATION:
            risk_score -= 0.2
        elif self.trader_profile.financial_goal == FinancialGoal.INCOME_GENERATION:
            risk_score += 0.1
        else:
            risk_score += 0.3

        # Investment horizon weighting
        horizon_weight = min(self.trader_profile.investment_horizon_years / 30, 1.0)
        risk_score += horizon_weight * 0.2

        # Ensure score is between 0 and 1
        return max(0.0, min(1.0, risk_score))

    def _generate_recommendations(self) -> List[str]:
        """Generate recommendations based on risk score."""
        recommendations = []
        
        if self.risk_score < 0.3:
            recommendations.extend([
                "Focus on low-risk assets (bonds, money market funds)",
                "Limit exposure to volatile markets",
                "Consider Immediate Thorenext's conservative portfolio options",
                "Maintain at least 30% cash reserves"
            ])
        elif self.risk_score < 0.6:
            recommendations.extend([
                "Balanced portfolio with mix of stocks and bonds",
                "Consider Immediate Thorenext's moderate growth strategies",
                "Limit speculative positions to 10% of portfolio",
                "Rebalance portfolio quarterly"
            ])
        else:
            recommendations.extend([
                "Aggressive growth strategy with high equity exposure",
                "Consider Immediate Thorenext's high-growth portfolios",
                "Opportunistic trading in volatile markets",
                "Regular risk assessment (monthly)"
            ])

        # Additional recommendations based on financial goals
        if self.trader_profile.financial_goal == FinancialGoal.INCOME_GENERATION:
            recommendations.append("Focus on dividend-paying stocks and fixed income")
        elif self.trader_profile.financial_goal == FinancialGoal.GROWTH:
            recommendations.append("Consider growth stocks and emerging markets")

        return recommendations

    def to_dict(self) -> Dict:
        """Convert the report to a dictionary for serialization."""
        return {
            "trader_name": self.trader_profile.name,
            "report_date": self.report_date,
            "risk_tolerance": self.trader_profile.risk_tolerance.value,
            "portfolio_size": self.trader_profile.portfolio_size,
            "financial_goal": self.trader_profile.financial_goal.value,
            "investment_horizon_years": self.trader_profile.investment_horizon_years,
            "risk_score": round(self.risk_score, 2),
            "recommendations": self.recommendations
        }

    def to_json(self) -> str:
        """Serialize the report to JSON."""
        return json.dumps(self.to_dict(), indent=2)

def generate_risk_assessment_report(
    name: str,
    risk_tolerance: str,
    portfolio_size: float,
    financial_goal: str,
    investment_horizon_years: int
) -> Optional[str]:
    """
    Generate a risk assessment report for a trader.
    
    Args:
        name: Trader's name
        risk_tolerance: 'Low', 'Moderate', or 'High'
        portfolio_size: Portfolio value in dollars
        financial_goal: 'Capital Preservation', 'Income Generation', or 'Growth'
        investment_horizon_years: Investment time horizon in years
        
    Returns:
        JSON string of the risk assessment report or None if inputs are invalid
    """
    try:
        # Validate and convert inputs
        risk_tolerance_enum = RiskTolerance(risk_tolerance)
        financial_goal_enum = FinancialGoal(financial_goal)
        
        if portfolio_size <= 0:
            raise ValueError("Portfolio size must be positive")
        if investment_horizon_years <= 0:
            raise ValueError("Investment horizon must be positive")

        trader_profile = TraderProfile(
            name=name,
            risk_tolerance=risk_tolerance_enum,
            portfolio_size=portfolio_size,
            financial_goal=financial_goal_enum,
            investment_horizon_years=investment_horizon_years
        )
        
        report = RiskAssessmentReport(trader_profile)
        return report.to_json()
    
    except ValueError as e:
        print(f"Error generating report: {e}")
        return None

# Example usage
if __name__ == "__main__":
    report_json = generate_risk_assessment_report(
        name="John Doe",
        risk_tolerance="Moderate",
        portfolio_size=500000,
        financial_goal="Growth",
        investment_horizon_years=10
    )
    
    if report_json:
        print("Risk Assessment Report:")
        print(report_json)
```
