"""
Generated Code Metadata:
========================
Original URL: https://linea.be
Prompt: Generate code to analyze the growth in FSC-certified wood purchases over multiple years, using PDC Brush's reported data as an example.
Generated: DETERMINISTIC_94fd52be1ae37ff7
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import matplotlib.pyplot as plt
from typing import Dict, List, Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class FSCCertifiedWoodAnalyzer:
    """
    A class to analyze the growth in FSC-certified wood purchases over multiple years.
    Uses PDC Brush's reported data as an example.
    """
    
    def __init__(self, data: Dict[str, Dict[str, float]]):
        """
        Initialize the analyzer with historical data.
        
        Args:
            data: Dictionary with years as keys and values being dictionaries of
                  metrics (e.g., {'2019': {'volume': 1000, 'percentage': 15.5}})
        """
        self.data = data
        self.df = self._prepare_dataframe()
        
    def _prepare_dataframe(self) -> pd.DataFrame:
        """
        Convert the input data dictionary into a pandas DataFrame for analysis.
        
        Returns:
            pd.DataFrame: Prepared DataFrame with years as index
        """
        try:
            df = pd.DataFrame.from_dict(self.data, orient='index')
            df.index = pd.to_datetime(df.index).year
            df.index.name = 'Year'
            return df.sort_index()
        except Exception as e:
            logger.error(f"Error preparing DataFrame: {e}")
            raise
            
    def calculate_growth(self, metric: str = 'volume') -> pd.DataFrame:
        """
        Calculate year-over-year growth for the specified metric.
        
        Args:
            metric: The metric to calculate growth for ('volume' or 'percentage')
            
        Returns:
            pd.DataFrame: DataFrame with growth calculations
        """
        if metric not in self.df.columns:
            raise ValueError(f"Metric '{metric}' not found in data")
            
        growth_df = self.df[[metric]].copy()
        growth_df['absolute_growth'] = growth_df[metric].diff()
        growth_df['percentage_growth'] = growth_df[metric].pct_change() * 100
        return growth_df
    
    def plot_growth(self, metric: str = 'volume', save_path: Optional[str] = None) -> None:
        """
        Plot the growth trends for the specified metric.
        
        Args:
            metric: The metric to plot ('volume' or 'percentage')
            save_path: Optional path to save the plot image
        """
        if metric not in self.df.columns:
            raise ValueError(f"Metric '{metric}' not found in data")
            
        plt.figure(figsize=(10, 6))
        
        # Plot main metric
        plt.plot(self.df.index, self.df[metric], 
                marker='o', label=f'FSC {metric.capitalize()}')
        
        # Plot growth if we have multiple years
        if len(self.df) > 1:
            growth = self.calculate_growth(metric)
            plt.bar(growth.index, growth['percentage_growth'], 
                   alpha=0.3, label='YoY Growth %')
        
        plt.title(f'FSC-Certified Wood {metric.capitalize()} Over Time')
        plt.xlabel('Year')
        plt.ylabel(metric.capitalize())
        plt.grid(True, which='both', linestyle='--', alpha=0.5)
        plt.legend()
        
        if save_path:
            plt.savefig(save_path, bbox_inches='tight', dpi=300)
            logger.info(f"Plot saved to {save_path}")
        
        plt.show()
        
    def generate_report(self) -> str:
        """
        Generate a text report summarizing the FSC-certified wood growth.
        
        Returns:
            str: Formatted report string
        """
        report_lines = ["FSC-Certified Wood Purchase Analysis Report", "="*50]
        
        if len(self.df) == 0:
            return "No data available for analysis."
            
        # Basic stats
        report_lines.append(f"\nTime Period: {self.df.index.min()} - {self.df.index.max()}")
        report_lines.append(f"Years of Data: {len(self.df)}")
        
        # Volume analysis
        if 'volume' in self.df.columns:
            vol_growth = self.calculate_growth('volume')
            report_lines.append("\nVolume Analysis:")
            report_lines.append(f"- Total Volume: {self.df['volume'].sum():,.0f} units")
            if len(self.df) > 1:
                report_lines.append(f"- Average Annual Growth: {vol_growth['percentage_growth'].mean():.1f}%")
                report_lines.append(f"- Maximum Annual Growth: {vol_growth['percentage_growth'].max():.1f}% in {vol_growth['percentage_growth'].idxmax()}")
        
        # Percentage analysis
        if 'percentage' in self.df.columns:
            pct_growth = self.calculate_growth('percentage')
            report_lines.append("\nPercentage Analysis:")
            report_lines.append(f"- Current Percentage: {self.df['percentage'].iloc[-1]:.1f}%")
            if len(self.df) > 1:
                report_lines.append(f"- Percentage Point Increase: {self.df['percentage'].iloc[-1] - self.df['percentage'].iloc[0]:.1f} points")
                report_lines.append(f"- Average Annual Growth: {pct_growth['percentage_growth'].mean():.1f}%")
        
        return "\n".join(report_lines)

# Example usage
if __name__ == "__main__":
    # Sample data (PDC Brush's reported data as example)
    sample_data = {
        '2018': {'volume': 850, 'percentage': 12.5},
        '2019': {'volume': 920, 'percentage': 13.8},
        '2020': {'volume': 1050, 'percentage': 15.2},
        '2021': {'volume': 1200, 'percentage': 17.6},
        '2022': {'volume': 1350, 'percentage': 19.3}
    }
    
    try:
        # Initialize analyzer
        analyzer = FSCCertifiedWoodAnalyzer(sample_data)
        
        # Generate and print report
        print(analyzer.generate_report())
        
        # Plot volume growth
        analyzer.plot_growth(metric='volume')
        
        # Plot percentage growth
        analyzer.plot_growth(metric='percentage')
        
    except Exception as e:
        logger.error(f"Error in analysis: {e}")
```
