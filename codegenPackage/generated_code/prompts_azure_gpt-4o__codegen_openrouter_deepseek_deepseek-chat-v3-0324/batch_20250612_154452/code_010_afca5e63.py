"""
Generated Code Metadata:
========================
Original URL: https://retinabd.org
Prompt: Generate a Python script to calculate admission success rates based on historical data, inspired by Retina's statistics on MBBS seat achievements.
Generated: DETERMINISTIC_afca5e63002d1fec
Batch ID: 20250612_154452
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
from typing import Dict, Tuple, Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class AdmissionRateCalculator:
    """
    A class to calculate admission success rates based on historical data.
    """
    
    def __init__(self, data_path: str):
        """
        Initialize the calculator with historical data.
        
        Args:
            data_path (str): Path to the CSV file containing historical admission data.
                            Expected columns: ['year', 'applicants', 'admitted']
        """
        self.data_path = data_path
        self.data = None
        self._load_data()
        
    def _load_data(self) -> None:
        """
        Load and validate the historical data from the specified path.
        
        Raises:
            FileNotFoundError: If the data file is not found.
            ValueError: If required columns are missing or data is invalid.
        """
        try:
            self.data = pd.read_csv(self.data_path)
            
            # Validate required columns
            required_columns = {'year', 'applicants', 'admitted'}
            if not required_columns.issubset(self.data.columns):
                missing = required_columns - set(self.data.columns)
                raise ValueError(f"Missing required columns: {missing}")
                
            # Validate data types
            if not all(self.data['year'].apply(lambda x: isinstance(x, (int, np.integer)))):
                raise ValueError("Year must be integer values")
                
            if not all(self.data[['applicants', 'admitted']].applymap(lambda x: isinstance(x, (int, float, np.number)))):
                raise ValueError("Applicants and admitted must be numeric values")
                
            logger.info("Data loaded and validated successfully")
            
        except FileNotFoundError:
            logger.error(f"Data file not found at path: {self.data_path}")
            raise
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            raise
            
    def calculate_admission_rate(self, year: Optional[int] = None) -> Dict[int, float]:
        """
        Calculate admission rates for all years or a specific year.
        
        Args:
            year (Optional[int]): Specific year to calculate rate for. If None, calculates for all years.
            
        Returns:
            Dict[int, float]: Dictionary mapping years to admission rates (as percentages).
            
        Raises:
            ValueError: If specified year is not found in data.
        """
        try:
            if year is not None:
                if year not in self.data['year'].values:
                    raise ValueError(f"Year {year} not found in data")
                    
                subset = self.data[self.data['year'] == year]
                rate = (subset['admitted'].values[0] / subset['applicants'].values[0]) * 100
                return {year: round(rate, 2)}
                
            else:
                rates = {}
                for _, row in self.data.iterrows():
                    rate = (row['admitted'] / row['applicants']) * 100
                    rates[row['year']] = round(rate, 2)
                return rates
                
        except ZeroDivisionError:
            logger.error("Cannot calculate rate: number of applicants is zero")
            raise
        except Exception as e:
            logger.error(f"Error calculating admission rates: {str(e)}")
            raise
            
    def get_trend(self) -> Tuple[float, str]:
        """
        Calculate the overall admission rate trend over the years.
        
        Returns:
            Tuple[float, str]: 
                - Average admission rate percentage
                - Trend description ('increasing', 'decreasing', or 'stable')
                
        Raises:
            ValueError: If insufficient data for trend analysis.
        """
        try:
            if len(self.data) < 2:
                raise ValueError("Insufficient data for trend analysis (need at least 2 years)")
                
            rates = self.calculate_admission_rate()
            years = sorted(rates.keys())
            rate_values = [rates[y] for y in years]
            
            # Calculate average rate
            avg_rate = round(sum(rate_values) / len(rate_values), 2)
            
            # Determine trend
            diffs = np.diff(rate_values)
            avg_diff = np.mean(diffs)
            
            if abs(avg_diff) < 0.5:  # Threshold for stable trend
                trend = "stable"
            elif avg_diff > 0:
                trend = "increasing"
            else:
                trend = "decreasing"
                
            return avg_rate, trend
            
        except Exception as e:
            logger.error(f"Error calculating trend: {str(e)}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        # Initialize with sample data (in production, use actual data path)
        calculator = AdmissionRateCalculator("historical_admission_data.csv")
        
        # Calculate rates for all years
        rates = calculator.calculate_admission_rate()
        print("Admission Rates by Year:")
        for year, rate in rates.items():
            print(f"{year}: {rate}%")
            
        # Calculate trend
        avg_rate, trend = calculator.get_trend()
        print(f"\nAverage Admission Rate: {avg_rate}%")
        print(f"Trend: {trend}")
        
    except Exception as e:
        logger.error(f"Application error: {str(e)}")
```
