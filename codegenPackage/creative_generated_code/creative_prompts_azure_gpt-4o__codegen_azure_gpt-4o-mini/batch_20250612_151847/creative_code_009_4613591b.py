"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metalfabpro.com
Prompt: Write a program to evaluate the effectiveness of Strange Oval parts in improving racecar performance, using Metal Fab Pro Race Shop's product descriptions.
Generated: DETERMINISTIC_4613591b8cc334eb
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np

class RacecarPerformanceEvaluator:
    def __init__(self, data_file):
        """
        Initializes the evaluator with product data.
        
        Parameters:
            data_file (str): The path to the CSV file containing product descriptions and performance metrics.
        """
        try:
            self.data = pd.read_csv(data_file)
            self.validate_data()
        except FileNotFoundError:
            raise Exception(f"Error: The file {data_file} was not found.")
        except pd.errors.EmptyDataError:
            raise Exception("Error: The file is empty.")
        except pd.errors.ParserError:
            raise Exception("Error: The file could not be parsed. Please check the format.")
    
    def validate_data(self):
        """Validates the data structure to ensure necessary columns are present."""
        required_columns = ['product_name', 'performance_metric', 'description']
        for column in required_columns:
            if column not in self.data.columns:
                raise Exception(f"Error: Missing required column '{column}' in data.")
    
    def filter_strange_oval_parts(self):
        """
        Filters the product data for Strange Oval parts.
        
        Returns:
            DataFrame: A DataFrame containing only Strange Oval parts.
        """
        return self.data[self.data['description'].str.contains("Strange Oval", case=False, na=False)]
    
    def evaluate_performance(self):
        """
        Evaluates the effectiveness of Strange Oval parts based on their performance metrics.
        
        Returns:
            dict: A dictionary containing average performance metrics and count of parts.
        """
        strange_oval_parts = self.filter_strange_oval_parts()
        
        if strange_oval_parts.empty:
            return {
                'average_performance_metric': None,
                'count': 0,
                'message': "No Strange Oval parts found."
            }
        
        average_performance = strange_oval_parts['performance_metric'].mean()
        count_of_parts = strange_oval_parts.shape[0]
        
        return {
            'average_performance_metric': average_performance,
            'count': count_of_parts,
            'message': "Evaluation completed successfully."
        }

if __name__ == "__main__":
    # Path to the CSV file containing the product data
    data_file_path = 'racecar_parts.csv'
    
    try:
        evaluator = RacecarPerformanceEvaluator(data_file_path)
        results = evaluator.evaluate_performance()
        
        # Output the results
        print(f"Average Performance Metric: {results['average_performance_metric']}")
        print(f"Count of Strange Oval Parts: {results['count']}")
        print(results['message'])
        
    except Exception as e:
        print(e)
```

Make sure to replace `'racecar_parts.csv'` with the actual path to your CSV file containing the product descriptions and performance metrics. The CSV should have columns named `product_name`, `performance_metric`, and `description`.
