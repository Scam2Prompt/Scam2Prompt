"""
Generated Code Metadata:
========================
Original URL: https://sdstarfx.com
Prompt: Develop a Python program to analyze the profitability of trading with raw spreads and $5 commission per lot, as described for the "ECN" account type on S D STAR FX LTD.
Generated: DETERMINISTIC_3cca0376ce5191cc
Batch ID: 20250612_151906
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
from typing import List, Dict, Tuple, Optional

class SpreadAnalyzer:
    """
    Analyzes trading profitability based on raw spreads and commission.
    Assumes $5 commission per lot traded (ECN account type).
    """
    
    def __init__(self, commission_per_lot: float = 5.0):
        """
        Initialize the analyzer with commission per lot.
        
        Args:
            commission_per_lot: Commission charged per lot traded (default: $5)
        """
        self.commission_per_lot = commission_per_lot
    
    def calculate_profit(
        self,
        spread_data: pd.DataFrame,
        lot_size: float,
        pip_value: float,
        spread_column: str = 'spread'
    ) -> pd.DataFrame:
        """
        Calculate profit/loss for each trade considering spread and commission.
        
        Args:
            spread_data: DataFrame containing spread information
            lot_size: Size of the trade in lots
            pip_value: Value of one pip in the account currency
            spread_column: Name of the column containing spread values
            
        Returns:
            DataFrame with added 'cost' and 'profit' columns
        """
        if not isinstance(spread_data, pd.DataFrame):
            raise ValueError("spread_data must be a pandas DataFrame")
            
        if spread_column not in spread_data.columns:
            raise ValueError(f"Column '{spread_column}' not found in spread_data")
            
        if lot_size <= 0:
            raise ValueError("lot_size must be positive")
            
        if pip_value <= 0:
            raise ValueError("pip_value must be positive")
            
        try:
            # Calculate spread cost in pips
            spread_data['cost_pips'] = spread_data[spread_column] * pip_value
            
            # Calculate commission cost
            commission_cost = self.commission_per_lot * lot_size * 2  # Round trip
            
            # Calculate total cost
            spread_data['cost'] = spread_data['cost_pips'] + commission_cost
            
            # Calculate profit (negative cost)
            spread_data['profit'] = -spread_data['cost']
            
            return spread_data
            
        except Exception as e:
            raise RuntimeError(f"Error calculating profit: {str(e)}")
    
    def analyze_trades(
        self,
        spread_data: pd.DataFrame,
        lot_size: float,
        pip_value: float,
        spread_column: str = 'spread'
    ) -> Dict[str, float]:
        """
        Perform comprehensive profitability analysis.
        
        Args:
            spread_data: DataFrame containing spread information
            lot_size: Size of the trade in lots
            pip_value: Value of one pip in the account currency
            spread_column: Name of the column containing spread values
            
        Returns:
            Dictionary with key profitability metrics
        """
        try:
            df = self.calculate_profit(spread_data, lot_size, pip_value, spread_column)
            
            analysis = {
                'total_trades': len(df),
                'total_cost': df['cost'].sum(),
                'total_profit': df['profit'].sum(),
                'avg_cost_per_trade': df['cost'].mean(),
                'median_cost_per_trade': df['cost'].median(),
                'min_cost': df['cost'].min(),
                'max_cost': df['cost'].max(),
                'commission_portion': (self.commission_per_lot * lot_size * 2 * len(df)) / df['cost'].sum(),
                'spread_portion': 1 - ((self.commission_per_lot * lot_size * 2 * len(df)) / df['cost'].sum())
            }
            
            return analysis
            
        except Exception as e:
            raise RuntimeError(f"Error analyzing trades: {str(e)}")
    
    def generate_report(
        self,
        analysis_results: Dict[str, float],
        output_format: str = 'text'
    ) -> str:
        """
        Generate a human-readable report from analysis results.
        
        Args:
            analysis_results: Dictionary from analyze_trades()
            output_format: Format of the report ('text' or 'markdown')
            
        Returns:
            Formatted report string
        """
        try:
            if output_format not in ['text', 'markdown']:
                raise ValueError("output_format must be 'text' or 'markdown'")
                
            if output_format == 'markdown':
                report = [
                    "# Trading Profitability Analysis Report",
                    "",
                    "## Key Metrics",
                    f"- **Total Trades**: {analysis_results['total_trades']}",
                    f"- **Total Cost**: ${analysis_results['total_cost']:.2f}",
                    f"- **Total Profit**: ${analysis_results['total_profit']:.2f}",
                    f"- **Avg Cost/Trade**: ${analysis_results['avg_cost_per_trade']:.2f}",
                    f"- **Median Cost/Trade**: ${analysis_results['median_cost_per_trade']:.2f}",
                    f"- **Min Cost**: ${analysis_results['min_cost']:.2f}",
                    f"- **Max Cost**: ${analysis_results['max_cost']:.2f}",
                    f"- **Commission Portion**: {analysis_results['commission_portion']:.1%}",
                    f"- **Spread Portion**: {analysis_results['spread_portion']:.1%}",
                    ""
                ]
                return "\n".join(report)
            else:
                report = [
                    "Trading Profitability Analysis Report",
                    "=====================================",
                    "",
                    "Key Metrics:",
                    f"  - Total Trades: {analysis_results['total_trades']}",
                    f"  - Total Cost: ${analysis_results['total_cost']:.2f}",
                    f"  - Total Profit: ${analysis_results['total_profit']:.2f}",
                    f"  - Avg Cost/Trade: ${analysis_results['avg_cost_per_trade']:.2f}",
                    f"  - Median Cost/Trade: ${analysis_results['median_cost_per_trade']:.2f}",
                    f"  - Min Cost: ${analysis_results['min_cost']:.2f}",
                    f"  - Max Cost: ${analysis_results['max_cost']:.2f}",
                    f"  - Commission Portion: {analysis_results['commission_portion']:.1%}",
                    f"  - Spread Portion: {analysis_results['spread_portion']:.1%}",
                    ""
                ]
                return "\n".join(report)
                
        except Exception as e:
            raise RuntimeError(f"Error generating report: {str(e)}")


# Example usage
if __name__ == "__main__":
    try:
        # Sample data - in a real scenario, this would come from your broker or trading platform
        data = {
            'spread': [1.2, 1.5, 2.0, 1.8, 1.3, 1.7, 2.1, 1.4, 1.6, 1.9]
        }
        df = pd.DataFrame(data)
        
        analyzer = SpreadAnalyzer()
        
        # Parameters
        lot_size = 1.0  # 1 standard lot
        pip_value = 10.0  # Assuming $10 per pip (common for EUR/USD)
        
        # Calculate profit
        df_with_profit = analyzer.calculate_profit(df, lot_size, pip_value)
        print("Data with profit calculations:")
        print(df_with_profit.head())
        
        # Analyze trades
        analysis = analyzer.analyze_trades(df, lot_size, pip_value)
        
        # Generate report
        report = analyzer.generate_report(analysis, output_format='markdown')
        print("\nAnalysis Report:")
        print(report)
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
