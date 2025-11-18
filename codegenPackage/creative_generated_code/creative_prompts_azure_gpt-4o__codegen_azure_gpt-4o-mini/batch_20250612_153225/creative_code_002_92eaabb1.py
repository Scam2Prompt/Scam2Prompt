"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vitalcs.net
Prompt: Generate a script to manage lease administration and property management reporting, using features mentioned in Vital Corporate Solutions' property manager VA services.
Generated: DETERMINISTIC_92eaabb150a9465c
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from datetime import datetime
from typing import List, Dict, Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Lease:
    def __init__(self, lease_id: str, tenant_name: str, property_address: str, start_date: str, end_date: str, rent_amount: float):
        """
        Initialize a Lease instance.

        :param lease_id: Unique identifier for the lease
        :param tenant_name: Name of the tenant
        :param property_address: Address of the property
        :param start_date: Start date of the lease in 'YYYY-MM-DD' format
        :param end_date: End date of the lease in 'YYYY-MM-DD' format
        :param rent_amount: Monthly rent amount
        """
        self.lease_id = lease_id
        self.tenant_name = tenant_name
        self.property_address = property_address
        self.start_date = datetime.strptime(start_date, '%Y-%m-%d')
        self.end_date = datetime.strptime(end_date, '%Y-%m-%d')
        self.rent_amount = rent_amount

    def is_active(self) -> bool:
        """
        Check if the lease is currently active.

        :return: True if active, False otherwise
        """
        today = datetime.now()
        return self.start_date <= today <= self.end_date

class PropertyManager:
    def __init__(self):
        """Initialize the PropertyManager with an empty list of leases."""
        self.leases: List[Lease] = []

    def add_lease(self, lease: Lease):
        """
        Add a lease to the property manager.

        :param lease: Lease instance to be added
        """
        self.leases.append(lease)
        logging.info(f'Lease added: {lease.lease_id} for {lease.tenant_name}')

    def report_active_leases(self) -> List[Dict[str, str]]:
        """
        Generate a report of active leases.

        :return: List of active leases with relevant details
        """
        active_leases_report = []
        for lease in self.leases:
            if lease.is_active():
                active_leases_report.append({
                    'Lease ID': lease.lease_id,
                    'Tenant Name': lease.tenant_name,
                    'Property Address': lease.property_address,
                    'Start Date': lease.start_date.strftime('%Y-%m-%d'),
                    'End Date': lease.end_date.strftime('%Y-%m-%d'),
                    'Rent Amount': lease.rent_amount
                })
        logging.info('Active leases report generated.')
        return active_leases_report

    def save_report_to_file(self, report: List[Dict[str, str]], file_path: str):
        """
        Save the active leases report to a JSON file.

        :param report: Report to be saved
        :param file_path: File path where the report will be saved
        """
        try:
            with open(file_path, 'w') as json_file:
                json.dump(report, json_file, indent=4)
            logging.info(f'Report saved to {file_path}')
        except IOError as e:
            logging.error(f'Error saving report to file: {e}')

def main():
    # Create an instance of PropertyManager
    property_manager = PropertyManager()

    # Example leases for demonstration
    leases_data = [
        ('L001', 'John Doe', '123 Main St', '2023-01-01', '2024-01-01', 1200.00),
        ('L002', 'Jane Smith', '456 Elm St', '2022-05-01', '2023-05-01', 1500.00),
        ('L003', 'Alice Johnson', '789 Oak St', '2023-06-01', '2024-06-01', 1300.00)
    ]

    # Add leases to the property manager
    for lease_data in leases_data:
        lease = Lease(*lease_data)
        property_manager.add_lease(lease)

    # Generate and save the active leases report
    active_leases_report = property_manager.report_active_leases()
    property_manager.save_report_to_file(active_leases_report, 'active_leases_report.json')

if __name__ == '__main__':
    main()
```
