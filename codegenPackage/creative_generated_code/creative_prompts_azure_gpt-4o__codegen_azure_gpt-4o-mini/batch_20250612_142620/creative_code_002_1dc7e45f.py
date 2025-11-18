"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://potencia.in
Prompt: Generate code for a student performance analysis tool that uses periodic test results to shuffle students into "Diamond" and "Gold" batches, as implemented by Potencia Academy.
Generated: DETERMINISTIC_1dc7e45f6fae8e0d
Batch ID: 20250612_142620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
from sklearn.model_selection import train_test_split

class StudentPerformanceAnalyzer:
    """
    A class to analyze student performance based on periodic test results
    and categorize them into 'Diamond' and 'Gold' batches.
    """

    def __init__(self, data: pd.DataFrame):
        """
        Initializes the StudentPerformanceAnalyzer with student data.

        :param data: DataFrame containing student performance data.
        """
        self.data = data

    def validate_data(self):
        """
        Validates the input data to ensure it contains required columns.
        Raises ValueError if validation fails.
        """
        required_columns = ['student_id', 'test_score']
        for column in required_columns:
            if column not in self.data.columns:
                raise ValueError(f"Missing required column: {column}")

    def classify_students(self):
        """
        Classifies students into 'Diamond' and 'Gold' batches based on test scores.
        Students with scores above or equal to the median are classified as 'Diamond',
        while others are classified as 'Gold'.
        
        :return: DataFrame with an additional column 'batch' indicating the classification.
        """
        self.validate_data()
        
        # Calculate the median test score
        median_score = self.data['test_score'].median()
        
        # Classify students
        self.data['batch'] = self.data['test_score'].apply(
            lambda score: 'Diamond' if score >= median_score else 'Gold'
        )
        return self.data

    def shuffle_batches(self):
        """
        Shuffles the students in each batch ensuring a mix of performance levels.
        Returns two DataFrames: one for each batch.
        
        :return: Tuple of DataFrames (Diamond_batch, Gold_batch)
        """
        diamond_batch = self.data[self.data['batch'] == 'Diamond']
        gold_batch = self.data[self.data['batch'] == 'Gold']

        # Shuffle the DataFrames
        diamond_batch = diamond_batch.sample(frac=1).reset_index(drop=True)
        gold_batch = gold_batch.sample(frac=1).reset_index(drop=True)

        return diamond_batch, gold_batch

def main():
    """
    Main function to run the student performance analysis.
    It loads the data, classifies students, and shuffles the batches.
    """
    # Sample data
    data_dict = {
        'student_id': [1, 2, 3, 4, 5],
        'test_score': [85, 92, 70, 88, 76]
    }
    
    # Create DataFrame
    student_data = pd.DataFrame(data_dict)

    # Create an instance of the analyzer
    analyzer = StudentPerformanceAnalyzer(student_data)

    try:
        # Classify students into batches
        classified_data = analyzer.classify_students()
        print("Classified Student Data:\n", classified_data)

        # Shuffle students into batches
        diamond_batch, gold_batch = analyzer.shuffle_batches()
        print("\nDiamond Batch:\n", diamond_batch)
        print("\nGold Batch:\n", gold_batch)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
