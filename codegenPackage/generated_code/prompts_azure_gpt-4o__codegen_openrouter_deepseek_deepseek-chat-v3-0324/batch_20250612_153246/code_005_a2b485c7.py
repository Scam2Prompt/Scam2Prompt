"""
Generated Code Metadata:
========================
Original URL: https://www.gmpinvestments.co.uk
Prompt: Develop a Python script to analyze local market history and regional planning policies for property investment, leveraging the expertise highlighted by Gold Mark Investment Limited.
Generated: DETERMINISTIC_a2b485c7444291b5
Batch ID: 20250612_153246
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
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import warnings
warnings.filterwarnings('ignore')

class PropertyMarketAnalyzer:
    """
    A class to analyze local property market history and regional planning policies.
    """
    
    def __init__(self, api_key=None):
        """
        Initialize the analyzer with optional API key for data services.
        
        Args:
            api_key (str, optional): API key for data services. Defaults to None.
        """
        self.api_key = api_key
        self.property_data = None
        self.policy_data = None
        
    def load_property_data(self, file_path=None, url=None):
        """
        Load property market data from either a local file or URL.
        
        Args:
            file_path (str, optional): Path to local CSV/Excel file. Defaults to None.
            url (str, optional): URL to fetch data from. Defaults to None.
            
        Raises:
            ValueError: If neither file_path nor url is provided.
            Exception: For other loading errors.
        """
        try:
            if file_path:
                if file_path.endswith('.csv'):
                    self.property_data = pd.read_csv(file_path)
                elif file_path.endswith(('.xls', '.xlsx')):
                    self.property_data = pd.read_excel(file_path)
                else:
                    raise ValueError("Unsupported file format. Please provide CSV or Excel file.")
            elif url:
                if url.endswith('.csv'):
                    self.property_data = pd.read_csv(url)
                elif url.endswith('.json'):
                    response = requests.get(url)
                    self.property_data = pd.DataFrame(response.json())
                else:
                    # Try web scraping for HTML tables
                    response = requests.get(url)
                    soup = BeautifulSoup(response.text, 'html.parser')
                    tables = soup.find_all('table')
                    if tables:
                        self.property_data = pd.read_html(str(tables[0]))[0]
                    else:
                        raise ValueError("No tables found in the provided URL.")
            else:
                raise ValueError("Either file_path or url must be provided.")
                
            # Basic data cleaning
            self._clean_property_data()
            
        except Exception as e:
            raise Exception(f"Error loading property data: {str(e)}")
    
    def _clean_property_data(self):
        """
        Clean and preprocess property data.
        """
        if self.property_data is not None:
            # Convert date columns to datetime
            date_cols = [col for col in self.property_data.columns if 'date' in col.lower()]
            for col in date_cols:
                self.property_data[col] = pd.to_datetime(self.property_data[col], errors='coerce')
                
            # Handle missing values
            self.property_data = self.property_data.dropna(subset=['price', 'area'])
            
            # Convert price and area to numeric
            self.property_data['price'] = pd.to_numeric(self.property_data['price'], errors='coerce')
            self.property_data['area'] = pd.to_numeric(self.property_data['area'], errors='coerce')
            
            # Calculate price per square meter
            self.property_data['price_per_sqm'] = self.property_data['price'] / self.property_data['area']
    
    def load_policy_data(self, file_path=None, url=None):
        """
        Load regional planning policy data from either a local file or URL.
        
        Args:
            file_path (str, optional): Path to local CSV/Excel file. Defaults to None.
            url (str, optional): URL to fetch data from. Defaults to None.
            
        Raises:
            ValueError: If neither file_path nor url is provided.
            Exception: For other loading errors.
        """
        try:
            if file_path:
                if file_path.endswith('.csv'):
                    self.policy_data = pd.read_csv(file_path)
                elif file_path.endswith(('.xls', '.xlsx')):
                    self.policy_data = pd.read_excel(file_path)
                else:
                    raise ValueError("Unsupported file format. Please provide CSV or Excel file.")
            elif url:
                if url.endswith('.json'):
                    response = requests.get(url)
                    self.policy_data = pd.DataFrame(response.json())
                else:
                    # Try web scraping for policy documents
                    response = requests.get(url)
                    soup = BeautifulSoup(response.text, 'html.parser')
                    policy_text = soup.get_text()
                    # Simple processing - in a real scenario, you'd use NLP here
                    self.policy_data = pd.DataFrame({'policy_text': [policy_text]})
            else:
                raise ValueError("Either file_path or url must be provided.")
                
        except Exception as e:
            raise Exception(f"Error loading policy data: {str(e)}")
    
    def analyze_market_trends(self, time_column='date', value_column='price_per_sqm'):
        """
        Analyze property market trends over time.
        
        Args:
            time_column (str): Column name for time data. Defaults to 'date'.
            value_column (str): Column name for value data. Defaults to 'price_per_sqm'.
            
        Returns:
            dict: Dictionary containing trend analysis results.
        """
        if self.property_data is None:
            raise ValueError("Property data not loaded. Please load data first.")
            
        results = {}
        
        try:
            # Time series analysis
            time_series = self.property_data.groupby(pd.Grouper(key=time_column, freq='M'))[value_column].mean()
            
            # Calculate growth rates
            monthly_growth = time_series.pct_change() * 100
            annual_growth = time_series.pct_change(12) * 100
            
            results['time_series'] = time_series
            results['monthly_growth'] = monthly_growth
            results['annual_growth'] = annual_growth
            
            # Linear regression for trend
            X = np.array(range(len(time_series))).reshape(-1, 1)
            y = time_series.values.reshape(-1, 1)
            
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            
            model = LinearRegression()
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            
            results['trend_model'] = {
                'coefficient': model.coef_[0][0],
                'intercept': model.intercept_[0],
                'mse': mean_squared_error(y_test, y_pred),
                'r2': r2_score(y_test, y_pred)
            }
            
        except Exception as e:
            raise Exception(f"Error analyzing market trends: {str(e)}")
            
        return results
    
    def visualize_trends(self, results, save_path=None):
        """
        Visualize market trends from analysis results.
        
        Args:
            results (dict): Results from analyze_market_trends.
            save_path (str, optional): Path to save the visualization. Defaults to None.
        """
        try:
            plt.figure(figsize=(15, 8))
            
            # Plot time series
            plt.subplot(2, 2, 1)
            results['time_series'].plot(title='Price per sqm Over Time')
            
            # Plot monthly growth
            plt.subplot(2, 2, 2)
            results['monthly_growth'].plot(title='Monthly Growth Rate (%)')
            
            # Plot annual growth
            plt.subplot(2, 2, 3)
            results['annual_growth'].plot(title='Annual Growth Rate (%)')
            
            # Plot regression line
            plt.subplot(2, 2, 4)
            time_series = results['time_series']
            X = np.array(range(len(time_series))).reshape(-1, 1)
            model = LinearRegression()
            model.fit(X, time_series.values.reshape(-1, 1))
            plt.scatter(time_series.index, time_series.values, color='blue')
            plt.plot(time_series.index, model.predict(X), color='red', linewidth=2)
            plt.title('Price Trend with Linear Regression')
            
            plt.tight_layout()
            
            if save_path:
                plt.savefig(save_path)
            else:
                plt.show()
                
        except Exception as e:
            raise Exception(f"Error visualizing trends: {str(e)}")
    
    def analyze_by_region(self, region_column='district'):
        """
        Analyze property prices by region.
        
        Args:
            region_column (str): Column name for region data. Defaults to 'district'.
            
        Returns:
            dict: Dictionary containing regional analysis results.
        """
        if self.property_data is None:
            raise ValueError("Property data not loaded. Please load data first.")
            
        results = {}
        
        try:
            # Regional price analysis
            regional_stats = self.property_data.groupby(region_column)['price_per_sqm'].agg(['mean', 'median', 'std', 'count'])
            results['regional_stats'] = regional_stats
            
            # Price distribution by region
            plt.figure(f
