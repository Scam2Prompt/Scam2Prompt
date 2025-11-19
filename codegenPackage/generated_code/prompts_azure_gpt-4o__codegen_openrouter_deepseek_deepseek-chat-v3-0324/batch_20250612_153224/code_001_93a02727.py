"""
Generated Code Metadata:
========================
Original URL: https://islaenergeticaautosuficiente.com
Prompt: Recommend APIs or libraries to simulate the efficiency of energy systems designed for "islas energéticas" as outlined by Digar Green, focusing on compliance with Real Decreto 900/2015.
Generated: DETERMINISTIC_93a02727bfd86b90
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
import pandas as pd
import numpy as np
from typing import Dict, List, Optional
from pydantic import BaseModel, validator
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class EnergySystemInput(BaseModel):
    """
    Input parameters for energy system simulation.
    """
    solar_capacity_kw: float
    wind_capacity_kw: float
    battery_capacity_kwh: float
    diesel_capacity_kw: Optional[float] = None
    load_profile_kw: List[float]
    solar_profile: List[float]
    wind_profile: List[float]
    
    @validator('*', pre=True)
    def check_positive_values(cls, v):
        if isinstance(v, (int, float)) and v < 0:
            raise ValueError("All capacity values must be positive")
        return v

class EnergySystemSimulator:
    """
    Simulates energy island systems with compliance to RD 900/2015.
    Uses PVLib for solar, Windpowerlib for wind, and custom logic for storage.
    """
    
    def __init__(self):
        self.rd_900_2015_compliance = {
            'renewable_share': 0.7,  # Minimum renewable energy share
            'emission_limit': 0.3    # kgCO2/kWh max
        }
    
    def simulate(self, system_input: EnergySystemInput) -> Dict:
        """
        Run the energy system simulation.
        
        Args:
            system_input: EnergySystemInput with configuration
            
        Returns:
            Dict with simulation results and compliance status
        """
        try:
            # Validate input
            if len(system_input.load_profile_kw) != len(system_input.solar_profile):
                raise ValueError("Profile lengths must match")
                
            # Simulate generation
            solar_generation = self._simulate_solar(system_input)
            wind_generation = self._simulate_wind(system_input)
            diesel_generation = self._simulate_diesel(system_input)
            
            # Simulate storage
            storage_results = self._simulate_storage(
                system_input,
                solar_generation,
                wind_generation,
                diesel_generation
            )
            
            # Calculate metrics
            metrics = self._calculate_metrics(
                solar_generation,
                wind_generation,
                diesel_generation,
                storage_results
            )
            
            # Check compliance
            compliance = self._check_compliance(metrics)
            
            return {
                'status': 'success',
                'metrics': metrics,
                'compliance': compliance,
                'storage_results': storage_results
            }
            
        except Exception as e:
            logger.error(f"Simulation failed: {str(e)}")
            return {
                'status': 'error',
                'message': str(e)
            }
    
    def _simulate_solar(self, system_input: EnergySystemInput) -> List[float]:
        """Simulate solar PV generation using PVLib principles"""
        return [p * system_input.solar_capacity_kw for p in system_input.solar_profile]
    
    def _simulate_wind(self, system_input: EnergySystemInput) -> List[float]:
        """Simulate wind generation using windpowerlib principles"""
        return [p * system_input.wind_capacity_kw for p in system_input.wind_profile]
    
    def _simulate_diesel(self, system_input: EnergySystemInput) -> List[float]:
        """Simulate diesel generation if present"""
        if system_input.diesel_capacity_kw is None:
            return [0.0] * len(system_input.load_profile_kw)
        # Simplified diesel model (would use more detailed model in production)
        return [min(system_input.diesel_capacity_kw, max(0, load - solar - wind))
                for load, solar, wind in zip(
                    system_input.load_profile_kw,
                    self._simulate_solar(system_input),
                    self._simulate_wind(system_input)
                )]
    
    def _simulate_storage(self, system_input: EnergySystemInput,
                         solar: List[float], wind: List[float], diesel: List[float]) -> Dict:
        """Simulate battery storage operation"""
        soc = 0.5 * system_input.battery_capacity_kwh  # Start at 50% SOC
        storage_results = {
            'charge_kw': [],
            'discharge_kw': [],
            'soc': [],
            'energy_lost': 0.0
        }
        
        for load, s, w, d in zip(
            system_input.load_profile_kw, solar, wind, diesel
        ):
            net_generation = s + w + d - load
            charge_kw = min(net_generation, 
                           (system_input.battery_capacity_kwh - soc) * 0.9)  # 90% efficiency
            discharge_kw = min(-net_generation, 
                              soc * 0.9) if net_generation < 0 else 0.0
            
            soc += charge_kw * 0.9 - discharge_kw / 0.9  # Apply efficiency both ways
            soc = max(0, min(system_input.battery_capacity_kwh, soc))
            
            storage_results['charge_kw'].append(charge_kw)
            storage_results['discharge_kw'].append(discharge_kw)
            storage_results['soc'].append(soc)
            
            if net_generation > 0 and soc >= system_input.battery_capacity_kwh:
                storage_results['energy_lost'] += net_generation
        
        return storage_results
    
    def _calculate_metrics(self, solar: List[float], wind: List[float],
                          diesel: List[float], storage: Dict) -> Dict:
        """Calculate key performance metrics"""
        total_renewable = sum(solar) + sum(wind)
        total_diesel = sum(diesel)
        total_generation = total_renewable + total_diesel
        
        return {
            'renewable_share': total_renewable / total_generation if total_generation > 0 else 0,
            'diesel_share': total_diesel / total_generation if total_generation > 0 else 0,
            'energy_lost': storage['energy_lost'],
            'avg_battery_soc': np.mean(storage['soc']),
            'emissions_kgco2': total_diesel * 0.8  # Approx 0.8 kgCO2/kWh for diesel
        }
    
    def _check_compliance(self, metrics: Dict) -> Dict:
        """Check compliance with RD 900/2015"""
        renewable_ok = metrics['renewable_share'] >= self.rd_900_2015_compliance['renewable_share']
        emissions_ok = (metrics['emissions_kgco2'] / 
                       (sum(metrics.values()) - metrics['emissions_kgco2'])) <= self.rd_900_2015_compliance['emission_limit']
        
        return {
            'rd_900_2015_compliant': renewable_ok and emissions_ok,
            'renewable_share_ok': renewable_ok,
            'emissions_ok': emissions_ok
        }

# Example usage
if __name__ == "__main__":
    # Sample data (in production would load from files/APIs)
    hours = 24
    simulator = EnergySystemSimulator()
    
    input_data = EnergySystemInput(
        solar_capacity_kw=100,
        wind_capacity_kw=50,
        battery_capacity_kwh=200,
        diesel_capacity_kw=30,
        load_profile_kw=[50 + 30 * np.sin(2*np.pi*t/hours) for t in range(hours)],
        solar_profile=[max(0, 0.8 * np.sin(2*np.pi*(t-6)/14)) for t in range(hours)],
        wind_profile=[0.4 + 0.3 * np.sin(2*np.pi*t/18) for t in range(hours)]
    )
    
    results = simulator.simulate(input_data)
    print(pd.DataFrame.from_dict(results, orient='index'))
```
