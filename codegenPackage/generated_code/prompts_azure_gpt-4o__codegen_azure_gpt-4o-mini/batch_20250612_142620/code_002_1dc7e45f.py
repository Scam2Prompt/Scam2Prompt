"""
Generated Code Metadata:
========================
Original URL: https://potencia.in
Prompt: Generate code for a student performance analysis tool that uses periodic test results to shuffle students into "Diamond" and "Gold" batches, as implemented by Potencia Academy.
Generated: DETERMINISTIC_1dc7e45f6fae8e0d
Batch ID: 20250612_142620
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

class StudentPerformanceAnalyzer:
    def __init__(self, data):
        """
        Initializes the StudentPerformanceAnalyzer with student data.

        :param data: A pandas DataFrame containing student test results.
        """
        self.data = data

    def validate_data(self):
        """
        Validates the input data to ensure it contains the necessary columns.
        
        Raises:
            ValueError: If required columns are missing.
        """
        required_columns = ['student_id', 'name', 'test_score']
        for column in required_columns:
            if column not in self.data.columns:
                raise ValueError(f"Missing required column: {column}")

    def categorize_students(self):
        """
        Categorizes students into 'Diamond' and 'Gold' batches based on their test scores.
        
        Returns:
            dict: A dictionary with batch names as keys and lists of student IDs as values.
        """
        # Calculate the median score to determine the cutoff for batches
        median_score = self.data['test_score'].median()
        
        # Create batches based on the median score
        diamond_batch = self.data[self.data['test_score'] > median_score]
        gold_batch = self.data[self.data['test_score'] <= median_score]
        
        return {
            'Diamond': diamond_batch['student_id'].tolist(),
            'Gold': gold_batch['student_id'].tolist()
        }

    def analyze_performance(self):
        """
        Main method to analyze student performance and categorize them into batches.
        
        Returns:
            dict: A dictionary with batch names as keys and lists of student IDs as values.
        """
        try:
            self.validate_data()
            return self.categorize_students()
        except ValueError as e:
            print(f"Error: {e}")
            return None

# Example usage
if __name__ == "__main__":
    # Sample data for testing
    data = {
        'student_id': [1, 2, 3, 4, 5],
        'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'test_score': [85, 92, 78, 88, 95]
    }
    
    # Create a DataFrame
    student_data = pd.DataFrame(data)
    
    # Initialize the analyzer
    analyzer = StudentPerformanceAnalyzer(student_data)
    
    # Analyze performance and get batches
    batches = analyzer.analyze_performance()
    
    if batches:
        print("Student Batches:")
        for batch_name, student_ids in batches.items():
            print(f"{batch_name} Batch: {student_ids}")
```
