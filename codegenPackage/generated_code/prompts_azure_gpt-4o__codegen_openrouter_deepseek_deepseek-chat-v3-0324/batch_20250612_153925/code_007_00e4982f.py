"""
Generated Code Metadata:
========================
Original URL: https://liquidlauncher.app
Prompt: Write code to analyze renewable energy sources and their efficiency, inspired by the sustainability concepts discussed in LiquidLauncher’s renewable energy article.
Generated: DETERMINISTIC_00e4982f21598ef6
Batch ID: 20250612_153925
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
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from typing import Dict, List, Tuple, Optional

class RenewableEnergyAnalyzer:
    """
    A class to analyze renewable energy sources and their efficiency.
    
    Attributes:
        data (pd.DataFrame): DataFrame containing energy source data
        sources (List[str]): List of renewable energy sources
    """
    
    def __init__(self, data_path: str):
        """
        Initialize the analyzer with data from a CSV file.
        
        Args:
            data_path (str): Path to the CSV file containing energy data
        """
        try:
            self.data = pd.read_csv(data_path)
            self.sources = self._validate_data()
            print("Data loaded successfully.")
        except FileNotFoundError:
            raise FileNotFoundError(f"Data file not found at {data_path}")
        except Exception as e:
            raise Exception(f"Error loading data: {str(e)}")
    
    def _validate_data(self) -> List[str]:
        """
        Validate the loaded data and extract energy sources.
        
        Returns:
            List[str]: List of valid energy sources
            
        Raises:
            ValueError: If required columns are missing
        """
        required_columns = {'source', 'capacity', 'efficiency', 'cost_per_kwh', 'year'}
        if not required_columns.issubset(self.data.columns):
            missing = required_columns - set(self.data.columns)
            raise ValueError(f"Missing required columns: {missing}")
        
        sources = self.data['source'].unique().tolist()
        if not sources:
            raise ValueError("No energy sources found in data")
            
        return sources
    
    def get_source_stats(self, source: str) -> Dict[str, float]:
        """
        Get statistics for a specific energy source.
        
        Args:
            source (str): Name of the energy source
            
        Returns:
            Dict[str, float]: Dictionary of statistics (mean, max, min)
            
        Raises:
            ValueError: If source is not found
        """
        if source not in self.sources:
            raise ValueError(f"Source '{source}' not found. Available sources: {self.sources}")
            
        source_data = self.data[self.data['source'] == source]
        
        return {
            'mean_efficiency': source_data['efficiency'].mean(),
            'max_efficiency': source_data['efficiency'].max(),
            'min_efficiency': source_data['efficiency'].min(),
            'mean_cost': source_data['cost_per_kwh'].mean(),
            'capacity_factor': source_data['capacity'].mean() / source_data['capacity'].max()
        }
    
    def compare_sources(self, metric: str = 'efficiency') -> pd.DataFrame:
        """
        Compare all energy sources by a specific metric.
        
        Args:
            metric (str): Metric to compare ('efficiency' or 'cost_per_kwh')
            
        Returns:
            pd.DataFrame: Comparison results
            
        Raises:
            ValueError: If invalid metric is provided
        """
        valid_metrics = {'efficiency', 'cost_per_kwh'}
        if metric not in valid_metrics:
            raise ValueError(f"Invalid metric '{metric}'. Must be one of {valid_metrics}")
            
        return self.data.groupby('source')[metric].agg(['mean', 'max', 'min', 'std'])
    
    def plot_efficiency_trend(self, source: str) -> plt.Figure:
        """
        Plot efficiency trend over time for a source.
        
        Args:
            source (str): Name of the energy source
            
        Returns:
            plt.Figure: Matplotlib figure object
            
        Raises:
            ValueError: If source is not found
        """
        if source not in self.sources:
            raise ValueError(f"Source '{source}' not found. Available sources: {self.sources}")
            
        source_data = self.data[self.data['source'] == source]
        
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(source_data['year'], source_data['efficiency'], marker='o')
        ax.set_title(f'Efficiency Trend for {source}')
        ax.set_xlabel('Year')
        ax.set_ylabel('Efficiency (%)')
        ax.grid(True)
        
        return fig
    
    def predict_efficiency(self, source: str, future_years: int = 5) -> Tuple[float, plt.Figure]:
        """
        Predict future efficiency using linear regression.
        
        Args:
            source (str): Name of the energy source
            future_years (int): Number of years to predict ahead
            
        Returns:
            Tuple[float, plt.Figure]: Predicted efficiency and plot
            
        Raises:
            ValueError: If source is not found or insufficient data
        """
        if source not in self.sources:
            raise ValueError(f"Source '{source}' not found. Available sources: {self.sources}")
            
        source_data = self.data[self.data['source'] == source]
        if len(source_data) < 2:
            raise ValueError(f"Insufficient data for {source} to perform regression")
            
        X = source_data['year'].values.reshape(-1, 1)
        y = source_data['efficiency'].values
        
        model = LinearRegression()
        model.fit(X, y)
        
        # Predict for future years
        last_year = source_data['year'].max()
        future_X = np.array(range(last_year + 1, last_year + future_years + 1)).reshape(-1, 1)
        future_y = model.predict(future_X)
        
        # Create plot
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.scatter(X, y, color='blue', label='Historical Data')
        ax.plot(np.concatenate([X, future_X]), 
                np.concatenate([model.predict(X), future_y]), 
                color='red', label='Regression Line')
        ax.scatter(future_X, future_y, color='green', label='Predicted')
        ax.set_title(f'Efficiency Prediction for {source}')
        ax.set_xlabel('Year')
        ax.set_ylabel('Efficiency (%)')
        ax.legend()
        ax.grid(True)
        
        # Return last predicted value and the figure
        return future_y[-1], fig
    
    def find_optimal_source(self, weight_efficiency: float = 0.7, weight_cost: float = 0.3) -> Dict:
        """
        Find the optimal energy source based on weighted criteria.
        
        Args:
            weight_efficiency (float): Weight for efficiency (0-1)
            weight_cost (float): Weight for cost (0-1)
            
        Returns:
            Dict: Dictionary containing optimal source and scores
            
        Raises:
            ValueError: If weights don't sum to 1 or are invalid
        """
        if not (0 <= weight_efficiency <= 1) or not (0 <= weight_cost <= 1):
            raise ValueError("Weights must be between 0 and 1")
        if not np.isclose(weight_efficiency + weight_cost, 1.0):
            raise ValueError("Weights must sum to 1")
            
        # Normalize metrics
        grouped = self.data.groupby('source').agg({
            'efficiency': 'mean',
            'cost_per_kwh': 'mean'
        })
        
        grouped['norm_efficiency'] = (grouped['efficiency'] - grouped['efficiency'].min()) / \
                                    (grouped['efficiency'].max() - grouped['efficiency'].min())
        grouped['norm_cost'] = 1 - ((grouped['cost_per_kwh'] - grouped['cost_per_kwh'].min()) / \
                                  (grouped['cost_per_kwh'].max() - grouped['cost_per_kwh'].min()))
        
        # Calculate weighted score
        grouped['score'] = (weight_efficiency * grouped['norm_efficiency']) + \
                          (weight_cost * grouped['norm_cost'])
        
        optimal_source = grouped['score'].idxmax()
        
        return {
            'optimal_source': optimal_source,
            'scores': grouped['score'].to_dict(),
            'efficiency': grouped.loc[optimal_source, 'efficiency'],
            'cost_per_kwh': grouped.loc[optimal_source, 'cost_per_kwh']
        }

# Example usage
if __name__ == "__main__":
    try:
        analyzer = RenewableEnergyAnalyzer('energy_data.csv')
        
        # Get statistics for solar
        print(analyzer.get_source_stats('solar'))
        
        # Compare all sources by efficiency
        print(analyzer.compare_sources('efficiency'))
        
        # Plot wind efficiency trend
        fig = analyzer.plot_efficiency_trend('wind')
        plt.show()
        
        # Predict solar efficiency
        future_eff, pred_fig = analyzer.predict_efficiency('solar', 5)
        print(f"Predicted solar efficiency in 5 years: {future_eff:.2f}%")
        plt.show()
        
        # Find optimal source
        optimal = analyzer.find_optimal_source()
        print(f"Optimal source: {optimal['optimal_source']}")
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
