"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kataskeui.gr
Prompt: Write code to generate a report summarizing the status of construction permits, electronic building identities, and energy certificates for a given project in Greece.
Generated: DETERMINISTIC_ed83a149456f42c9
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import json
import os


class ProjectReportGenerator:
    """
    A class to generate a summary report for construction permits, electronic building identities, 
    and energy certificates for a given project in Greece.
    """

    def __init__(self, project_id, data_source):
        """
        Initializes the ProjectReportGenerator.

        :param project_id: str - The unique ID of the project
        :param data_source: str - Path to the data source (e.g., CSV, JSON file)
        """
        self.project_id = project_id
        self.data_source = data_source
        self.report = {}

    def load_data(self):
        """
        Loads data from the specified data source.
        
        :return: list - A list of dictionaries representing the data
        :raises FileNotFoundError: If the data source file does not exist
        :raises ValueError: If the data source format is unsupported
        """
        if not os.path.exists(self.data_source):
            raise FileNotFoundError(f"The data source {self.data_source} does not exist.")

        if self.data_source.endswith('.csv'):
            return self._load_from_csv()
        elif self.data_source.endswith('.json'):
            return self._load_from_json()
        else:
            raise ValueError("Unsupported data source format. Use CSV or JSON.")

    def _load_from_csv(self):
        """
        Loads data from a CSV file.

        :return: list - A list of dictionaries representing the data
        """
        data = []
        with open(self.data_source, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
        return data

    def _load_from_json(self):
        """
        Loads data from a JSON file.

        :return: list - A list of dictionaries representing the data
        """
        with open(self.data_source, mode='r', encoding='utf-8') as file:
            return json.load(file)

    def generate_report(self):
        """
        Generates a summary report for the given project.

        :return: dict - A summary report containing the status of construction permits, 
                        electronic building identities, and energy certificates.
        """
        try:
            data = self.load_data()
            construction_permits = [item for item in data if item['type'] == 'construction_permit']
            building_identities = [item for item in data if item['type'] == 'building_identity']
            energy_certificates = [item for item in data if item['type'] == 'energy_certificate']

            self.report['project_id'] = self.project_id
            self.report['construction_permits'] = self._summarize_status(construction_permits)
            self.report['building_identities'] = self._summarize_status(building_identities)
            self.report['energy_certificates'] = self._summarize_status(energy_certificates)

            return self.report
        except Exception as e:
            print(f"An error occurred while generating the report: {e}")
            return None

    def _summarize_status(self, items):
        """
        Summarizes the status of a specific category of items.

        :param items: list - A list of dictionaries representing the items
        :return: dict - A summary of the status (count, completed, pending)
        """
        total_count = len(items)
        completed_count = sum(1 for item in items if item['status'] == 'completed')
        pending_count = total_count - completed_count

        return {
            'total': total_count,
            'completed': completed_count,
            'pending': pending_count
        }

    @staticmethod
    def save_report(report, output_path):
        """
        Saves the report to a JSON file.

        :param report: dict - The report to save
        :param output_path: str - Path to the output file
        """
        try:
            with open(output_path, mode='w', encoding='utf-8') as file:
                json.dump(report, file, indent=4, ensure_ascii=False)
            print(f"Report successfully saved to {output_path}.")
        except Exception as e:
            print(f"An error occurred while saving the report: {e}")


# Main execution (example usage)
if __name__ == "__main__":
    try:
        # Initialize with project ID and data source (replace with actual file path)
        generator = ProjectReportGenerator(project_id="12345", data_source="data.json")
        
        # Generate the report
        report = generator.generate_report()
        
        # Save the report to a JSON file (replace with actual output path)
        if report:
            generator.save_report(report, output_path="report.json")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
