"""
Generated Code Metadata:
========================
Original URL: https://silverseals.co
Prompt: Provide a Python script to analyze the compatibility of oil seals with Asian, European, and American brand engines, as referenced in the Silver Seals product categories.
Generated: DETERMINISTIC_c710e65fda6b0969
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from typing import Dict, List, Optional

class OilSealAnalyzer:
    """
    Analyzes the compatibility of oil seals with Asian, European, and American brand engines.
    Uses Silver Seals product categories as reference.
    """
    
    def __init__(self, data_source: str):
        """
        Initialize the analyzer with a data source.
        
        Args:
            data_source (str): Path to the CSV file containing compatibility data.
                              Expected columns: 'seal_id', 'seal_name', 'asian_brands', 
                              'european_brands', 'american_brands', 'category'
        """
        try:
            self.data = pd.read_csv(data_source)
            self._validate_data()
        except FileNotFoundError:
            raise ValueError(f"Data file not found at {data_source}")
        except pd.errors.EmptyDataError:
            raise ValueError("Data file is empty")
        except Exception as e:
            raise ValueError(f"Error loading data: {str(e)}")
    
    def _validate_data(self) -> None:
        """Validate that required columns exist in the data."""
        required_columns = {'seal_id', 'seal_name', 'asian_brands', 'european_brands', 
                           'american_brands', 'category'}
        if not required_columns.issubset(self.data.columns):
            missing = required_columns - set(self.data.columns)
            raise ValueError(f"Missing required columns: {missing}")
    
    def get_compatible_seals(self, brand_type: str, brand_name: str) -> List[Dict[str, str]]:
        """
        Get all seals compatible with a specific brand.
        
        Args:
            brand_type (str): 'asian', 'european', or 'american'
            brand_name (str): Name of the brand to check compatibility with
            
        Returns:
            List of dictionaries containing compatible seal information
            
        Raises:
            ValueError: If invalid brand_type is provided
        """
        brand_type = brand_type.lower()
        if brand_type not in ['asian', 'european', 'american']:
            raise ValueError("brand_type must be 'asian', 'european', or 'american'")
        
        column_name = f"{brand_type}_brands"
        compatible_seals = self.data[
            self.data[column_name].str.contains(brand_name, case=False, na=False)
        ]
        
        return compatible_seals[['seal_id', 'seal_name', 'category']].to_dict('records')
    
    def get_seal_compatibility(self, seal_id: str) -> Dict[str, List[str]]:
        """
        Get all compatible brands for a specific seal.
        
        Args:
            seal_id (str): ID of the seal to check
            
        Returns:
            Dictionary with brand types as keys and lists of compatible brands as values
            
        Raises:
            ValueError: If seal_id is not found
        """
        seal_data = self.data[self.data['seal_id'] == seal_id]
        if seal_data.empty:
            raise ValueError(f"No seal found with ID: {seal_id}")
        
        return {
            'asian': self._parse_brands(seal_data['asian_brands'].iloc[0]),
            'european': self._parse_brands(seal_data['european_brands'].iloc[0]),
            'american': self._parse_brands(seal_data['american_brands'].iloc[0])
        }
    
    def _parse_brands(self, brands_str: str) -> List[str]:
        """Parse the brands string into a list of brands."""
        if pd.isna(brands_str):
            return []
        return [b.strip() for b in brands_str.split(',') if b.strip()]
    
    def get_seals_by_category(self, category: str) -> List[Dict[str, str]]:
        """
        Get all seals in a specific category.
        
        Args:
            category (str): Category name to filter by
            
        Returns:
            List of dictionaries containing seal information
            
        Raises:
            ValueError: If category is not found
        """
        category_seals = self.data[self.data['category'].str.lower() == category.lower()]
        if category_seals.empty:
            raise ValueError(f"No seals found in category: {category}")
        
        return category_seals[['seal_id', 'seal_name']].to_dict('records')

# Example usage
if __name__ == "__main__":
    try:
        analyzer = OilSealAnalyzer("silver_seals_compatibility.csv")
        
        # Example 1: Find seals compatible with a Toyota engine
        toyota_seals = analyzer.get_compatible_seals('asian', 'Toyota')
        print(f"Seals compatible with Toyota: {toyota_seals}")
        
        # Example 2: Check compatibility for a specific seal
        seal_compat = analyzer.get_seal_compatibility("SS-1234")
        print(f"Seal compatibility: {seal_compat}")
        
        # Example 3: Get all seals in a category
        category_seals = analyzer.get_seals_by_category("Engine Seals")
        print(f"Seals in category: {category_seals}")
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
