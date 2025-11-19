"""
Generated Code Metadata:
========================
Original URL: https://galmudugmof.so
Prompt: Generate a Python script to analyze the budget data for the Galmudug State of Somalia, referencing the Budget Framework Paper FY 2025 and the approved budget details.
Generated: DETERMINISTIC_d209960e951cbe68
Batch ID: 20250612_163835
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
import matplotlib.pyplot as plt
from pathlib import Path
import logging
from typing import Dict, Tuple, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class BudgetAnalyzer:
    """
    A class to analyze budget data for Galmudug State of Somalia.
    
    Attributes:
        budget_data (pd.DataFrame): The loaded budget data
        framework_data (pd.DataFrame): The loaded budget framework data
    """
    
    def __init__(self, budget_file: str, framework_file: str):
        """
        Initialize the BudgetAnalyzer with file paths.
        
        Args:
            budget_file: Path to the approved budget details CSV/Excel file
            framework_file: Path to the Budget Framework Paper CSV/Excel file
        """
        self.budget_data = None
        self.framework_data = None
        self._load_data(budget_file, framework_file)
        
    def _load_data(self, budget_file: str, framework_file: str) -> None:
        """
        Load budget data from files with error handling.
        
        Args:
            budget_file: Path to budget details file
            framework_file: Path to framework paper file
            
        Raises:
            FileNotFoundError: If either file doesn't exist
            ValueError: If data format is invalid
        """
        try:
            # Check files exist
            if not Path(budget_file).exists():
                raise FileNotFoundError(f"Budget file not found: {budget_file}")
            if not Path(framework_file).exists():
                raise FileNotFoundError(f"Framework file not found: {framework_file}")
            
            # Load data based on file extension
            if budget_file.endswith('.csv'):
                self.budget_data = pd.read_csv(budget_file)
            elif budget_file.endswith(('.xls', '.xlsx')):
                self.budget_data = pd.read_excel(budget_file)
            else:
                raise ValueError("Unsupported budget file format")
                
            if framework_file.endswith('.csv'):
                self.framework_data = pd.read_csv(framework_file)
            elif framework_file.endswith(('.xls', '.xlsx')):
                self.framework_data = pd.read_excel(framework_file)
            else:
                raise ValueError("Unsupported framework file format")
                
            logger.info("Data loaded successfully")
            
            # Validate required columns
            self._validate_data()
            
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            raise
            
    def _validate_data(self) -> None:
        """
        Validate that required columns exist in the loaded data.
        
        Raises:
            ValueError: If required columns are missing
        """
        required_budget_cols = {'category', 'allocated', 'spent', 'department'}
        required_framework_cols = {'category', 'projected', 'priority'}
        
        if not required_budget_cols.issubset(self.budget_data.columns):
            missing = required_budget_cols - set(self.budget_data.columns)
            raise ValueError(f"Missing columns in budget data: {missing}")
            
        if not required_framework_cols.issubset(self.framework_data.columns):
            missing = required_framework_cols - set(self.framework_data.columns)
            raise ValueError(f"Missing columns in framework data: {missing}")
            
        logger.info("Data validation passed")
    
    def get_budget_summary(self) -> Dict[str, float]:
        """
        Generate a summary of the budget data.
        
        Returns:
            Dictionary with summary statistics
        """
        if self.budget_data is None:
            raise ValueError("Budget data not loaded")
            
        return {
            'total_allocated': self.budget_data['allocated'].sum(),
            'total_spent': self.budget_data['spent'].sum(),
            'utilization_rate': self.budget_data['spent'].sum() / self.budget_data['allocated'].sum(),
            'departments': len(self.budget_data['department'].unique()),
            'categories': len(self.budget_data['category'].unique())
        }
    
    def compare_with_framework(self) -> pd.DataFrame:
        """
        Compare actual budget with framework projections.
        
        Returns:
            DataFrame with comparison results
        """
        if self.budget_data is None or self.framework_data is None:
            raise ValueError("Data not loaded")
            
        # Merge data on category
        merged = pd.merge(
            self.budget_data.groupby('category')['allocated'].sum().reset_index(),
            self.framework_data[['category', 'projected']],
            on='category',
            how='left'
        )
        
        # Calculate variance
        merged['variance'] = merged['allocated'] - merged['projected']
        merged['variance_pct'] = (merged['variance'] / merged['projected']) * 100
        
        return merged.sort_values('variance_pct', ascending=False)
    
    def plot_department_allocation(self, save_path: Optional[str] = None) -> None:
        """
        Create a visualization of budget allocation by department.
        
        Args:
            save_path: Optional path to save the plot
        """
        if self.budget_data is None:
            raise ValueError("Budget data not loaded")
            
        department_totals = self.budget_data.groupby('department')['allocated'].sum().sort_values()
        
        plt.figure(figsize=(12, 8))
        department_totals.plot(kind='barh', color='skyblue')
        plt.title('Budget Allocation by Department - Galmudug State FY2025')
        plt.xlabel('Allocated Budget (USD)')
        plt.ylabel('Department')
        plt.grid(axis='x', linestyle='--', alpha=0.7)
        
        if save_path:
            plt.savefig(save_path, bbox_inches='tight', dpi=300)
            logger.info(f"Plot saved to {save_path}")
        else:
            plt.show()
    
    def generate_report(self, output_file: str) -> None:
        """
        Generate a comprehensive budget analysis report.
        
        Args:
            output_file: Path to save the report
        """
        try:
            with open(output_file, 'w') as f:
                # Summary section
                summary = self.get_budget_summary()
                f.write("Galmudug State Budget Analysis Report - FY2025\n")
                f.write("="*50 + "\n\n")
                f.write("Budget Summary:\n")
                f.write(f"Total Allocated: ${summary['total_allocated']:,.2f}\n")
                f.write(f"Total Spent: ${summary['total_spent']:,.2f}\n")
                f.write(f"Utilization Rate: {summary['utilization_rate']:.1%}\n")
                f.write(f"Departments: {summary['departments']}\n")
                f.write(f"Budget Categories: {summary['categories']}\n\n")
                
                # Comparison section
                f.write("Budget vs Framework Comparison:\n")
                comparison = self.compare_with_framework()
                f.write(comparison.to_string())
                
            logger.info(f"Report generated successfully at {output_file}")
            
        except Exception as e:
            logger.error(f"Error generating report: {str(e)}")
            raise


# Example usage
if __name__ == "__main__":
    try:
        # Initialize analyzer with data files
        analyzer = BudgetAnalyzer(
            budget_file="galmudug_budget_2025.csv",
            framework_file="galmudug_framework_2025.csv"
        )
        
        # Generate and print summary
        summary = analyzer.get_budget_summary()
        print("Budget Summary:")
        for k, v in summary.items():
            print(f"{k.replace('_', ' ').title()}: {v}")
        
        # Generate comparison report
        analyzer.generate_report("galmudug_budget_analysis_2025.txt")
        
        # Create visualization
        analyzer.plot_department_allocation("department_allocation.png")
        
    except Exception as e:
        logger.error(f"Budget analysis failed: {str(e)}")
```
