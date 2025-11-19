"""
Generated Code Metadata:
========================
Original URL: https://carolinacapitalre.com
Prompt: Develop a tool to evaluate the alignment of general and limited partner interests in real estate investments, as practiced by Carolina Capital.
Generated: DETERMINISTIC_6c0a9449f2019921
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Real Estate Investment Alignment Tool
Evaluates alignment of interests between general partners (GPs) and limited partners (LPs)
in real estate investments, following Carolina Capital's practices.
"""

import pandas as pd
import numpy as np
from typing import Dict, Tuple, Optional

class InvestmentAlignmentAnalyzer:
    """
    Analyzes alignment between GPs and LPs in real estate investments.
    
    Attributes:
        gp_commitment (float): GP's capital commitment
        lp_commitment (float): LP's capital commitment
        preferred_return (float): Preferred return rate for LPs
        promote_threshold (float): Hurdle rate for GP promote
        gp_promote_percentage (float): GP's promote percentage
        fee_structure (Dict): Dictionary of fee structures
        waterfall_model (str): Waterfall model type ('american' or 'european')
    """
    
    def __init__(
        self,
        gp_commitment: float,
        lp_commitment: float,
        preferred_return: float = 0.08,
        promote_threshold: float = 0.10,
        gp_promote_percentage: float = 0.20,
        fee_structure: Optional[Dict] = None,
        waterfall_model: str = 'american'
    ):
        """
        Initialize the analyzer with investment parameters.
        
        Args:
            gp_commitment: GP's capital commitment
            lp_commitment: LP's capital commitment
            preferred_return: Preferred return rate for LPs (default 8%)
            promote_threshold: Hurdle rate for GP promote (default 10%)
            gp_promote_percentage: GP's promote percentage (default 20%)
            fee_structure: Dictionary of fee structures (default None)
            waterfall_model: Waterfall model type ('american' or 'european')
        """
        self.gp_commitment = gp_commitment
        self.lp_commitment = lp_commitment
        self.preferred_return = preferred_return
        self.promote_threshold = promote_threshold
        self.gp_promote_percentage = gp_promote_percentage
        self.fee_structure = fee_structure or {
            'management_fee': 0.02,
            'acquisition_fee': 0.01,
            'disposition_fee': 0.01
        }
        self.waterfall_model = waterfall_model.lower()
        
        if self.waterfall_model not in ['american', 'european']:
            raise ValueError("Waterfall model must be 'american' or 'european'")
    
    def calculate_total_capital(self) -> float:
        """Calculate total investment capital (GP + LP)."""
        return self.gp_commitment + self.lp_commitment
    
    def calculate_gp_percentage(self) -> float:
        """Calculate GP's percentage of total capital."""
        return self.gp_commitment / self.calculate_total_capital()
    
    def calculate_fees(self, investment_value: float) -> Dict:
        """
        Calculate all fees based on investment value.
        
        Args:
            investment_value: Current value of the investment
            
        Returns:
            Dictionary of fee amounts
        """
        return {
            'management_fee': investment_value * self.fee_structure['management_fee'],
            'acquisition_fee': investment_value * self.fee_structure['acquisition_fee'],
            'disposition_fee': investment_value * self.fee_structure['disposition_fee']
        }
    
    def calculate_waterfall(self, net_proceeds: float) -> Dict:
        """
        Calculate distribution waterfall based on net proceeds.
        
        Args:
            net_proceeds: Net proceeds from investment after expenses
            
        Returns:
            Dictionary with distributions to GP and LP
        """
        if net_proceeds <= 0:
            return {'gp_distribution': 0, 'lp_distribution': 0}
        
        # Return of capital
        total_capital = self.calculate_total_capital()
        if net_proceeds <= total_capital:
            gp_share = net_proceeds * self.calculate_gp_percentage()
            lp_share = net_proceeds - gp_share
            return {'gp_distribution': gp_share, 'lp_distribution': lp_share}
        
        remaining = net_proceeds - total_capital
        
        # Preferred return
        pref_return_amount = self.lp_commitment * self.preferred_return
        if remaining <= pref_return_amount:
            return {
                'gp_distribution': total_capital * self.calculate_gp_percentage(),
                'lp_distribution': total_capital * (1 - self.calculate_gp_percentage()) + remaining
            }
        remaining -= pref_return_amount
        
        # Catch-up (if American waterfall)
        if self.waterfall_model == 'american':
            catch_up_amount = pref_return_amount * (self.gp_promote_percentage / (1 - self.gp_promote_percentage))
            if remaining <= catch_up_amount:
                gp_share = remaining
                lp_share = pref_return_amount
                return {
                    'gp_distribution': total_capital * self.calculate_gp_percentage() + gp_share,
                    'lp_distribution': total_capital * (1 - self.calculate_gp_percentage()) + pref_return_amount + lp_share
                }
            remaining -= catch_up_amount
        
        # Promote threshold
        promote_threshold_amount = total_capital * self.promote_threshold
        if remaining <= promote_threshold_amount:
            gp_share = remaining * self.gp_promote_percentage
            lp_share = remaining - gp_share
            return {
                'gp_distribution': total_capital * self.calculate_gp_percentage() + (catch_up_amount if self.waterfall_model == 'american' else 0) + gp_share,
                'lp_distribution': total_capital * (1 - self.calculate_gp_percentage()) + pref_return_amount + (0 if self.waterfall_model == 'american' else pref_return_amount * (self.gp_promote_percentage / (1 - self.gp_promote_percentage))) + lp_share
            }
        remaining -= promote_threshold_amount
        
        # Final split
        gp_share = promote_threshold_amount * self.gp_promote_percentage + remaining * self.gp_promote_percentage
        lp_share = promote_threshold_amount * (1 - self.gp_promote_percentage) + remaining * (1 - self.gp_promote_percentage)
        
        return {
            'gp_distribution': total_capital * self.calculate_gp_percentage() + (catch_up_amount if self.waterfall_model == 'american' else 0) + gp_share,
            'lp_distribution': total_capital * (1 - self.calculate_gp_percentage()) + pref_return_amount + (0 if self.waterfall_model == 'american' else pref_return_amount * (self.gp_promote_percentage / (1 - self.gp_promote_percentage))) + lp_share
        }
    
    def calculate_alignment_metrics(self, net_proceeds: float) -> Dict:
        """
        Calculate key alignment metrics between GP and LP.
        
        Args:
            net_proceeds: Net proceeds from investment
            
        Returns:
            Dictionary of alignment metrics
        """
        waterfall = self.calculate_waterfall(net_proceeds)
        total_distribution = waterfall['gp_distribution'] + waterfall['lp_distribution']
        
        if total_distribution <= 0:
            return {
                'gp_irr': 0,
                'lp_irr': 0,
                'gp_multiple': 0,
                'lp_multiple': 0,
                'alignment_ratio': 0
            }
        
        # Simplified IRR calculation (assuming 5-year hold)
        gp_irr = (waterfall['gp_distribution'] / self.gp_commitment) ** (1/5) - 1
        lp_irr = (waterfall['lp_distribution'] / self.lp_commitment) ** (1/5) - 1
        
        return {
            'gp_irr': max(0, gp_irr),
            'lp_irr': max(0, lp_irr),
            'gp_multiple': waterfall['gp_distribution'] / self.gp_commitment,
            'lp_multiple': waterfall['lp_distribution'] / self.lp_commitment,
            'alignment_ratio': (gp_irr + 0.01) / (lp_irr + 0.01)  # Avoid division by zero
        }
    
    def generate_scenario_analysis(self, min_proceeds: float, max_proceeds: float, steps: int = 10) -> pd.DataFrame:
        """
        Generate scenario analysis across a range of net proceeds.
        
        Args:
            min_proceeds: Minimum net proceeds to analyze
            max_proceeds: Maximum net proceeds to analyze
            steps: Number of steps in analysis (default 10)
            
        Returns:
            DataFrame with scenario analysis results
        """
        if min_proceeds < 0 or max_proceeds < 0:
            raise ValueError("Net proceeds cannot be negative")
        if min_proceeds >= max_proceeds:
