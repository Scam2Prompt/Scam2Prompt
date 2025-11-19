"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smkn1kadipaten.sch.id
Prompt: Develop a code snippet that automates the generation of student performance reports for the PSAJ assessments mentioned on the SMKN 1 Kadipaten site.
Generated: DETERMINISTIC_91cc05fbf7251439
Batch ID: 20250612_164206
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import os

class StudentPerformanceReportGenerator:
    def __init__(self, input_file, output_dir):
        """
        Initializes the report generator with the input file and output directory.
        :param input_file: Path to the CSV file containing student assessment data.
        :param output_dir: Directory where the generated reports will be saved.
        """
        self.input_file = input_file
        self.output_dir = output_dir

    def _validate_input(self):
        """
        Validates the existence of the input file and output directory.
        Raises:
            FileNotFoundError: If the input file does not exist.
            NotADirectoryError: If the output directory does not exist or is not a directory.
        """
        if not os.path.isfile(self.input_file):
            raise FileNotFoundError(f"Input file '{self.input_file}' not found.")
        if not os.path.isdir(self.output_dir):
            raise NotADirectoryError(f"Output directory '{self.output_dir}' is invalid.")

    def generate_reports(self):
        """
        Generates student performance reports in text file format.
        Each report contains the student's name, ID, scores, and overall performance.
        """
        self._validate_input()

        try:
            with open(self.input_file, mode='r', encoding='utf-8') as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    try:
                        self._generate_individual_report(row)
                    except Exception as e:
                        print(f"Error generating report for student {row.get('Student Name', 'Unknown')}: {e}")
        except Exception as e:
            print(f"Failed to process input file: {e}")

    def _generate_individual_report(self, student_data):
        """
        Generates an individual student's performance report.
        :param student_data: Dictionary containing student details and performance data.
        """
        student_name = student_data.get('Student Name', 'Unknown')
        student_id = student_data.get('Student ID', 'Unknown')
        scores = {key: value for key, value in student_data.items() if key.startswith('Score')}
        overall_performance = self._calculate_performance(scores)

        report_content = f"""
        Student Performance Report
        --------------------------
        Name: {student_name}
        ID: {student_id}

        Scores:
        {self._format_scores(scores)}

        Overall Performance: {overall_performance}
        """

        output_file_path = os.path.join(self.output_dir, f"{student_name}_{student_id}_Report.txt")
        try:
            with open(output_file_path, mode='w', encoding='utf-8') as report_file:
                report_file.write(report_content.strip())
                print(f"Report generated successfully for {student_name} (ID: {student_id}).")
        except Exception as e:
            raise RuntimeError(f"Failed to write report for {student_name} (ID: {student_id}): {e}")

    def _calculate_performance(self, scores):
        """
        Calculates overall performance based on scores.
        :param scores: Dictionary containing assessment scores.
        :return: A string representation of overall performance.
        """
        try:
            total_score = sum(float(value) for value in scores.values())
            average_score = total_score / len(scores)
            if average_score >= 90:
                return "Excellent"
            elif average_score >= 75:
                return "Good"
            elif average_score >= 50:
                return "Average"
            else:
                return "Needs Improvement"
        except ValueError:
            raise ValueError("Invalid score values encountered during performance calculation.")

    def _format_scores(self, scores):
        """
        Formats the scores for display in the report.
        :param scores: Dictionary containing assessment scores.
        :return: A formatted string representation of the scores.
        """
        return "\n".join([f"{key}: {value}" for key, value in scores.items()])


# Example usage:
if __name__ == "__main__":
    INPUT_CSV_FILE = "student_assessments.csv"  # Input CSV file containing student data
    OUTPUT_DIRECTORY = "performance_reports"  # Directory to save reports

    # Ensure the output directory exists
    os.makedirs(OUTPUT_DIRECTORY, exist_ok=True)

    # Create the report generator instance and generate reports
    report_generator = StudentPerformanceReportGenerator(INPUT_CSV_FILE, OUTPUT_DIRECTORY)
    report_generator.generate_reports()
```
