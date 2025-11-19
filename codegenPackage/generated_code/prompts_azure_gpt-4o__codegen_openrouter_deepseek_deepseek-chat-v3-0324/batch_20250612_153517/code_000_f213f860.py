"""
Generated Code Metadata:
========================
Original URL: https://fesit.cl
Prompt: Write Python code to analyze Chilean tax system data and generate reports based on principles like certainty, coherence, and simplicity, as emphasized by FESIT.
Generated: DETERMINISTIC_f213f860b49595ee
Batch ID: 20250612_153517
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
from typing import Dict, List, Optional, Tuple
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ChileanTaxAnalyzer:
    """
    A class to analyze Chilean tax system data based on FESIT principles:
    - Certainty: Clear and predictable tax rules
    - Coherence: Logical consistency within the tax system
    - Simplicity: Easy to understand and comply with
    """
    
    def __init__(self, data_path: str):
        """
        Initialize the analyzer with tax data.
        
        Args:
            data_path: Path to the tax data file (CSV or Excel)
        """
        self.data_path = Path(data_path)
        self.tax_data = None
        self.load_data()
        
    def load_data(self) -> None:
        """
        Load tax data from the specified file.
        Supports CSV and Excel formats.
        """
        try:
            if self.data_path.suffix == '.csv':
                self.tax_data = pd.read_csv(self.data_path)
            elif self.data_path.suffix in ('.xlsx', '.xls'):
                self.tax_data = pd.read_excel(self.data_path)
            else:
                raise ValueError("Unsupported file format. Please provide CSV or Excel file.")
            
            logger.info(f"Successfully loaded tax data from {self.data_path}")
            
        except FileNotFoundError:
            logger.error(f"File not found: {self.data_path}")
            raise
        except Exception as e:
            logger.error(f"Error loading tax data: {str(e)}")
            raise
            
    def validate_data(self) -> bool:
        """
        Validate the loaded tax data for required columns and data quality.
        
        Returns:
            bool: True if data is valid, False otherwise
        """
        required_columns = ['tax_type', 'tax_rate', 'revenue', 'year']
        
        if not all(col in self.tax_data.columns for col in required_columns):
            logger.error("Missing required columns in tax data")
            return False
            
        if self.tax_data.isnull().values.any():
            logger.warning("Tax data contains missing values")
            
        return True
    
    def analyze_certainty(self) -> Dict[str, float]:
        """
        Analyze tax certainty by measuring rate stability over time.
        
        Returns:
            Dict: Dictionary with tax type and rate stability score
        """
        if not self.validate_data():
            raise ValueError("Invalid tax data for analysis")
            
        certainty_scores = {}
        
        for tax_type in self.tax_data['tax_type'].unique():
            type_data = self.tax_data[self.tax_data['tax_type'] == tax_type]
            rate_changes = type_data['tax_rate'].diff().abs().sum()
            years = type_data['year'].nunique()
            
            # Score: lower rate changes = higher certainty
            score = 1 - (rate_changes / (years * 10))  # Normalize to 0-1 range
            certainty_scores[tax_type] = max(0, min(1, score))
            
        return certainty_scores
    
    def analyze_coherence(self) -> Dict[str, float]:
        """
        Analyze tax coherence by comparing similar tax types' rates.
        
        Returns:
            Dict: Dictionary with tax type and coherence score
        """
        if not self.validate_data():
            raise ValueError("Invalid tax data for analysis")
            
        # Group similar tax types (this would be expanded in a real implementation)
        tax_groups = {
            'income': ['corporate_income', 'personal_income'],
            'consumption': ['vat', 'excise']
        }
        
        coherence_scores = {}
        
        for group, taxes in tax_groups.items():
            group_data = self.tax_data[self.tax_data['tax_type'].isin(taxes)]
            if len(group_data) < 2:
                continue
                
            avg_rate = group_data['tax_rate'].mean()
            std_dev = group_data['tax_rate'].std()
            
            # Score: lower std dev = higher coherence
            score = 1 - (std_dev / (avg_rate + 1e-6))  # Avoid division by zero
            for tax in taxes:
                coherence_scores[tax] = max(0, min(1, score))
                
        return coherence_scores
    
    def analyze_simplicity(self) -> Dict[str, float]:
        """
        Analyze tax simplicity by counting unique rates and exceptions.
        
        Returns:
            Dict: Dictionary with tax type and simplicity score
        """
        if not self.validate_data():
            raise ValueError("Invalid tax data for analysis")
            
        simplicity_scores = {}
        
        for tax_type in self.tax_data['tax_type'].unique():
            type_data = self.tax_data[self.tax_data['tax_type'] == tax_type]
            unique_rates = type_data['tax_rate'].nunique()
            years = type_data['year'].nunique()
            
            # Score: fewer rate changes = higher simplicity
            score = 1 - (unique_rates / years)
            simplicity_scores[tax_type] = max(0, min(1, score))
            
        return simplicity_scores
    
    def generate_report(self, output_path: str = "tax_analysis_report.xlsx") -> None:
        """
        Generate a comprehensive tax analysis report.
        
        Args:
            output_path: Path to save the report (Excel format)
        """
        try:
            # Create a Pandas Excel writer
            writer = pd.ExcelWriter(output_path, engine='xlsxwriter')
            
            # Generate analysis results
            certainty = self.analyze_certainty()
            coherence = self.analyze_coherence()
            simplicity = self.analyze_simplicity()
            
            # Create DataFrames for each analysis
            certainty_df = pd.DataFrame(list(certainty.items()), columns=['Tax Type', 'Certainty Score'])
            coherence_df = pd.DataFrame(list(coherence.items()), columns=['Tax Type', 'Coherence Score'])
            simplicity_df = pd.DataFrame(list(simplicity.items()), columns=['Tax Type', 'Simplicity Score'])
            
            # Write each DataFrame to a different worksheet
            certainty_df.to_excel(writer, sheet_name='Certainty', index=False)
            coherence_df.to_excel(writer, sheet_name='Coherence', index=False)
            simplicity_df.to_excel(writer, sheet_name='Simplicity', index=False)
            
            # Create summary sheet
            summary_df = certainty_df.merge(coherence_df, on='Tax Type').merge(simplicity_df, on='Tax Type')
            summary_df['Overall Score'] = summary_df[['Certainty Score', 'Coherence Score', 'Simplicity Score']].mean(axis=1)
            summary_df.to_excel(writer, sheet_name='Summary', index=False)
            
            # Save the Excel file
            writer.close()
            logger.info(f"Successfully generated tax analysis report at {output_path}")
            
        except Exception as e:
            logger.error(f"Error generating report: {str(e)}")
            raise
    
    def plot_tax_trends(self, tax_type: str, output_path: Optional[str] = None) -> None:
        """
        Plot tax rate trends over time for a specific tax type.
        
        Args:
            tax_type: Type of tax to plot
            output_path: Optional path to save the plot image
        """
        try:
            type_data = self.tax_data[self.tax_data['tax_type'] == tax_type]
            
            if type_data.empty:
                logger.warning(f"No data found for tax type: {tax_type}")
                return
                
            plt.figure(figsize=(10, 6))
            plt.plot(type_data['year'], type_data['tax_rate'], marker='o')
            plt.title(f'Tax Rate Trend for {tax_type}')
            plt.xlabel('Year')
            plt.ylabel('Tax Rate (%)')
            plt.grid(True)
            
            if output_path:
                plt.savefig(output_path)
                logger.info(f"Saved tax trend plot to {output_path}")
            else:
                plt.show()
                
        except Exception as e:
            logger.error(f"Error plotting tax trends: {str(e)}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        # Initialize analyzer with sample data
        analyzer = ChileanTaxAnalyzer("chilean_tax_data.csv")
        
        # Generate and save reports
        analyzer.generate_report()
        
        # Plot specific tax trends
        analyzer.plot_tax_trends("vat", "vat_trend.png")
        
    except Exception as e:
        logger.error(f"Error in tax analysis: {str(e)}")
```
