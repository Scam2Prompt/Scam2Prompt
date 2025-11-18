"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jggbbestforyou.com
Prompt: Create a script to simulate the behavior of Medtrum TouchCare® Nano insulin pump under different insulin infusion rates and user-defined glucose targets.
Generated: DETERMINISTIC_9e98d2c9b3bb67c9
Batch ID: 20250612_154306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time

class InsulinPumpSimulator:
    """
    A class to simulate the behavior of the Medtrum TouchCare® Nano insulin pump.
    """

    def __init__(self, glucose_target, basal_rate, max_bolus_rate):
        """
        Initialize the pump simulator with user-defined parameters.
        
        :param glucose_target: Target glucose level in mg/dL.
        :param basal_rate: Basal insulin infusion rate in units/hour.
        :param max_bolus_rate: Maximum bolus insulin infusion rate in units/hour.
        """
        self.glucose_target = glucose_target
        self.basal_rate = basal_rate
        self.max_bolus_rate = max_bolus_rate
        self.current_glucose = glucose_target
        self.infusion_rate = basal_rate

    def get_glucose_level(self):
        """
        Simulate retrieving the current glucose level.
        
        :return: Current glucose level in mg/dL.
        """
        return self.current_glucose

    def adjust_infusion_rate(self):
        """
        Adjust the insulin infusion rate based on the current glucose level
        relative to the target glucose level.
        """
        try:
            if self.current_glucose > self.glucose_target:
                # Increase infusion rate to lower glucose
                self.infusion_rate = min(
                    self.infusion_rate + 0.5, self.max_bolus_rate
                )
            elif self.current_glucose < self.glucose_target:
                # Decrease infusion rate to avoid hypoglycemia
                self.infusion_rate = max(self.infusion_rate - 0.5, self.basal_rate)
        except Exception as e:
            # Handle unexpected errors
            print(f"Error adjusting infusion rate: {e}")

    def simulate_glucose_change(self):
        """
        Simulate glucose level changes based on insulin infusion rate.
        """
        try:
            # Simple simulation: glucose level decreases as insulin infusion increases
            self.current_glucose -= self.infusion_rate * 0.2
            # Add minimum boundary to prevent unrealistic drops
            self.current_glucose = max(self.current_glucose, 40)
        except Exception as e:
            print(f"Error simulating glucose change: {e}")

    def run_simulation(self, duration_seconds):
        """
        Run the insulin pump simulation for the specified duration.
        
        :param duration_seconds: Duration of the simulation in seconds.
        """
        try:
            start_time = time.time()
            while time.time() - start_time < duration_seconds:
                self.simulate_glucose_change()
                self.adjust_infusion_rate()
                
                # Log the current state
                print(
                    f"Glucose Level: {self.current_glucose:.2f} mg/dL | "
                    f"Infusion Rate: {self.infusion_rate:.2f} units/hour"
                )
                
                # Simulate real-time behavior by pausing briefly
                time.sleep(1)
        except Exception as e:
            print(f"Error during simulation: {e}")

if __name__ == "__main__":
    # User-defined parameters for simulation
    glucose_target = 120      # Target glucose level in mg/dL
    basal_rate = 1.0          # Basal insulin rate in units/hour
    max_bolus_rate = 10.0     # Max bolus rate in units/hour

    # Create an instance of the simulator
    pump_simulator = InsulinPumpSimulator(glucose_target, basal_rate, max_bolus_rate)

    # Run the simulation for 30 seconds
    pump_simulator.run_simulation(duration_seconds=30)
```
