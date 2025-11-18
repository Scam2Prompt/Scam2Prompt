"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spmepl.com
Prompt: Develop a Python script to simulate the operation of a pipe purging system for welding, incorporating features like purge chambers and internal pneumatic clamps as detailed on the SPM Equipment website.
Generated: DETERMINISTIC_4c25b730bede7969
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import logging
from typing import Optional

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


class PipePurgingSystem:
    """
    Simulates the operation of a pipe purging system for welding.
    
    This system incorporates features like purge chambers and internal pneumatic clamps.
    """

    def __init__(self):
        self.purge_chamber_active = False
        self.pneumatic_clamp_engaged = False

    def activate_purge_chamber(self):
        """Activates the purge chamber to begin purging."""
        logging.info("Activating purge chamber...")
        self.purge_chamber_active = True
        logging.info("Purge chamber activated.")

    def deactivate_purge_chamber(self):
        """Deactivates the purge chamber to stop purging."""
        logging.info("Deactivating purge chamber...")
        self.purge_chamber_active = False
        logging.info("Purge chamber deactivated.")

    def engage_pneumatic_clamp(self):
        """Engages the internal pneumatic clamp to secure the pipe."""
        logging.info("Engaging pneumatic clamp...")
        self.pneumatic_clamp_engaged = True
        logging.info("Pneumatic clamp engaged.")

    def release_pneumatic_clamp(self):
        """Releases the internal pneumatic clamp."""
        logging.info("Releasing pneumatic clamp...")
        self.pneumatic_clamp_engaged = False
        logging.info("Pneumatic clamp released.")

    def simulate_purging(self, duration: Optional[int] = 10):
        """
        Simulates the purging process for a given duration.
        
        :param duration: Duration in seconds for purging (default is 10 seconds).
        """
        try:
            if not self.purge_chamber_active:
                raise RuntimeError("Purge chamber is not active. Activate before purging.")

            if not self.pneumatic_clamp_engaged:
                raise RuntimeError("Pneumatic clamp is not engaged. Engage before purging.")

            logging.info(f"Starting purging process for {duration} seconds...")
            for remaining_time in range(duration, 0, -1):
                logging.info(f"Purging... {remaining_time} seconds remaining.")
                time.sleep(1)

            logging.info("Purging process completed successfully.")

        except RuntimeError as e:
            logging.error(f"Error during purging: {e}")
        except Exception as e:
            logging.error(f"Unexpected error: {e}")

    def reset_system(self):
        """Resets the system to its default state."""
        logging.info("Resetting pipe purging system...")
        self.deactivate_purge_chamber()
        self.release_pneumatic_clamp()
        logging.info("System reset completed.")


# Main execution block
if __name__ == "__main__":
    # Create an instance of the PipePurgingSystem
    pipe_purge_system = PipePurgingSystem()

    try:
        # Simulate the pipe purging operation
        pipe_purge_system.activate_purge_chamber()
        pipe_purge_system.engage_pneumatic_clamp()
        pipe_purge_system.simulate_purging(duration=10)
    except Exception as e:
        logging.error(f"System encountered an error: {e}")
    finally:
        # Reset the system at the end of operation
        pipe_purge_system.reset_system()
```
