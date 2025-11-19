"""
Generated Code Metadata:
========================
Original URL: https://anima.art.br
Prompt: Develop a Python script to analyze student enrollment data for Ânima's courses, categorizing them into "basic," "advanced," and "specialized" levels.
Generated: DETERMINISTIC_9867e672b4be48c7
Batch ID: 20250612_151428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

class EnrollmentAnalyzer:
    """
    A class to analyze student enrollment data for Ânima's courses.
    It categorizes courses into 'basic', 'advanced', and 'specialized' levels.
    """

    def __init__(self, data_file):
        """
        Initializes the EnrollmentAnalyzer with the provided data file.

        :param data_file: str - Path to the CSV file containing enrollment data.
        """
        self.data_file = data_file
        self.enrollment_data = None

    def load_data(self):
        """
        Loads the enrollment data from the specified CSV file.
        Handles file not found and parsing errors.
        """
        try:
            self.enrollment_data = pd.read_csv(self.data_file)
            print("Data loaded successfully.")
        except FileNotFoundError:
            print(f"Error: The file {self.data_file} was not found.")
            raise
        except pd.errors.EmptyDataError:
            print("Error: The file is empty.")
            raise
        except pd.errors.ParserError:
            print("Error: There was a problem parsing the file.")
            raise

    def categorize_courses(self):
        """
        Categorizes courses into 'basic', 'advanced', and 'specialized' levels.
        Assumes the enrollment data has a 'course_level' column.
        Returns a dictionary with counts of each category.
        """
        if self.enrollment_data is None:
            raise ValueError("Enrollment data is not loaded. Please call load_data() first.")

        # Initialize category counts
        category_counts = {
            'basic': 0,
            'advanced': 0,
            'specialized': 0
        }

        # Count the number of courses in each category
        for level in self.enrollment_data['course_level']:
            if level in category_counts:
                category_counts[level] += 1
            else:
                print(f"Warning: Unrecognized course level '{level}' found in data.")

        return category_counts

    def display_results(self, category_counts):
        """
        Displays the results of the course categorization.

        :param category_counts: dict - A dictionary containing counts of each category.
        """
        print("Course Level Analysis:")
        for level, count in category_counts.items():
            print(f"{level.capitalize()}: {count}")

def main():
    """
    Main function to execute the enrollment analysis.
    """
    # Path to the enrollment data CSV file
    data_file = 'enrollment_data.csv'

    # Create an instance of EnrollmentAnalyzer
    analyzer = EnrollmentAnalyzer(data_file)

    # Load the data
    analyzer.load_data()

    # Categorize the courses
    category_counts = analyzer.categorize_courses()

    # Display the results
    analyzer.display_results(category_counts)

if __name__ == "__main__":
    main()
```
