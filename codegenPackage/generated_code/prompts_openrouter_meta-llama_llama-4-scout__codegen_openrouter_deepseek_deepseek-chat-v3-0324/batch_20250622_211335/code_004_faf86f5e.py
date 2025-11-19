"""
Generated Code Metadata:
========================
Original URL: https://gottrumpmemes.net
Prompt: Generate a Python script to analyze real estate market trends in Las Vegas, including median home prices and sales volume over time, assuming access to historical sales data.
Generated: DETERMINISTIC_faf86f5ecd00c999
Batch ID: 20250622_211335
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
from datetime import datetime
import logging
from typing import Tuple, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class RealEstateAnalyzer:
    """
    A class to analyze real estate market trends in Las Vegas.
    
    Attributes:
        data (pd.DataFrame): Historical sales data
    """
    
    def __init__(self, data_path: str):
        """
        Initialize the analyzer with historical sales data.
        
        Args:
            data_path (str): Path to the CSV file containing historical sales data
        """
        try:
            self.data = pd.read_csv(data_path)
            self._validate_data()
            self._preprocess_data()
            logger.info("Data loaded and preprocessed successfully")
        except Exception as e:
            logger.error(f"Error initializing analyzer: {str(e)}")
            raise
    
    def _validate_data(self) -> None:
        """
        Validate that required columns exist in the data.
        
        Raises:
            ValueError: If required columns are missing
        """
        required_columns = {'sale_date', 'price', 'property_type', 'sqft', 'bedrooms'}
        missing_columns = required_columns - set(self.data.columns)
        if missing_columns:
            raise ValueError(f"Missing required columns: {missing_columns}")
    
    def _preprocess_data(self) -> None:
        """
        Preprocess the data by converting dates and handling missing values.
        """
        # Convert sale_date to datetime
        self.data['sale_date'] = pd.to_datetime(self.data['sale_date'])
        
        # Extract year and month for grouping
        self.data['year'] = self.data['sale_date'].dt.year
        self.data['month'] = self.data['sale_date'].dt.month
        
        # Handle missing values
        self.data['price'] = self.data['price'].fillna(0)
        self.data['sqft'] = self.data['sqft'].fillna(self.data['sqft'].median())
        
        # Filter out invalid prices
        self.data = self.data[self.data['price'] > 0]
    
    def get_median_prices_over_time(
        self, 
        property_type: Optional[str] = None, 
        start_date: Optional[str] = None, 
        end_date: Optional[str] = None
    ) -> pd.DataFrame:
        """
        Calculate median prices over time, optionally filtered by property type and date range.
        
        Args:
            property_type (str, optional): Filter by property type (e.g., 'Single Family', 'Condo')
            start_date (str, optional): Start date in 'YYYY-MM-DD' format
            end_date (str, optional): End date in 'YYYY-MM-DD' format
            
        Returns:
            pd.DataFrame: DataFrame with median prices by month
        """
        try:
            data = self.data.copy()
            
            # Apply filters if provided
            if property_type:
                data = data[data['property_type'] == property_type]
            
            if start_date:
                start_date = pd.to_datetime(start_date)
                data = data[data['sale_date'] >= start_date]
            
            if end_date:
                end_date = pd.to_datetime(end_date)
                data = data[data['sale_date'] <= end_date]
            
            # Group by year and month, calculate median price
            result = data.groupby(['year', 'month'])['price'].median().reset_index()
            result['date'] = pd.to_datetime(result['year'].astype(str) + '-' + result['month'].astype(str))
            
            return result.sort_values('date')
        
        except Exception as e:
            logger.error(f"Error calculating median prices: {str(e)}")
            raise
    
    def get_sales_volume_over_time(
        self, 
        property_type: Optional[str] = None, 
        start_date: Optional[str] = None, 
        end_date: Optional[str] = None
    ) -> pd.DataFrame:
        """
        Calculate sales volume over time, optionally filtered by property type and date range.
        
        Args:
            property_type (str, optional): Filter by property type (e.g., 'Single Family', 'Condo')
            start_date (str, optional): Start date in 'YYYY-MM-DD' format
            end_date (str, optional): End date in 'YYYY-MM-DD' format
            
        Returns:
            pd.DataFrame: DataFrame with sales count by month
        """
        try:
            data = self.data.copy()
            
            # Apply filters if provided
            if property_type:
                data = data[data['property_type'] == property_type]
            
            if start_date:
                start_date = pd.to_datetime(start_date)
                data = data[data['sale_date'] >= start_date]
            
            if end_date:
                end_date = pd.to_datetime(end_date)
                data = data[data['sale_date'] <= end_date]
            
            # Group by year and month, count sales
            result = data.groupby(['year', 'month']).size().reset_index(name='sales_count')
            result['date'] = pd.to_datetime(result['year'].astype(str) + '-' + result['month'].astype(str))
            
            return result.sort_values('date')
        
        except Exception as e:
            logger.error(f"Error calculating sales volume: {str(e)}")
            raise
    
    def plot_trends(
        self, 
        property_type: Optional[str] = None, 
        start_date: Optional[str] = None, 
        end_date: Optional[str] = None
    ) -> Tuple[plt.Figure, plt.Axes]:
        """
        Plot median prices and sales volume trends.
        
        Args:
            property_type (str, optional): Filter by property type
            start_date (str, optional): Start date in 'YYYY-MM-DD' format
            end_date (str, optional): End date in 'YYYY-MM-DD' format
            
        Returns:
            Tuple[plt.Figure, plt.Axes]: Figure and axes objects
        """
        try:
            # Get data
            prices = self.get_median_prices_over_time(property_type, start_date, end_date)
            volume = self.get_sales_volume_over_time(property_type, start_date, end_date)
            
            # Create figure with two subplots
            fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
            
            # Plot median prices
            ax1.plot(prices['date'], prices['price'], color='tab:blue')
            ax1.set_title('Median Home Prices Over Time')
            ax1.set_ylabel('Price ($)')
            ax1.grid(True)
            
            # Plot sales volume
            ax2.bar(volume['date'], volume['sales_count'], color='tab:orange')
            ax2.set_title('Sales Volume Over Time')
            ax2.set_ylabel('Number of Sales')
            ax2.grid(True)
            
            plt.tight_layout()
            return fig, (ax1, ax2)
        
        except Exception as e:
            logger.error(f"Error plotting trends: {str(e)}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        # Initialize analyzer with sample data
        analyzer = RealEstateAnalyzer('las_vegas_home_sales.csv')
        
        # Get median prices for single family homes in 2022
        median_prices = analyzer.get_median_prices_over_time(
            property_type='Single Family',
            start_date='2022-01-01',
            end_date='2022-12-31'
        )
        print("Median Prices:")
        print(median_prices.head())
        
        # Get sales volume for condos in 2021
        sales_volume = analyzer.get_sales_volume_over_time(
            property_type='Condo',
            start_date='2021-01-01',
            end_date='2021-12-31'
        )
        print("\nSales Volume:")
        print(sales_volume.head())
        
        # Plot trends for all properties
        fig, axes = analyzer.plot_trends()
        plt.savefig('las_vegas_real_estate_trends.png')
        plt.close()
        
    except Exception as e:
        logger.error(f"Error in main execution: {str(e)}")
```
