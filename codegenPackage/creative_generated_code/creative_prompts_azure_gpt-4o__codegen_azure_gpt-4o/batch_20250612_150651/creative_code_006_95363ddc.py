"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://armourersandbrasiers.co.uk
Prompt: Develop a program to generate reports on the impact of grants given by the Armourers & Brasiers' Gauntlet Trust, including metrics for educational outcomes and research advancements.
Generated: DETERMINISTIC_95363ddc294af343
Batch ID: 20250612_150651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a Python implementation of the requested program:

```python
import csv
import json
from datetime import datetime


class GrantImpactReportGenerator:
    """
    A program to generate reports on the impact of grants given by the Armourers & Brasiers' Gauntlet Trust.
    Reports include metrics for educational outcomes and research advancements.
    """

    def __init__(self, grant_data_file):
        """
        Initializes the report generator with a source of grant data.

        :param grant_data_file: Path to the CSV file containing grant data
        """
        self.grant_data_file = grant_data_file
        self.grant_data = []

    def load_data(self):
        """
        Loads grant data from a CSV file into memory.
        """
        try:
            with open(self.grant_data_file, mode='r') as file:
                reader = csv.DictReader(file)
                self.grant_data = [row for row in reader]
        except FileNotFoundError:
            print(f"Error: The file '{self.grant_data_file}' was not found.")
            raise
        except Exception as e:
            print(f"Error: An error occurred while loading grant data: {e}")
            raise

    def calculate_impact_metrics(self):
        """
        Calculates aggregate metrics for educational outcomes and research advancements.

        :return: Dictionary containing impact metrics
        """
        metrics = {
            "total_grants": 0,
            "total_funding": 0.0,
            "educational_outcomes": 0,
            "research_advancements": 0
        }

        for grant in self.grant_data:
            try:
                metrics["total_grants"] += 1
                metrics["total_funding"] += float(grant.get("FundingAmount", 0))
                metrics["educational_outcomes"] += int(grant.get("EducationalOutcomes", 0))
                metrics["research_advancements"] += int(grant.get("ResearchAdvancements", 0))
            except ValueError:
                print(f"Warning: Invalid data format in grant record {grant}")
                continue

        return metrics

    def generate_report(self, output_file):
        """
        Generates a JSON report summarizing the impact of grants.

        :param output_file: Path to the output JSON file
        """
        metrics = self.calculate_impact_metrics()
        report = {
            "report_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "metrics": metrics
        }

        try:
            with open(output_file, mode='w') as file:
                json.dump(report, file, indent=4)
            print(f"Report successfully generated: {output_file}")
        except Exception as e:
            print(f"Error: Failed to write the report to '{output_file}': {e}")
            raise


if __name__ == "__main__":
    # File paths (modify as needed)
    grant_data_file = "grants_data.csv"
    output_report_file = "grant_impact_report.json"

    # Generate the grant impact report
    try:
        report_generator = GrantImpactReportGenerator(grant_data_file)
        report_generator.load_data()
        report_generator.generate_report(output_report_file)
    except Exception as e:
        print(f"Critical Error: The program encountered an issue and was unable to complete the report: {e}")
```

### Notes:
1. Replace `"grants_data.csv"` with the actual path to your input CSV file containing grant data.
2. Replace `"grant_impact_report.json"` with the desired path to save the JSON report.
3. The CSV file is expected to have at least the following columns: `FundingAmount`, `EducationalOutcomes`, `ResearchAdvancements`.
