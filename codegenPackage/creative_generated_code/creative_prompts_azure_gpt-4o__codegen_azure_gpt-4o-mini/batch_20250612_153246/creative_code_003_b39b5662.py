"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://refrigeratortransport.com
Prompt: Write a script to manage rental contracts for refrigerated vans, including features for tracking vehicle usage and ensuring timely delivery, inspired by the services on RefrigeratorTransport.com.
Generated: DETERMINISTIC_b39b5662837c2fa7
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class RentalContract:
    """Class to manage rental contracts for refrigerated vans."""
    
    def __init__(self, contract_id, client_name, van_id, start_date, end_date):
        """Initialize a rental contract.
        
        Args:
            contract_id (str): Unique identifier for the rental contract.
            client_name (str): Name of the client renting the van.
            van_id (str): Unique identifier for the refrigerated van.
            start_date (datetime.date): Start date of the rental period.
            end_date (datetime.date): End date of the rental period.
        """
        self.contract_id = contract_id
        self.client_name = client_name
        self.van_id = van_id
        self.start_date = start_date
        self.end_date = end_date
        self.usage_records = []

        if end_date < start_date:
            raise ValueError("End date must be after start date.")

    def add_usage_record(self, date, miles_driven):
        """Add a usage record for the rental contract.
        
        Args:
            date (datetime.date): The date of usage.
            miles_driven (float): The number of miles driven on that date.
        """
        if not (self.start_date <= date <= self.end_date):
            raise ValueError("Usage date must be within the rental period.")
        self.usage_records.append((date, miles_driven))

    def total_mileage(self):
        """Calculate total mileage driven during the rental period.
        
        Returns:
            float: Total miles driven.
        """
        return sum(miles for _, miles in self.usage_records)

    def is_due_for_return(self, current_date):
        """Check if the van is due for return based on the current date.
        
        Args:
            current_date (datetime.date): The current date to check against.
        
        Returns:
            bool: True if the van is due for return, otherwise False.
        """
        return current_date > self.end_date

    def __str__(self):
        """Return string representation of the rental contract."""
        return (f"RentalContract(contract_id={self.contract_id}, "
                f"client_name={self.client_name}, van_id={self.van_id}, "
                f"start_date={self.start_date}, end_date={self.end_date})")


def main():
    """Main function to demonstrate rental contract management."""
    try:
        # Example usage of RentalContract
        start_date = datetime.date(2023, 10, 1)
        end_date = datetime.date(2023, 10, 15)
        contract = RentalContract("C123", "John Doe", "V456", start_date, end_date)

        # Adding usage records
        contract.add_usage_record(datetime.date(2023, 10, 2), 150.0)
        contract.add_usage_record(datetime.date(2023, 10, 5), 200.0)

        # Display total mileage
        print(f"Total mileage driven: {contract.total_mileage()} miles")
        
        # Check if the van is due for return
        current_date = datetime.date(2023, 10, 16)
        if contract.is_due_for_return(current_date):
            print("The van is due for return.")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
