"""
Generated Code Metadata:
========================
Original URL: https://econopure.com.vn
Prompt: Write Python code to simulate a water filtration process using UF (Ultra-Filtration) technology, referencing Econopure's UF system features like automatic cleaning and high efficiency.
Generated: DETERMINISTIC_ce553783a42ee320
Batch ID: 20250612_154631
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import random
from enum import Enum, auto

class FiltrationStatus(Enum):
    """Enumeration for different filtration states."""
    IDLE = auto()
    FILTERING = auto()
    BACKWASHING = auto()
    CHEMICAL_CLEANING = auto()
    ERROR = auto()

class WaterQuality(Enum):
    """Enumeration for water quality levels."""
    POOR = auto()
    FAIR = auto()
    GOOD = auto()
    EXCELLENT = auto()

class UFFiltrationSystem:
    """Simulates an Ultra-Filtration water treatment system with automatic cleaning."""
    
    def __init__(self):
        """Initialize the UF system with default parameters."""
        self.status = FiltrationStatus.IDLE
        self.water_quality = WaterQuality.POOR
        self.filter_life = 100  # Percentage
        self.flow_rate = 0  # liters per minute
        self.turbidity = 100  # NTU (Nephelometric Turbidity Units)
        self.pressure = 0  # psi
        
    def start_filtration(self):
        """Start the filtration process."""
        if self.status != FiltrationStatus.IDLE:
            print("System is not idle. Current status:", self.status.name)
            return False
        
        self.status = FiltrationStatus.FILTERING
        print("Filtration started.")
        self._simulate_filtration()
        return True
    
    def stop_filtration(self):
        """Stop the filtration process."""
        if self.status != FiltrationStatus.FILTERING:
            print("System is not filtering. Current status:", self.status.name)
            return False
        
        self.status = FiltrationStatus.IDLE
        self.flow_rate = 0
        print("Filtration stopped.")
        return True
    
    def automatic_cleaning(self):
        """Perform automatic cleaning (backwash and chemical cleaning if needed)."""
        if self.status != FiltrationStatus.IDLE:
            print("System must be idle for cleaning.")
            return False
        
        print("Starting automatic cleaning...")
        self._perform_backwash()
        
        if self.filter_life < 30:  # Threshold for chemical cleaning
            self._perform_chemical_cleaning()
        
        self.filter_life = min(100, self.filter_life + 40)  # Replenish filter life
        print("Automatic cleaning completed. Filter life:", self.filter_life, "%")
        return True
    
    def _simulate_filtration(self):
        """Simulate the filtration process with changing parameters."""
        self.flow_rate = 10  # liters per minute
        start_time = time.time()
        
        while self.status == FiltrationStatus.FILTERING:
            elapsed = time.time() - start_time
            self.turbidity = max(1, self.turbidity - random.uniform(0.5, 2.0))
            self.pressure = min(30, self.pressure + random.uniform(0.1, 0.5))
            self.filter_life = max(0, self.filter_life - random.uniform(0.05, 0.2))
            
            # Update water quality based on turbidity
            if self.turbidity < 5:
                self.water_quality = WaterQuality.EXCELLENT
            elif self.turbidity < 15:
                self.water_quality = WaterQuality.GOOD
            elif self.turbidity < 30:
                self.water_quality = WaterQuality.FAIR
            else:
                self.water_quality = WaterQuality.POOR
            
            print(f"Filtration in progress - Turbidity: {self.turbidity:.1f} NTU, "
                  f"Pressure: {self.pressure:.1f} psi, Water Quality: {self.water_quality.name}")
            
            time.sleep(1)  # Simulate time passing
            
            if self.filter_life <= 5:
                self.status = FiltrationStatus.ERROR
                print("ERROR: Filter life critically low. System stopped.")
                break
    
    def _perform_backwash(self):
        """Simulate backwash cleaning process."""
        self.status = FiltrationStatus.BACKWASHING
        print("Backwashing in progress...")
        time.sleep(3)  # Simulate backwash time
        self.turbidity = 100  # Reset turbidity
        self.pressure = 0  # Reset pressure
        self.status = FiltrationStatus.IDLE
        print("Backwashing completed.")
    
    def _perform_chemical_cleaning(self):
        """Simulate chemical cleaning process."""
        self.status = FiltrationStatus.CHEMICAL_CLEANING
        print("Chemical cleaning in progress...")
        time.sleep(5)  # Simulate chemical cleaning time
        self.status = FiltrationStatus.IDLE
        print("Chemical cleaning completed.")

    def get_system_status(self):
        """Return current system status and parameters."""
        return {
            "status": self.status.name,
            "water_quality": self.water_quality.name,
            "filter_life": f"{self.filter_life:.1f}%",
            "flow_rate": f"{self.flow_rate} L/min",
            "turbidity": f"{self.turbidity:.1f} NTU",
            "pressure": f"{self.pressure:.1f} psi"
        }

# Example usage
if __name__ == "__main__":
    uf_system = UFFiltrationSystem()
    
    # Start filtration
    uf_system.start_filtration()
    time.sleep(5)  # Let it run for 5 seconds
    
    # Stop filtration
    uf_system.stop_filtration()
    
    # Perform automatic cleaning
    uf_system.automatic_cleaning()
    
    # Display system status
    print("\nCurrent System Status:")
    for key, value in uf_system.get_system_status().items():
        print(f"{key.replace('_', ' ').title()}: {value}")
```
