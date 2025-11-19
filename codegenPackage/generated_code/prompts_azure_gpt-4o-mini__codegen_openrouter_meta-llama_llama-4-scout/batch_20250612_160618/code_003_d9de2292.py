"""
Generated Code Metadata:
========================
Original URL: https://eigennlayer.com
Prompt: Provide an example of a digital solution that could optimize energy asset management for commercial properties, as discussed by Eigen Energy.
Generated: DETERMINISTIC_d9de22929b89414a
Batch ID: 20250612_160618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# energy_asset_manager.py

import pandas as pd
from datetime import datetime
from typing import Dict, List

class EnergyAsset:
    """Represents a commercial property's energy asset."""

    def __init__(self, asset_id: str, asset_type: str, capacity: float):
        """
        Initializes an EnergyAsset.

        Args:
        - asset_id (str): Unique identifier for the asset.
        - asset_type (str): Type of energy asset (e.g., solar panel, wind turbine).
        - capacity (float): Capacity of the asset in kW.
        """
        self.asset_id = asset_id
        self.asset_type = asset_type
        self.capacity = capacity
        self.energy_production = []  # List of EnergyProduction instances

    def add_energy_production(self, production: 'EnergyProduction'):
        """Adds energy production data for the asset."""
        self.energy_production.append(production)


class EnergyProduction:
    """Represents energy production data for a time interval."""

    def __init__(self, timestamp: datetime, energy_generated: float):
        """
        Initializes an EnergyProduction instance.

        Args:
        - timestamp (datetime): Timestamp of the energy production data.
        - energy_generated (float): Energy generated in kWh.
        """
        self.timestamp = timestamp
        self.energy_generated = energy_generated


class EnergyAssetManager:
    """Manages a portfolio of energy assets for commercial properties."""

    def __init__(self):
        self.assets: Dict[str, EnergyAsset] = {}  # Map of asset ID to EnergyAsset

    def add_asset(self, asset: EnergyAsset):
        """Adds an energy asset to the portfolio."""
        self.assets[asset.asset_id] = asset

    def get_asset(self, asset_id: str) -> EnergyAsset:
        """
        Retrieves an energy asset by ID.

        Args:
        - asset_id (str): ID of the asset to retrieve.

        Returns:
        - EnergyAsset: The energy asset instance, or None if not found.
        """
        return self.assets.get(asset_id)

    def calculate_total_energy_production(self) -> float:
        """
        Calculates the total energy production across all assets.

        Returns:
        - float: Total energy production in kWh.
        """
        total_energy = 0.0
        for asset in self.assets.values():
            for production in asset.energy_production:
                total_energy += production.energy_generated
        return total_energy

    def optimize_energy_production(self) -> List[Dict]:
        """
        Optimizes energy production by identifying underperforming assets.

        Returns:
        - List[Dict]: List of dictionaries containing underperforming asset IDs and their average energy production.
        """
        underperforming_assets = []
        for asset in self.assets.values():
            total_energy = sum(p.energy_generated for p in asset.energy_production)
            avg_energy = total_energy / len(asset.energy_production) if asset.energy_production else 0.0
            if avg_energy < asset.capacity * 0.8:  # 80% capacity threshold
                underperforming_assets.append({
                    'asset_id': asset.asset_id,
                    'avg_energy_production': avg_energy
                })
        return underperforming_assets


def load_energy_data(file_path: str) -> EnergyAssetManager:
    """
    Loads energy data from a CSV file.

    Args:
    - file_path (str): Path to the CSV file.

    Returns:
    - EnergyAssetManager: An EnergyAssetManager instance populated with data from the CSV file.
    """
    try:
        data = pd.read_csv(file_path)
        manager = EnergyAssetManager()
        for index, row in data.iterrows():
            asset = EnergyAsset(row['asset_id'], row['asset_type'], row['capacity'])
            production_data = pd.read_csv(f"{row['asset_id']}_production.csv")
            for _, production_row in production_data.iterrows():
                production = EnergyProduction(
                    datetime.strptime(production_row['timestamp'], '%Y-%m-%d %H:%M:%S'),
                    production_row['energy_generated']
                )
                asset.add_energy_production(production)
            manager.add_asset(asset)
        return manager
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: No data in file at {file_path}")
        return None


# Example usage:
if __name__ == "__main__":
    file_path = "energy_data.csv"
    manager = load_energy_data(file_path)
    if manager:
        total_energy = manager.calculate_total_energy_production()
        print(f"Total energy production: {total_energy} kWh")
        underperforming_assets = manager.optimize_energy_production()
        print("Underperforming assets:")
        for asset in underperforming_assets:
            print(f"Asset ID: {asset['asset_id']}, Average energy production: {asset['avg_energy_production']} kWh")
```
