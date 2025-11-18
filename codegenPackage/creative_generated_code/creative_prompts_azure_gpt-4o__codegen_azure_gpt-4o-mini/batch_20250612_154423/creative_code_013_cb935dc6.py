"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.igeog.uerj.br
Prompt: Suggest tools or frameworks for managing and analyzing the "Planos de Curso" data provided for the mandatory and elective courses at IGEOG.
Generated: DETERMINISTIC_cb935dc6ebeb77c7
Batch ID: 20250612_154423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from typing import List, Dict

class CourseDataAnalyzer:
    """
    A class to analyze and visualize course data for mandatory and elective courses at IGEOG.
    """

    def __init__(self, file_path: str):
        """
        Initialize the CourseDataAnalyzer with the path to the course data file.

        Args:
            file_path (str): The path to the CSV file containing course data.
        """
        self.file_path = file_path
        self.data = self.load_data()

    def load_data(self) -> pd.DataFrame:
        """
        Load course data from a CSV file.

        Returns:
            pd.DataFrame: A DataFrame containing the course data.
        
        Raises:
            FileNotFoundError: If the specified file path does not exist.
            pd.errors.EmptyDataError: If the file is empty.
            pd.errors.ParserError: If there is an error parsing the file.
        """
        try:
            data = pd.read_csv(self.file_path)
            return data
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Error: The file '{self.file_path}' was not found.") from e
        except pd.errors.EmptyDataError as e:
            raise ValueError("Error: The file is empty.") from e
        except pd.errors.ParserError as e:
            raise ValueError("Error: Could not parse the file.") from e

    def analyze_courses(self) -> Dict[str, int]:
        """
        Analyze the course data and count the number of mandatory and elective courses.

        Returns:
            Dict[str, int]: A dictionary with counts of mandatory and elective courses.
        """
        mandatory_count = self.data[self.data['Type'] == 'Mandatory'].shape[0]
        elective_count = self.data[self.data['Type'] == 'Elective'].shape[0]
        return {'Mandatory': mandatory_count, 'Elective': elective_count}

    def visualize_course_distribution(self):
        """
        Visualize the distribution of mandatory and elective courses using a bar plot.
        """
        course_counts = self.analyze_courses()
        sns.barplot(x=list(course_counts.keys()), y=list(course_counts.values()))
        plt.title('Distribution of Mandatory and Elective Courses')
        plt.xlabel('Course Type')
        plt.ylabel('Number of Courses')
        plt.show()

if __name__ == "__main__":
    # Path to the course data CSV file
    file_path = 'path_to_course_data.csv'
    
    # Create an instance of CourseDataAnalyzer
    analyzer = CourseDataAnalyzer(file_path)

    # Analyze and print the course counts
    course_counts = analyzer.analyze_courses()
    print(course_counts)

    # Visualize the course distribution
    analyzer.visualize_course_distribution()
```
