"""
Generated Code Metadata:
========================
Original URL: https://gosonicsolutions.com
Prompt: How can I evaluate the cost-effectiveness of outsourcing my industrial parts cleaning to a service like Sonic Solutions, based on their case studies?
Generated: DETERMINISTIC_71dceccf633e3564
Batch ID: 20250612_140414
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
from typing import Dict, List, Optional

class CostEffectivenessAnalyzer:
    """
    Analyzes the cost-effectiveness of outsourcing industrial parts cleaning
    based on case study data from a service provider like Sonic Solutions.
    """
    
    def __init__(self, in_house_data: Dict[str, float], case_studies: List[Dict[str, float]]):
        """
        Initialize the analyzer with in-house costs and case study data.
        
        Args:
            in_house_data: Dictionary containing in-house cleaning cost metrics
                Example: {
                    'labor_cost_per_hour': 25.0,
                    'chemical_cost_per_month': 1200.0,
                    'equipment_maintenance_per_year': 5000.0,
                    'energy_cost_per_month': 800.0,
                    'parts_processed_per_month': 10000
                }
            case_studies: List of dictionaries containing case study data from provider
                Example: [{
                    'service_cost_per_part': 0.15,
                    'parts_processed': 12000,
                    'savings_percentage': 20.0,
                    'quality_improvement': 15.0
                }]
        """
        self.in_house_data = in_house_data
        self.case_studies = case_studies
        
    def calculate_in_house_cost_per_part(self) -> float:
        """Calculate the total in-house cost per part processed."""
        try:
            monthly_labor = self.in_house_data['labor_cost_per_hour'] * 160  # Assuming 160 working hours/month
            monthly_chemical = self.in_house_data['chemical_cost_per_month']
            monthly_equipment = self.in_house_data['equipment_maintenance_per_year'] / 12
            monthly_energy = self.in_house_data['energy_cost_per_month']
            
            total_monthly_cost = monthly_labor + monthly_chemical + monthly_equipment + monthly_energy
            return total_monthly_cost / self.in_house_data['parts_processed_per_month']
        except KeyError as e:
            raise ValueError(f"Missing required in-house data field: {e}")
        except ZeroDivisionError:
            raise ValueError("Parts processed per month cannot be zero")
    
    def analyze_case_studies(self) -> pd.DataFrame:
        """
        Analyze all case studies and compare against in-house costs.
        
        Returns:
            DataFrame with comparison metrics for each case study
        """
        try:
            in_house_cost = self.calculate_in_house_cost_per_part()
            results = []
            
            for study in self.case_studies:
                outsourced_cost = study['service_cost_per_part']
                savings = in_house_cost - outsourced_cost
                savings_percentage = (savings / in_house_cost) * 100
                
                results.append({
                    'case_study_id': self.case_studies.index(study) + 1,
                    'in_house_cost_per_part': in_house_cost,
                    'outsourced_cost_per_part': outsourced_cost,
                    'absolute_savings': savings,
                    'percentage_savings': savings_percentage,
                    'reported_savings_percentage': study.get('savings_percentage', None),
                    'quality_improvement': study.get('quality_improvement', None),
                    'parts_volume': study.get('parts_processed', None)
                })
            
            return pd.DataFrame(results)
        except Exception as e:
            raise ValueError(f"Error analyzing case studies: {str(e)}")
    
    def generate_report(self, analysis_results: pd.DataFrame) -> str:
        """Generate a human-readable report from the analysis results."""
        report = []
        report.append("Cost-Effectiveness Analysis Report")
        report.append("="*40)
        report.append(f"In-House Cost per Part: ${self.calculate_in_house_cost_per_part():.4f}")
        report.append("\nCase Study Comparisons:")
        
        for _, row in analysis_results.iterrows():
            report.append(f"\nCase Study #{row['case_study_id']}:")
            report.append(f"- Outsourced Cost: ${row['outsourced_cost_per_part']:.4f}")
            report.append(f"- Absolute Savings: ${row['absolute_savings']:.4f}")
            report.append(f"- Percentage Savings: {row['percentage_savings']:.2f}%")
            if not pd.isna(row['reported_savings_percentage']):
                report.append(f"- Reported Savings: {row['reported_savings_percentage']:.2f}%")
            if not pd.isna(row['quality_improvement']):
                report.append(f"- Quality Improvement: +{row['quality_improvement']:.2f}%")
        
        return "\n".join(report)

# Example usage
if __name__ == "__main__":
    # Sample data
    in_house_costs = {
        'labor_cost_per_hour': 28.50,
        'chemical_cost_per_month': 1500.0,
        'equipment_maintenance_per_year': 7500.0,
        'energy_cost_per_month': 950.0,
        'parts_processed_per_month': 15000
    }
    
    sonic_case_studies = [
        {
            'service_cost_per_part': 0.18,
            'parts_processed': 18000,
            'savings_percentage': 22.5,
            'quality_improvement': 18.0
        },
        {
            'service_cost_per_part': 0.22,
            'parts_processed': 12000,
            'savings_percentage': 15.0
        }
    ]
    
    try:
        analyzer = CostEffectivenessAnalyzer(in_house_costs, sonic_case_studies)
        results = analyzer.analyze_case_studies()
        report = analyzer.generate_report(results)
        print(report)
    except ValueError as e:
        print(f"Error: {str(e)}")
```
