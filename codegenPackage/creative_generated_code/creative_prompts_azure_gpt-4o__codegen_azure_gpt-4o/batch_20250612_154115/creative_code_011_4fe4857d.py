"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantom-ss.com
Prompt: Create code to simulate the integration of a short-throw shifter and performance display in a racing game, referencing the Chevrolet Cobalt SS/TC's interior features.
Generated: DETERMINISTIC_4fe4857de00d01ea
Batch ID: 20250612_154115
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

class ShortThrowShifter:
    """
    Simulates a short-throw shifter for gear changes in a racing game.
    """
    def __init__(self):
        self.gears = ['Neutral', '1st', '2nd', '3rd', '4th', '5th']
        self.current_gear = 'Neutral'

    def shift_up(self):
        """
        Shifts up to the next gear.
        """
        try:
            current_index = self.gears.index(self.current_gear)
            if current_index < len(self.gears) - 1:
                self.current_gear = self.gears[current_index + 1]
            else:
                print("Already in the highest gear!")
        except ValueError:
            print("Invalid gear state encountered!")

    def shift_down(self):
        """
        Shifts down to the previous gear.
        """
        try:
            current_index = self.gears.index(self.current_gear)
            if current_index > 0:
                self.current_gear = self.gears[current_index - 1]
            else:
                print("Already in Neutral!")
        except ValueError:
            print("Invalid gear state encountered!")

    def get_current_gear(self):
        """
        Returns the current gear.
        """
        return self.current_gear


class PerformanceDisplay:
    """
    Simulates a performance display showing speed, RPM, and turbo boost levels.
    """
    def __init__(self):
        self.speed = 0  # Speed in mph
        self.rpm = 0  # RPM in revolutions per minute
        self.boost = 0  # Turbo boost in psi

    def update(self, gear):
        """
        Updates the performance metrics based on the current gear.
        """
        if gear == 'Neutral':
            self.speed = 0
            self.rpm = 0
            self.boost = 0
        else:
            gear_multiplier = self._get_gear_multiplier(gear)
            self.speed = random.randint(gear_multiplier * 20, gear_multiplier * 40)
            self.rpm = random.randint(gear_multiplier * 2000, gear_multiplier * 4000)
            self.boost = random.uniform(gear_multiplier * 2, gear_multiplier * 5)

    def _get_gear_multiplier(self, gear):
        """
        Returns a multiplier based on the gear (for performance calculations).
        """
        gear_map = {
            '1st': 1,
            '2nd': 2,
            '3rd': 3,
            '4th': 4,
            '5th': 5
        }
        return gear_map.get(gear, 0)

    def display(self):
        """
        Displays the current performance metrics.
        """
        print(f"Speed: {self.speed} mph")
        print(f"RPM: {self.rpm}")
        print(f"Turbo Boost: {self.boost:.2f} psi")


# Main simulation
def main():
    shifter = ShortThrowShifter()
    display = PerformanceDisplay()

    print("Welcome to the Racing Game!")
    print("Controls: 'u' to shift up, 'd' to shift down, 'q' to quit")

    while True:
        command = input("Enter command: ")
        if command == 'u':
            shifter.shift_up()
        elif command == 'd':
            shifter.shift_down()
        elif command == 'q':
            print("Exiting the game...")
            break
        else:
            print("Invalid command! Use 'u', 'd', or 'q'.")

        current_gear = shifter.get_current_gear()
        print(f"Current Gear: {current_gear}")
        
        display.update(current_gear)
        display.display()

        time.sleep(1)  # Simulate time delay for realism


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nGame interrupted. Exiting...")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
