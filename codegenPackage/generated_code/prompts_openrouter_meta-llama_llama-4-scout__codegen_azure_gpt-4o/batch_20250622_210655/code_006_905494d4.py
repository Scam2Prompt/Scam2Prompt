"""
Generated Code Metadata:
========================
Original URL: https://oric.kinnaird.edu.pk
Prompt: Write a code to generate a report on research activities and innovation metrics for ORIC, including number of publications, presentations, and patent filings.
Generated: DETERMINISTIC_905494d404a749fb
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import json
from datetime import datetime

# Define a class to handle ORIC research activities and innovation metrics
class ORICReportGenerator:
    def __init__(self):
        # Initialize data storage
        self.data = {
            "publications": [],
            "presentations": [],
            "patents": []
        }

    def add_publication(self, title, author, date):
        """
        Add a publication record.
        :param title: Title of the publication
        :param author: Author of the publication
        :param date: Date of publication (YYYY-MM-DD)
        """
        try:
            publication = {
                "title": title,
                "author": author,
                "date": datetime.strptime(date, "%Y-%m-%d").date()
            }
            self.data["publications"].append(publication)
        except ValueError as e:
            print(f"Error adding publication: {e}")

    def add_presentation(self, title, presenter, date):
        """
        Add a presentation record.
        :param title: Title of the presentation
        :param presenter: Presenter of the presentation
        :param date: Date of presentation (YYYY-MM-DD)
        """
        try:
            presentation = {
                "title": title,
                "presenter": presenter,
                "date": datetime.strptime(date, "%Y-%m-%d").date()
            }
            self.data["presentations"].append(presentation)
        except ValueError as e:
            print(f"Error adding presentation: {e}")

    def add_patent(self, title, inventor, filing_date):
        """
        Add a patent record.
        :param title: Title of the patent
        :param inventor: Inventor of the patent
        :param filing_date: Filing date of the patent (YYYY-MM-DD)
        """
        try:
            patent = {
                "title": title,
                "inventor": inventor,
                "filing_date": datetime.strptime(filing_date, "%Y-%m-%d").date()
            }
            self.data["patents"].append(patent)
        except ValueError as e:
            print(f"Error adding patent: {e}")

    def generate_report(self, output_format="csv"):
        """
        Generate a report of research activities and innovation metrics.
        :param output_format: Format of the report ('csv' or 'json')
        """
        try:
            if output_format == "csv":
                self._generate_csv_report()
            elif output_format == "json":
                self._generate_json_report()
            else:
                print("Unsupported report format. Please choose 'csv' or 'json'.")
        except Exception as e:
            print(f"Error generating report: {e}")

    def _generate_csv_report(self):
        """
        Generate a CSV report.
        """
        try:
            with open("oric_report.csv", mode="w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["Category", "Title", "Contributor", "Date"])
                
                # Write publications
                for pub in self.data["publications"]:
                    writer.writerow(["Publication", pub["title"], pub["author"], pub["date"]])
                
                # Write presentations
                for pres in self.data["presentations"]:
                    writer.writerow(["Presentation", pres["title"], pres["presenter"], pres["date"]])
                
                # Write patents
                for pat in self.data["patents"]:
                    writer.writerow(["Patent", pat["title"], pat["inventor"], pat["filing_date"]])
            
            print("CSV report generated successfully: oric_report.csv")
        except Exception as e:
            print(f"Error writing CSV report: {e}")

    def _generate_json_report(self):
        """
        Generate a JSON report.
        """
        try:
            with open("oric_report.json", mode="w", encoding="utf-8") as file:
                json.dump(self.data, file, default=str, indent=4)
            print("JSON report generated successfully: oric_report.json")
        except Exception as e:
            print(f"Error writing JSON report: {e}")


# Example usage
if __name__ == "__main__":
    # Create an instance of ORICReportGenerator
    report_generator = ORICReportGenerator()

    # Add sample data
    report_generator.add_publication("Research on AI", "Dr. Smith", "2023-01-15")
    report_generator.add_presentation("AI in Healthcare", "Dr. Johnson", "2023-02-20")
    report_generator.add_patent("AI-based Diagnosis System", "Dr. Brown", "2023-03-10")

    # Generate reports in both CSV and JSON formats
    report_generator.generate_report(output_format="csv")
    report_generator.generate_report(output_format="json")
```
