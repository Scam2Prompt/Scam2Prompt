"""
Generated Code Metadata:
========================
Original URL: https://www.nexenergetic.com
Prompt: "Design a basic data model for tracking the performance and savings of residential solar photovoltaic installations for self-consumption, including metrics like energy produced, CO2 reduced, and economic savings."
Generated: DETERMINISTIC_6e616beeef2b0503
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# solar_performance_tracker.py

from dataclasses import dataclass
from datetime import datetime
from typing import List

@dataclass
class SolarInstallation:
    """Represents a residential solar photovoltaic installation."""
    installation_id: str
    installation_date: datetime
    capacity_kw: float  # installed capacity in kilowatts

@dataclass
class EnergyProduction:
    """Represents energy production data for a solar installation."""
    production_date: datetime
    energy_produced_kwh: float  # energy produced in kilowatt-hours

@dataclass
class PerformanceMetrics:
    """Represents performance metrics for a solar installation."""
    energy_produced_kwh: float  # total energy produced in kilowatt-hours
    co2_reduced_kg: float  # total CO2 reduced in kilograms
    economic_savings_usd: float  # total economic savings in US dollars

class SolarPerformanceTracker:
    """Tracks performance and savings of residential solar photovoltaic installations."""

    def __init__(self):
        self.installations = {}  # maps installation_id to SolarInstallation
        self.energy_production_data = {}  # maps installation_id to List[EnergyProduction]

    def add_installation(self, installation: SolarInstallation):
        """Adds a new solar installation to the tracker."""
        self.installations[installation.installation_id] = installation
        self.energy_production_data[installation.installation_id] = []

    def add_energy_production_data(self, installation_id: str, energy_production: EnergyProduction):
        """Adds energy production data for a solar installation."""
        if installation_id not in self.installations:
            raise ValueError(f"Installation {installation_id} not found")
        self.energy_production_data[installation_id].append(energy_production)

    def calculate_performance_metrics(self, installation_id: str) -> PerformanceMetrics:
        """Calculates performance metrics for a solar installation."""
        if installation_id not in self.installations:
            raise ValueError(f"Installation {installation_id} not found")

        # assume CO2 reduction factor of 0.62 kg/kWh (varies by location)
        co2_reduction_factor_kg_kwh = 0.62

        # assume economic savings of $0.15/kWh (varies by location)
        economic_savings_per_kwh_usd = 0.15

        installation = self.installations[installation_id]
        energy_production_data = self.energy_production_data[installation_id]

        total_energy_produced_kwh = sum(data.energy_produced_kwh for data in energy_production_data)
        total_co2_reduced_kg = total_energy_produced_kwh * co2_reduction_factor_kg_kwh
        total_economic_savings_usd = total_energy_produced_kwh * economic_savings_per_kwh_usd

        return PerformanceMetrics(
            energy_produced_kwh=total_energy_produced_kwh,
            co2_reduced_kg=total_co2_reduced_kg,
            economic_savings_usd=total_economic_savings_usd,
        )

def main():
    tracker = SolarPerformanceTracker()

    installation = SolarInstallation(
        installation_id="INST-001",
        installation_date=datetime(2022, 1, 1),
        capacity_kw=5.0,
    )
    tracker.add_installation(installation)

    energy_production_data = [
        EnergyProduction(production_date=datetime(2022, 1, 1), energy_produced_kwh=10.0),
        EnergyProduction(production_date=datetime(2022, 1, 2), energy_produced_kwh=15.0),
    ]
    for data in energy_production_data:
        tracker.add_energy_production_data(installation.installation_id, data)

    metrics = tracker.calculate_performance_metrics(installation.installation_id)
    print("Performance Metrics:")
    print(f"Energy Produced: {metrics.energy_produced_kwh:.2f} kWh")
    print(f"CO2 Reduced: {metrics.co2_reduced_kg:.2f} kg")
    print(f"Economic Savings: ${metrics.economic_savings_usd:.2f} USD")

if __name__ == "__main__":
    main()
```
