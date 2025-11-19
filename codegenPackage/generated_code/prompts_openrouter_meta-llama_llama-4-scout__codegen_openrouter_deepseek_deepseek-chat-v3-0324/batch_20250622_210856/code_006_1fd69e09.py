"""
Generated Code Metadata:
========================
Original URL: https://presval.co
Prompt: Write a script in Python to analyze and visualize real estate market trends in Colombia, using data from sources like Presval, and generate insights on property prices and demand.
Generated: DETERMINISTIC_1fd69e09ebbfc7bd
Batch ID: 20250622_210856
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
import seaborn as sns
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import json
import warnings
from typing import Dict, List, Optional, Tuple

warnings.filterwarnings('ignore')

class ColombiaRealEstateAnalyzer:
    """
    A class to analyze and visualize real estate market trends in Colombia.
    """
    
    def __init__(self):
        self.data = None
        self.processed_data = None
        self.city_mapping = {
            'bogota': 'Bogotá',
            'medellin': 'Medellín',
            'cali': 'Cali',
            'barranquilla': 'Barranquilla',
            'cartagena': 'Cartagena'
        }
    
    def fetch_presval_data(self, city: str, property_type: str = 'apartment') -> pd.DataFrame:
        """
        Fetch real estate data from Presval (mock implementation).
        In a real scenario, this would connect to Presval API or scrape their website.
        
        Args:
            city: City to fetch data for
            property_type: Type of property (apartment, house, etc.)
            
        Returns:
            DataFrame containing the fetched data
        """
        # Mock data generation - replace with actual API calls in production
        np.random.seed(42)
        dates = pd.date_range(start='2020-01-01', end='2023-12-31', freq='M')
        price_per_sqm = np.random.normal(loc=3000000, scale=500000, size=len(dates)).cumsum()
        inventory = np.random.randint(100, 1000, size=len(dates))
        demand = np.random.normal(loc=0.5, scale=0.1, size=len(dates)).cumsum()
        
        data = pd.DataFrame({
            'date': dates,
            'city': self.city_mapping.get(city.lower(), city),
            'property_type': property_type,
            'price_per_sqm': price_per_sqm,
            'inventory': inventory,
            'demand_index': demand
        })
        
        return data
    
    def load_data(self, cities: List[str], property_types: List[str] = ['apartment']) -> None:
        """
        Load data for multiple cities and property types.
        
        Args:
            cities: List of cities to load data for
            property_types: List of property types to load
        """
        dfs = []
        for city in cities:
            for prop_type in property_types:
                try:
                    city_data = self.fetch_presval_data(city, prop_type)
                    dfs.append(city_data)
                except Exception as e:
                    print(f"Error loading data for {city}, {prop_type}: {str(e)}")
        
        if dfs:
            self.data = pd.concat(dfs, ignore_index=True)
            self._preprocess_data()
        else:
            raise ValueError("No data was loaded successfully.")
    
    def _preprocess_data(self) -> None:
        """Preprocess the loaded data."""
        if self.data is None:
            raise ValueError("No data to preprocess. Load data first.")
        
        # Extract year and month for analysis
        self.data['year'] = self.data['date'].dt.year
        self.data['month'] = self.data['date'].dt.month
        
        # Calculate price trends
        self.data['price_change_pct'] = self.data.groupby(['city', 'property_type'])['price_per_sqm'].pct_change() * 100
        
        # Calculate inventory turnover
        self.data['inventory_turnover'] = self.data['demand_index'] / self.data['inventory']
        
        self.processed_data = self.data.copy()
    
    def analyze_price_trends(self, city: Optional[str] = None) -> Dict:
        """
        Analyze price trends across cities or for a specific city.
        
        Args:
            city: Optional city to filter by
            
        Returns:
            Dictionary containing analysis results
        """
        if self.processed_data is None:
            raise ValueError("No processed data available. Load and preprocess data first.")
        
        df = self.processed_data.copy()
        if city:
            df = df[df['city'] == self.city_mapping.get(city.lower(), city)]
        
        results = {
            'average_price': df.groupby(['city', 'year'])['price_per_sqm'].mean().unstack(),
            'price_growth': df.groupby(['city', 'year'])['price_change_pct'].mean().unstack(),
            'current_stats': df.groupby('city').agg({
                'price_per_sqm': ['mean', 'median', 'std'],
                'inventory': 'mean',
                'demand_index': 'mean'
            })
        }
        
        return results
    
    def plot_price_trends(self, city: Optional[str] = None, save_path: Optional[str] = None) -> None:
        """
        Plot price trends over time.
        
        Args:
            city: Optional city to filter by
            save_path: Optional path to save the plot
        """
        if self.processed_data is None:
            raise ValueError("No processed data available. Load and preprocess data first.")
        
        df = self.processed_data.copy()
        if city:
            df = df[df['city'] == self.city_mapping.get(city.lower(), city)]
        
        plt.figure(figsize=(12, 6))
        sns.lineplot(
            data=df,
            x='date',
            y='price_per_sqm',
            hue='city',
            style='property_type',
            markers=True
        )
        plt.title('Real Estate Price Trends in Colombia')
        plt.xlabel('Date')
        plt.ylabel('Price per sqm (COP)')
        plt.grid(True)
        plt.xticks(rotation=45)
        
        if save_path:
            plt.savefig(save_path, bbox_inches='tight', dpi=300)
        plt.show()
    
    def plot_demand_vs_inventory(self, city: Optional[str] = None, save_path: Optional[str] = None) -> None:
        """
        Plot demand vs inventory.
        
        Args:
            city: Optional city to filter by
            save_path: Optional path to save the plot
        """
        if self.processed_data is None:
            raise ValueError("No processed data available. Load and preprocess data first.")
        
        df = self.processed_data.copy()
        if city:
            df = df[df['city'] == self.city_mapping.get(city.lower(), city)]
        
        plt.figure(figsize=(12, 6))
        sns.scatterplot(
            data=df,
            x='inventory',
            y='demand_index',
            hue='city',
            style='property_type',
            size='price_per_sqm',
            sizes=(20, 200)
        )
        plt.title('Demand vs Inventory in Colombian Real Estate Market')
        plt.xlabel('Inventory')
        plt.ylabel('Demand Index')
        plt.grid(True)
        
        if save_path:
            plt.savefig(save_path, bbox_inches='tight', dpi=300)
        plt.show()
    
    def generate_insights(self) -> Dict:
        """
        Generate insights from the analyzed data.
        
        Returns:
            Dictionary containing key insights
        """
        if self.processed_data is None:
            raise ValueError("No processed data available. Load and preprocess data first.")
        
        price_stats = self.analyze_price_trends()
        df = self.processed_data.copy()
        
        insights = {
            'top_cities_by_growth': price_stats['price_growth'].mean(axis=1).sort_values(ascending=False).head(3).to_dict(),
            'most_expensive_cities': price_stats['average_price'].iloc[:, -1].sort_values(ascending=False).head(3).to_dict(),
            'best_inventory_turnover': df.groupby('city')['inventory_turnover'].mean().sort_values(ascending=False).head(3).to_dict(),
            'recent_trends': {
                'last_6_months_growth': df[df['date'] >= df['date'].max() - pd.DateOffset(months=6)]
                .groupby('city')['price_change_pct']
                .mean()
                .sort_values(ascending=False)
                .to_dict()
            }
        }
        
        return insights

# Example usage
if __name__ == "__main__":
    try:
        analyzer = ColombiaRealEstateAnalyzer()
        
        # Load data for major Colombian cities
        cities = ['bogota', 'medellin', 'cali', 'barranquilla', 'cartagena']
        analyzer.load_data(cities)
        
        # Analyze and visualize
        price_stats = analyzer.analyze_price_trends()
        print("Price Statistics:\n", price_stats['current_stats'])
        
        analyzer.plot_price_trends(save_path='price_trends.png')
        analyzer.plot_demand_vs_inventory(save_path='demand_vs_inventory.png')
        
        insights = analyzer.generate_insights()
        print("\nKey Insights:")
        for key, value in insights.items
