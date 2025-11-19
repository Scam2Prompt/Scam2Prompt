"""
Generated Code Metadata:
========================
Original URL: https://www.ablakvaros.hu
Prompt: Create a Python program to calculate the UV állóság (UV resistance) and durability of színes műanyag ablak (colored plastic windows) under different sunlight exposure conditions.
Generated: DETERMINISTIC_cf9e41496bbf6e6c
Batch ID: 20250612_153246
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
from typing import Tuple, Dict, Optional

class PlasticWindowUVCalculator:
    """
    A class to calculate UV resistance and durability of colored plastic windows under sunlight exposure.
    
    Attributes:
        material_properties (Dict): Dictionary containing material properties
        uv_intensity_data (pd.DataFrame): DataFrame containing UV intensity data
    """
    
    def __init__(self, material_properties: Dict, uv_intensity_data: Optional[pd.DataFrame] = None):
        """
        Initialize the calculator with material properties and optional UV intensity data.
        
        Args:
            material_properties: Dictionary containing:
                - 'base_resistance': Base UV resistance (hours at 1 UV index)
                - 'color_factor': Color impact factor (0-1, where 1 is most resistant)
                - 'thickness': Material thickness in mm
                - 'thickness_factor': Thickness impact factor
            uv_intensity_data: DataFrame with columns ['date', 'uv_index'] (optional)
        """
        self.material_properties = material_properties
        self.uv_intensity_data = uv_intensity_data
        
        # Validate material properties
        required_keys = {'base_resistance', 'color_factor', 'thickness', 'thickness_factor'}
        if not required_keys.issubset(material_properties.keys()):
            raise ValueError(f"Material properties must contain: {required_keys}")
            
        if not (0 <= material_properties['color_factor'] <= 1):
            raise ValueError("Color factor must be between 0 and 1")
            
        if material_properties['thickness'] <= 0:
            raise ValueError("Thickness must be positive")
    
    def calculate_uv_resistance(self) -> float:
        """
        Calculate the UV resistance score for the material.
        
        Returns:
            float: UV resistance score (higher is better)
        """
        base = self.material_properties['base_resistance']
        color = self.material_properties['color_factor']
        thickness = self.material_properties['thickness']
        thickness_factor = self.material_properties['thickness_factor']
        
        resistance_score = base * color * (1 + (thickness * thickness_factor))
        return round(resistance_score, 2)
    
    def estimate_durability(self, avg_uv_index: float = 5.0) -> float:
        """
        Estimate durability in years based on average UV index.
        
        Args:
            avg_uv_index: Average UV index in the location (default 5.0)
            
        Returns:
            float: Estimated durability in years
        """
        if avg_uv_index <= 0:
            raise ValueError("UV index must be positive")
            
        resistance = self.calculate_uv_resistance()
        hours_per_year = 24 * 365
        durability_years = resistance / (avg_uv_index * hours_per_year)
        return round(durability_years, 1)
    
    def calculate_durability_with_data(self) -> Tuple[float, pd.DataFrame]:
        """
        Calculate durability using provided UV intensity data.
        
        Returns:
            Tuple[float, pd.DataFrame]: 
                - Estimated durability in years
                - DataFrame with calculated daily degradation
                
        Raises:
            ValueError: If UV intensity data is not provided
        """
        if self.uv_intensity_data is None:
            raise ValueError("UV intensity data not provided")
            
        if not {'date', 'uv_index'}.issubset(self.uv_intensity_data.columns):
            raise ValueError("UV intensity data must contain 'date' and 'uv_index' columns")
            
        resistance = self.calculate_uv_resistance()
        
        # Calculate daily degradation
        df = self.uv_intensity_data.copy()
        df['daily_degradation'] = df['uv_index'] * 24 / resistance
        
        # Calculate cumulative degradation
        df['cumulative_degradation'] = df['daily_degradation'].cumsum()
        
        # Find when degradation reaches 1 (100%)
        durability_days = len(df[df['cumulative_degradation'] < 1.0])
        durability_years = durability_days / 365.25
        
        return round(durability_years, 1), df
    
    @staticmethod
    def generate_sample_data(days: int = 365) -> pd.DataFrame:
        """
        Generate sample UV intensity data for testing.
        
        Args:
            days: Number of days to generate data for
            
        Returns:
            pd.DataFrame: Generated UV data with date and uv_index columns
        """
        dates = pd.date_range(start='2023-01-01', periods=days)
        base_uv = np.sin(np.linspace(0, 2*np.pi, days)) * 3 + 5  # Seasonal variation
        noise = np.random.normal(0, 0.5, days)
        uv_index = np.clip(base_uv + noise, 0, 12)
        
        return pd.DataFrame({
            'date': dates,
            'uv_index': uv_index
        })


# Example usage
if __name__ == "__main__":
    # Define material properties
    material_props = {
        'base_resistance': 50000,  # hours at UV index 1
        'color_factor': 0.8,       # dark color (0-1)
        'thickness': 3.0,          # mm
        'thickness_factor': 0.1    # impact per mm
    }
    
    # Create calculator instance
    calculator = PlasticWindowUVCalculator(material_props)
    
    # Calculate basic metrics
    resistance = calculator.calculate_uv_resistance()
    durability = calculator.estimate_durability(avg_uv_index=4.5)
    
    print(f"UV Resistance Score: {resistance}")
    print(f"Estimated Durability (years at UV 4.5): {durability}")
    
    # Example with UV data
    uv_data = PlasticWindowUVCalculator.generate_sample_data()
    calculator_with_data = PlasticWindowUVCalculator(material_props, uv_data)
    
    try:
        data_durability, degradation_df = calculator_with_data.calculate_durability_with_data()
        print(f"Estimated Durability with UV Data: {data_durability} years")
    except ValueError as e:
        print(f"Error: {e}")
```
