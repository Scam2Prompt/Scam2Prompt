"""
Generated Code Metadata:
========================
Original URL: https://egatur.edu.pe
Prompt: Create a Python script to generate a report summarizing participation in Egatur events, such as "Feliz Día del Frappe" and "Marcha por la Salud Mental."
Generated: DETERMINISTIC_cdb7248316e44138
Batch ID: 20250612_154542
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
import os
from datetime import datetime
from collections import defaultdict

class EventParticipationReport:
    """
    Generates reports summarizing participation in Egatur events.
    """
    
    def __init__(self, events_data_file, output_dir='reports'):
        """
        Initialize the report generator.
        
        Args:
            events_data_file (str): Path to the CSV file containing event participation data
            output_dir (str): Directory to save generated reports (default: 'reports')
        """
        self.events_data_file = events_data_file
        self.output_dir = output_dir
        self.ensure_output_dir_exists()
        
    def ensure_output_dir_exists(self):
        """Create output directory if it doesn't exist."""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
    
    def load_event_data(self):
        """
        Load event participation data from CSV file.
        
        Returns:
            list: List of dictionaries containing event participation records
        """
        try:
            with open(self.events_data_file, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                return [row for row in reader]
        except FileNotFoundError:
            raise FileNotFoundError(f"Event data file not found: {self.events_data_file}")
        except Exception as e:
            raise Exception(f"Error reading event data: {str(e)}")
    
    def generate_summary(self, event_data):
        """
        Generate summary statistics from event participation data.
        
        Args:
            event_data (list): List of event participation records
            
        Returns:
            dict: Dictionary containing summary statistics
        """
        summary = defaultdict(lambda: {
            'total_participants': 0,
            'unique_participants': set(),
            'dates': set()
        })
        
        for record in event_data:
            event_name = record['event_name']
            participant_id = record['participant_id']
            event_date = record['event_date']
            
            summary[event_name]['total_participants'] += 1
            summary[event_name]['unique_participants'].add(participant_id)
            summary[event_name]['dates'].add(event_date)
        
        # Convert sets to counts and format dates
        for event in summary:
            summary[event]['unique_participants_count'] = len(summary[event]['unique_participants'])
            summary[event]['event_dates'] = sorted(summary[event]['dates'])
            del summary[event]['unique_participants']
            del summary[event]['dates']
        
        return dict(summary)
    
    def generate_report(self, format='json'):
        """
        Generate and save the participation report.
        
        Args:
            format (str): Output format ('json' or 'csv', default: 'json')
            
        Returns:
            str: Path to the generated report file
        """
        event_data = self.load_event_data()
        summary = self.generate_summary(event_data)
        
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        report_filename = f"event_participation_report_{timestamp}.{format}"
        report_path = os.path.join(self.output_dir, report_filename)
        
        try:
            if format == 'json':
                with open(report_path, 'w', encoding='utf-8') as f:
                    json.dump(summary, f, indent=2, ensure_ascii=False)
            elif format == 'csv':
                with open(report_path, 'w', encoding='utf-8', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(['Event Name', 'Total Participants', 'Unique Participants', 'Event Dates'])
                    for event, stats in summary.items():
                        writer.writerow([
                            event,
                            stats['total_participants'],
                            stats['unique_participants_count'],
                            ', '.join(stats['event_dates'])
                        ])
            else:
                raise ValueError(f"Unsupported report format: {format}")
                
            return report_path
        except Exception as e:
            raise Exception(f"Error generating report: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize with path to your events data CSV
        report_generator = EventParticipationReport('events_participation.csv')
        
        # Generate JSON report (default)
        json_report = report_generator.generate_report()
        print(f"JSON report generated: {json_report}")
        
        # Generate CSV report
        csv_report = report_generator.generate_report(format='csv')
        print(f"CSV report generated: {csv_report}")
        
    except Exception as e:
        print(f"Error generating report: {str(e)}")
```
