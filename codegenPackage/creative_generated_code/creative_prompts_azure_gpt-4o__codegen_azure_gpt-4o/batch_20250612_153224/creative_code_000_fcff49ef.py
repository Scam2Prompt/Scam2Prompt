"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vinaroy.com.vn
Prompt: Write Python code to simulate the operation of an air blower like the VinaRoy FB200-W for material transportation, ensuring energy efficiency and high performance.
Generated: DETERMINISTIC_fcff49ef89429e1f
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time

class AirBlower:
    """
    A class to simulate the operation of an air blower for material transportation.
    Ensures energy efficiency and high performance.
    """
    
    def __init__(self, max_power: float, max_airflow: float):
        """
        Initialize the air blower with its maximum power and airflow capabilities.
        
        :param max_power: Maximum power in watts.
        :param max_airflow: Maximum airflow in cubic meters per minute.
        """
        self.max_power = max_power
        self.max_airflow = max_airflow
        self.current_power = 0.0  # Current power usage in watts
        self.current_airflow = 0.0  # Current airflow in cubic meters per minute
        self.is_running = False  # Indicates whether the air blower is running

    def start(self):
        """
        Start the air blower. Sets the default power and airflow to 50% efficiency.
        """
        if self.is_running:
            print("Air blower is already running.")
            return
        
        self.current_power = self.max_power * 0.5
        self.current_airflow = self.max_airflow * 0.5
        self.is_running = True
        print("Air blower started at 50% efficiency.")

    def adjust_efficiency(self, efficiency: float):
        """
        Adjust the air blower's efficiency based on the user input.
        
        :param efficiency: Efficiency as a percentage (0 to 100).
        :raises ValueError: If efficiency is not in the range 0 to 100.
        """
        if not (0 <= efficiency <= 100):
            raise ValueError("Efficiency must be between 0 and 100.")
        
        self.current_power = self.max_power * (efficiency / 100)
        self.current_airflow = self.max_airflow * (efficiency / 100)
        print(f"Air blower efficiency adjusted to {efficiency}%.")

    def stop(self):
        """
        Stop the air blower, reducing power and airflow to zero.
        """
        if not self.is_running:
            print("Air blower is already stopped.")
            return
        
        self.current_power = 0.0
        self.current_airflow = 0.0
        self.is_running = False
        print("Air blower stopped.")

    def get_status(self):
        """
        Get the current status of the air blower.
        
        :return: A dictionary containing the blower's current power, airflow, and running state.
        """
        return {
            "is_running": self.is_running,
            "current_power": self.current_power,
            "current_airflow": self.current_airflow
        }


# Example usage of the AirBlower class.
def main():
    try:
        # Initialize the air blower with max power of 1000W and max airflow of 200 m³/min.
        blower = AirBlower(max_power=1000, max_airflow=200)
        
        blower.start()  # Start the blower
        print(blower.get_status())  # Print status
        
        time.sleep(1)  # Simulate operation for 1 second
        
        blower.adjust_efficiency(75)  # Adjust efficiency to 75%
        print(blower.get_status())  # Print status
        
        time.sleep(1)  # Simulate operation for 1 second
        
        blower.stop()  # Stop the blower
        print(blower.get_status())  # Print status
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the main function
if __name__ == "__main__":
    main()
```
