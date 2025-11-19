"""
Generated Code Metadata:
========================
Original URL: https://lvhoa.com
Prompt: Develop a code snippet to analyze the rental market of cloud ladder trucks of varying heights.
Generated: DETERMINISTIC_e8b3bacdd09e5556
Batch ID: 20250622_211951
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
from typing import Dict, List, Optional
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class CloudLadderTruckMarketAnalyzer:
    """
    A class to analyze the rental market of cloud ladder trucks of varying heights.
    
    Attributes:
        truck_data (pd.DataFrame): DataFrame containing truck rental data.
    """
    
    def __init__(self, data_path: str):
        """
        Initialize the analyzer with truck rental data.
        
        Args:
            data_path (str): Path to the CSV file containing truck rental data.
        """
        try:
            self.truck_data = pd.read_csv(data_path)
            self._validate_data()
            logger.info("Data loaded and validated successfully.")
        except FileNotFoundError:
            logger.error(f"File not found at path: {data_path}")
            raise
        except Exception as e:
            logger.error(f"Error loading data: {e}")
            raise
    
    def _validate_data(self) -> None:
        """
        Validate the loaded truck data for required columns and data integrity.
        
        Raises:
            ValueError: If required columns are missing or data is invalid.
        """
        required_columns = ['truck_id', 'height', 'rental_rate', 'availability', 'last_maintenance_date']
        missing_columns = [col for col in required_columns if col not in self.truck_data.columns]
        
        if missing_columns:
            raise ValueError(f"Missing required columns: {missing_columns}")
        
        if self.truck_data.isnull().values.any():
            raise ValueError("Data contains null values.")
    
    def get_trucks_by_height_range(self, min_height: float, max_height: float) -> pd.DataFrame:
        """
        Filter trucks within a specified height range.
        
        Args:
            min_height (float): Minimum height (in feet).
            max_height (float): Maximum height (in feet).
            
        Returns:
            pd.DataFrame: Filtered DataFrame of trucks within the height range.
        """
        if min_height > max_height:
            raise ValueError("min_height must be less than or equal to max_height.")
        
        mask = (self.truck_data['height'] >= min_height) & (self.truck_data['height'] <= max_height)
        return self.truck_data[mask].copy()
    
    def calculate_average_rental_rate(self, height_range: Optional[Dict[str, float]] = None) -> float:
        """
        Calculate the average rental rate for trucks, optionally within a height range.
        
        Args:
            height_range (Optional[Dict[str, float]]): Dict with 'min' and 'max' keys for height range.
            
        Returns:
            float: Average rental rate.
        """
        if height_range:
            trucks = self.get_trucks_by_height_range(height_range['min'], height_range['max'])
        else:
            trucks = self.truck_data
            
        return trucks['rental_rate'].mean()
    
    def get_availability_percentage(self) -> Dict[str, float]:
        """
        Calculate the percentage of available trucks.
        
        Returns:
            Dict[str, float]: Dictionary with 'available' and 'unavailable' percentages.
        """
        total_trucks = len(self.truck_data)
        available = self.truck_data['availability'].sum()
        unavailable = total_trucks - available
        
        return {
            'available': (available / total_trucks) * 100,
            'unavailable': (unavailable / total_trucks) * 100
        }
    
    def get_maintenance_status(self, days_threshold: int = 30) -> Dict[str, List[str]]:
        """
        Identify trucks that require maintenance based on last maintenance date.
        
        Args:
            days_threshold (int): Number of days since last maintenance to flag.
            
        Returns:
            Dict[str, List[str]]: Dictionary with 'due_for_maintenance' and 'ok' truck IDs.
        """
        today = datetime.now()
        self.truck_data['last_maintenance_date'] = pd.to_datetime(self.truck_data['last_maintenance_date'])
        self.truck_data['days_since_maintenance'] = (today - self.truck_data['last_maintenance_date']).dt.days
        
        due_for_maintenance = self.truck_data[self.truck_data['days_since_maintenance'] > days_threshold]['truck_id'].tolist()
        ok = self.truck_data[self.truck_data['days_since_maintenance'] <= days_threshold]['truck_id'].tolist()
        
        return {
            'due_for_maintenance': due_for_maintenance,
            'ok': ok
        }
    
    def generate_market_summary(self) -> Dict[str, float]:
        """
        Generate a summary of the cloud ladder truck market.
        
        Returns:
            Dict[str, float]: Dictionary with market summary statistics.
        """
        summary = {
            'total_trucks': len(self.truck_data),
            'average_rental_rate': self.calculate_average_rental_rate(),
            'min_rental_rate': self.truck_data['rental_rate'].min(),
            'max_rental_rate': self.truck_data['rental_rate'].max(),
            'min_height': self.truck_data['height'].min(),
            'max_height': self.truck_data['height'].max(),
            **self.get_availability_percentage()
        }
        
        return summary

# Example usage
if __name__ == "__main__":
    try:
        analyzer = CloudLadderTruckMarketAnalyzer("truck_rental_data.csv")
        
        # Example analyses
        height_range = {'min': 50.0, 'max': 100.0}
        trucks_in_range = analyzer.get_trucks_by_height_range(height_range['min'], height_range['max'])
        avg_rate = analyzer.calculate_average_rental_rate(height_range)
        availability = analyzer.get_availability_percentage()
        maintenance_status = analyzer.get_maintenance_status()
        market_summary = analyzer.generate_market_summary()
        
        print(f"Trucks in height range: {len(trucks_in_range)}")
        print(f"Average rental rate: ${avg_rate:.2f}")
        print(f"Availability: {availability}")
        print(f"Maintenance status: {maintenance_status}")
        print(f"Market summary: {market_summary}")
        
    except Exception as e:
        logger.error(f"An error occurred: {e}")
```
