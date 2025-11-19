"""
Generated Code Metadata:
========================
Original URL: https://starshot90.com
Prompt: Write a function to analyze employee retention metrics during turbulent times, based on the strategies described in the "Strategies for Employee Retention in Turbulent Times" section of the Star Shot 90 website.
Generated: DETERMINISTIC_fe5f9c5c9760df8f
Batch ID: 20250612_154657
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from datetime import datetime
from typing import Dict, List, Tuple, Optional

class EmployeeRetentionAnalyzer:
    """
    Analyzes employee retention metrics during turbulent times based on various strategies.
    
    Attributes:
        employee_data (pd.DataFrame): DataFrame containing employee records.
        retention_strategies (List[str]): List of retention strategies implemented.
        turbulent_periods (List[Tuple[datetime, datetime]]): List of start and end dates of turbulent periods.
    """
    
    def __init__(self, employee_data: pd.DataFrame, retention_strategies: List[str], turbulent_periods: List[Tuple[datetime, datetime]]):
        """
        Initializes the analyzer with employee data, retention strategies, and turbulent periods.
        
        Args:
            employee_data: DataFrame with columns like 'employee_id', 'join_date', 'exit_date', 'strategy_applied'.
            retention_strategies: List of retention strategies to analyze.
            turbulent_periods: List of tuples representing start and end dates of turbulent periods.
        """
        self.employee_data = employee_data
        self.retention_strategies = retention_strategies
        self.turbulent_periods = turbulent_periods
        
        # Validate input data
        self._validate_data()
    
    def _validate_data(self) -> None:
        """Validates the input data for required columns and data types."""
        required_columns = {'employee_id', 'join_date', 'exit_date', 'strategy_applied'}
        if not required_columns.issubset(self.employee_data.columns):
            raise ValueError(f"Input DataFrame must contain columns: {required_columns}")
        
        if not isinstance(self.retention_strategies, list):
            raise TypeError("retention_strategies must be a list")
        
        for period in self.turbulent_periods:
            if len(period) != 2 or not all(isinstance(date, datetime) for date in period):
                raise TypeError("Each turbulent period must be a tuple of two datetime objects")
    
    def _is_in_turbulent_period(self, date: Optional[datetime]) -> bool:
        """
        Checks if a given date falls within any turbulent period.
        
        Args:
            date: The date to check. If None, returns False.
            
        Returns:
            bool: True if the date is within a turbulent period, False otherwise.
        """
        if date is None:
            return False
        
        for start, end in self.turbulent_periods:
            if start <= date <= end:
                return True
        return False
    
    def calculate_retention_rate(self) -> Dict[str, float]:
        """
        Calculates retention rate for each strategy during turbulent periods.
        
        Returns:
            Dict[str, float]: Dictionary mapping each strategy to its retention rate.
                             Retention rate is defined as the percentage of employees
                             who did not exit during turbulent periods.
        """
        retention_rates = {}
        
        for strategy in self.retention_strategies:
            # Filter employees who had the strategy applied
            strategy_employees = self.employee_data[self.employee_data['strategy_applied'] == strategy]
            
            if len(strategy_employees) == 0:
                retention_rates[strategy] = 0.0
                continue
            
            retained = 0
            for _, employee in strategy_employees.iterrows():
                exit_date = employee['exit_date']
                if not self._is_in_turbulent_period(exit_date):
                    retained += 1
            
            retention_rate = (retained / len(strategy_employees)) * 100
            retention_rates[strategy] = round(retention_rate, 2)
        
        return retention_rates
    
    def calculate_avg_tenure_during_turbulence(self) -> Dict[str, float]:
        """
        Calculates average tenure (in days) of employees who exited during turbulent periods per strategy.
        
        Returns:
            Dict[str, float]: Dictionary mapping each strategy to the average tenure
                             of employees who exited during turbulent periods.
        """
        avg_tenures = {}
        
        for strategy in self.retention_strategies:
            # Filter employees who had the strategy applied and exited during turbulence
            strategy_employees = self.employee_data[self.employee_data['strategy_applied'] == strategy]
            turbulent_exits = []
            
            for _, employee in strategy_employees.iterrows():
                exit_date = employee['exit_date']
                if self._is_in_turbulent_period(exit_date):
                    tenure = (exit_date - employee['join_date']).days
                    turbulent_exits.append(tenure)
            
            if turbulent_exits:
                avg_tenure = sum(turbulent_exits) / len(turbulent_exits)
                avg_tenures[strategy] = round(avg_tenure, 2)
            else:
                avg_tenures[strategy] = 0.0
        
        return avg_tenures
    
    def generate_retention_report(self) -> Dict[str, Dict[str, float]]:
        """
        Generates a comprehensive retention report with multiple metrics.
        
        Returns:
            Dict[str, Dict[str, float]]: Dictionary containing retention metrics for each strategy.
        """
        return {
            'retention_rate': self.calculate_retention_rate(),
            'avg_tenure_during_turbulence': self.calculate_avg_tenure_during_turbulence()
        }

# Example usage (commented out for production)
# if __name__ == "__main__":
#     # Sample data
#     data = {
#         'employee_id': [1, 2, 3, 4, 5],
#         'join_date': [
#             datetime(2020, 1, 1),
#             datetime(2020, 2, 1),
#             datetime(2020, 3, 1),
#             datetime(2020, 4, 1),
#             datetime(2020, 5, 1)
#         ],
#         'exit_date': [
#             datetime(2021, 1, 1),
#             datetime(2020, 12, 1),  # During turbulence
#             None,  # Still employed
#             datetime(2020, 11, 1),  # During turbulence
#             None   # Still employed
#         ],
#         'strategy_applied': [
#             'flexible_work',
#             'mental_health_support',
#             'flexible_work',
#             'mental_health_support',
#             'flexible_work'
#         ]
#     }
#     
#     df = pd.DataFrame(data)
#     strategies = ['flexible_work', 'mental_health_support']
#     turbulent_periods = [(datetime(2020, 10, 1), datetime(2020, 12, 31))]
#     
#     analyzer = EmployeeRetentionAnalyzer(df, strategies, turbulent_periods)
#     report = analyzer.generate_retention_report()
#     print(report)
```
