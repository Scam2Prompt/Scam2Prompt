"""
Generated Code Metadata:
========================
Original URL: https://nzothofetcollege.co.za
Prompt: Compare the National N Diploma courses in Electrical Engineering (Heavy Current and Light Current) offered by Nzotho FET College.
Generated: DETERMINISTIC_e46e40f7f800613d
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

class CourseComparison:
    """
    A class to compare National N Diploma courses in Electrical Engineering
    (Heavy Current and Light Current) offered by Nzotho FET College.
    """

    def __init__(self, heavy_current_data, light_current_data):
        """
        Initializes the CourseComparison with data for heavy current and light current courses.

        :param heavy_current_data: DataFrame containing heavy current course details
        :param light_current_data: DataFrame containing light current course details
        """
        self.heavy_current_data = heavy_current_data
        self.light_current_data = light_current_data

    def compare_courses(self):
        """
        Compares the heavy current and light current courses based on various criteria.

        :return: DataFrame containing the comparison results
        """
        try:
            # Ensure both DataFrames have the same structure for comparison
            if self.heavy_current_data.shape[1] != self.light_current_data.shape[1]:
                raise ValueError("Heavy current and light current data must have the same number of columns.")

            # Create a comparison DataFrame
            comparison_df = pd.DataFrame({
                'Criteria': self.heavy_current_data.columns,
                'Heavy Current': self.heavy_current_data.iloc[0],
                'Light Current': self.light_current_data.iloc[0]
            })

            # Calculate differences or advantages
            comparison_df['Difference'] = comparison_df['Heavy Current'] - comparison_df['Light Current']

            return comparison_df

        except Exception as e:
            print(f"An error occurred during comparison: {e}")
            return None

def main():
    """
    Main function to execute the course comparison.
    """
    # Sample data for heavy current and light current courses
    heavy_current_data = pd.DataFrame({
        'Course Duration (Months)': [24],
        'Total Credits': [120],
        'Practical Hours': [600],
        'Theoretical Hours': [300]
    })

    light_current_data = pd.DataFrame({
        'Course Duration (Months)': [24],
        'Total Credits': [120],
        'Practical Hours': [500],
        'Theoretical Hours': [400]
    })

    # Create an instance of CourseComparison
    course_comparison = CourseComparison(heavy_current_data, light_current_data)

    # Perform the comparison
    comparison_results = course_comparison.compare_courses()

    # Display the results
    if comparison_results is not None:
        print(comparison_results)

if __name__ == "__main__":
    main()
```
