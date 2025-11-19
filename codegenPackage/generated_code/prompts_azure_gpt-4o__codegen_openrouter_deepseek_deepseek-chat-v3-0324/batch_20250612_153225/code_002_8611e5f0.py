"""
Generated Code Metadata:
========================
Original URL: https://universalsolar1.com
Prompt: Generate code to model the financial profitability of solar projects using Universal Solar's approach to financing partnerships with major investment groups worldwide.
Generated: DETERMINISTIC_8611e5f05ae84c36
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Solar Project Financial Model for Universal Solar's Financing Partnerships

This module models the financial profitability of solar projects using Universal Solar's
approach to financing partnerships with major investment groups worldwide.
"""

import numpy as np
import pandas as pd
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from enum import Enum, auto


class ProjectType(Enum):
    """Types of solar projects supported by the model."""
    UTILITY_SCALE = auto()
    COMMERCIAL = auto()
    RESIDENTIAL = auto()
    INDUSTRIAL = auto()


class FinancingType(Enum):
    """Types of financing arrangements available."""
    EQUITY = auto()
    DEBT = auto()
    LEASE = auto()
    PPA = auto()  # Power Purchase Agreement


@dataclass
class SolarProject:
    """Represents a solar project with financial parameters."""
    name: str
    project_type: ProjectType
    capacity_kw: float
    capex_per_kw: float
    opex_per_kw_per_year: float
    degradation_rate: float  # annual panel degradation
    lifetime_years: int
    location: str
    solar_irradiance: float  # kWh/m2/day
    performance_ratio: float  # system efficiency (0-1)


@dataclass
class FinancingTerms:
    """Represents financing terms from investment partners."""
    financing_type: FinancingType
    interest_rate: Optional[float] = None  # for debt financing
    term_years: Optional[int] = None
    equity_percentage: Optional[float] = None  # for equity financing
    lease_rate: Optional[float] = None  # $/kWh for lease/PPA
    tax_benefits: Optional[Dict[str, float]] = None  # e.g., {'ITC': 0.26, 'MACRS': 0.21}


class SolarFinancialModel:
    """Models the financial profitability of solar projects."""
    
    def __init__(self, project: SolarProject, financing: FinancingTerms):
        self.project = project
        self.financing = financing
        self._validate_inputs()
        
    def _validate_inputs(self):
        """Validate model inputs."""
        if self.project.capacity_kw <= 0:
            raise ValueError("Project capacity must be positive")
        if self.project.capex_per_kw <= 0:
            raise ValueError("CAPEX per kW must be positive")
        if not 0 <= self.project.degradation_rate <= 1:
            raise ValueError("Degradation rate must be between 0 and 1")
        if self.financing.financing_type == FinancingType.DEBT and self.financing.interest_rate is None:
            raise ValueError("Interest rate must be provided for debt financing")
    
    def calculate_energy_production(self) -> pd.DataFrame:
        """Calculate annual energy production considering degradation."""
        years = range(1, self.project.lifetime_years + 1)
        production = []
        
        # Base annual production in kWh
        base_production = (
            self.project.capacity_kw * 
            self.project.solar_irradiance * 365 * 
            self.project.performance_ratio
        )
        
        for year in years:
            degradation_factor = (1 - self.project.degradation_rate) ** (year - 1)
            production.append(base_production * degradation_factor)
            
        return pd.DataFrame({
            'Year': years,
            'Production_kWh': production
        })
    
    def calculate_financials(self, electricity_price: float, discount_rate: float) -> Dict:
        """Calculate financial metrics for the project."""
        energy_df = self.calculate_energy_production()
        years = energy_df['Year'].values
        production = energy_df['Production_kWh'].values
        
        # Revenue calculations
        if self.financing.financing_type in (FinancingType.LEASE, FinancingType.PPA):
            revenue = production * self.financing.lease_rate
        else:
            revenue = production * electricity_price
            
        # Cost calculations
        opex = np.full(len(years), self.project.opex_per_kw_per_year * self.project.capacity_kw)
        capex = np.zeros(len(years))
        capex[0] = self.project.capex_per_kw * self.project.capacity_kw
        
        # Apply tax benefits if available
        tax_benefits = np.zeros(len(years))
        if self.financing.tax_benefits:
            if 'ITC' in self.financing.tax_benefits:
                tax_benefits[0] += capex[0] * self.financing.tax_benefits['ITC']
            if 'MACRS' in self.financing.tax_benefits:
                # Simplified 5-year MACRS
                macrs_rates = [0.2, 0.32, 0.192, 0.1152, 0.1152, 0.0576]
                for i, rate in enumerate(macrs_rates[:min(6, len(years))]):
                    tax_benefits[i] += capex[0] * rate * self.financing.tax_benefits['MACRS']
        
        # Cash flow calculations
        cash_flow = revenue - opex - capex + tax_benefits
        
        # Apply financing costs
        if self.financing.financing_type == FinancingType.DEBT:
            principal = capex[0]
            annual_payment = np.pmt(
                self.financing.interest_rate,
                self.financing.term_years,
                -principal
            )
            for year in range(min(self.financing.term_years, len(years))):
                cash_flow[year] -= annual_payment
        
        # Calculate financial metrics
        npv = np.npv(discount_rate, cash_flow)
        irr = np.irr(cash_flow)
        payback_period = self._calculate_payback_period(cash_flow)
        
        return {
            'npv': npv,
            'irr': irr,
            'payback_period': payback_period,
            'cash_flows': cash_flow,
            'detailed': pd.DataFrame({
                'Year': years,
                'Production_kWh': production,
                'Revenue': revenue,
                'OPEX': opex,
                'CAPEX': capex,
                'Tax_Benefits': tax_benefits,
                'Cash_Flow': cash_flow
            })
        }
    
    def _calculate_payback_period(self, cash_flows: np.ndarray) -> float:
        """Calculate the payback period in years."""
        cumulative = 0
        for i, cf in enumerate(cash_flows):
            cumulative += cf
            if cumulative >= 0:
                return i + (abs(cumulative - cf) / cf if cf != 0 else 0)
        return float('inf')  # Never pays back
    
    def sensitivity_analysis(self, 
                           electricity_price_range: Tuple[float, float, int],
                           discount_rate_range: Tuple[float, float, int],
                           capex_range: Tuple[float, float, int]) -> Dict:
        """Perform sensitivity analysis on key parameters."""
        results = []
        
        # Generate parameter ranges
        electricity_prices = np.linspace(*electricity_price_range)
        discount_rates = np.linspace(*discount_rate_range)
        capex_values = np.linspace(*capex_range)
        
        # Original values
        original_capex = self.project.capex_per_kw
        
        for price in electricity_prices:
            for rate in discount_rates:
                for capex in capex_values:
                    self.project.capex_per_kw = capex
                    financials = self.calculate_financials(price, rate)
                    results.append({
                        'Electricity_Price': price,
                        'Discount_Rate': rate,
                        'CAPEX_per_kW': capex,
                        'NPV': financials['npv'],
                        'IRR': financials['irr'],
                        'Payback_Period': financials['payback_period']
                    })
        
        # Restore original capex
        self.project.capex_per_kw = original_capex
        
        return pd.DataFrame(results)


# Example usage
if __name__ == "__main__":
    # Create a sample project
    project = SolarProject(
        name="Sunny Valley Solar Farm",
        project_type=ProjectType.UTILITY_SCALE,
        capacity_kw=10000,  # 10 MW
        capex_per_kw=1000,  # $1000/kW
        opex_per_kw_per_year=20,  # $20/kW/year
        degradation_rate=0.005,  # 0.5% per year
        lifetime_years=25,
        location="California",
        solar_irradiance=5.5,  # kWh/m2/day
        performance_ratio=0.75
    )
    
    # Create financing terms
    financing = FinancingTerms(
        financing_type=FinancingType.PPA,
        lease_rate=0.08,  # $0.08/kWh
        tax
