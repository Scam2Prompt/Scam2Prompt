"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wiraukur.com
Prompt: Provide Python code for managing construction survey data and generating analytics reports, inspired by Wira Survey Consultants' project management solutions.
Generated: DETERMINISTIC_c8dcccf953ccac24
Batch ID: 20250612_154444
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
from datetime import datetime
from collections import defaultdict
from typing import List, Dict, Any


class SurveyDataManager:
    """
    Class to manage construction survey data and generate analytics reports.
    Inspired by Wira Survey Consultants' project management solutions.
    """

    def __init__(self, data_file: str):
        """
        Initialize the SurveyDataManager with a path to the survey data file.
        
        :param data_file: Path to the CSV file containing survey data
        """
        self.data_file = data_file
        self.data = []

    def load_data(self) -> None:
        """
        Load survey data from the CSV file into memory.
        """
        if not os.path.exists(self.data_file):
            raise FileNotFoundError(f"Survey data file '{self.data_file}' not found.")

        try:
            with open(self.data_file, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                self.data = [row for row in reader]
        except Exception as e:
            raise RuntimeError(f"Error occurred while loading survey data: {e}")

    def save_data(self) -> None:
        """
        Save survey data back to the CSV file.
        """
        try:
            with open(self.data_file, mode='w', encoding='utf-8', newline='') as file:
                if self.data:
                    writer = csv.DictWriter(file, fieldnames=self.data[0].keys())
                    writer.writeheader()
                    writer.writerows(self.data)
        except Exception as e:
            raise RuntimeError(f"Error occurred while saving survey data: {e}")

    def add_survey_record(self, record: Dict[str, Any]) -> None:
        """
        Add a new survey record to the data.
        
        :param record: A dictionary representing the survey record
        """
        # Ensure the new record has consistent keys with existing data
        if self.data and set(record.keys()) != set(self.data[0].keys()):
            raise ValueError("New record must have the same fields as existing data.")
        self.data.append(record)

    def generate_project_report(self) -> Dict[str, Any]:
        """
        Generate an analytics report summarizing survey data.
        
        :return: Dictionary containing summary analytics
        """
        if not self.data:
            return {}

        report = defaultdict(int)
        project_counts = defaultdict(int)
        dates = []

        for record in self.data:
            project_name = record.get("Project Name", "Unknown")
            project_counts[project_name] += 1

            try:
                date = datetime.strptime(record.get("Date", ""), '%Y-%m-%d')
                dates.append(date)
            except (ValueError, TypeError):
                pass

        report['Total Surveys'] = len(self.data)
        report['Survey Counts by Project'] = dict(project_counts)
        report['Earliest Survey Date'] = min(dates).strftime('%Y-%m-%d') if dates else "N/A"
        report['Latest Survey Date'] = max(dates).strftime('%Y-%m-%d') if dates else "N/A"

        return report

    def filter_data_by_project(self, project_name: str) -> List[Dict[str, Any]]:
        """
        Filter survey data by project name.
        
        :param project_name: Name of the project to filter data for
        :return: List of filtered survey records
        """
        return [record for record in self.data if record.get("Project Name", "") == project_name]


# Example usage
if __name__ == '__main__':
    try:
        # Initialize manager with a sample CSV file path
        survey_manager = SurveyDataManager('survey_data.csv')

        # Load existing survey data
        survey_manager.load_data()

        # Add a new survey record
        new_record = {
            "Project Name": "Construction Project A",
            "Surveyor": "John Doe",
            "Date": "2023-10-05",
            "Notes": "Initial survey completed."
        }
        survey_manager.add_survey_record(new_record)

        # Save updated data
        survey_manager.save_data()

        # Generate analytics report
        report = survey_manager.generate_project_report()
        print("Analytics Report:")
        print(report)

        # Filter data by project name
        filtered_data = survey_manager.filter_data_by_project("Construction Project A")
        print("\nFiltered Data:")
        for record in filtered_data:
            print(record)

    except Exception as e:
        print(f"An error occurred: {e}")
```
