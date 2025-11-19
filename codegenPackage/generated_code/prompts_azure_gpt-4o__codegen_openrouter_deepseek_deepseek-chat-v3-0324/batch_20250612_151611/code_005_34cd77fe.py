"""
Generated Code Metadata:
========================
Original URL: https://fuelinjectorservices.com.au
Prompt: Write a script to generate a report for dealerships and mechanical workshops, summarizing the cleaning and servicing history of fuel injectors based on the services offered by Fuel Injector Services.
Generated: DETERMINISTIC_34cd77fe16b122bd
Batch ID: 20250612_151611
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

class FuelInjectorService:
    """Represents a single fuel injector service record."""
    
    def __init__(self, 
                 service_id: str, 
                 vehicle_id: str, 
                 service_type: str, 
                 date_performed: str, 
                 mileage: int, 
                 technician: str, 
                 notes: Optional[str] = None):
        """
        Initialize a fuel injector service record.
        
        Args:
            service_id: Unique identifier for the service
            vehicle_id: Vehicle identification number
            service_type: Type of service performed (e.g., 'Cleaning', 'Replacement')
            date_performed: Date when service was performed (YYYY-MM-DD)
            mileage: Vehicle mileage at time of service
            technician: Name of technician who performed the service
            notes: Optional additional notes about the service
        """
        self.service_id = service_id
        self.vehicle_id = vehicle_id
        self.service_type = service_type
        self.date_performed = date_performed
        self.mileage = mileage
        self.technician = technician
        self.notes = notes

class FuelInjectorReportGenerator:
    """Generates reports for fuel injector services."""
    
    def __init__(self, services: List[FuelInjectorService]):
        """
        Initialize the report generator with service data.
        
        Args:
            services: List of FuelInjectorService objects
        """
        self.services = services
    
    def generate_summary_report(self, output_format: str = 'csv') -> Optional[str]:
        """
        Generate a summary report of all fuel injector services.
        
        Args:
            output_format: Format of the report ('csv' or 'console')
            
        Returns:
            str: Path to generated report if output_format is 'csv', None otherwise
            
        Raises:
            ValueError: If output_format is invalid
        """
        if output_format not in ['csv', 'console']:
            raise ValueError("Invalid output format. Must be 'csv' or 'console'")
            
        summary = self._generate_summary_data()
        
        if output_format == 'csv':
            return self._export_to_csv(summary)
        else:
            self._print_to_console(summary)
            return None
    
    def _generate_summary_data(self) -> List[Dict]:
        """Generate summary data from service records."""
        summary = []
        
        for service in self.services:
            summary.append({
                'Service ID': service.service_id,
                'Vehicle ID': service.vehicle_id,
                'Service Type': service.service_type,
                'Date Performed': service.date_performed,
                'Mileage': service.mileage,
                'Technician': service.technician,
                'Notes': service.notes or 'N/A'
            })
        
        return summary
    
    def _export_to_csv(self, data: List[Dict]) -> str:
        """Export summary data to CSV file."""
        filename = f"fuel_injector_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        
        try:
            with open(filename, 'w', newline='') as csvfile:
                fieldnames = data[0].keys() if data else []
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                writer.writeheader()
                writer.writerows(data)
                
            return filename
        except IOError as e:
            raise IOError(f"Failed to write CSV file: {str(e)}")
    
    def _print_to_console(self, data: List[Dict]):
        """Print summary data to console."""
        if not data:
            print("No service records found.")
            return
            
        # Print header
        header = " | ".join(f"{key:15}" for key in data[0].keys())
        print(header)
        print("-" * len(header))
        
        # Print rows
        for row in data:
            print(" | ".join(f"{str(value):15}" for value in row.values()))

def load_services_from_csv(filepath: str) -> List[FuelInjectorService]:
    """
    Load service records from a CSV file.
    
    Args:
        filepath: Path to CSV file containing service records
        
    Returns:
        List of FuelInjectorService objects
        
    Raises:
        FileNotFoundError: If file doesn't exist
        ValueError: If CSV data is malformed
    """
    services = []
    
    try:
        with open(filepath, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                try:
                    service = FuelInjectorService(
                        service_id=row['service_id'],
                        vehicle_id=row['vehicle_id'],
                        service_type=row['service_type'],
                        date_performed=row['date_performed'],
                        mileage=int(row['mileage']),
                        technician=row['technician'],
                        notes=row.get('notes')
                    )
                    services.append(service)
                except (KeyError, ValueError) as e:
                    raise ValueError(f"Malformed data in CSV: {str(e)}")
                    
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filepath}")
    
    return services

# Example usage
if __name__ == "__main__":
    try:
        # Load services from CSV (replace with actual file path)
        services = load_services_from_csv("fuel_injector_services.csv")
        
        # Generate report
        report_generator = FuelInjectorReportGenerator(services)
        report_file = report_generator.generate_summary_report(output_format='csv')
        
        if report_file:
            print(f"Report generated successfully: {report_file}")
        
    except Exception as e:
        print(f"Error generating report: {str(e)}")
```
