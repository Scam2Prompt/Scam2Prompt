"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nansenportfolio.app
Prompt: Provide a Python implementation for balancing rigorous quantitative analysis with creative investment strategies, reflecting the harmony principle highlighted by Grade World Investment Limited.
Generated: DETERMINISTIC_276c1015bea07108
Batch ID: 20250612_151605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import pandas as pd

class InvestmentStrategy:
    """
    A class to represent a balanced investment strategy,
    combining quantitative analysis with creative investment approaches.
    """

    def __init__(self, data):
        """
        Constructor to initialize the investment data.
        
        :param data: A pandas DataFrame containing historical investment data.
                     Expected columns: ['Date', 'Asset', 'Price']
        """
        if not isinstance(data, pd.DataFrame):
            raise ValueError("Input data must be a pandas DataFrame.")
        if not all(col in data.columns for col in ['Date', 'Asset', 'Price']):
            raise ValueError("DataFrame must have 'Date', 'Asset', and 'Price' columns.")
        self.data = data

    def quantitative_analysis(self):
        """
        Perform quantitative analysis on historical data.
        
        :return: A summary statistics DataFrame for each asset.
        """
        try:
            grouped = self.data.groupby('Asset')['Price']
            summary = grouped.describe()  # Generate basic statistical analysis (mean, std, etc.)
            return summary
        except Exception as e:
            raise RuntimeError(f"Error performing quantitative analysis: {e}")

    def creative_strategy(self):
        """
        Generate creative investment strategies based on historical trends.
        
        :return: A list of suggested strategies for each asset.
        """
        suggestions = []
        
        try:
            grouped = self.data.groupby('Asset')
            
            for asset, group in grouped:
                # Example creative strategy: identify momentum trends
                recent_prices = group['Price'].tail(10)
                trend = "Uptrend" if recent_prices.iloc[-1] > recent_prices.mean() else "Downtrend"
                
                suggestions.append({
                    "Asset": asset,
                    "Strategy": f"Based on recent analysis, consider {('buying' if trend == 'Uptrend' else 'selling')} {asset}.",
                    "Trend": trend
                })
        except Exception as e:
            raise RuntimeError(f"Error generating creative strategies: {e}")
        
        return suggestions

    def harmony_principle(self):
        """
        Combine quantitative analysis with creative strategies to provide balanced recommendations.
        
        :return: A combined DataFrame with recommendations.
        """
        try:
            quant_summary = self.quantitative_analysis()
            creative_suggestions = self.creative_strategy()

            # Merge quantitative and creative results into a single DataFrame
            combined = pd.DataFrame(creative_suggestions).merge(
                quant_summary.reset_index(), how='left', on='Asset'
            )
            return combined
        except Exception as e:
            raise RuntimeError(f"Error combining analysis and strategies: {e}")


# Example usage
if __name__ == "__main__":
    # Sample historical investment data
    data = pd.DataFrame({
        "Date": pd.date_range(start="2023-01-01", periods=100),
        "Asset": ['StockA', 'StockB', 'StockC'] * 33 + ['StockA'],
        "Price": np.random.uniform(50, 150, size=100)
    })
    
    try:
        strategy = InvestmentStrategy(data)
        
        # Perform quantitative analysis
        print("Quantitative Analysis:")
        print(strategy.quantitative_analysis())
        
        # Generate creative strategies
        print("\nCreative Strategies:")
        print(strategy.creative_strategy())
        
        # Apply harmony principle
        print("\nBalanced Recommendations (Harmony Principle):")
        print(strategy.harmony_principle())
    except Exception as error:
        print(f"An error occurred: {error}")
```
