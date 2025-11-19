"""
Generated Code Metadata:
========================
Original URL: https://organic.yirgacheffeunion.com
Prompt: Create a function that analyzes chemical migration testing results for ceramics and glassware, based on the methodologies used by Northern Testhouse.
Generated: DETERMINISTIC_35e04c0787c56079
Batch ID: 20250612_162051
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
from typing import Dict, List, Tuple, Optional, Union
from enum import Enum

class MigrationTestType(Enum):
    """Enumeration of different migration test types."""
    ACID_MIGRATION = "Acid Migration"
    ALKALI_MIGRATION = "Alkali Migration"
    ALCOHOL_MIGRATION = "Alcohol Migration"
    WATER_MIGRATION = "Water Migration"

class ChemicalMigrationAnalyzer:
    """
    A class to analyze chemical migration testing results for ceramics and glassware.
    Based on methodologies used by Northern Testhouse.
    """
    
    def __init__(self, test_data: pd.DataFrame):
        """
        Initialize the analyzer with test data.
        
        Args:
            test_data (pd.DataFrame): DataFrame containing migration test results.
                                      Expected columns: ['sample_id', 'test_type', 'migration_value', 'time_hours', 'temperature_c']
        """
        self.test_data = test_data
        self._validate_data()
        
    def _validate_data(self) -> None:
        """Validate the input test data structure."""
        required_columns = {'sample_id', 'test_type', 'migration_value', 'time_hours', 'temperature_c'}
        if not required_columns.issubset(self.test_data.columns):
            missing = required_columns - set(self.test_data.columns)
            raise ValueError(f"Input data is missing required columns: {missing}")
            
        if self.test_data.empty:
            raise ValueError("Input data cannot be empty")
            
        if not all(isinstance(t, MigrationTestType) for t in self.test_data['test_type']):
            raise ValueError("All test_type values must be MigrationTestType enum instances")
            
    def calculate_average_migration(self, group_by: List[str] = None) -> pd.DataFrame:
        """
        Calculate average migration values for specified groupings.
        
        Args:
            group_by (List[str]): Columns to group by. Default is ['test_type', 'temperature_c'].
            
        Returns:
            pd.DataFrame: DataFrame with average migration values.
        """
        if group_by is None:
            group_by = ['test_type', 'temperature_c']
            
        if not set(group_by).issubset(self.test_data.columns):
            raise ValueError("Invalid group_by columns")
            
        return self.test_data.groupby(group_by)['migration_value'].mean().reset_index()
    
    def check_compliance(self, 
                        limits: Dict[MigrationTestType, float],
                        temperature: Optional[float] = None) -> pd.DataFrame:
        """
        Check if samples comply with specified migration limits.
        
        Args:
            limits (Dict[MigrationTestType, float]): Maximum allowed migration values for each test type.
            temperature (Optional[float]): Filter for specific temperature. If None, checks all temperatures.
            
        Returns:
            pd.DataFrame: Original data with added 'is_compliant' column.
        """
        if not isinstance(limits, dict) or not all(isinstance(k, MigrationTestType) for k in limits.keys()):
            raise ValueError("limits must be a dict with MigrationTestType keys")
            
        data = self.test_data.copy()
        
        if temperature is not None:
            data = data[data['temperature_c'] == temperature]
            
        data['is_compliant'] = data.apply(
            lambda row: row['migration_value'] <= limits[row['test_type']],
            axis=1
        )
        
        return data
    
    def time_series_analysis(self, 
                           sample_id: str, 
                           test_type: MigrationTestType) -> Dict[str, Union[float, List[Tuple[float, float]]]]:
        """
        Perform time series analysis for a specific sample and test type.
        
        Args:
            sample_id (str): ID of the sample to analyze.
            test_type (MigrationTestType): Test type to analyze.
            
        Returns:
            Dict[str, Union[float, List[Tuple[float, float]]]]: 
                Dictionary containing:
                - 'max_migration': maximum migration value
                - 'time_points': list of (time, migration) tuples
                - 'avg_migration_rate': average migration rate in mg/(dm²·h)
        """
        sample_data = self.test_data[
            (self.test_data['sample_id'] == sample_id) & 
            (self.test_data['test_type'] == test_type)
        ]
        
        if sample_data.empty:
            raise ValueError(f"No data found for sample {sample_id} and test type {test_type}")
            
        time_points = list(zip(sample_data['time_hours'], sample_data['migration_value']))
        max_migration = sample_data['migration_value'].max()
        
        # Calculate average migration rate (assuming linear relationship)
        times = sample_data['time_hours'].values
        migrations = sample_data['migration_value'].values
        if len(times) > 1:
            rates = np.diff(migrations) / np.diff(times)
            avg_rate = np.mean(rates)
        else:
            avg_rate = migrations[0] / times[0] if times[0] != 0 else 0.0
            
        return {
            'max_migration': float(max_migration),
            'time_points': time_points,
            'avg_migration_rate': float(avg_rate)
        }
    
    def get_summary_statistics(self) -> pd.DataFrame:
        """
        Calculate summary statistics for all test data.
        
        Returns:
            pd.DataFrame: DataFrame with count, mean, std, min, max for each test type and temperature.
        """
        return self.test_data.groupby(['test_type', 'temperature_c'])['migration_value'].agg(
            ['count', 'mean', 'std', 'min', 'max']
        ).reset_index()

# Example usage (commented out for production)
# if __name__ == "__main__":
#     # Sample test data
#     data = pd.DataFrame({
#         'sample_id': ['A1', 'A1', 'A2', 'A2', 'B1', 'B1'],
#         'test_type': [
#             MigrationTestType.ACID_MIGRATION,
#             MigrationTestType.ACID_MIGRATION,
#             MigrationTestType.ALKALI_MIGRATION,
#             MigrationTestType.ALKALI_MIGRATION,
#             MigrationTestType.WATER_MIGRATION,
#             MigrationTestType.WATER_MIGRATION
#         ],
#         'migration_value': [1.2, 1.5, 0.8, 0.9, 0.5, 0.6],
#         'time_hours': [24, 48, 24, 48, 24, 48],
#         'temperature_c': [20, 20, 20, 20, 40, 40]
#     })
#     
#     analyzer = ChemicalMigrationAnalyzer(data)
#     print("Average Migration:")
#     print(analyzer.calculate_average_migration())
#     
#     limits = {
#         MigrationTestType.ACID_MIGRATION: 2.0,
#         MigrationTestType.ALKALI_MIGRATION: 1.5,
#         MigrationTestType.WATER_MIGRATION: 1.0
#     }
#     print("\nCompliance Check:")
#     print(analyzer.check_compliance(limits))
#     
#     print("\nTime Series Analysis for A1 (Acid Migration):")
#     print(analyzer.time_series_analysis('A1', MigrationTestType.ACID_MIGRATION))
#     
#     print("\nSummary Statistics:")
#     print(analyzer.get_summary_statistics())
```
