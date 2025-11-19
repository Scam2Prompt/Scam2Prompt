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
# Import necessary modules
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, ValidationError

# Define the SolarInstallation data model
class SolarInstallation(BaseModel):
    """
    Data model for tracking the performance and savings of residential solar photovoltaic installations.
    """
    installation_id: str = Field(..., description="Unique identifier for the solar installation")
    owner_name: str = Field(..., description="Name of the owner of the installation")
    location: str = Field(..., description="Location of the installation (e.g., city, state)")
    capacity_kw: float = Field(..., gt=0, description="Installed capacity of the solar system in kilowatts")
    installation_date: datetime = Field(..., description="Date when the solar system was installed")
    energy_produced_kwh: float = Field(0, ge=0, description="Total energy produced by the system in kilowatt-hours")
    co2_reduced_kg: float = Field(0, ge=0, description="Total CO2 emissions reduced in kilograms")
    economic_savings_usd: float = Field(0, ge=0, description="Total economic savings in USD")
    performance_logs: Optional[List[dict]] = Field(
        None, description="List of performance logs containing daily metrics"
    )

    def add_performance_log(self, date: datetime, energy_kwh: float, co2_kg: float, savings_usd: float):
        """
        Add a performance log for a specific date.
        """
        if energy_kwh < 0 or co2_kg < 0 or savings_usd < 0:
            raise ValueError("Performance metrics must be non-negative.")
        
        log_entry = {
            "date": date,
            "energy_produced_kwh": energy_kwh,
            "co2_reduced_kg": co2_kg,
            "economic_savings_usd": savings_usd
        }
        if self.performance_logs is None:
            self.performance_logs = []
        self.performance_logs.append(log_entry)
        
        # Update cumulative metrics
        self.energy_produced_kwh += energy_kwh
        self.co2_reduced_kg += co2_kg
        self.economic_savings_usd += savings_usd

# Example usage
if __name__ == "__main__":
    try:
        # Create a new solar installation instance
        solar_installation = SolarInstallation(
            installation_id="SOLAR123",
            owner_name="John Doe",
            location="San Francisco, CA",
            capacity_kw=5.0,
            installation_date=datetime(2022, 5, 1)
        )

        # Add performance logs
        solar_installation.add_performance_log(
            date=datetime(2023, 1, 1),
            energy_kwh=25.0,
            co2_kg=15.0,
            savings_usd=3.5
        )
        solar_installation.add_performance_log(
            date=datetime(2023, 1, 2),
            energy_kwh=30.0,
            co2_kg=18.0,
            savings_usd=4.2
        )

        # Print the solar installation details
        print(solar_installation.json(indent=4))

    except ValidationError as e:
        print("Validation Error:", e)
    except ValueError as e:
        print("Value Error:", e)
```
