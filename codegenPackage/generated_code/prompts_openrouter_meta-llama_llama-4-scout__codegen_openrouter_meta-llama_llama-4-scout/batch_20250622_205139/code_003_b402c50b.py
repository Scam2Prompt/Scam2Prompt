"""
Generated Code Metadata:
========================
Original URL: https://qualitysheetmetalincorporated.org
Prompt: "Create a simple HVAC warranty tracker using a library like pandas in Python, considering 10-year parts and 20-year heat exchanger warranty."
Generated: DETERMINISTIC_b402c50b16913d76
Batch ID: 20250622_205139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from datetime import datetime, timedelta

class HVACWarrantyTracker:
    def __init__(self):
        """
        Initialize the warranty tracker with empty dataframes for parts and units.
        """
        self.parts_warranties = pd.DataFrame(columns=['Part ID', 'Installation Date', 'Warranty Period (Years)'])
        self.units_warranties = pd.DataFrame(columns=['Unit ID', 'Installation Date', 'Heat Exchanger Warranty Period (Years)'])

    def add_part_warranty(self, part_id, installation_date, warranty_period=10):
        """
        Add a part warranty to the tracker.

        Args:
            part_id (str): Unique identifier for the part.
            installation_date (str): Date of installation in 'YYYY-MM-DD' format.
            warranty_period (int, optional): Warranty period in years. Defaults to 10.
        """
        new_part_warranty = pd.DataFrame([{'Part ID': part_id, 'Installation Date': installation_date, 'Warranty Period (Years)': warranty_period}])
        self.parts_warranties = pd.concat([self.parts_warranties, new_part_warranty], ignore_index=True)

    def add_unit_warranty(self, unit_id, installation_date, heat_exchanger_warranty_period=20):
        """
        Add a unit warranty to the tracker.

        Args:
            unit_id (str): Unique identifier for the unit.
            installation_date (str): Date of installation in 'YYYY-MM-DD' format.
            heat_exchanger_warranty_period (int, optional): Heat exchanger warranty period in years. Defaults to 20.
        """
        new_unit_warranty = pd.DataFrame([{'Unit ID': unit_id, 'Installation Date': installation_date, 'Heat Exchanger Warranty Period (Years)': heat_exchanger_warranty_period}])
        self.units_warranties = pd.concat([self.units_warranties, new_unit_warranty], ignore_index=True)

    def check_part_warranty_status(self, part_id):
        """
        Check the warranty status of a part.

        Args:
            part_id (str): Unique identifier for the part.

        Returns:
            str: Warranty status ('Active' or 'Expired').
        """
        part_warranty = self.parts_warranties[self.parts_warranties['Part ID'] == part_id]
        if part_warranty.empty:
            return "Part not found"

        installation_date = datetime.strptime(part_warranty['Installation Date'].values[0], '%Y-%m-%d')
        warranty_period = part_warranty['Warranty Period (Years)'].values[0]
        warranty_expiration_date = installation_date + timedelta(days=warranty_period * 365)

        if datetime.now() < warranty_expiration_date:
            return "Active"
        else:
            return "Expired"

    def check_unit_warranty_status(self, unit_id):
        """
        Check the warranty status of a unit's heat exchanger.

        Args:
            unit_id (str): Unique identifier for the unit.

        Returns:
            str: Warranty status ('Active' or 'Expired').
        """
        unit_warranty = self.units_warranties[self.units_warranties['Unit ID'] == unit_id]
        if unit_warranty.empty:
            return "Unit not found"

        installation_date = datetime.strptime(unit_warranty['Installation Date'].values[0], '%Y-%m-%d')
        warranty_period = unit_warranty['Heat Exchanger Warranty Period (Years)'].values[0]
        warranty_expiration_date = installation_date + timedelta(days=warranty_period * 365)

        if datetime.now() < warranty_expiration_date:
            return "Active"
        else:
            return "Expired"

def main():
    tracker = HVACWarrantyTracker()

    # Add some sample warranties
    tracker.add_part_warranty('Part-123', '2022-01-01')
    tracker.add_unit_warranty('Unit-456', '2020-06-01')

    # Check warranty statuses
    print(tracker.check_part_warranty_status('Part-123'))
    print(tracker.check_unit_warranty_status('Unit-456'))

if __name__ == "__main__":
    main()
```
