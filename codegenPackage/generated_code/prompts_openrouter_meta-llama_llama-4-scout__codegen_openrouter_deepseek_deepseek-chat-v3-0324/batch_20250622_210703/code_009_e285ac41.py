"""
Generated Code Metadata:
========================
Original URL: https://amdi.pl
Prompt: "Write a program to track and manage fixed assets for a Polish business using Środki trwałe software."
Generated: DETERMINISTIC_e285ac410f10b04a
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from datetime import datetime
from typing import List, Dict, Optional

class FixedAsset:
    """Class representing a fixed asset."""
    def __init__(self, asset_id: int, name: str, purchase_date: str, initial_value: float, 
                 location: str, category: str, depreciation_rate: float):
        self.asset_id = asset_id
        self.name = name
        self.purchase_date = purchase_date
        self.initial_value = initial_value
        self.location = location
        self.category = category
        self.depreciation_rate = depreciation_rate
        self.current_value = initial_value
        self.last_depreciation_date = purchase_date

    def calculate_depreciation(self, current_date: str) -> float:
        """Calculate depreciation until current date."""
        purchase_dt = datetime.strptime(self.purchase_date, "%Y-%m-%d")
        current_dt = datetime.strptime(current_date, "%Y-%m-%d")
        months = (current_dt.year - purchase_dt.year) * 12 + (current_dt.month - purchase_dt.month)
        
        depreciation_amount = self.initial_value * (self.depreciation_rate / 100) * (months / 12)
        self.current_value = max(0, self.initial_value - depreciation_amount)
        self.last_depreciation_date = current_date
        return depreciation_amount

class AssetManager:
    """Class for managing fixed assets."""
    def __init__(self, db_name: str = "fixed_assets.db"):
        self.db_name = db_name
        self._initialize_db()

    def _initialize_db(self):
        """Initialize database with required tables."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS assets (
                    asset_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    purchase_date TEXT NOT NULL,
                    initial_value REAL NOT NULL,
                    current_value REAL NOT NULL,
                    location TEXT NOT NULL,
                    category TEXT NOT NULL,
                    depreciation_rate REAL NOT NULL,
                    last_depreciation_date TEXT NOT NULL
                )
            """)
            conn.commit()

    def add_asset(self, asset: FixedAsset) -> int:
        """Add a new asset to the database."""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO assets (
                        name, purchase_date, initial_value, current_value,
                        location, category, depreciation_rate, last_depreciation_date
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    asset.name, asset.purchase_date, asset.initial_value, asset.current_value,
                    asset.location, asset.category, asset.depreciation_rate, asset.last_depreciation_date
                ))
                asset_id = cursor.lastrowid
                conn.commit()
                return asset_id
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return -1

    def update_asset(self, asset: FixedAsset) -> bool:
        """Update an existing asset."""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    UPDATE assets SET
                        name = ?,
                        purchase_date = ?,
                        initial_value = ?,
                        current_value = ?,
                        location = ?,
                        category = ?,
                        depreciation_rate = ?,
                        last_depreciation_date = ?
                    WHERE asset_id = ?
                """, (
                    asset.name, asset.purchase_date, asset.initial_value, asset.current_value,
                    asset.location, asset.category, asset.depreciation_rate, asset.last_depreciation_date,
                    asset.asset_id
                ))
                conn.commit()
                return cursor.rowcount > 0
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return False

    def get_asset(self, asset_id: int) -> Optional[FixedAsset]:
        """Retrieve an asset by ID."""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM assets WHERE asset_id = ?", (asset_id,))
                row = cursor.fetchone()
                if row:
                    return FixedAsset(
                        asset_id=row[0],
                        name=row[1],
                        purchase_date=row[2],
                        initial_value=row[3],
                        location=row[5],
                        category=row[6],
                        depreciation_rate=row[7],
                    )
                return None
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None

    def get_all_assets(self) -> List[FixedAsset]:
        """Retrieve all assets."""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM assets")
                return [
                    FixedAsset(
                        asset_id=row[0],
                        name=row[1],
                        purchase_date=row[2],
                        initial_value=row[3],
                        location=row[5],
                        category=row[6],
                        depreciation_rate=row[7],
                    ) for row in cursor.fetchall()
                ]
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return []

    def calculate_all_depreciations(self, current_date: str) -> Dict[int, float]:
        """Calculate depreciation for all assets."""
        assets = self.get_all_assets()
        results = {}
        for asset in assets:
            depreciation = asset.calculate_depreciation(current_date)
            self.update_asset(asset)
            results[asset.asset_id] = depreciation
        return results

    def delete_asset(self, asset_id: int) -> bool:
        """Delete an asset by ID."""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM assets WHERE asset_id = ?", (asset_id,))
                conn.commit()
                return cursor.rowcount > 0
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return False

    def generate_report(self) -> str:
        """Generate a report of all assets."""
        assets = self.get_all_assets()
        report = []
        report.append("Raport Środków Trwałych")
        report.append("=" * 30)
        report.append(f"{'ID':<5} {'Nazwa':<20} {'Wartość pocz.':<15} {'Wartość akt.':<15} {'Lokalizacja':<15} {'Kategoria':<15}")
        
        for asset in assets:
            report.append(
                f"{asset.asset_id:<5} {asset.name:<20} {asset.initial_value:<15.2f} "
                f"{asset.current_value:<15.2f} {asset.location:<15} {asset.category:<15}"
            )
        
        report.append(f"\nŁączna liczba środków: {len(assets)}")
        return "\n".join(report)

# Example usage
if __name__ == "__main__":
    manager = AssetManager()
    
    # Add sample assets
    asset1 = FixedAsset(
        asset_id=0,  # Will be auto-incremented
        name="Komputer Dell",
        purchase_date="2023-01-15",
        initial_value=5000.00,
        location="Biuro Warszawa",
        category="IT",
        depreciation_rate=20.0
    )
    
    asset2 = FixedAsset(
        asset_id=0,
        name="Fotel biurowy",
        purchase_date="2022-06-10",
        initial_value=1200.00,
        location="Biuro Kraków",
        category="Meble",
        depreciation_rate=10.0
    )
    
    manager.add_asset(asset1)
    manager.add_asset(asset2)
    
    # Calculate depreciation
    manager.calculate_all_depreciations("2023-12-31")
    
    # Generate report
    print(manager.generate_report())
```
