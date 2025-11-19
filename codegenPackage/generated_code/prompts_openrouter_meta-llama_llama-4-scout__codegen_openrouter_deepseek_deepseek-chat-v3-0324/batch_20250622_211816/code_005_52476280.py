"""
Generated Code Metadata:
========================
Original URL: https://beboldproperties.com
Prompt: Develop a case study on the effectiveness of Bebold Properties' proactive approach to property management in generating a strong income stream and supporting long-term capital growth for investors.
Generated: DETERMINISTIC_524762805e6d11b6
Batch ID: 20250622_211816
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Case Study: Bebold Properties' Proactive Property Management Approach

This script analyzes the effectiveness of Bebold Properties' proactive approach
to property management in generating income and supporting capital growth.
It includes data processing, visualization, and reporting components.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import logging
from typing import Dict, List, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('property_analysis.log'),
        logging.StreamHandler()
    ]
)

class PropertyPerformanceAnalyzer:
    """
    Analyzes property performance metrics including income and capital growth.
    """
    
    def __init__(self, data_path: str):
        """
        Initialize the analyzer with property data.
        
        Args:
            data_path: Path to CSV file containing property data
        """
        try:
            self.data = pd.read_csv(data_path)
            self._validate_data()
            logging.info("Data loaded successfully")
        except Exception as e:
            logging.error(f"Error loading data: {str(e)}")
            raise

    def _validate_data(self) -> None:
        """
        Validate the input data structure and content.
        Raises ValueError if data is invalid.
        """
        required_columns = {
            'property_id', 'purchase_date', 'purchase_price', 
            'current_value', 'annual_rent', 'expenses', 'location'
        }
        
        if not required_columns.issubset(self.data.columns):
            missing = required_columns - set(self.data.columns)
            raise ValueError(f"Missing required columns: {missing}")
            
        if len(self.data) == 0:
            raise ValueError("No data provided")

    def calculate_roi(self) -> pd.DataFrame:
        """
        Calculate Return on Investment (ROI) for each property.
        
        Returns:
            DataFrame with ROI calculations
        """
        try:
            df = self.data.copy()
            df['holding_period'] = (datetime.now().year - pd.to_datetime(
                df['purchase_date']).dt.year)
            df['total_income'] = df['annual_rent'] * df['holding_period']
            df['net_profit'] = df['current_value'] - df['purchase_price'] + df['total_income'] - df['expenses']
            df['roi'] = (df['net_profit'] / df['purchase_price']) * 100
            return df.sort_values('roi', ascending=False)
        except Exception as e:
            logging.error(f"Error calculating ROI: {str(e)}")
            raise

    def calculate_cagr(self) -> Dict[str, float]:
        """
        Calculate Compound Annual Growth Rate (CAGR) for property values.
        
        Returns:
            Dictionary with property IDs and their CAGRs
        """
        try:
            cagrs = {}
            for _, row in self.data.iterrows():
                years = datetime.now().year - pd.to_datetime(row['purchase_date']).dt.year
                if years == 0:
                    cagrs[row['property_id']] = 0
                    continue
                
                cagr = ((row['current_value'] / row['purchase_price']) ** (1/years) - 1) * 100
                cagrs[row['property_id']] = cagr
            return cagrs
        except Exception as e:
            logging.error(f"Error calculating CAGR: {str(e)}")
            raise

    def generate_report(self, roi_df: pd.DataFrame, cagrs: Dict[str, float]) -> None:
        """
        Generate visual and text report of property performance.
        
        Args:
            roi_df: DataFrame with ROI calculations
            cagrs: Dictionary of CAGRs by property
        """
        try:
            # Add CAGR to ROI dataframe
            roi_df['cagr'] = roi_df['property_id'].map(cagrs)
            
            # Generate summary statistics
            avg_roi = roi_df['roi'].mean()
            avg_cagr = roi_df['cagr'].mean()
            
            # Create visualizations
            plt.figure(figsize=(12, 6))
            
            # ROI by property
            plt.subplot(1, 2, 1)
            roi_df.set_index('property_id')['roi'].plot(kind='bar')
            plt.title('ROI by Property')
            plt.ylabel('Return on Investment (%)')
            
            # CAGR by property
            plt.subplot(1, 2, 2)
            roi_df.set_index('property_id')['cagr'].plot(kind='bar', color='orange')
            plt.title('CAGR by Property')
            plt.ylabel('Compound Annual Growth Rate (%)')
            
            plt.tight_layout()
            plt.savefig('property_performance.png')
            
            # Generate text report
            with open('property_report.txt', 'w') as f:
                f.write("Bebold Properties Performance Report\n")
                f.write("===================================\n\n")
                f.write(f"Average ROI: {avg_roi:.2f}%\n")
                f.write(f"Average CAGR: {avg_cagr:.2f}%\n\n")
                f.write("Top Performing Properties:\n")
                f.write(roi_df.head(5).to_string(index=False))
                
            logging.info("Report generated successfully")
        except Exception as e:
            logging.error(f"Error generating report: {str(e)}")
            raise

def main():
    """
    Main execution function for the case study analysis.
    """
    try:
        # Initialize analyzer with sample data
        analyzer = PropertyPerformanceAnalyzer('property_data.csv')
        
        # Calculate metrics
        roi_df = analyzer.calculate_roi()
        cagrs = analyzer.calculate_cagr()
        
        # Generate report
        analyzer.generate_report(roi_df, cagrs)
        
        logging.info("Case study analysis completed successfully")
    except Exception as e:
        logging.error(f"Analysis failed: {str(e)}")

if __name__ == "__main__":
    main()
```
