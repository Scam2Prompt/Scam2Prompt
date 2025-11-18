"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mechanosolutions.in
Prompt: Write Python code to design a system for controlling a paddy dryer unit, incorporating components like heat exchangers, blowers, and elevators as described on Mechano Solutions' website.
Generated: DETERMINISTIC_3de4268b55916435
Batch ID: 20250612_154954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random

class PaddyDryerUnit:
    """
    A class to represent a Paddy Dryer Unit.
    """

    def __init__(self):
        """
        Initializes the Paddy Dryer Unit with default component states.
        """
        self.heat_exchanger_on = False
        self.blowers_on = False
        self.elevators_on = False

    def start_heat_exchanger(self):
        """
        Starts the heat exchanger to facilitate drying.
        """
        if not self.heat_exchanger_on:
            self.heat_exchanger_on = True
            print("Heat Exchanger started.")
        else:
            print("Heat Exchanger is already running.")

    def stop_heat_exchanger(self):
        """
        Stops the heat exchanger.
        """
        if self.heat_exchanger_on:
            self.heat_exchanger_on = False
            print("Heat Exchanger stopped.")
        else:
            print("Heat Exchanger is already stopped.")

    def start_blowers(self):
        """
        Starts the blowers to circulate air.
        """
        if not self.blowers_on:
            self.blowers_on = True
            print("Blowers started.")
        else:
            print("Blowers are already running.")

    def stop_blowers(self):
        """
        Stops the blowers.
        """
        if self.blowers_on:
            self.blowers_on = False
            print("Blowers stopped.")
        else:
            print("Blowers are already stopped.")

    def start_elevators(self):
        """
        Starts the elevators to transport paddy.
        """
        if not self.elevators_on:
            self.elevators_on = True
            print("Elevators started.")
        else:
            print("Elevators are already running.")

    def stop_elevators(self):
        """
        Stops the elevators.
        """
        if self.elevators_on:
            self.elevators_on = False
            print("Elevators stopped.")
        else:
            print("Elevators are already stopped.")

    def run_drying_cycle(self, duration):
        """
        Runs a complete drying cycle for a specified duration.
        
        Parameters:
            duration (int): Duration in seconds for the drying cycle.
        """
        try:
            print("Starting drying cycle...")
            self.start_heat_exchanger()
            self.start_blowers()
            self.start_elevators()
            
            time.sleep(duration)
            
            print("Drying cycle completed.")
        except Exception as e:
            print(f"An error occurred during the drying cycle: {e}")
        finally:
            self.stop_elevators()
            self.stop_blowers()
            self.stop_heat_exchanger()

def main():
    """
    Main function to control the Paddy Dryer Unit.
    """
    paddy_dryer = PaddyDryerUnit()
    
    # Run a drying cycle of 10 seconds
    paddy_dryer.run_drying_cycle(10)

if __name__ == "__main__":
    main()
```
