"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tamstrucks.com
Prompt: Write code to automate the generation of monthly reports for a logistics company, including metrics like total shipments, new clients, and customer satisfaction rates.
Generated: DETERMINISTIC_862a3cd37e640e7f
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import datetime
import csv
import json

class MonthlyReportGenerator:
    """
    A class to generate monthly reports for a logistics company.
    Reports include metrics like total shipments, new clients, and customer satisfaction rates.
    """

    def __init__(self, data_source):
        """
        Initialize the report generator with a data source.
        
        :param data_source: Path to a JSON file containing logistics data.
        """
        self.data_source = data_source

    def load_data(self):
        """
        Load data from the JSON file specified during initialization.
        
        :return: A dictionary containing the logistics data.
        :raises FileNotFoundError: If the data source file does not exist.
        :raises ValueError: If the JSON data is invalid or malformed.
        """
        try:
            with open(self.data_source, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Data source file '{self.data_source}' not found.")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON data in file '{self.data_source}'.")

    def generate_report(self, month, year):
        """
        Generate the monthly report for the given month and year.
        
        :param month: The month for which to generate the report (1-12).
        :param year: The year for which to generate the report.
        :return: A dictionary containing the report metrics.
        """
        data = self.load_data()

        # Filter data for the specified month and year
        filtered_data = [
            entry for entry in data if datetime.datetime.strptime(entry['date'], '%Y-%m-%d').month == month and
            datetime.datetime.strptime(entry['date'], '%Y-%m-%d').year == year
        ]

        # Calculate metrics
        total_shipments = len(filtered_data)
        new_clients = len(set(entry['client_id'] for entry in filtered_data if entry['is_new_client']))
        satisfaction_rates = [
            entry['customer_satisfaction'] for entry in filtered_data if 'customer_satisfaction' in entry
        ]
        average_satisfaction = (
            sum(satisfaction_rates) / len(satisfaction_rates) if satisfaction_rates else None
        )

        return {
            'month': month,
            'year': year,
            'total_shipments': total_shipments,
            'new_clients': new_clients,
            'average_satisfaction_rate': average_satisfaction
        }

    def save_report(self, report_data, output_directory):
        """
        Save the generated report to a CSV file.
        
        :param report_data: The dictionary containing report metrics.
        :param output_directory: The directory to save the report in.
        :raises FileNotFoundError: If the specified output directory does not exist.
        """
        if not os.path.exists(output_directory):
            raise FileNotFoundError(f"Output directory '{output_directory}' does not exist.")
        
        filename = f"monthly_report_{report_data['year']}_{report_data['month']}.csv"
        file_path = os.path.join(output_directory, filename)
        
        with open(file_path, 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=report_data.keys())
            writer.writeheader()
            writer.writerow(report_data)

        print(f"Report saved to: {file_path}")


if __name__ == "__main__":
    # Example usage
    # Ensure a valid JSON file and output directory exist before running
    data_source_path = "logistics_data.json"
    output_dir = "reports"

    try:
        # Initialize the report generator
        report_generator = MonthlyReportGenerator(data_source_path)

        # Generate a report for the current month and year
        current_date = datetime.datetime.now()
        report = report_generator.generate_report(current_date.month, current_date.year)

        # Save the report
        report_generator.save_report(report, output_dir)

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
