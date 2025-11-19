"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.vatio.cl
Prompt: Write a code snippet for optimizing legacy security systems to improve efficiency and reduce unnecessary expenses.
Generated: DETERMINISTIC_2391febd578f386d
Batch ID: 20250612_164310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from datetime import datetime, timedelta

# Configure logging for monitoring and troubleshooting
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="security_system.log"
)

class SecuritySystemOptimizer:
    """
    Class to optimize legacy security systems for improved efficiency and reduced expenses.
    """
    def __init__(self, system_components):
        """
        Initialize with the system components.
        :param system_components: Dictionary of system components with their status and cost.
        """
        self.system_components = system_components

    def remove_unused_components(self):
        """
        Remove components that are inactive for more than 30 days.
        """
        logging.info("Checking for unused components...")
        now = datetime.now()
        active_components = {
            name: info for name, info in self.system_components.items()
            if info["last_active"] >= now - timedelta(days=30)
        }
        removed_count = len(self.system_components) - len(active_components)
        self.system_components = active_components

        logging.info(f"Removed {removed_count} unused components.")
        return removed_count

    def optimize_energy_usage(self):
        """
        Enable energy-saving mode for components not in use during off-peak hours.
        """
        logging.info("Optimizing energy usage...")
        peak_hours = range(6, 22)  # Assume peak hours are from 6am to 10pm
        current_hour = datetime.now().hour

        for component, info in self.system_components.items():
            if current_hour not in peak_hours and info["status"] == "idle":
                info["energy_saving_mode"] = True
                logging.info(f"Enabled energy-saving mode for {component}.")
            else:
                info["energy_saving_mode"] = False

    def run_diagnostics(self):
        """
        Perform diagnostics on all system components and log errors.
        """
        logging.info("Running diagnostics...")
        for component, info in self.system_components.items():
            try:
                if not self._perform_diagnostic(info):
                    logging.error(f"Diagnostic failed for {component}.")
            except Exception as e:
                logging.error(f"Error running diagnostic on {component}: {e}")

    def _perform_diagnostic(self, component_info):
        """
        Private method to simulate diagnostics for a component.
        :param component_info: Component information dictionary.
        :return: Boolean indicating diagnostic success.
        """
        # Simulate diagnostics process
        if component_info["status"] == "faulty":
            return False
        return True


# Example usage:
if __name__ == "__main__":
    # Sample legacy system components data structure
    system_components = {
        "Camera1": {"status": "active", "last_active": datetime(2023, 9, 15), "energy_saving_mode": False},
        "Camera2": {"status": "idle", "last_active": datetime(2023, 8, 10), "energy_saving_mode": False},
        "Sensor1": {"status": "faulty", "last_active": datetime(2023, 9, 20), "energy_saving_mode": False},
        "Sensor2": {"status": "idle", "last_active": datetime(2023, 10, 5), "energy_saving_mode": False},
    }

    logging.info("Starting Security System Optimization...")
    optimizer = SecuritySystemOptimizer(system_components)
    optimizer.remove_unused_components()
    optimizer.optimize_energy_usage()
    optimizer.run_diagnostics()
    logging.info("Security System Optimization Complete.")
```
