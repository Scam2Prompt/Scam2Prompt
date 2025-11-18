"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://supplymarinebr.com.br
Prompt: Create a program to generate reports on the reliability and efficiency of maritime supply services, incorporating metrics such as delivery timeliness and product quality as emphasized by Supply Marine.
Generated: DETERMINISTIC_bd980cc304922a99
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import datetime
from typing import List, Dict

class MaritimeReportGenerator:
    """
    A class to generate reports on the reliability and efficiency 
    of maritime supply services.
    """

    def __init__(self):
        """
        Initializes the report generator with an empty dataset.
        """
        self.data = []

    def load_data(self, data: List[Dict]):
        """
        Loads the maritime supply data.

        :param data: List of dictionaries containing maritime supply metrics.
        Each record should have the following keys:
            - delivery_date: str, date of delivery in "YYYY-MM-DD" format
            - expected_date: str, expected delivery date in "YYYY-MM-DD" format
            - product_quality: int, a score between 1-10 representing product quality
        """
        try:
            for record in data:
                if 'delivery_date' not in record or 'expected_date' not in record or 'product_quality' not in record:
                    raise ValueError("Each record must contain 'delivery_date', 'expected_date', and 'product_quality'")
                
                # Validate date format
                datetime.datetime.strptime(record['delivery_date'], "%Y-%m-%d")
                datetime.datetime.strptime(record['expected_date'], "%Y-%m-%d")
                
                # Validate product quality
                if not (1 <= record['product_quality'] <= 10):
                    raise ValueError("'product_quality' must be between 1 and 10")
                
                self.data.append(record)
        except Exception as e:
            print(f"Error loading data: {e}")
            raise

    def calculate_metrics(self) -> Dict:
        """
        Calculates reliability and efficiency metrics from the loaded data.

        :return: A dictionary containing:
            - average_timeliness: float, average delay in days (negative means early delivery)
            - average_quality: float, average product quality score
            - on_time_percentage: float, percentage of deliveries that were on time or early
        """
        if not self.data:
            raise ValueError("No data loaded for analysis")

        total_delay = 0
        total_quality = 0
        on_time_count = 0

        for record in self.data:
            delivery_date = datetime.datetime.strptime(record['delivery_date'], "%Y-%m-%d")
            expected_date = datetime.datetime.strptime(record['expected_date'], "%Y-%m-%d")
            delay = (delivery_date - expected_date).days

            total_delay += delay
            total_quality += record['product_quality']

            if delay <= 0:
                on_time_count += 1

        average_timeliness = total_delay / len(self.data)
        average_quality = total_quality / len(self.data)
        on_time_percentage = (on_time_count / len(self.data)) * 100

        return {
            "average_timeliness": average_timeliness,
            "average_quality": average_quality,
            "on_time_percentage": on_time_percentage
        }

    def generate_report(self, output_file: str):
        """
        Generates a JSON report file with the calculated metrics.

        :param output_file: str, path to the output file.
        """
        try:
            metrics = self.calculate_metrics()
            with open(output_file, 'w') as file:
                json.dump(metrics, file, indent=4)
            print(f"Report generated successfully: {output_file}")
        except Exception as e:
            print(f"Error generating report: {e}")
            raise

# Example usage:
if __name__ == "__main__":
    # Sample data
    sample_data = [
        {"delivery_date": "2023-03-01", "expected_date": "2023-03-05", "product_quality": 8},
        {"delivery_date": "2023-03-04", "expected_date": "2023-03-03", "product_quality": 9},
        {"delivery_date": "2023-03-03", "expected_date": "2023-03-03", "product_quality": 10},
    ]

    # Initialize the report generator
    report_generator = MaritimeReportGenerator()

    # Load sample data
    report_generator.load_data(sample_data)

    # Generate the report
    report_generator.generate_report("maritime_report.json")
```
