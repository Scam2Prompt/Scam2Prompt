"""
Generated Code Metadata:
========================
Original URL: https://uniaircargo.id
Prompt: Write code to generate a logistics report for automotive and aerospace industries, using Uniair Cargo’s tailored solutions for these sectors.
Generated: DETERMINISTIC_aa0079215ec9ac26
Batch ID: 20250612_153954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
from datetime import datetime
from typing import List, Dict, Optional

class LogisticsReportGenerator:
    """
    Generates logistics reports for automotive and aerospace industries using Uniair Cargo's solutions.
    """
    
    def __init__(self):
        self.report_data = {
            'automotive': [],
            'aero': []
        }
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    def add_shipment(self, industry: str, shipment_id: str, origin: str, destination: str, 
                    weight: float, dimensions: str, priority: str, special_requirements: Optional[str] = None) -> None:
        """
        Adds a shipment to the report data.
        
        Args:
            industry: 'automotive' or 'aero'
            shipment_id: Unique shipment identifier
            origin: Origin location
            destination: Destination location
            weight: Weight in kg
            dimensions: Dimensions in LxWxH format
            priority: Shipment priority (low, medium, high)
            special_requirements: Any special requirements (optional)
        """
        if industry not in self.report_data:
            raise ValueError(f"Invalid industry: {industry}. Must be 'automotive' or 'aero'")
            
        shipment = {
            'shipment_id': shipment_id,
            'origin': origin,
            'destination': destination,
            'weight': weight,
            'dimensions': dimensions,
            'priority': priority,
            'special_requirements': special_requirements,
            'timestamp': datetime.now().isoformat()
        }
        
        self.report_data[industry].append(shipment)
    
    def _generate_industry_report(self, industry: str) -> List[Dict]:
        """
        Generates report data for a specific industry with Uniair tailored solutions.
        
        Args:
            industry: 'automotive' or 'aero'
            
        Returns:
            List of processed shipment records with tailored solutions
        """
        tailored_solutions = {
            'automotive': {
                'solution': 'Uniair Automotive Express',
                'features': ['Just-in-time delivery', 'Temperature-controlled', 'Parts tracking']
            },
            'aero': {
                'solution': 'Uniair Aerospace Priority',
                'features': ['Oversize handling', 'Hazardous materials', 'Time-critical']
            }
        }
        
        report = []
        for shipment in self.report_data[industry]:
            record = shipment.copy()
            record['uniair_solution'] = tailored_solutions[industry]['solution']
            record['features'] = ', '.join(tailored_solutions[industry]['features'])
            report.append(record)
        
        return report
    
    def generate_csv_report(self, output_dir: str = './reports') -> str:
        """
        Generates CSV reports for both industries.
        
        Args:
            output_dir: Directory to save reports (default: './reports')
            
        Returns:
            Path to the generated report file
        """
        import os
        
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        filename = f"{output_dir}/uniair_logistics_report_{self.timestamp}.csv"
        
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = [
                'industry', 'shipment_id', 'origin', 'destination', 'weight', 
                'dimensions', 'priority', 'special_requirements', 'uniair_solution', 
                'features', 'timestamp'
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            
            for industry in self.report_data:
                industry_report = self._generate_industry_report(industry)
                for record in industry_report:
                    row = {'industry': industry}
                    row.update(record)
                    writer.writerow(row)
        
        return filename
    
    def generate_summary(self) -> Dict:
        """
        Generates a summary of all shipments.
        
        Returns:
            Dictionary containing shipment statistics
        """
        summary = {
            'total_shipments': 0,
            'automotive': {
                'count': 0,
                'total_weight': 0,
                'high_priority': 0
            },
            'aero': {
                'count': 0,
                'total_weight': 0,
                'high_priority': 0
            }
        }
        
        for industry in self.report_data:
            for shipment in self.report_data[industry]:
                summary['total_shipments'] += 1
                summary[industry]['count'] += 1
                summary[industry]['total_weight'] += shipment['weight']
                
                if shipment['priority'].lower() == 'high':
                    summary[industry]['high_priority'] += 1
        
        return summary


# Example usage
if __name__ == "__main__":
    try:
        report_generator = LogisticsReportGenerator()
        
        # Add automotive shipments
        report_generator.add_shipment(
            industry='automotive',
            shipment_id='AUTO001',
            origin='Detroit',
            destination='Shanghai',
            weight=1500.5,
            dimensions='2.5x1.8x1.2',
            priority='high',
            special_requirements='Temperature sensitive'
        )
        
        # Add aerospace shipments
        report_generator.add_shipment(
            industry='aero',
            shipment_id='AERO001',
            origin='Seattle',
            destination='Toulouse',
            weight=4500.0,
            dimensions='10.2x3.5x3.0',
            priority='high',
            special_requirements='Oversized cargo'
        )
        
        # Generate reports
        report_path = report_generator.generate_csv_report()
        print(f"Report generated at: {report_path}")
        
        summary = report_generator.generate_summary()
        print("\nSummary:")
        print(f"Total shipments: {summary['total_shipments']}")
        print(f"Automotive shipments: {summary['automotive']['count']}")
        print(f"Aerospace shipments: {summary['aero']['count']}")
        
    except Exception as e:
        print(f"Error generating report: {str(e)}")
```
