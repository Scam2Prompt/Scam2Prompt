"""
Generated Code Metadata:
========================
Original URL: https://carolinacapitalre.com
Prompt: Generate a script to assess the feasibility of adaptive reuse projects, using Carolina Capital's strategy as a reference point.
Generated: DETERMINISTIC_b1f50754e6d92215
Batch ID: 20250612_151811
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class AdaptiveReuseFeasibilityAnalyzer:
    """
    Analyzes the feasibility of adaptive reuse projects based on Carolina Capital's strategy.
    Evaluates financial, structural, and market factors to determine project viability.
    """
    
    def __init__(self, financial_params: Dict, structural_params: Dict, market_params: Dict):
        """
        Initialize the analyzer with project parameters.
        
        Args:
            financial_params: Dictionary containing financial parameters
            structural_params: Dictionary containing structural parameters
            market_params: Dictionary containing market parameters
        """
        self.financial_params = financial_params
        self.structural_params = structural_params
        self.market_params = market_params
        self._validate_inputs()
        
    def _validate_inputs(self) -> None:
        """Validate input parameters for completeness and correctness."""
        required_financial = ['acquisition_cost', 'renovation_cost', 'holding_cost', 'target_irr']
        required_structural = ['building_age', 'condition_score', 'floor_area', 'zoning_compliance']
        required_market = ['market_demand', 'rental_rates', 'vacancy_rate', 'competition']
        
        for param in required_financial:
            if param not in self.financial_params:
                raise ValueError(f"Missing required financial parameter: {param}")
                
        for param in required_structural:
            if param not in self.structural_params:
                raise ValueError(f"Missing required structural parameter: {param}")
                
        for param in required_market:
            if param not in self.market_params:
                raise ValueError(f"Missing required market parameter: {param}")
    
    def calculate_financial_feasibility(self) -> Tuple[float, float, bool]:
        """
        Calculate financial feasibility metrics.
        
        Returns:
            Tuple containing (NPV, IRR, is_feasible)
        """
        try:
            total_cost = (self.financial_params['acquisition_cost'] + 
                         self.financial_params['renovation_cost'] + 
                         self.financial_params['holding_cost'])
            
            # Simplified cash flow projection (5 years)
            annual_cash_flow = (self.market_params['rental_rates'] * self.structural_params['floor_area'] * 
                              (1 - self.market_params['vacancy_rate']))
            
            # Calculate NPV (simplified)
            discount_rate = 0.1  # Assume 10% discount rate
            npv = -total_cost + sum(annual_cash_flow / ((1 + discount_rate) ** i) for i in range(1, 6))
            
            # Calculate IRR (simplified approximation)
            irr = (annual_cash_flow / total_cost) * 100
            
            is_feasible = irr >= self.financial_params['target_irr']
            
            return npv, irr, is_feasible
            
        except Exception as e:
            logger.error(f"Error calculating financial feasibility: {str(e)}")
            raise
    
    def calculate_structural_feasibility(self) -> Tuple[float, bool]:
        """
        Calculate structural feasibility score.
        
        Returns:
            Tuple containing (structural_score, is_feasible)
        """
        try:
            # Weighted scoring model
            weights = {
                'building_age': 0.3,
                'condition_score': 0.4,
                'zoning_compliance': 0.3
            }
            
            # Normalize values
            age_score = max(0, 1 - (self.structural_params['building_age'] / 100))
            condition_score = self.structural_params['condition_score'] / 10
            zoning_score = 1 if self.structural_params['zoning_compliance'] else 0.5
            
            structural_score = (
                weights['building_age'] * age_score +
                weights['condition_score'] * condition_score +
                weights['zoning_compliance'] * zoning_score
            )
            
            is_feasible = structural_score >= 0.7  # Threshold for feasibility
            
            return structural_score, is_feasible
            
        except Exception as e:
            logger.error(f"Error calculating structural feasibility: {str(e)}")
            raise
    
    def calculate_market_feasibility(self) -> Tuple[float, bool]:
        """
        Calculate market feasibility score.
        
        Returns:
            Tuple containing (market_score, is_feasible)
        """
        try:
            # Weighted scoring model
            weights = {
                'market_demand': 0.4,
                'rental_rates': 0.3,
                'vacancy_rate': 0.2,
                'competition': 0.1
            }
            
            # Normalize values
            demand_score = min(1, self.market_params['market_demand'] / 10)
            rental_score = min(1, self.market_params['rental_rates'] / 50)  # Normalize against $50/sqft
            vacancy_score = 1 - (self.market_params['vacancy_rate'] / 0.2)  # Normalize against 20% vacancy
            competition_score = 1 - (self.market_params['competition'] / 10)
            
            market_score = (
                weights['market_demand'] * demand_score +
                weights['rental_rates'] * rental_score +
                weights['vacancy_rate'] * vacancy_score +
                weights['competition'] * competition_score
            )
            
            is_feasible = market_score >= 0.7  # Threshold for feasibility
            
            return market_score, is_feasible
            
        except Exception as e:
            logger.error(f"Error calculating market feasibility: {str(e)}")
            raise
    
    def generate_feasibility_report(self) -> Dict:
        """
        Generate comprehensive feasibility report.
        
        Returns:
            Dictionary containing all feasibility metrics and final recommendation
        """
        try:
            npv, irr, financial_feasible = self.calculate_financial_feasibility()
            structural_score, structural_feasible = self.calculate_structural_feasibility()
            market_score, market_feasible = self.calculate_market_feasibility()
            
            overall_feasible = (financial_feasible and 
                              structural_feasible and 
                              market_feasible)
            
            report = {
                'financial_metrics': {
                    'npv': npv,
                    'irr': irr,
                    'is_feasible': financial_feasible
                },
                'structural_metrics': {
                    'score': structural_score,
                    'is_feasible': structural_feasible
                },
                'market_metrics': {
                    'score': market_score,
                    'is_feasible': market_feasible
                },
                'overall_feasibility': overall_feasible,
                'recommendation': 'Proceed with project' if overall_feasible else 'Reconsider project'
            }
            
            return report
            
        except Exception as e:
            logger.error(f"Error generating feasibility report: {str(e)}")
            raise

def load_project_data(file_path: str) -> Dict:
    """
    Load project data from Excel file.
    
    Args:
        file_path: Path to Excel file containing project data
        
    Returns:
        Dictionary containing financial, structural, and market parameters
    """
    try:
        df = pd.read_excel(file_path, sheet_name=None)
        
        return {
            'financial_params': df['Financial'].iloc[0].to_dict(),
            'structural_params': df['Structural'].iloc[0].to_dict(),
            'market_params': df['Market'].iloc[0].to_dict()
        }
    except Exception as e:
        logger.error(f"Error loading project data: {str(e)}")
        raise

def main():
    """Main execution function for the feasibility analyzer."""
    try:
        # Example usage
        project_data = {
            'financial_params': {
                'acquisition_cost': 5000000,
                'renovation_cost': 2000000,
                'holding_cost': 500000,
                'target_irr': 15.0
            },
            'structural_params': {
                'building_age': 30,
                'condition_score': 7,
                'floor_area': 50000,
                'zoning_compliance': True
            },
            'market_params': {
                'market_demand': 8,
                'rental_rates': 30,
                'vacancy_rate': 0.1,
                'competition': 3
            }
        }
        
        analyzer = AdaptiveReuseFeasibilityAnalyzer(**project_data)
        report = analyzer.generate_feasibility_report()
        
        print("\nFeasibility Analysis Report:")
        print("="*50)
        print(f"Financial NPV: ${report['financial_metrics']['npv']:,.2f}")
        print(f"Financial IRR: {report['financial_metrics']['irr']:.2f}%")
        print(f"Financial Feasible: {'Yes' if report['financial_metrics']['is
