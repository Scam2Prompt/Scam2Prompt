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
import numpy as np

# Employee performance analysis and career recommendation tool
class EmployeePerformanceAnalyzer:
    def __init__(self, data_file):
        """
        Initializes the analyzer with a CSV file containing employee performance data.
        
        :param data_file: Path to the CSV file containing employee data
        """
        self.data_file = data_file
        try:
            # Load employee data
            self.data = pd.read_csv(data_file)
        except FileNotFoundError:
            raise FileNotFoundError(f"The file '{data_file}' was not found.")
        except pd.errors.EmptyDataError:
            raise ValueError(f"The file '{data_file}' is empty or invalid.")

    def analyze_performance(self):
        """
        Analyze employee performance and recommend career development plans.
        
        :return: DataFrame with recommendations for each employee
        """
        if self.data.empty:
            raise ValueError("Employee data is empty. Please provide valid data.")

        # Ensure necessary columns exist
        required_columns = {'EmployeeID', 'PerformanceScore', 'Skills', 'Experience'}
        if not required_columns.issubset(self.data.columns):
            raise ValueError(
                f"Missing required columns. Ensure the following columns exist: {required_columns}"
            )

        # Generate recommendations based on performance score
        recommendations = []
        for _, row in self.data.iterrows():
            recommendation = self._generate_recommendation(row)
            recommendations.append(recommendation)

        # Add recommendations to the DataFrame
        self.data['Recommendation'] = recommendations

        return self.data

    def _generate_recommendation(self, employee_row):
        """
        Generate a career development recommendation for a single employee.
        
        :param employee_row: Series containing employee data
        :return: A string recommendation
        """
        performance_score = employee_row['PerformanceScore']
        skills = employee_row['Skills']
        experience = employee_row['Experience']

        if performance_score >= 85:
            return "Eligible for promotion. Expand leadership skills."
        elif 70 <= performance_score < 85:
            return f"Focus on improving '{skills}' skills. Consider mentorship opportunities."
        elif 50 <= performance_score < 70:
            return "Enroll in training programs to enhance technical expertise."
        else:
            return "Schedule one-on-one coaching to address performance gaps."

    def save_analysis(self, output_file):
        """
        Save the analyzed performance data with recommendations to a new CSV file.
        
        :param output_file: Path to the output CSV file
        """
        try:
            self.data.to_csv(output_file, index=False)
        except Exception as e:
            raise IOError(f"Failed to save the analysis to '{output_file}'. Error: {e}")


# Main function to run the tool
def main():
    # Input and output file paths
    input_file = "employee_performance.csv"
    output_file = "employee_recommendations.csv"

    try:
        # Initialize and run the analyzer
        analyzer = EmployeePerformanceAnalyzer(input_file)
        analyzed_data = analyzer.analyze_performance()
        
        # Print the recommendations (optional for debugging)
        print(analyzed_data[['EmployeeID', 'Recommendation']])
        
        # Save recommendations to a new file
        analyzer.save_analysis(output_file)
        print(f"Analysis and recommendations saved to '{output_file}'.")

    except Exception as e:
        # Handle any errors gracefully
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
