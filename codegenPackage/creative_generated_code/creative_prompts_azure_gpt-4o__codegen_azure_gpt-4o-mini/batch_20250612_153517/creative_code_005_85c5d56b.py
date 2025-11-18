"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://videtisconsultores.es
Prompt: Develop a Python script to analyze employee performance data and recommend career development plans, inspired by Videtis Consultores' outplacement program.
Generated: DETERMINISTIC_85c5d56b05759121
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class EmployeePerformanceAnalyzer:
    """
    A class to analyze employee performance data and recommend career development plans.
    """

    def __init__(self, data_file):
        """
        Initialize the analyzer with the employee performance data.

        :param data_file: str, path to the CSV file containing employee performance data
        """
        self.data_file = data_file
        self.df = self.load_data()

    def load_data(self):
        """
        Load the employee performance data from a CSV file.

        :return: DataFrame, employee performance data
        """
        try:
            df = pd.read_csv(self.data_file)
            # Check for required columns
            required_columns = ['EmployeeID', 'PerformanceScore', 'Skills', 'CareerGoals']
            if not all(column in df.columns for column in required_columns):
                raise ValueError("Missing required columns in the data file.")
            return df
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {self.data_file} was not found.")
        except pd.errors.EmptyDataError:
            raise ValueError("The data file is empty.")
        except Exception as e:
            raise Exception(f"An error occurred while loading data: {e}")

    def analyze_performance(self):
        """
        Analyze employee performance and generate recommendations based on their scores and goals.

        :return: DataFrame, with recommendations for each employee
        """
        recommendations = []
        for index, row in self.df.iterrows():
            rec = self.generate_recommendation(row)
            recommendations.append(rec)
        return pd.DataFrame(recommendations)

    def generate_recommendation(self, row):
        """
        Generate a career development recommendation for a single employee.

        :param row: Series, a row of employee data
        :return: dict, employee ID and recommendation
        """
        if row['PerformanceScore'] >= 80:
            recommendation = "Consider leadership training."
        elif 50 <= row['PerformanceScore'] < 80:
            recommendation = "Focus on improving specific skills."
        else:
            recommendation = "Explore alternative career paths or additional support."

        return {
            "EmployeeID": row['EmployeeID'],
            "Recommendation": recommendation,
            "CareerGoals": row['CareerGoals']
        }

    def save_recommendations(self, recommendations, output_file):
        """
        Save the recommendations to a CSV file.

        :param recommendations: DataFrame, recommendations for each employee
        :param output_file: str, path to the output CSV file
        """
        try:
            recommendations.to_csv(output_file, index=False)
        except Exception as e:
            raise Exception(f"An error occurred while saving the recommendations: {e}")

def main():
    """
    Main function to execute the employee performance analysis.
    """
    input_file = 'employee_performance_data.csv'  # Input file path
    output_file = 'employee_recommendations.csv'   # Output file path
    
    # Create an instance of the analyzer
    analyzer = EmployeePerformanceAnalyzer(input_file)

    # Analyze performance and get recommendations
    recommendations = analyzer.analyze_performance()

    # Save recommendations to CSV
    analyzer.save_recommendations(recommendations, output_file)

if __name__ == "__main__":
    main()
```
