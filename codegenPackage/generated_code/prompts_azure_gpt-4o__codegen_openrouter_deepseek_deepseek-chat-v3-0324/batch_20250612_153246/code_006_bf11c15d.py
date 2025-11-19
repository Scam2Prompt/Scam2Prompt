"""
Generated Code Metadata:
========================
Original URL: https://amdi.pl
Prompt: Write a program to track fixed assets and depreciation using AMDI's "Środki trwałe" module.
Generated: DETERMINISTIC_bf11c15d6ec3c2ae
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from dataclasses import dataclass
from typing import List, Optional
from enum import Enum, auto
import csv
import json
import os

class AssetCategory(Enum):
    """Enum representing different categories of fixed assets."""
    BUILDINGS = auto()
    MACHINERY = auto()
    VEHICLES = auto()
    EQUIPMENT = auto()
    FURNITURE = auto()
    SOFTWARE = auto()

@dataclass
class DepreciationMethod:
    """Dataclass representing a depreciation method."""
    name: str
    rate: float
    description: str

@dataclass
class FixedAsset:
    """Dataclass representing a fixed asset."""
    id: str
    name: str
    category: AssetCategory
    acquisition_date: datetime.date
    acquisition_cost: float
    residual_value: float
    useful_life_years: int
    depreciation_method: DepreciationMethod
    current_book_value: float = 0.0
    is_active: bool = True

    def __post_init__(self):
        """Initialize current book value to acquisition cost."""
        self.current_book_value = self.acquisition_cost

class AssetManager:
    """Class to manage fixed assets and their depreciation."""
    
    def __init__(self):
        """Initialize the asset manager with empty assets list."""
        self.assets: List[FixedAsset] = []
        self.depreciation_methods = [
            DepreciationMethod("Straight-line", 1.0, "Equal depreciation each year"),
            DepreciationMethod("Double-declining", 2.0, "Double the straight-line rate"),
            DepreciationMethod("Units of Production", 0.0, "Based on usage")
        ]
    
    def add_asset(self, asset: FixedAsset) -> None:
        """Add a new fixed asset to the manager."""
        if not isinstance(asset, FixedAsset):
            raise ValueError("Only FixedAsset objects can be added")
        self.assets.append(asset)
    
    def remove_asset(self, asset_id: str) -> bool:
        """Remove an asset by its ID."""
        for i, asset in enumerate(self.assets):
            if asset.id == asset_id:
                self.assets.pop(i)
                return True
        return False
    
    def calculate_depreciation(self, asset_id: str, as_of_date: datetime.date) -> Optional[float]:
        """Calculate depreciation for an asset up to a given date."""
        asset = self._find_asset(asset_id)
        if not asset or not asset.is_active:
            return None
        
        days_owned = (as_of_date - asset.acquisition_date).days
        if days_owned <= 0:
            return 0.0
        
        years_owned = days_owned / 365.25
        useful_life = asset.useful_life_years
        
        if asset.depreciation_method.name == "Straight-line":
            annual_depreciation = (asset.acquisition_cost - asset.residual_value) / useful_life
            total_depreciation = min(annual_depreciation * years_owned, 
                                   asset.acquisition_cost - asset.residual_value)
        
        elif asset.depreciation_method.name == "Double-declining":
            rate = (2.0 / useful_life)
            book_value = asset.acquisition_cost
            total_depreciation = 0.0
            
            for _ in range(int(years_owned)):
                dep = book_value * rate
                remaining_value = asset.acquisition_cost - total_depreciation - dep
                if remaining_value < asset.residual_value:
                    dep = asset.acquisition_cost - total_depreciation - asset.residual_value
                total_depreciation += dep
                book_value -= dep
                if book_value <= asset.residual_value:
                    break
        
        else:
            raise ValueError("Unsupported depreciation method")
        
        return total_depreciation
    
    def update_book_values(self, as_of_date: datetime.date) -> None:
        """Update book values for all assets based on depreciation."""
        for asset in self.assets:
            if asset.is_active:
                depreciation = self.calculate_depreciation(asset.id, as_of_date)
                if depreciation is not None:
                    asset.current_book_value = asset.acquisition_cost - depreciation
    
    def _find_asset(self, asset_id: str) -> Optional[FixedAsset]:
        """Find an asset by its ID."""
        for asset in self.assets:
            if asset.id == asset_id:
                return asset
        return None
    
    def export_to_csv(self, filename: str) -> None:
        """Export assets to a CSV file."""
        if not filename.endswith('.csv'):
            filename += '.csv'
        
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = [
                'id', 'name', 'category', 'acquisition_date', 
                'acquisition_cost', 'residual_value', 'useful_life_years',
                'depreciation_method', 'current_book_value', 'is_active'
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
            for asset in self.assets:
                writer.writerow({
                    'id': asset.id,
                    'name': asset.name,
                    'category': asset.category.name,
                    'acquisition_date': asset.acquisition_date.isoformat(),
                    'acquisition_cost': asset.acquisition_cost,
                    'residual_value': asset.residual_value,
                    'useful_life_years': asset.useful_life_years,
                    'depreciation_method': asset.depreciation_method.name,
                    'current_book_value': asset.current_book_value,
                    'is_active': asset.is_active
                })
    
    def import_from_csv(self, filename: str) -> None:
        """Import assets from a CSV file."""
        if not os.path.exists(filename):
            raise FileNotFoundError(f"File {filename} not found")
        
        with open(filename, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    category = AssetCategory[row['category']]
                    method_name = row['depreciation_method']
                    method = next(m for m in self.depreciation_methods if m.name == method_name)
                    
                    asset = FixedAsset(
                        id=row['id'],
                        name=row['name'],
                        category=category,
                        acquisition_date=datetime.date.fromisoformat(row['acquisition_date']),
                        acquisition_cost=float(row['acquisition_cost']),
                        residual_value=float(row['residual_value']),
                        useful_life_years=int(row['useful_life_years']),
                        depreciation_method=method,
                        current_book_value=float(row['current_book_value']),
                        is_active=row['is_active'].lower() == 'true'
                    )
                    self.assets.append(asset)
                except (KeyError, ValueError, StopIteration) as e:
                    print(f"Skipping invalid asset data: {e}")
    
    def generate_depreciation_report(self, as_of_date: datetime.date) -> str:
        """Generate a JSON report of depreciation calculations."""
        report = {
            "report_date": as_of_date.isoformat(),
            "assets": []
        }
        
        for asset in self.assets:
            depreciation = self.calculate_depreciation(asset.id, as_of_date)
            report["assets"].append({
                "id": asset.id,
                "name": asset.name,
                "category": asset.category.name,
                "acquisition_date": asset.acquisition_date.isoformat(),
                "acquisition_cost": asset.acquisition_cost,
                "current_book_value": asset.current_book_value,
                "accumulated_depreciation": asset.acquisition_cost - asset.current_book_value,
                "depreciation_method": asset.depreciation_method.name,
                "is_active": asset.is_active
            })
        
        return json.dumps(report, indent=2)

# Example usage
if __name__ == "__main__":
    manager = AssetManager()
    
    # Create some depreciation methods
    straight_line = DepreciationMethod("Straight-line", 1.0, "Equal depreciation each year")
    double_declining = DepreciationMethod("Double-declining", 2.0, "Double the straight-line rate")
    
    # Add some assets
    today = datetime.date.today()
    asset1 = FixedAsset(
        id="AST001",
        name="Company Vehicle",
        category=AssetCategory.VEHICLES,
        acquisition_date=today.replace(year=today.year - 2),
        acquisition_cost=50000.0,
        residual_value=5000.0,
        useful_life_years=5,
        depreciation_method=straight_line
    )
    
    asset2 = FixedAsset(
        id="AST002",
        name="Office Printer",
        category=AssetCategory.EQUIPMENT,
        acquisition_date=today.replace(year=today.year - 1),
        acquisition_cost=2000.0,
        residual_value=200.0,
        useful_life_years=3,
        depreciation_method=double_declining
    )
    
    manager.add_asset(asset1)
    manager.add_asset(asset2)
    
    # Update book values
    manager.update_book_values(today)
    
    # Export to
