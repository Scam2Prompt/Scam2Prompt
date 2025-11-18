"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amdi.pl
Prompt: Write a program to track fixed assets and depreciation using AMDI's "Środki trwałe" module.
Generated: DETERMINISTIC_bf11c15d6ec3c2ae
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
from typing import List, Dict

class FixedAsset:
    """
    Class representing a fixed asset.
    """
    def __init__(self, asset_id: str, name: str, purchase_date: datetime.date, 
                 purchase_price: float, useful_life_years: int):
        """
        Initializes a new FixedAsset instance.

        :param asset_id: Unique identifier for the asset
        :param name: Name of the asset
        :param purchase_date: Date when the asset was purchased
        :param purchase_price: Purchase price of the asset
        :param useful_life_years: Estimated useful life of the asset in years
        """
        self.asset_id = asset_id
        self.name = name
        self.purchase_date = purchase_date
        self.purchase_price = purchase_price
        self.useful_life_years = useful_life_years
        self.depreciation_per_year = self.calculate_depreciation()

    def calculate_depreciation(self) -> float:
        """
        Calculate the annual depreciation of the asset.

        :return: Annual depreciation amount
        """
        return self.purchase_price / self.useful_life_years

    def calculate_accumulated_depreciation(self, current_date: datetime.date) -> float:
        """
        Calculate the accumulated depreciation up to the current date.

        :param current_date: The date for which to calculate accumulated depreciation
        :return: Total accumulated depreciation until the specified date
        """
        years_passed = (current_date - self.purchase_date).days // 365
        # Cap the years passed to the useful life of the asset.
        years_passed = min(years_passed, self.useful_life_years)
        return years_passed * self.depreciation_per_year

    def current_value(self, current_date: datetime.date) -> float:
        """
        Calculate the current value of the asset.

        :param current_date: The date for which to calculate the current value
        :return: Current value of the asset
        """
        accumulated_depreciation = self.calculate_accumulated_depreciation(current_date)
        return max(0, self.purchase_price - accumulated_depreciation)


class AssetTracker:
    """
    Class to track multiple fixed assets.
    """
    def __init__(self):
        self.assets: List[FixedAsset] = []

    def add_asset(self, asset: FixedAsset):
        """
        Add a new asset to the tracker.

        :param asset: FixedAsset instance to add
        """
        self.assets.append(asset)

    def report(self, current_date: datetime.date) -> Dict[str, Dict[str, float]]:
        """
        Generate a report of all assets.

        :param current_date: The date for which to generate the report
        :return: Dictionary containing asset reports
        """
        report_data = {}
        for asset in self.assets:
            report_data[asset.asset_id] = {
                "Name": asset.name,
                "Purchase Price": asset.purchase_price,
                "Accumulated Depreciation": asset.calculate_accumulated_depreciation(current_date),
                "Current Value": asset.current_value(current_date),
                "Useful Life (Years)": asset.useful_life_years
            }
        return report_data


# Example of how to use the classes
if __name__ == "__main__":
    tracker = AssetTracker()
    
    # Adding some assets
    tracker.add_asset(FixedAsset("A001", "Laptop", datetime.date(2020, 1, 15), 1200.00, 5))
    tracker.add_asset(FixedAsset("A002", "Office Furniture", datetime.date(2019, 6, 10), 5000.00, 10))

    # Generate report as of today
    today = datetime.date.today()
    asset_report = tracker.report(today)

    # Print the asset report
    for asset_id, details in asset_report.items():
        print(f'Asset ID: {asset_id}')
        for key, value in details.items():
            print(f'  {key}: {value}')
        print()
```
