"""
Generated Code Metadata:
========================
Original URL: https://vfmadvisory.com
Prompt: "Write a financial model for a Public-Private Partnership (PPP) project in Bangladesh, including feasibility study and transaction advisory services."
Generated: DETERMINISTIC_0037d25d59143a02
Batch ID: 20250622_210703
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
from datetime import datetime, timedelta
from typing import Dict, List, Tuple, Optional

class PPPFinancialModel:
    """
    Financial model for Public-Private Partnership (PPP) projects in Bangladesh.
    Includes feasibility study and transaction advisory components.
    """
    
    def __init__(self, project_name: str, project_duration: int, currency: str = "BDT"):
        """
        Initialize the PPP financial model.
        
        Args:
            project_name: Name of the PPP project
            project_duration: Duration in years
            currency: Currency used (default: BDT - Bangladeshi Taka)
        """
        self.project_name = project_name
        self.project_duration = project_duration
        self.currency = currency
        self.cashflows = pd.DataFrame()
        self.financial_metrics = {}
        self.feasibility_study = {}
        self.transaction_advisory = {}
        
    def add_cashflows(self, inflows: Dict[str, List[float]], outflows: Dict[str, List[float]]) -> None:
        """
        Add cash inflows and outflows to the model.
        
        Args:
            inflows: Dictionary of inflow categories with annual values
            outflows: Dictionary of outflow categories with annual values
        """
        years = list(range(1, self.project_duration + 1))
        self.cashflows["Year"] = years
        
        # Add inflows
        for category, values in inflows.items():
            if len(values) != self.project_duration:
                raise ValueError(f"Inflow '{category}' must have {self.project_duration} values")
            self.cashflows[f"Inflow_{category}"] = values
            
        # Add outflows
        for category, values in outflows.items():
            if len(values) != self.project_duration:
                raise ValueError(f"Outflow '{category}' must have {self.project_duration} values")
            self.cashflows[f"Outflow_{category}"] = values
            
        # Calculate net cash flow
        total_inflows = self.cashflows.filter(like="Inflow_").sum(axis=1)
        total_outflows = self.cashflows.filter(like="Outflow_").sum(axis=1)
        self.cashflows["Net_Cash_Flow"] = total_inflows - total_outflows
        
    def calculate_financial_metrics(self, discount_rate: float) -> None:
        """
        Calculate key financial metrics for the project.
        
        Args:
            discount_rate: Discount rate for NPV calculation
        """
        if self.cashflows.empty:
            raise ValueError("Cashflows must be added before calculating metrics")
            
        # Calculate cumulative cash flow
        self.cashflows["Cumulative_Cash_Flow"] = self.cashflows["Net_Cash_Flow"].cumsum()
        
        # Calculate NPV
        discounted_cashflows = [
            cf / ((1 + discount_rate) ** year) 
            for year, cf in enumerate(self.cashflows["Net_Cash_Flow"], 1)
        ]
        self.financial_metrics["NPV"] = sum(discounted_cashflows)
        
        # Calculate IRR (approximation)
        try:
            self.financial_metrics["IRR"] = np.irr(self.cashflows["Net_Cash_Flow"].tolist())
        except:
            self.financial_metrics["IRR"] = None
            
        # Calculate payback period
        positive_cashflow_year = self.cashflows[self.cashflows["Cumulative_Cash_Flow"] > 0].index.min()
        if positive_cashflow_year is not None:
            last_negative_year = positive_cashflow_year - 1
            last_negative_cumulative = self.cashflows.loc[last_negative_year, "Cumulative_Cash_Flow"]
            positive_cashflow = self.cashflows.loc[positive_cashflow_year, "Net_Cash_Flow"]
            payback_period = last_negative_year + (-last_negative_cumulative / positive_cashflow)
            self.financial_metrics["Payback_Period"] = payback_period
        else:
            self.financial_metrics["Payback_Period"] = None
            
    def conduct_feasibility_study(
        self,
        market_demand: Dict[str, float],
        technical_viability: Dict[str, bool],
        legal_compliance: Dict[str, bool],
        social_impact: Dict[str, float]
    ) -> None:
        """
        Conduct feasibility study for the PPP project.
        
        Args:
            market_demand: Market demand indicators
            technical_viability: Technical feasibility indicators
            legal_compliance: Legal compliance indicators
            social_impact: Social impact indicators
        """
        self.feasibility_study = {
            "market_demand": market_demand,
            "technical_viability": technical_viability,
            "legal_compliance": legal_compliance,
            "social_impact": social_impact,
            "overall_feasibility": self._assess_overall_feasibility(
                market_demand, technical_viability, legal_compliance, social_impact
            )
        }
        
    def _assess_overall_feasibility(
        self,
        market_demand: Dict[str, float],
        technical_viability: Dict[str, bool],
        legal_compliance: Dict[str, bool],
        social_impact: Dict[str, float]
    ) -> bool:
        """Assess overall project feasibility based on study components."""
        # Market demand threshold
        demand_score = sum(market_demand.values()) / len(market_demand)
        
        # Technical viability (all must be True)
        tech_viable = all(technical_viability.values())
        
        # Legal compliance (all must be True)
        legal_compliant = all(legal_compliance.values())
        
        # Social impact threshold
        social_score = sum(social_impact.values()) / len(social_impact)
        
        return (demand_score > 0.7 and tech_viable and legal_compliant and social_score > 0.6)
        
    def provide_transaction_advisory(
        self,
        procurement_strategy: str,
        risk_allocation: Dict[str, str],
        contract_terms: Dict[str, str],
        financing_structure: Dict[str, float]
    ) -> None:
        """
        Provide transaction advisory services for the PPP project.
        
        Args:
            procurement_strategy: Selected procurement approach
            risk_allocation: Risk allocation between parties
            contract_terms: Key contract terms
            financing_structure: Financing mix (debt/equity/etc.)
        """
        self.transaction_advisory = {
            "procurement_strategy": procurement_strategy,
            "risk_allocation": risk_allocation,
            "contract_terms": contract_terms,
            "financing_structure": financing_structure,
            "recommendations": self._generate_recommendations(
                procurement_strategy, risk_allocation, contract_terms, financing_structure
            )
        }
        
    def _generate_recommendations(
        self,
        procurement_strategy: str,
        risk_allocation: Dict[str, str],
        contract_terms: Dict[str, str],
        financing_structure: Dict[str, float]
    ) -> List[str]:
        """Generate recommendations based on transaction advisory inputs."""
        recommendations = []
        
        # Check financing structure balance
        if financing_structure.get("debt", 0) > 0.7:
            recommendations.append("Consider reducing debt ratio to below 70% for better financial stability")
            
        # Check risk allocation fairness
        if sum(1 for v in risk_allocation.values() if v == "Public") / len(risk_allocation) > 0.6:
            recommendations.append("Re-evaluate risk allocation to ensure fair distribution between public and private partners")
            
        # Check contract term completeness
        required_terms = ["duration", "termination", "performance_metrics"]
        if not all(term in contract_terms for term in required_terms):
            recommendations.append("Ensure all key contract terms are included: duration, termination, and performance metrics")
            
        return recommendations
        
    def generate_report(self) -> Dict[str, Dict]:
        """
        Generate comprehensive project report with all analysis.
        
        Returns:
            Dictionary containing all project analysis results
        """
        return {
            "project_info": {
                "name": self.project_name,
                "duration": self.project_duration,
                "currency": self.currency
            },
            "cashflows": self.cashflows.to_dict(),
            "financial_metrics": self.financial_metrics,
            "feasibility_study": self.feasibility_study,
            "transaction_advisory": self.transaction_advisory
        }


# Example usage
if __name__ == "__main__":
    # Initialize model for a 10-year PPP project
    ppp_model = PPPFinancialModel("Dhaka Metro Rail PPP", 10)
    
    # Add cashflows
    inflows = {
        "ticket_sales": [5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500],
        "advertising": [200, 220, 240, 260,
