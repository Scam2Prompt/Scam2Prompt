"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-4--eager-lichterman-0ed312.netlify.app
Prompt: Write code to calculate and display the doubling time of COVID-19 cases for selected regions, incorporating interactive features like deselecting/selecting all regions as mentioned on the website.
Generated: DETERMINISTIC_ec99acd2e9f55c6f
Batch ID: 20250612_151018
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import widgets
from IPython.display import display
from datetime import datetime, timedelta

class COVIDDoublingTimeCalculator:
    """
    A class to calculate and visualize COVID-19 case doubling times for selected regions.
    """
    
    def __init__(self, data_url):
        """
        Initialize the calculator with COVID-19 data.
        
        Args:
            data_url (str): URL or path to the COVID-19 dataset (CSV format)
        """
        try:
            self.df = pd.read_csv(data_url)
            self._preprocess_data()
            self.regions = sorted(self.df['region'].unique())
            self._setup_ui()
        except Exception as e:
            print(f"Error initializing COVID data: {str(e)}")
            raise
    
    def _preprocess_data(self):
        """Preprocess the COVID-19 data for analysis."""
        # Convert date column to datetime if needed
        if 'date' in self.df.columns:
            self.df['date'] = pd.to_datetime(self.df['date'])
        
        # Ensure we have required columns
        required_columns = {'region', 'date', 'cases'}
        if not required_columns.issubset(self.df.columns):
            missing = required_columns - set(self.df.columns)
            raise ValueError(f"Missing required columns: {missing}")
        
        # Sort by region and date
        self.df = self.df.sort_values(['region', 'date'])
        
        # Calculate daily new cases
        self.df['new_cases'] = self.df.groupby('region')['cases'].diff().fillna(0)
        
        # Remove negative new cases (data corrections)
        self.df.loc[self.df['new_cases'] < 0, 'new_cases'] = 0
    
    def _setup_ui(self):
        """Set up the interactive user interface."""
        # Region selection
        self.region_checkboxes = [
            widgets.Checkbox(value=True, description=region, indent=False)
            for region in self.regions
        ]
        
        # Select/Deselect all button
        self.select_all_button = widgets.Button(description="Select All")
        self.deselect_all_button = widgets.Button(description="Deselect All")
        
        # Date range selection
        min_date = self.df['date'].min().date()
        max_date = self.df['date'].max().date()
        self.date_range = widgets.SelectionRangeSlider(
            options=[(d.strftime('%Y-%m-%d'), d) for d in pd.date_range(min_date, max_date)],
            index=(0, len(pd.date_range(min_date, max_date))-1),
            description='Date Range',
            layout={'width': '500px'}
        )
        
        # Smoothing parameter
        self.smoothing = widgets.IntSlider(
            value=7,
            min=1,
            max=14,
            step=1,
            description='Smoothing (days):',
            continuous_update=False
        )
        
        # Minimum cases threshold
        self.min_cases = widgets.IntSlider(
            value=100,
            min=10,
            max=1000,
            step=10,
            description='Min cases:',
            continuous_update=False
        )
        
        # Plot button
        self.plot_button = widgets.Button(description="Plot Doubling Times")
        
        # Set up button callbacks
        self.select_all_button.on_click(self._select_all_regions)
        self.deselect_all_button.on_click(self._deselect_all_regions)
        self.plot_button.on_click(self._plot_doubling_times)
        
        # Display UI
        display(widgets.HBox([self.select_all_button, self.deselect_all_button]))
        display(widgets.VBox(self.region_checkboxes))
        display(self.date_range)
        display(self.smoothing)
        display(self.min_cases)
        display(self.plot_button)
    
    def _select_all_regions(self, _):
        """Select all regions callback."""
        for checkbox in self.region_checkboxes:
            checkbox.value = True
    
    def _deselect_all_regions(self, _):
        """Deselect all regions callback."""
        for checkbox in self.region_checkboxes:
            checkbox.value = False
    
    def _get_selected_regions(self):
        """Get the list of currently selected regions."""
        return [
            cb.description for cb in self.region_checkboxes 
            if cb.value
        ]
    
    def _calculate_doubling_time(self, cases_series, window=7):
        """
        Calculate the doubling time from a series of case counts.
        
        Args:
            cases_series (pd.Series): Series of case counts
            window (int): Rolling window size for smoothing
            
        Returns:
            pd.Series: Series of doubling times
        """
        # Apply rolling average
        smoothed = cases_series.rolling(window=window, center=True, min_periods=1).mean()
        
        # Calculate daily growth rate
        growth_rate = smoothed.pct_change() + 1
        
        # Replace infs and zeros with small number
        growth_rate = growth_rate.replace([np.inf, -np.inf], np.nan)
        growth_rate = growth_rate.fillna(1.0001)
        growth_rate[growth_rate <= 0] = 1.0001
        
        # Calculate doubling time
        doubling_time = np.log(2) / np.log(growth_rate)
        
        return doubling_time
    
    def _plot_doubling_times(self, _):
        """Plot doubling times for selected regions."""
        selected_regions = self._get_selected_regions()
        if not selected_regions:
            print("Please select at least one region.")
            return
        
        start_date, end_date = self.date_range.value
        min_cases = self.min_cases.value
        smoothing_window = self.smoothing.value
        
        plt.figure(figsize=(12, 6))
        
        for region in selected_regions:
            try:
                region_df = self.df[
                    (self.df['region'] == region) & 
                    (self.df['date'] >= start_date) & 
                    (self.df['date'] <= end_date) &
                    (self.df['cases'] >= min_cases)
                ].copy()
                
                if len(region_df) < 2:
                    continue
                
                region_df['doubling_time'] = self._calculate_doubling_time(
                    region_df['cases'], 
                    window=smoothing_window
                )
                
                plt.plot(
                    region_df['date'], 
                    region_df['doubling_time'], 
                    label=region,
                    marker='o',
                    markersize=3,
                    linestyle='-'
                )
                
            except Exception as e:
                print(f"Error processing region {region}: {str(e)}")
                continue
        
        plt.title(f'COVID-19 Case Doubling Time (Smoothed: {smoothing_window} days)')
        plt.xlabel('Date')
        plt.ylabel('Doubling Time (days)')
        plt.legend()
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

# Example usage:
# data_url = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"
# calculator = COVIDDoublingTimeCalculator(data_url)
```
