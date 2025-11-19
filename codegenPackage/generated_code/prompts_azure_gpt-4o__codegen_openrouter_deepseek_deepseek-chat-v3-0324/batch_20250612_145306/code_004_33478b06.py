"""
Generated Code Metadata:
========================
Original URL: https://lbicgroup.com
Prompt: Create a script to analyze the cost-effectiveness of manufacturing processes for Angle Cocks and Empty Load Boxes, referencing LBIC Engineering Group's focus on brake system components.
Generated: DETERMINISTIC_33478b069b69ca4b
Batch ID: 20250612_145306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Cost-Effectiveness Analysis for Manufacturing Processes
Focus: Angle Cocks and Empty Load Boxes (Brake System Components)
Reference: LBIC Engineering Group

This script analyzes the cost-effectiveness of manufacturing processes
for Angle Cocks and Empty Load Boxes by comparing various cost factors
and production metrics.
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Tuple
import matplotlib.pyplot as plt
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('manufacturing_analysis.log'),
        logging.StreamHandler()
    ]
)

class ManufacturingCostAnalyzer:
    """
    Analyzes cost-effectiveness of manufacturing processes for brake components.
    """
    
    def __init__(self):
        self.components = {
            'angle_cocks': {
                'material_cost': 0,
                'labor_cost': 0,
                'overhead_cost': 0,
                'production_volume': 0,
                'defect_rate': 0.0
            },
            'empty_load_boxes': {
                'material_cost': 0,
                'labor_cost': 0,
                'overhead_cost': 0,
                'production_volume': 0,
                'defect_rate': 0.0
            }
        }
        self.exchange_rate = 1.0  # Default to 1, can be set for currency conversion
        
    def set_exchange_rate(self, rate: float) -> None:
        """Set currency exchange rate for cost calculations."""
        if rate <= 0:
            raise ValueError("Exchange rate must be positive")
        self.exchange_rate = rate
        logging.info(f"Exchange rate set to: {rate}")
    
    def input_component_data(
        self,
        component: str,
        material_cost: float,
        labor_cost: float,
        overhead_cost: float,
        production_volume: int,
        defect_rate: float
    ) -> None:
        """
        Input manufacturing data for a specific component.
        
        Args:
            component: 'angle_cocks' or 'empty_load_boxes'
            material_cost: Cost of materials per unit
            labor_cost: Labor cost per unit
            overhead_cost: Overhead cost per unit
            production_volume: Number of units produced
            defect_rate: Defect rate as a decimal (e.g., 0.05 for 5%)
        """
        if component not in self.components:
            raise ValueError(f"Invalid component: {component}")
        
        if any(cost < 0 for cost in [material_cost, labor_cost, overhead_cost]):
            raise ValueError("Costs cannot be negative")
            
        if production_volume <= 0:
            raise ValueError("Production volume must be positive")
            
        if not 0 <= defect_rate <= 1:
            raise ValueError("Defect rate must be between 0 and 1")
            
        self.components[component] = {
            'material_cost': material_cost,
            'labor_cost': labor_cost,
            'overhead_cost': overhead_cost,
            'production_volume': production_volume,
            'defect_rate': defect_rate
        }
        logging.info(f"Data updated for {component}")
    
    def calculate_unit_cost(self, component: str) -> float:
        """
        Calculate total cost per unit for a component.
        
        Args:
            component: 'angle_cocks' or 'empty_load_boxes'
            
        Returns:
            Total cost per unit
        """
        if component not in self.components:
            raise ValueError(f"Invalid component: {component}")
            
        data = self.components[component]
        return (data['material_cost'] + data['labor_cost'] + data['overhead_cost']) * self.exchange_rate
    
    def calculate_total_cost(self, component: str) -> float:
        """
        Calculate total cost for production volume including defects.
        
        Args:
            component: 'angle_cocks' or 'empty_load_boxes'
            
        Returns:
            Total cost accounting for production volume and defects
        """
        if component not in self.components:
            raise ValueError(f"Invalid component: {component}")
            
        data = self.components[component]
        unit_cost = self.calculate_unit_cost(component)
        effective_units = data['production_volume'] * (1 + data['defect_rate'])
        return unit_cost * effective_units
    
    def calculate_cost_per_good_unit(self, component: str) -> float:
        """
        Calculate cost per good (non-defective) unit.
        
        Args:
            component: 'angle_cocks' or 'empty_load_boxes'
            
        Returns:
            Cost per good unit
        """
        if component not in self.components:
            raise ValueError(f"Invalid component: {component}")
            
        total_cost = self.calculate_total_cost(component)
        data = self.components[component]
        good_units = data['production_volume'] * (1 - data['defect_rate'])
        return total_cost / good_units if good_units > 0 else float('inf')
    
    def compare_components(self) -> Dict[str, Dict[str, float]]:
        """
        Compare cost-effectiveness metrics between both components.
        
        Returns:
            Dictionary containing comparison metrics
        """
        comparison = {}
        for component in self.components:
            comparison[component] = {
                'unit_cost': self.calculate_unit_cost(component),
                'total_cost': self.calculate_total_cost(component),
                'cost_per_good_unit': self.calculate_cost_per_good_unit(component),
                'defect_cost': self.calculate_total_cost(component) * self.components[component]['defect_rate']
            }
        return comparison
    
    def generate_report(self) -> pd.DataFrame:
        """
        Generate a comprehensive report of cost analysis.
        
        Returns:
            Pandas DataFrame containing the analysis report
        """
        comparison = self.compare_components()
        report_data = []
        
        for component, metrics in comparison.items():
            report_data.append({
                'Component': component.replace('_', ' ').title(),
                'Unit Cost ($)': round(metrics['unit_cost'], 2),
                'Total Cost ($)': round(metrics['total_cost'], 2),
                'Cost per Good Unit ($)': round(metrics['cost_per_good_unit'], 2),
                'Defect Cost ($)': round(metrics['defect_cost'], 2),
                'Defect Rate (%)': round(self.components[component]['defect_rate'] * 100, 2),
                'Production Volume': self.components[component]['production_volume']
            })
            
        return pd.DataFrame(report_data)
    
    def plot_cost_comparison(self) -> None:
        """Generate visualization comparing costs between components."""
        report = self.generate_report()
        
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
        fig.suptitle('Manufacturing Cost Comparison: Angle Cocks vs Empty Load Boxes')
        
        # Unit Cost Comparison
        report.plot.bar(x='Component', y='Unit Cost ($)', ax=axes[0, 0], legend=False)
        axes[0, 0].set_title('Unit Cost Comparison')
        axes[0, 0].set_ylabel('Cost ($)')
        
        # Total Cost Comparison
        report.plot.bar(x='Component', y='Total Cost ($)', ax=axes[0, 1], legend=False)
        axes[0, 1].set_title('Total Cost Comparison')
        axes[0, 1].set_ylabel('Cost ($)')
        
        # Cost per Good Unit
        report.plot.bar(x='Component', y='Cost per Good Unit ($)', ax=axes[1, 0], legend=False)
        axes[1, 0].set_title('Cost per Good Unit')
        axes[1, 0].set_ylabel('Cost ($)')
        
        # Defect Rate Comparison
        report.plot.bar(x='Component', y='Defect Rate (%)', ax=axes[1, 1], legend=False)
        axes[1, 1].set_title('Defect Rate Comparison')
        axes[1, 1].set_ylabel('Percentage (%)')
        
        plt.tight_layout()
        plt.savefig('cost_comparison.png')
        logging.info("Cost comparison visualization saved as 'cost_comparison.png'")
        plt.close()

def main():
    """Main execution function for the cost analysis."""
    try:
        analyzer = ManufacturingCostAnalyzer()
        
        # Example data for Angle Cocks
        analyzer.input_component_data(
            component='angle_cocks',
            material_cost=15.50,
            labor_cost=8.75,
            overhead_cost=5.25,
            production_volume=10000,
            defect_rate=0.03  # 3%
        )
        
        # Example data for Empty Load Boxes
        analyzer.input_component_data(
            component='empty_load_boxes',
            material_cost=22.80,
            labor_cost=6.50,
            overhead_cost=4.75,
            production_volume=8000,
            defect_rate=0.02  # 2%
        )
        
        # Generate and display report
        report = analyzer.generate_report()
        print("\nManufacturing Cost Analysis Report
