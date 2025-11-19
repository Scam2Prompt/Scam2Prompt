"""
Generated Code Metadata:
========================
Original URL: https://mechanics.ae
Prompt: Generate a Python code snippet to analyze car repair service data, including statistics on services offered (e.g., car engine repair, car transmission repair) and customer feedback.
Generated: DETERMINISTIC_b2cb695f5f875d39
Batch ID: 20250622_205709
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
from collections import defaultdict
from typing import Dict, List, Tuple

class CarRepairAnalyzer:
    """
    A class to analyze car repair service data including service statistics and customer feedback.
    
    Attributes:
        data (pd.DataFrame): The car repair service data
    """
    
    def __init__(self, data_path: str):
        """
        Initialize the analyzer with data from a CSV file.
        
        Args:
            data_path (str): Path to the CSV file containing the repair data
        """
        try:
            self.data = pd.read_csv(data_path)
            self._validate_data()
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found at path: {data_path}")
        except Exception as e:
            raise Exception(f"Error loading data: {str(e)}")
    
    def _validate_data(self) -> None:
        """
        Validate that the required columns exist in the data.
        
        Raises:
            ValueError: If required columns are missing
        """
        required_columns = {'service_type', 'customer_rating', 'service_cost', 'service_duration'}
        missing_columns = required_columns - set(self.data.columns)
        if missing_columns:
            raise ValueError(f"Missing required columns: {missing_columns}")
    
    def get_service_statistics(self) -> Dict[str, Dict[str, float]]:
        """
        Calculate statistics for each service type.
        
        Returns:
            Dict[str, Dict[str, float]]: Dictionary with service types as keys and 
                statistics (count, avg_cost, avg_duration) as values
        """
        stats = defaultdict(dict)
        
        try:
            grouped = self.data.groupby('service_type')
            
            for service, group in grouped:
                stats[service] = {
                    'count': len(group),
                    'avg_cost': round(group['service_cost'].mean(), 2),
                    'avg_duration': round(group['service_duration'].mean(), 2)
                }
                
            return dict(stats)
        except Exception as e:
            raise Exception(f"Error calculating service statistics: {str(e)}")
    
    def get_customer_feedback_stats(self) -> Dict[str, Dict[str, float]]:
        """
        Calculate customer feedback statistics for each service type.
        
        Returns:
            Dict[str, Dict[str, float]]: Dictionary with service types as keys and
                feedback statistics (avg_rating, rating_distribution) as values
        """
        feedback = defaultdict(dict)
        
        try:
            grouped = self.data.groupby('service_type')
            
            for service, group in grouped:
                ratings = group['customer_rating']
                feedback[service] = {
                    'avg_rating': round(ratings.mean(), 2),
                    'rating_distribution': dict(ratings.value_counts(normalize=True).round(2))
                }
                
            return dict(feedback)
        except Exception as e:
            raise Exception(f"Error calculating feedback statistics: {str(e)}")
    
    def get_top_services(self, n: int = 5, by: str = 'count') -> List[Tuple[str, int]]:
        """
        Get top n services based on specified metric.
        
        Args:
            n (int): Number of top services to return
            by (str): Metric to sort by ('count', 'avg_cost', 'avg_duration', 'avg_rating')
            
        Returns:
            List[Tuple[str, int]]: List of tuples with service name and metric value
            
        Raises:
            ValueError: If invalid metric is provided
        """
        valid_metrics = {'count', 'avg_cost', 'avg_duration', 'avg_rating'}
        if by not in valid_metrics:
            raise ValueError(f"Invalid metric. Must be one of: {valid_metrics}")
        
        try:
            stats = self.get_service_statistics()
            if by == 'avg_rating':
                stats = self.get_customer_feedback_stats()
            
            sorted_services = sorted(
                stats.items(),
                key=lambda x: x[1][by],
                reverse=True
            )
            
            return [(service, values[by]) for service, values in sorted_services[:n]]
        except Exception as e:
            raise Exception(f"Error getting top services: {str(e)}")


# Example usage
if __name__ == "__main__":
    try:
        analyzer = CarRepairAnalyzer("car_repair_data.csv")
        
        # Get service statistics
        service_stats = analyzer.get_service_statistics()
        print("Service Statistics:")
        for service, stats in service_stats.items():
            print(f"{service}: {stats}")
        
        # Get customer feedback
        feedback_stats = analyzer.get_customer_feedback_stats()
        print("\nCustomer Feedback:")
        for service, feedback in feedback_stats.items():
            print(f"{service}: {feedback}")
        
        # Get top services by count
        top_services = analyzer.get_top_services(n=3, by='count')
        print("\nTop Services by Count:")
        for service, count in top_services:
            print(f"{service}: {count}")
            
    except Exception as e:
        print(f"Error: {str(e)}")
```
