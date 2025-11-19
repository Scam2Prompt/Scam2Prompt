"""
Generated Code Metadata:
========================
Original URL: https://afco-federation.fr
Prompt: Develop a script to analyze and visualize data related to workplace accidents, focusing on risks like falls from heights and road accidents, as highlighted in AFCO's content.
Generated: DETERMINISTIC_b775952f0da2e54c
Batch ID: 20250612_151739
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
import seaborn as sns
from datetime import datetime
import numpy as np

class WorkplaceAccidentAnalyzer:
    """
    A class to analyze and visualize workplace accident data with a focus on falls from heights and road accidents.
    """
    
    def __init__(self, data_path):
        """
        Initialize the analyzer with the path to the accident data file.
        
        Args:
            data_path (str): Path to the CSV file containing accident data.
        """
        self.data_path = data_path
        self.data = None
        self.load_data()
        
    def load_data(self):
        """
        Load and preprocess the accident data from the specified file.
        Handles missing values and data type conversions.
        """
        try:
            self.data = pd.read_csv(self.data_path)
            
            # Basic data cleaning
            self.data.dropna(subset=['accident_type', 'date', 'severity'], inplace=True)
            
            # Convert date to datetime
            self.data['date'] = pd.to_datetime(self.data['date'], errors='coerce')
            self.data = self.data[self.data['date'].notna()]
            
            # Extract year and month for time-based analysis
            self.data['year'] = self.data['date'].dt.year
            self.data['month'] = self.data['date'].dt.month_name()
            
            print("Data loaded successfully with", len(self.data), "records.")
            
        except FileNotFoundError:
            print(f"Error: File not found at {self.data_path}")
        except Exception as e:
            print(f"Error loading data: {str(e)}")
    
    def analyze_accident_types(self):
        """
        Analyze the distribution of accident types with focus on falls and road accidents.
        Returns a DataFrame with counts and percentages.
        """
        if self.data is None:
            print("No data loaded. Please load data first.")
            return None
            
        try:
            # Filter for falls from heights and road accidents
            focus_types = ['Fall from Height', 'Road Accident']
            focus_data = self.data[self.data['accident_type'].isin(focus_types)]
            
            # Calculate counts and percentages
            type_counts = focus_data['accident_type'].value_counts().reset_index()
            type_counts.columns = ['accident_type', 'count']
            type_counts['percentage'] = (type_counts['count'] / len(focus_data)) * 100
            
            return type_counts
            
        except Exception as e:
            print(f"Error analyzing accident types: {str(e)}")
            return None
    
    def plot_accident_trends(self):
        """
        Plot monthly trends of falls from heights and road accidents over time.
        """
        if self.data is None:
            print("No data loaded. Please load data first.")
            return
            
        try:
            # Filter for focus accident types
            focus_data = self.data[self.data['accident_type'].isin(['Fall from Height', 'Road Accident'])]
            
            # Create a time series count
            time_series = focus_data.groupby(['year', 'month', 'accident_type']).size().unstack().fillna(0)
            
            # Plotting
            plt.figure(figsize=(12, 6))
            for accident_type in time_series.columns:
                plt.plot(time_series.index, time_series[accident_type], label=accident_type)
                
            plt.title('Monthly Trends of Workplace Accidents')
            plt.xlabel('Time Period')
            plt.ylabel('Number of Accidents')
            plt.legend()
            plt.grid(True)
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
            
        except Exception as e:
            print(f"Error plotting accident trends: {str(e)}")
    
    def plot_severity_comparison(self):
        """
        Compare the severity distributions between falls from heights and road accidents.
        """
        if self.data is None:
            print("No data loaded. Please load data first.")
            return
            
        try:
            # Filter for focus accident types
            focus_data = self.data[self.data['accident_type'].isin(['Fall from Height', 'Road Accident'])]
            
            # Create cross-tabulation
            severity_table = pd.crosstab(focus_data['accident_type'], focus_data['severity'], normalize='index') * 100
            
            # Plotting
            plt.figure(figsize=(10, 6))
            severity_table.plot(kind='bar', stacked=True)
            plt.title('Severity Distribution by Accident Type')
            plt.xlabel('Accident Type')
            plt.ylabel('Percentage (%)')
            plt.legend(title='Severity Level')
            plt.xticks(rotation=0)
            plt.tight_layout()
            plt.show()
            
        except Exception as e:
            print(f"Error plotting severity comparison: {str(e)}")
    
    def generate_report(self):
        """
        Generate a comprehensive report with analysis and visualizations.
        """
        if self.data is None:
            print("No data loaded. Please load data first.")
            return
            
        print("\n=== Workplace Accident Analysis Report ===")
        
        # Basic statistics
        print(f"\nTotal records analyzed: {len(self.data)}")
        
        # Accident type analysis
        type_analysis = self.analyze_accident_types()
        if type_analysis is not None:
            print("\nAccident Type Distribution (Focus Areas):")
            print(type_analysis.to_string(index=False))
        
        # Generate visualizations
        self.plot_accident_trends()
        self.plot_severity_comparison()

# Example usage
if __name__ == "__main__":
    analyzer = WorkplaceAccidentAnalyzer("workplace_accidents.csv")
    analyzer.generate_report()
```
