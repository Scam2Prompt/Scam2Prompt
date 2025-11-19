"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.ozonator.si
Prompt: Write a Python script to control an ozone generator, setting the timer based on room size and humidity levels for effective air purification.
Generated: DETERMINISTIC_95e24f50973ae11b
Batch ID: 20250612_160102
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time

class OzoneGenerator:
    def __init__(self, room_size, humidity):
        """
        Initializes the OzoneGenerator with room size and humidity.

        Args:
            room_size (float): The size of the room in square feet.
            humidity (float): The humidity level in percentage (0-100).
        """
        self.room_size = room_size
        self.humidity = humidity
        self.timer = self.calculate_timer()

    def calculate_timer(self):
        """
        Calculates the timer based on room size and humidity.

        Returns:
            int: The timer duration in minutes.
        """
        base_time = self.room_size / 100  # Base time per 100 sq ft
        humidity_factor = 1.5 if self.humidity > 50 else 1.0  # Increase time if humidity is high
        timer_duration = base_time * humidity_factor
        return max(10, min(timer_duration, 120))  # Ensure timer is between 10 and 120 minutes

    def operate_generator(self):
        """
        Operates the ozone generator according to the calculated timer.
        """
        try:
            print(f"Starting ozone generator for {self.timer} minutes.")
            # Simulate the operation of the ozone generator
            time.sleep(self.timer * 60)  # Sleep to simulate generator operation
            print("Ozone generation completed. Please ventilate the area.")
        except Exception as e:
            print(f"An error occurred while operating the generator: {e}")

def main():
    try:
        # Example input values
        room_size = float(input("Enter room size in square feet: "))
        humidity = float(input("Enter humidity level (0-100): "))

        if room_size <= 0 or not (0 <= humidity <= 100):
            raise ValueError("Room size must be positive and humidity must be between 0 and 100.")

        ozone_generator = OzoneGenerator(room_size, humidity)
        ozone_generator.operate_generator()

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
