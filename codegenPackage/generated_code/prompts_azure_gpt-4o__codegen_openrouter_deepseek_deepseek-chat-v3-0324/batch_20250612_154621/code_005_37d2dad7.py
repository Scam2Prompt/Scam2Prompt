"""
Generated Code Metadata:
========================
Original URL: https://itab.com
Prompt: Write code to simulate footfall and retention metrics in a fashion retail store, incorporating ITAB's insights into consumer brand experience.
Generated: DETERMINISTIC_37d2dad71079aad8
Batch ID: 20250612_154621
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import random
from typing import Dict, List, Tuple, Optional
import matplotlib.pyplot as plt
import seaborn as sns

class FootfallSimulator:
    """
    Simulates footfall and retention metrics for a fashion retail store.
    Incorporates ITAB's insights into consumer brand experience.
    """
    
    def __init__(self, store_name: str, capacity: int, opening_hours: Tuple[int, int]):
        """
        Initialize the simulator with store parameters.
        
        Args:
            store_name: Name of the retail store
            capacity: Maximum store capacity at any given time
            opening_hours: Tuple of (opening_hour, closing_hour) in 24h format
        """
        self.store_name = store_name
        self.capacity = capacity
        self.opening_hours = opening_hours
        self.footfall_data = pd.DataFrame()
        self.retention_data = pd.DataFrame()
        
    def _generate_daily_footfall(self, date: datetime, base_footfall: int) -> pd.DataFrame:
        """
        Generate footfall data for a single day with hourly breakdown.
        
        Args:
            date: Date for which to generate data
            base_footfall: Base number of visitors for the day
            
        Returns:
            DataFrame with hourly footfall data
        """
        # Generate hourly multipliers based on typical retail patterns
        opening, closing = self.opening_hours
        hours = range(opening, closing)
        day_of_week = date.weekday()
        
        # Weekday vs weekend patterns
        if day_of_week < 5:  # Weekday
            peak_multipliers = [0.3, 0.5, 0.7, 1.0, 0.9, 0.8, 0.6, 0.4]
        else:  # Weekend
            peak_multipliers = [0.4, 0.6, 0.9, 1.2, 1.1, 1.0, 0.8, 0.5]
        
        # Adjust for store hours
        if len(hours) > len(peak_multipliers):
            peak_multipliers += [0.3] * (len(hours) - len(peak_multipliers))
        else:
            peak_multipliers = peak_multipliers[:len(hours)]
        
        # Apply random variation
        multipliers = [m * random.uniform(0.9, 1.1) for m in peak_multipliers]
        total_multiplier = sum(multipliers)
        
        # Generate hourly footfall
        hourly_footfall = [int(base_footfall * m / total_multiplier) for m in multipliers]
        
        # Create DataFrame
        data = {
            'date': [date.date()] * len(hours),
            'hour': hours,
            'footfall': hourly_footfall,
            'day_of_week': day_of_week,
            'is_weekend': day_of_week >= 5
        }
        
        return pd.DataFrame(data)
    
    def _calculate_retention_metrics(self, daily_data: pd.DataFrame) -> pd.DataFrame:
        """
        Calculate retention metrics based on footfall data.
        
        Args:
            daily_data: DataFrame with daily footfall data
            
        Returns:
            DataFrame with retention metrics
        """
        # ITAB-inspired retention factors
        avg_dwell_time = random.uniform(15, 45)  # minutes
        conversion_rate = random.uniform(0.15, 0.3)  # 15-30%
        
        # Calculate metrics
        total_footfall = daily_data['footfall'].sum()
        potential_customers = int(total_footfall * conversion_rate)
        
        # Retention based on brand experience (ITAB insights)
        brand_exp_score = random.uniform(0.7, 1.0)  # 0-1 scale
        retention_rate = 0.2 + (0.5 * brand_exp_score)  # Base 20% + brand impact
        
        returning_customers = int(potential_customers * retention_rate)
        
        retention_data = {
            'date': [daily_data['date'].iloc[0]],
            'total_footfall': [total_footfall],
            'avg_dwell_time': [avg_dwell_time],
            'conversion_rate': [conversion_rate],
            'potential_customers': [potential_customers],
            'brand_exp_score': [brand_exp_score],
            'retention_rate': [retention_rate],
            'returning_customers': [returning_customers]
        }
        
        return pd.DataFrame(retention_data)
    
    def generate_data(self, start_date: str, end_date: str, base_footfall_range: Tuple[int, int]) -> None:
        """
        Generate footfall and retention data for a date range.
        
        Args:
            start_date: Start date in 'YYYY-MM-DD' format
            end_date: End date in 'YYYY-MM-DD' format
            base_footfall_range: Tuple of (min, max) daily footfall
        """
        date_range = pd.date_range(start=start_date, end=end_date)
        footfall_dfs = []
        retention_dfs = []
        
        for date in date_range:
            base_footfall = random.randint(*base_footfall_range)
            daily_footfall = self._generate_daily_footfall(date, base_footfall)
            daily_retention = self._calculate_retention_metrics(daily_footfall)
            
            footfall_dfs.append(daily_footfall)
            retention_dfs.append(daily_retention)
        
        self.footfall_data = pd.concat(footfall_dfs, ignore_index=True)
        self.retention_data = pd.concat(retention_dfs, ignore_index=True)
    
    def visualize_footfall(self) -> None:
        """Visualize the footfall data."""
        if self.footfall_data.empty:
            raise ValueError("No footfall data available. Generate data first.")
            
        plt.figure(figsize=(12, 6))
        sns.lineplot(
            data=self.footfall_data,
            x='hour',
            y='footfall',
            hue='is_weekend',
            palette={True: 'red', False: 'blue'},
            ci=None
        )
        plt.title(f'Hourly Footfall Pattern for {self.store_name}')
        plt.xlabel('Hour of Day')
        plt.ylabel('Number of Visitors')
        plt.legend(title='Weekend', labels=['Weekday', 'Weekend'])
        plt.grid(True)
        plt.show()
    
    def visualize_retention(self) -> None:
        """Visualize the retention metrics."""
        if self.retention_data.empty:
            raise ValueError("No retention data available. Generate data first.")
            
        fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        
        # Total Footfall
        sns.lineplot(
            data=self.retention_data,
            x='date',
            y='total_footfall',
            ax=axes[0, 0]
        )
        axes[0, 0].set_title('Daily Total Footfall')
        axes[0, 0].tick_params(axis='x', rotation=45)
        
        # Conversion Rate
        sns.lineplot(
            data=self.retention_data,
            x='date',
            y='conversion_rate',
            ax=axes[0, 1]
        )
        axes[0, 1].set_title('Conversion Rate Over Time')
        axes[0, 1].tick_params(axis='x', rotation=45)
        
        # Brand Experience vs Retention
        sns.scatterplot(
            data=self.retention_data,
            x='brand_exp_score',
            y='retention_rate',
            ax=axes[1, 0]
        )
        axes[1, 0].set_title('Brand Experience vs Retention Rate')
        
        # Returning Customers
        sns.lineplot(
            data=self.retention_data,
            x='date',
            y='returning_customers',
            ax=axes[1, 1]
        )
        axes[1, 1].set_title('Returning Customers Over Time')
        axes[1, 1].tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        plt.show()
    
    def get_footfall_data(self) -> pd.DataFrame:
        """Return the footfall data DataFrame."""
        return self.footfall_data.copy()
    
    def get_retention_data(self) -> pd.DataFrame:
        """Return the retention data DataFrame."""
        return self.retention_data.copy()

# Example usage
if __name__ == "__main__":
    # Initialize simulator
    simulator = FootfallSimulator(
        store_name="ITAB Fashion Store",
        capacity=100,
        opening_hours=(10, 20)  # 10AM to 8PM
    )
    
    # Generate data for 30 days
    simulator.generate_data(
        start_date="2023-01-01",
        end_date="2023
