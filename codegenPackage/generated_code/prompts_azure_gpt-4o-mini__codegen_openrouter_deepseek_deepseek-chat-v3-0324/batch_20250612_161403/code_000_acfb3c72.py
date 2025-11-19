"""
Generated Code Metadata:
========================
Original URL: https://www.limpiezadetuboscostablanca.net
Prompt: Write a Python function that utilizes a library to detect water leaks in residential plumbing systems, similar to the advanced detection systems described on Limpieza de Tubos Costablanca.
Generated: DETERMINISTIC_acfb3c72fd00a0ec
Batch ID: 20250612_161403
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
from typing import Dict, Optional, Tuple
import logging
from dataclasses import dataclass

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class SensorReading:
    """Dataclass to hold sensor readings."""
    pressure: float
    flow_rate: float
    temperature: float
    timestamp: float

class LeakDetector:
    """
    A class to simulate water leak detection in residential plumbing systems.
    Uses pressure and flow rate analysis to detect potential leaks.
    """
    
    def __init__(self, threshold_pressure_drop: float = 0.15, 
                 threshold_flow_rate: float = 0.1):
        """
        Initialize the leak detector with configurable thresholds.
        
        Args:
            threshold_pressure_drop: Percentage pressure drop considered abnormal
            threshold_flow_rate: Minimum flow rate (in GPM) when no fixtures are in use
        """
        self.threshold_pressure_drop = threshold_pressure_drop
        self.threshold_flow_rate = threshold_flow_rate
        self.baseline_pressure = None
        self.last_reading = None
        
    def _simulate_sensor_reading(self) -> SensorReading:
        """Simulate sensor readings (in a real system, this would interface with actual sensors)."""
        # Simulate normal pressure between 40-80 PSI
        pressure = random.uniform(40.0, 80.0)
        
        # Simulate occasional pressure drops (potential leaks)
        if random.random() < 0.05:  # 5% chance of simulated leak
            pressure *= (1 - random.uniform(0.2, 0.5))
            
        # Simulate flow rate (0 when no fixtures in use, up to 5 GPM when in use)
        flow_rate = 0.0 if random.random() < 0.7 else random.uniform(0.5, 5.0)
        
        # Simulate temperature between 50-70°F (typical for residential water)
        temperature = random.uniform(50.0, 70.0)
        
        return SensorReading(
            pressure=pressure,
            flow_rate=flow_rate,
            temperature=temperature,
            timestamp=time.time()
        )
    
    def _analyze_reading(self, reading: SensorReading) -> Tuple[bool, Optional[str]]:
        """
        Analyze sensor readings for potential leaks.
        
        Returns:
            Tuple of (leak_detected, reason)
        """
        # Check if we have enough data
        if self.baseline_pressure is None:
            self.baseline_pressure = reading.pressure
            return False, None
            
        # Check for abnormal pressure drop
        pressure_drop = (self.baseline_pressure - reading.pressure) / self.baseline_pressure
        if pressure_drop > self.threshold_pressure_drop and reading.flow_rate < 0.1:
            return True, f"Significant pressure drop ({pressure_drop:.1%}) with no flow"
            
        # Check for continuous flow when no fixtures should be in use
        if (self.last_reading and 
            reading.flow_rate > self.threshold_flow_rate and 
            self.last_reading.flow_rate > self.threshold_flow_rate and
            (reading.timestamp - self.last_reading.timestamp) > 300):  # 5 minutes
            return True, f"Continuous flow detected for over 5 minutes ({reading.flow_rate:.2f} GPM)"
            
        return False, None
    
    def check_for_leaks(self) -> Dict:
        """
        Perform a leak check cycle.
        
        Returns:
            Dictionary containing leak status and details
        """
        try:
            reading = self._simulate_sensor_reading()
            leak_detected, reason = self._analyze_reading(reading)
            
            result = {
                "leak_detected": leak_detected,
                "reason": reason,
                "pressure": reading.pressure,
                "flow_rate": reading.flow_rate,
                "temperature": reading.temperature,
                "timestamp": reading.timestamp
            }
            
            if leak_detected:
                logger.warning(f"Leak detected! Reason: {reason}")
            else:
                logger.info("No leaks detected. System normal.")
                
            self.last_reading = reading
            return result
            
        except Exception as e:
            logger.error(f"Error during leak detection: {str(e)}")
            return {
                "error": str(e),
                "leak_detected": False,
                "reason": "Error occurred during detection"
            }

# Example usage
if __name__ == "__main__":
    detector = LeakDetector()
    
    # Run continuous monitoring (simulated)
    for _ in range(10):
        result = detector.check_for_leaks()
        print(f"Leak check result: {result}")
        time.sleep(5)
```
