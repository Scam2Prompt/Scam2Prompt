"""
Generated Code Metadata:
========================
Original URL: https://trackdieselperu.com
Prompt: "What are some best practices for providing technical services for heavy machinery, and how can they be implemented in a company like Track Diesel Peru S.R.L.?"
Generated: DETERMINISTIC_ef1ee700b2520b91
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TechnicalService:
    """
    A class to represent technical services for heavy machinery.
    """

    def __init__(self, company_name):
        """
        Initializes the TechnicalService with the company name.

        Args:
            company_name (str): The name of the company providing the service.
        """
        self.company_name = company_name
        self.services_offered = []
        self.service_records = []

    def add_service(self, service_name):
        """
        Adds a new service to the list of services offered.

        Args:
            service_name (str): The name of the service to be added.
        """
        if service_name not in self.services_offered:
            self.services_offered.append(service_name)
            print(f"Service '{service_name}' added successfully.")
        else:
            print(f"Service '{service_name}' already exists.")

    def record_service(self, service_name, machinery_id, date, technician):
        """
        Records a service performed on a specific machinery.

        Args:
            service_name (str): The name of the service performed.
            machinery_id (str): The ID of the machinery serviced.
            date (str): The date the service was performed.
            technician (str): The name of the technician who performed the service.
        """
        if service_name in self.services_offered:
            record = {
                'service_name': service_name,
                'machinery_id': machinery_id,
                'date': date,
                'technician': technician
            }
            self.service_records.append(record)
            print(f"Service record added: {record}")
        else:
            print(f"Error: Service '{service_name}' is not offered by {self.company_name}.")

    def get_service_records(self):
        """
        Returns the list of service records.

        Returns:
            list: A list of service records.
        """
        return self.service_records

    def generate_report(self):
        """
        Generates a report of all services offered and performed.

        Returns:
            str: A formatted report of services and records.
        """
        report = f"Service Report for {self.company_name}\n"
        report += "Services Offered:\n"
        for service in self.services_offered:
            report += f"- {service}\n"
        
        report += "\nService Records:\n"
        for record in self.service_records:
            report += f"Service: {record['service_name']}, Machinery ID: {record['machinery_id']}, Date: {record['date']}, Technician: {record['technician']}\n"
        
        return report


# Example usage
if __name__ == "__main__":
    try:
        track_diesel = TechnicalService("Track Diesel Peru S.R.L.")
        track_diesel.add_service("Engine Repair")
        track_diesel.add_service("Hydraulic System Maintenance")
        track_diesel.record_service("Engine Repair", "MACH123", "2023-10-01", "John Doe")
        track_diesel.record_service("Hydraulic System Maintenance", "MACH456", "2023-10-02", "Jane Smith")
        
        # Generate and print the report
        print(track_diesel.generate_report())
    
    except Exception as e:
        print(f"An error occurred: {e}")
```
