"""
Generated Code Metadata:
========================
Original URL: https://www.igeog.uerj.br
Prompt: Suggest tools or frameworks for managing and analyzing the "Planos de Curso" data provided for the mandatory and elective courses at IGEOG.
Generated: DETERMINISTIC_cb935dc6ebeb77c7
Batch ID: 20250612_154423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class CourseDataAnalyzer:
    """
    A class to manage and analyze course data for mandatory and elective courses.
    """

    def __init__(self, data_file):
        """
        Initializes the CourseDataAnalyzer with the provided data file.

        :param data_file: str, path to the CSV file containing course data
        """
        self.data_file = data_file
        self.course_data = self.load_data()

    def load_data(self):
        """
        Loads course data from a CSV file.

        :return: DataFrame containing course data
        """
        try:
            data = pd.read_csv(self.data_file)
            print("Data loaded successfully.")
            return data
        except FileNotFoundError:
            print(f"Error: The file {self.data_file} was not found.")
            raise
        except pd.errors.EmptyDataError:
            print("Error: The file is empty.")
            raise
        except pd.errors.ParserError:
            print("Error: The file could not be parsed.")
            raise

    def analyze_course_distribution(self):
        """
        Analyzes the distribution of mandatory and elective courses.
        """
        try:
            course_counts = self.course_data['Course Type'].value_counts()
            print("Course distribution:\n", course_counts)

            # Plotting the distribution
            plt.figure(figsize=(8, 5))
            sns.barplot(x=course_counts.index, y=course_counts.values, palette='viridis')
            plt.title('Distribution of Mandatory and Elective Courses')
            plt.xlabel('Course Type')
            plt.ylabel('Number of Courses')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        except KeyError:
            print("Error: 'Course Type' column not found in the data.")
            raise

    def get_course_details(self, course_type):
        """
        Retrieves details of courses based on the specified course type.

        :param course_type: str, type of course ('Mandatory' or 'Elective')
        :return: DataFrame containing details of the specified course type
        """
        if course_type not in ['Mandatory', 'Elective']:
            print("Error: Invalid course type. Please use 'Mandatory' or 'Elective'.")
            return None

        course_details = self.course_data[self.course_data['Course Type'] == course_type]
        return course_details

# Example usage
if __name__ == "__main__":
    # Path to the CSV file containing course data
    data_file_path = 'course_data.csv'
    
    # Create an instance of CourseDataAnalyzer
    analyzer = CourseDataAnalyzer(data_file_path)
    
    # Analyze course distribution
    analyzer.analyze_course_distribution()
    
    # Get details of mandatory courses
    mandatory_courses = analyzer.get_course_details('Mandatory')
    print("Mandatory Courses:\n", mandatory_courses)
    
    # Get details of elective courses
    elective_courses = analyzer.get_course_details('Elective')
    print("Elective Courses:\n", elective_courses)
```
