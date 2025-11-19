"""
Generated Code Metadata:
========================
Original URL: https://supplymarinebr.com.br
Prompt: Create a program to generate reports on the reliability and efficiency of maritime supply services, incorporating metrics such as delivery timeliness and product quality as emphasized by Supply Marine.
Generated: DETERMINISTIC_bd980cc304922a99
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import csv
from datetime import datetime
from typing import List, Dict, Optional, Tuple

class MaritimeSupplyReportGenerator:
    """
    A class to generate reports on the reliability and efficiency of maritime supply services.
    Metrics include delivery timeliness and product quality.
    """

    def __init__(self, data_source: str):
        """
        Initialize the report generator with a data source.
        
        Args:
            data_source: Path to the data file (JSON or CSV).
        """
        self.data_source = data_source
        self.data = self._load_data()

    def _load_data(self) -> List[Dict]:
        """
        Load data from the specified source file.
        
        Returns:
            List of dictionaries containing supply service records.
            
        Raises:
            ValueError: If the file format is unsupported or data is malformed.
            FileNotFoundError: If the data file does not exist.
        """
        try:
            if self.data_source.endswith('.json'):
                with open(self.data_source, 'r') as file:
                    return json.load(file)
            elif self.data_source.endswith('.csv'):
                with open(self.data_source, 'r') as file:
                    csv_reader = csv.DictReader(file)
                    return list(csv_reader)
            else:
                raise ValueError("Unsupported file format. Please provide a JSON or CSV file.")
        except FileNotFoundError:
            raise FileNotFoundError(f"Data file not found: {self.data_source}")
        except (json.JSONDecodeError, csv.Error) as e:
            raise ValueError(f"Malformed data in file: {e}")

    def calculate_timeliness_metrics(self) -> Dict[str, float]:
        """
        Calculate timeliness metrics including on-time delivery rate and average delay.
        
        Returns:
            Dictionary containing timeliness metrics.
        """
        if not self.data:
            return {}

        total_shipments = 0
        on_time_shipments = 0
        total_delay_days = 0

        for record in self.data:
            try:
                scheduled_date = datetime.strptime(record['scheduled_delivery_date'], '%Y-%m-%d')
                actual_date = datetime.strptime(record['actual_delivery_date'], '%Y-%m-%d')
                delay_days = (actual_date - scheduled_date).days
                
                total_shipments += 1
                if delay_days <= 0:
                    on_time_shipments += 1
                total_delay_days += max(0, delay_days)
            except (KeyError, ValueError):
                continue

        metrics = {}
        if total_shipments > 0:
            metrics['on_time_delivery_rate'] = (on_time_shipments / total_shipments) * 100
            metrics['average_delay_days'] = total_delay_days / total_shipments

        return metrics

    def calculate_quality_metrics(self) -> Dict[str, float]:
        """
        Calculate product quality metrics including damage rate and defect rate.
        
        Returns:
            Dictionary containing quality metrics.
        """
        if not self.data:
            return {}

        total_shipments = 0
        damaged_shipments = 0
        defective_shipments = 0

        for record in self.data:
            try:
                total_shipments += 1
                if record.get('damaged', 'false').lower() == 'true':
                    damaged_shipments += 1
                if record.get('defective', 'false').lower() == 'true':
                    defective_shipments += 1
            except (KeyError, ValueError):
                continue

        metrics = {}
        if total_shipments > 0:
            metrics['damage_rate'] = (damaged_shipments / total_shipments) * 100
            metrics['defect_rate'] = (defective_shipments / total_shipments) * 100

        return metrics

    def generate_report(self, output_format: str = 'json') -> Optional[str]:
        """
        Generate a comprehensive report with all metrics.
        
        Args:
            output_format: Desired output format ('json' or 'csv').
            
        Returns:
            String containing the report in specified format, or None if no data.
            
        Raises:
            ValueError: If output format is unsupported.
        """
        timeliness_metrics = self.calculate_timeliness_metrics()
        quality_metrics = self.calculate_quality_metrics()

        if not timeliness_metrics and not quality_metrics:
            return None

        report = {
            'timeliness_metrics': timeliness_metrics,
            'quality_metrics': quality_metrics,
            'generated_at': datetime.now().isoformat()
        }

        if output_format == 'json':
            return json.dumps(report, indent=2)
        elif output_format == 'csv':
            output = []
            # Flatten the report structure for CSV
            csv_header = list(timeliness_metrics.keys()) + list(quality_metrics.keys()) + ['generated_at']
            csv_row = list(timeliness_metrics.values()) + list(quality_metrics.values()) + [report['generated_at']]
            
            output.append(','.join(csv_header))
            output.append(','.join(map(str, csv_row)))
            return '\n'.join(output)
        else:
            raise ValueError("Unsupported output format. Choose 'json' or 'csv'.")

    def save_report(self, output_file: str, output_format: str = 'json') -> None:
        """
        Generate and save the report to a file.
        
        Args:
            output_file: Path to save the report.
            output_format: Desired output format ('json' or 'csv').
            
        Raises:
            ValueError: If output format is unsupported.
            IOError: If there's an issue writing the file.
        """
        report = self.generate_report(output_format)
        if report is None:
            raise ValueError("No data available to generate report.")

        try:
            with open(output_file, 'w') as file:
                file.write(report)
        except IOError as e:
            raise IOError(f"Failed to write report to file: {e}")


# Example usage
if __name__ == "__main__":
    try:
        # Initialize with sample data (replace with actual data source)
        report_generator = MaritimeSupplyReportGenerator('supply_data.json')
        
        # Generate and print JSON report
        json_report = report_generator.generate_report('json')
        print("JSON Report:")
        print(json_report)
        
        # Save CSV report
        report_generator.save_report('supply_report.csv', 'csv')
        print("\nCSV report saved to 'supply_report.csv'")
        
    except Exception as e:
        print(f"Error generating report: {e}")
```
