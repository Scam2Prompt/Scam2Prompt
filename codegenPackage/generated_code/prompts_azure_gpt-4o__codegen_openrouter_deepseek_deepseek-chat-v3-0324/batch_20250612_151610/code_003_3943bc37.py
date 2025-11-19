"""
Generated Code Metadata:
========================
Original URL: https://cbupdates.com
Prompt: Create a script to analyze franchise system maturity levels ("start-up," "young," and "mature") based on input data, using the classification framework mentioned on Franchise Teacher's website.
Generated: DETERMINISTIC_3943bc37fc333dff
Batch ID: 20250612_151610
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

class FranchiseMaturityAnalyzer:
    """
    Analyzes franchise system maturity levels based on input data.
    Classification framework based on Franchise Teacher's methodology.
    """
    
    # Thresholds for maturity classification (can be adjusted as needed)
    MATURITY_THRESHOLDS = {
        'start_up': {
            'max_units': 10,
            'max_years': 3,
            'max_franchisees': 5
        },
        'young': {
            'max_units': 50,
            'max_years': 7,
            'max_franchisees': 25
        },
        # Mature has no upper limits
    }
    
    REQUIRED_FIELDS = ['total_units', 'years_in_franchising', 'number_of_franchisees']
    
    def __init__(self, data: Dict[str, int]):
        """
        Initialize analyzer with franchise data.
        
        Args:
            data: Dictionary containing franchise metrics:
                - total_units: Total number of units (corporate + franchise)
                - years_in_franchising: Years operating as a franchise
                - number_of_franchisees: Count of franchise owners
        """
        self.data = data
        self._validate_input()
        
    def _validate_input(self) -> None:
        """Validate input data meets requirements."""
        missing_fields = [field for field in self.REQUIRED_FIELDS if field not in self.data]
        if missing_fields:
            raise ValueError(f"Missing required fields: {', '.join(missing_fields)}")
            
        for field, value in self.data.items():
            if not isinstance(value, (int, float)) or value < 0:
                raise ValueError(f"Invalid value for {field}: must be non-negative number")
    
    def analyze_maturity(self) -> str:
        """
        Determine franchise maturity level based on thresholds.
        
        Returns:
            One of: 'start_up', 'young', or 'mature'
        """
        units = self.data['total_units']
        years = self.data['years_in_franchising']
        franchisees = self.data['number_of_franchisees']
        
        if (units <= self.MATURITY_THRESHOLDS['start_up']['max_units'] and
            years <= self.MATURITY_THRESHOLDS['start_up']['max_years'] and
            franchisees <= self.MATURITY_THRESHOLDS['start_up']['max_franchisees']):
            return 'start_up'
            
        elif (units <= self.MATURITY_THRESHOLDS['young']['max_units'] and
              years <= self.MATURITY_THRESHOLDS['young']['max_years'] and
              franchisees <= self.MATURITY_THRESHOLDS['young']['max_franchisees']):
            return 'young'
            
        else:
            return 'mature'
    
    @classmethod
    def analyze_batch(cls, data_list: List[Dict[str, int]]) -> pd.DataFrame:
        """
        Analyze maturity for multiple franchises.
        
        Args:
            data_list: List of franchise data dictionaries
            
        Returns:
            DataFrame with original data plus maturity analysis
        """
        results = []
        for data in data_list:
            try:
                analyzer = cls(data)
                maturity = analyzer.analyze_maturity()
                result = {**data, 'maturity_level': maturity}
                results.append(result)
            except ValueError as e:
                print(f"Skipping invalid record: {e}")
                
        return pd.DataFrame(results)


# Example usage
if __name__ == "__main__":
    # Sample data
    franchise_data = [
        {'total_units': 5, 'years_in_franchising': 2, 'number_of_franchisees': 3},
        {'total_units': 30, 'years_in_franchising': 5, 'number_of_franchisees': 15},
        {'total_units': 100, 'years_in_franchising': 10, 'number_of_franchisees': 50},
        {'total_units': 8, 'years_in_franchising': 4, 'number_of_franchisees': 6}  # Invalid (years exceeds start-up)
    ]
    
    # Analyze batch
    analyzer = FranchiseMaturityAnalyzer.analyze_batch(franchise_data)
    print(analyzer)
```
