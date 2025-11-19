"""
Generated Code Metadata:
========================
Original URL: https://visa-pwr.com
Prompt: Write a script to generate reports on visa application centre performance, incorporating metrics on customer experience and security considerations.
Generated: DETERMINISTIC_7650628db82fcf34
Batch ID: 20250622_212709
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
import datetime
from collections import defaultdict
from typing import Dict, List, Tuple, Optional

class VisaApplicationCentreReportGenerator:
    """
    Generates performance reports for Visa Application Centres (VACs).
    Includes metrics on customer experience and security considerations.
    """

    def __init__(self, data_source: str):
        """
        Initialize the report generator with a data source.
        
        Args:
            data_source: Path to the data file (CSV or JSON)
        """
        self.data_source = data_source
        self.data = None
        self.load_data()

    def load_data(self) -> None:
        """Load and validate the input data."""
        try:
            if self.data_source.endswith('.csv'):
                with open(self.data_source, 'r') as f:
                    reader = csv.DictReader(f)
                    self.data = list(reader)
            elif self.data_source.endswith('.json'):
                with open(self.data_source, 'r') as f:
                    self.data = json.load(f)
            else:
                raise ValueError("Unsupported file format. Only CSV and JSON are supported.")
            
            if not self.data:
                raise ValueError("No data found in the file.")
                
        except FileNotFoundError:
            raise FileNotFoundError(f"Data file not found: {self.data_source}")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format in the data file.")
        except Exception as e:
            raise Exception(f"Error loading data: {str(e)}")

    def calculate_customer_experience_metrics(self) -> Dict[str, float]:
        """
        Calculate customer experience metrics.
        
        Returns:
            Dictionary containing customer experience metrics:
            - average_wait_time: Average wait time in minutes
            - satisfaction_score: Average satisfaction score (1-5)
            - processing_time: Average processing time in minutes
        """
        if not self.data:
            raise ValueError("No data available for calculation.")
            
        total_wait = 0
        total_satisfaction = 0
        total_processing = 0
        count = 0
        
        for record in self.data:
            try:
                total_wait += float(record.get('wait_time', 0))
                total_satisfaction += float(record.get('satisfaction_score', 0))
                total_processing += float(record.get('processing_time', 0))
                count += 1
            except (ValueError, TypeError):
                continue
        
        if count == 0:
            return {
                'average_wait_time': 0,
                'satisfaction_score': 0,
                'processing_time': 0
            }
            
        return {
            'average_wait_time': round(total_wait / count, 2),
            'satisfaction_score': round(total_satisfaction / count, 2),
            'processing_time': round(total_processing / count, 2)
        }

    def calculate_security_metrics(self) -> Dict[str, float]:
        """
        Calculate security-related metrics.
        
        Returns:
            Dictionary containing security metrics:
            - security_incidents: Number of security incidents
            - screening_failures: Number of screening failures
            - incident_rate: Incident rate per 1000 applicants
        """
        if not self.data:
            raise ValueError("No data available for calculation.")
            
        incidents = 0
        failures = 0
        applicants = 0
        
        for record in self.data:
            try:
                incidents += int(record.get('security_incidents', 0))
                failures += int(record.get('screening_failures', 0))
                applicants += 1
            except (ValueError, TypeError):
                continue
        
        incident_rate = (incidents / applicants * 1000) if applicants > 0 else 0
        
        return {
            'security_incidents': incidents,
            'screening_failures': failures,
            'incident_rate': round(incident_rate, 2)
        }

    def generate_centre_report(self, centre_id: str) -> Dict:
        """
        Generate a comprehensive report for a specific centre.
        
        Args:
            centre_id: ID of the centre to generate report for
            
        Returns:
            Dictionary containing full report for the centre
        """
        if not self.data:
            raise ValueError("No data available for report generation.")
            
        centre_data = [record for record in self.data if record.get('centre_id') == centre_id]
        
        if not centre_data:
            raise ValueError(f"No data found for centre ID: {centre_id}")
            
        customer_metrics = self.calculate_customer_experience_metrics()
        security_metrics = self.calculate_security_metrics()
        
        return {
            'centre_id': centre_id,
            'report_date': datetime.datetime.now().isoformat(),
            'customer_experience': customer_metrics,
            'security_metrics': security_metrics,
            'total_applications': len(centre_data)
        }

    def generate_summary_report(self) -> Dict:
        """
        Generate a summary report for all centres.
        
        Returns:
            Dictionary containing summary metrics for all centres
        """
        if not self.data:
            raise ValueError("No data available for report generation.")
            
        centres = defaultdict(list)
        for record in self.data:
            centre_id = record.get('centre_id')
            if centre_id:
                centres[centre_id].append(record)
                
        summary = {
            'total_centres': len(centres),
            'total_applications': len(self.data),
            'centres': {}
        }
        
        for centre_id, centre_data in centres.items():
            self.data = centre_data
            summary['centres'][centre_id] = {
                'customer_experience': self.calculate_customer_experience_metrics(),
                'security_metrics': self.calculate_security_metrics(),
                'applications': len(centre_data)
            }
            
        # Restore original data
        self.load_data()
        
        return summary

    def save_report(self, report: Dict, output_file: str) -> None:
        """
        Save the generated report to a file.
        
        Args:
            report: The report dictionary to save
            output_file: Path to the output file
        """
        try:
            if output_file.endswith('.json'):
                with open(output_file, 'w') as f:
                    json.dump(report, f, indent=4)
            elif output_file.endswith('.csv'):
                # Flatten the report structure for CSV output
                flat_data = []
                if 'centres' in report:
                    for centre_id, metrics in report['centres'].items():
                        row = {
                            'centre_id': centre_id,
                            'report_date': report.get('report_date', ''),
                            **metrics['customer_experience'],
                            **metrics['security_metrics'],
                            'applications': metrics['applications']
                        }
                        flat_data.append(row)
                else:
                    flat_data.append({
                        'centre_id': report.get('centre_id', ''),
                        'report_date': report.get('report_date', ''),
                        **report['customer_experience'],
                        **report['security_metrics'],
                        'applications': report.get('total_applications', 0)
                    })
                
                with open(output_file, 'w', newline='') as f:
                    writer = csv.DictWriter(f, fieldnames=flat_data[0].keys())
                    writer.writeheader()
                    writer.writerows(flat_data)
            else:
                raise ValueError("Unsupported output format. Only JSON and CSV are supported.")
                
        except Exception as e:
            raise Exception(f"Error saving report: {str(e)}")


# Example usage
if __name__ == "__main__":
    try:
        # Initialize with sample data
        generator = VisaApplicationCentreReportGenerator("vac_data.csv")
        
        # Generate a report for a specific centre
        centre_report = generator.generate_centre_report("VAC123")
        generator.save_report(centre_report, "centre_report.json")
        
        # Generate a summary report for all centres
        summary_report = generator.generate_summary_report()
        generator.save_report(summary_report, "summary_report.csv")
        
    except Exception as e:
        print(f"Error generating reports: {str(e)}")
```
