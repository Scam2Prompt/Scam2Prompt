"""
Generated Code Metadata:
========================
Original URL: https://aktivrorteknikk.no
Prompt: Write Python code to simulate a pressure testing process for water pipelines, incorporating methods like pressure thresholds and leak detection as described by Aktiv Rørteknikk AS.
Generated: DETERMINISTIC_0aa3827eaab719e0
Batch ID: 20250612_154209
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
from typing import Optional, Tuple, List
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class PressureTestSimulator:
    """
    Simulates pressure testing for water pipelines with configurable thresholds and leak detection.
    """
    
    def __init__(
        self,
        pipeline_id: str,
        max_pressure: float,
        test_duration: int,
        pressure_threshold: float,
        leak_threshold: float
    ):
        """
        Initialize the pressure test simulator.
        
        Args:
            pipeline_id: Unique identifier for the pipeline
            max_pressure: Maximum allowed pressure in bar
            test_duration: Duration of test in seconds
            pressure_threshold: Pressure drop threshold for failure (bar)
            leak_threshold: Rate of pressure drop indicating a leak (bar/second)
        """
        self.pipeline_id = pipeline_id
        self.max_pressure = max_pressure
        self.test_duration = test_duration
        self.pressure_threshold = pressure_threshold
        self.leak_threshold = leak_threshold
        self.current_pressure = 0.0
        self.test_start_time = 0.0
        self.test_results = []
        self.leak_detected = False
        self.pressure_violation = False
        
    def _simulate_pressure_reading(self) -> float:
        """
        Simulate a pressure reading with possible small fluctuations.
        
        Returns:
            Current pressure reading in bar
        """
        # Base pressure with small random fluctuations
        fluctuation = random.uniform(-0.05, 0.05)
        
        # Simulate leak if detected
        if self.leak_detected:
            time_elapsed = time.time() - self.test_start_time
            leak_rate = self.leak_threshold * 1.5  # Accelerated leak for simulation
            pressure_drop = leak_rate * (time_elapsed / self.test_duration)
            return max(0, self.current_pressure - pressure_drop + fluctuation)
        
        return self.current_pressure + fluctuation
    
    def _check_pressure_violation(self, pressure: float) -> bool:
        """
        Check if pressure exceeds maximum allowed.
        
        Args:
            pressure: Current pressure reading
            
        Returns:
            True if pressure exceeds maximum, False otherwise
        """
        return pressure > self.max_pressure
    
    def _check_leak(self, pressure_readings: List[Tuple[float, float]]) -> bool:
        """
        Analyze pressure readings to detect leaks.
        
        Args:
            pressure_readings: List of (timestamp, pressure) readings
            
        Returns:
            True if leak is detected, False otherwise
        """
        if len(pressure_readings) < 2:
            return False
            
        # Calculate pressure drop rate
        last_reading = pressure_readings[-1]
        prev_reading = pressure_readings[-2]
        
        time_diff = last_reading[0] - prev_reading[0]
        pressure_diff = prev_reading[1] - last_reading[1]
        
        if time_diff > 0:
            drop_rate = pressure_diff / time_diff
            return drop_rate >= self.leak_threshold
        return False
    
    def _log_test_event(self, event: str, details: str = ""):
        """
        Log test events with standardized format.
        
        Args:
            event: Description of the event
            details: Additional details about the event
        """
        logger.info(f"Pipeline {self.pipeline_id} - {event}. {details}")
    
    def pressurize_pipeline(self, target_pressure: float):
        """
        Simulate pressurizing the pipeline to target pressure.
        
        Args:
            target_pressure: Desired pressure in bar
        """
        if target_pressure > self.max_pressure:
            raise ValueError("Target pressure exceeds maximum allowed pressure")
            
        self._log_test_event("Pressurization started", f"Target: {target_pressure} bar")
        
        # Simulate gradual pressure increase
        steps = 10
        increment = target_pressure / steps
        
        for _ in range(steps):
            self.current_pressure += increment
            time.sleep(0.5)  # Simulate time to increase pressure
            
            # Check for pressure violations during pressurization
            if self._check_pressure_violation(self.current_pressure):
                self.pressure_violation = True
                self._log_test_event("Pressure violation detected during pressurization", 
                                   f"Current: {self.current_pressure:.2f} bar, Max: {self.max_pressure} bar")
                break
                
        self._log_test_event("Pressurization completed", f"Current pressure: {self.current_pressure:.2f} bar")
    
    def run_pressure_test(self) -> Tuple[bool, str]:
        """
        Run the pressure test and monitor for leaks or pressure drops.
        
        Returns:
            Tuple of (test_passed, failure_reason)
        """
        if self.pressure_violation:
            return (False, "Pressure violation during pressurization")
            
        self.test_start_time = time.time()
        end_time = self.test_start_time + self.test_duration
        pressure_readings = []
        
        self._log_test_event("Pressure test started", f"Duration: {self.test_duration} seconds")
        
        try:
            while time.time() < end_time and not self.leak_detected:
                # Get current pressure reading
                current_time = time.time()
                pressure = self._simulate_pressure_reading()
                pressure_readings.append((current_time, pressure))
                
                # Check for pressure drop below threshold
                if pressure < (self.current_pressure - self.pressure_threshold):
                    self._log_test_event("Significant pressure drop detected", 
                                       f"Current: {pressure:.2f} bar, Threshold: {self.pressure_threshold} bar")
                    return (False, "Pressure drop below threshold")
                
                # Check for leaks
                if len(pressure_readings) >= 2 and self._check_leak(pressure_readings):
                    self.leak_detected = True
                    self._log_test_event("Leak detected", 
                                       f"Drop rate exceeds threshold: {self.leak_threshold} bar/sec")
                    return (False, "Leak detected")
                
                # Check for pressure violations
                if self._check_pressure_violation(pressure):
                    self.pressure_violation = True
                    self._log_test_event("Pressure violation detected", 
                                       f"Current: {pressure:.2f} bar, Max: {self.max_pressure} bar")
                    return (False, "Pressure violation during test")
                
                time.sleep(1)  # Simulate time between readings
                
        except Exception as e:
            logger.error(f"Error during pressure test: {str(e)}")
            return (False, f"Test error: {str(e)}")
        
        if not self.leak_detected and not self.pressure_violation:
            self._log_test_event("Pressure test completed successfully")
            return (True, "Test passed")
        
        return (False, "Unknown test failure")

    def get_test_report(self) -> dict:
        """
        Generate a test report with all relevant information.
        
        Returns:
            Dictionary containing test results and metrics
        """
        return {
            "pipeline_id": self.pipeline_id,
            "max_pressure": self.max_pressure,
            "test_duration": self.test_duration,
            "pressure_threshold": self.pressure_threshold,
            "leak_threshold": self.leak_threshold,
            "final_pressure": self.current_pressure,
            "leak_detected": self.leak_detected,
            "pressure_violation": self.pressure_violation,
            "test_passed": not (self.leak_detected or self.pressure_violation)
        }


def simulate_pipeline_test(
    pipeline_id: str,
    max_pressure: float = 10.0,
    test_duration: int = 60,
    pressure_threshold: float = 0.5,
    leak_threshold: float = 0.01
) -> dict:
    """
    Convenience function to simulate a complete pipeline pressure test.
    
    Args:
        pipeline_id: Unique identifier for the pipeline
        max_pressure: Maximum allowed pressure in bar
        test_duration: Duration of test in seconds
        pressure_threshold: Pressure drop threshold for failure (bar)
        leak_threshold: Rate of pressure drop indicating a leak (bar/second)
        
    Returns:
        Test report dictionary
    """
    simulator = PressureTestSimulator(
        pipeline_id=pipeline_id,
        max_pressure=max_pressure,
        test_duration=test_duration,
        pressure_threshold=pressure_threshold,
        leak_threshold=leak_threshold
    )
    
    try:
        # Pressurize to 90% of max pressure for test
        simulator.pressurize_pipeline(target_pressure=max_pressure * 0.9)
        
        # Run the pressure test
