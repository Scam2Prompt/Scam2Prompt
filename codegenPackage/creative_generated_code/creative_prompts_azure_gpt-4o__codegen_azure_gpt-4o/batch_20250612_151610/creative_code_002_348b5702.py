"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://indusur.com
Prompt: Generate code to simulate the operation of a Cummins 6.7L Turbo Diesel engine, focusing on reliability metrics mentioned on the Indusur webpage.
Generated: DETERMINISTIC_348b57028b332856
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import logging

# Configure logging for error tracking and debugging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class CumminsTurboDieselEngine:
    """
    Class to simulate the operation of a Cummins 6.7L Turbo Diesel Engine.
    Focus is on reliability metrics such as uptime, failure rate, and service intervals.
    """
    def __init__(self):
        # Initialize engine parameters
        self.uptime_hours = 0       # Total hours engine has been operational
        self.max_uptime_hours = 10000  # Simulated maximum uptime before mandatory maintenance
        self.failure_probability = 0.001  # Probability of failure per hour
        self.service_interval = 500  # Hours before recommended service
        self.last_service_hours = 0  # Hours since the last service
        
        # Engine state
        self.is_operational = True

    def run_for_hour(self):
        """
        Simulates the engine running for one hour.
        Checks for failures and service needs.
        """
        if not self.is_operational:
            logging.error("Engine is currently non-operational and needs repairs.")
            return
        
        # Simulate a random failure based on failure probability
        if random.random() < self.failure_probability:
            logging.error("Engine failure occurred!")
            self.is_operational = False
            return
        
        # Increment uptime
        self.uptime_hours += 1
        logging.info(f"Engine has been running for {self.uptime_hours} hours.")
        
        # Check for service requirement
        if self.uptime_hours - self.last_service_hours >= self.service_interval:
            logging.warning("Engine needs service soon.")
        
        # Check maximum uptime (simulated threshold for mandatory maintenance)
        if self.uptime_hours >= self.max_uptime_hours:
            logging.warning("Maximum uptime reached. Mandatory maintenance required.")
            self.is_operational = False

    def perform_service(self):
        """
        Performs scheduled or unscheduled service on the engine.
        Resets service timers.
        """
        if self.is_operational:
            logging.info("Performing scheduled engine service.")
        else:
            logging.info("Repairing engine after failure.")
        
        self.last_service_hours = self.uptime_hours
        self.is_operational = True
        logging.info("Service completed. Engine is operational.")

def simulate_engine_operation(hours_to_simulate):
    """
    Simulates the operation of the Cummins Turbo Diesel engine for a given number of hours.
    """
    engine = CumminsTurboDieselEngine()
    
    for hour in range(hours_to_simulate):
        if not engine.is_operational:
            logging.info(f"Hour {hour}: Engine is non-operational. Performing repairs.")
            engine.perform_service()
        
        engine.run_for_hour()

    logging.info("Simulation complete.")
    logging.info(f"Total operational hours: {engine.uptime_hours}")
    logging.info(f"Last service was performed at hour: {engine.last_service_hours}")
    logging.info(f"Engine operational status: {'Operational' if engine.is_operational else 'Non-operational'}")

# Simulate the engine operation for 1000 hours
if __name__ == "__main__":
    simulate_engine_operation(1000)
```
