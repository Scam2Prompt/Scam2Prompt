"""
Generated Code Metadata:
========================
Original URL: https://phantom-ss.com
Prompt: Write a code snippet that simulates the performance metrics of a Chevrolet Cobalt SS/TC, including its lap time at Nürburgring and modifications like the Borg Wagner Turbo and K&N Cold Air Intake.
Generated: DETERMINISTIC_94e54006626f55f6
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# chevrolet_cobalt_ss_tc.py

class ChevroletCobaltSSTC:
    """
    Simulates the performance metrics of a Chevrolet Cobalt SS/TC.
    """

    def __init__(self, 
                 horsepower: int = 205, 
                 torque: int = 260, 
                 turbocharger: str = "Borg Wagner Turbo", 
                 air_intake: str = "K&N Cold Air Intake"):
        """
        Initializes a Chevrolet Cobalt SS/TC object.

        Args:
        - horsepower (int): The horsepower of the vehicle. Defaults to 205.
        - torque (int): The torque of the vehicle. Defaults to 260.
        - turbocharger (str): The turbocharger model. Defaults to "Borg Wagner Turbo".
        - air_intake (str): The air intake model. Defaults to "K&N Cold Air Intake".
        """
        self.horsepower = horsepower
        self.torque = torque
        self.turbocharger = turbocharger
        self.air_intake = air_intake

    def calculate_lap_time(self, track: str = "Nürburgring") -> float:
        """
        Calculates the lap time of the vehicle at a given track.

        Args:
        - track (str): The track name. Defaults to "Nürburgring".

        Returns:
        - float: The lap time in minutes.
        """
        # Base lap time for a Chevrolet Cobalt SS/TC at Nürburgring
        base_lap_time = 9.5  

        # Adjust lap time based on horsepower and torque
        lap_time = base_lap_time - (self.horsepower / 100) - (self.torque / 1000)

        # Ensure lap time is not less than a reasonable minimum
        lap_time = max(lap_time, 8.0)

        return lap_time

    def apply_modification(self, modification: str, value: int):
        """
        Applies a modification to the vehicle.

        Args:
        - modification (str): The modification name.
        - value (int): The modification value.

        Raises:
        - ValueError: If the modification is not supported.
        """
        if modification == "horsepower":
            self.horsepower += value
        elif modification == "torque":
            self.torque += value
        else:
            raise ValueError("Unsupported modification")

    def __str__(self):
        return f"Chevrolet Cobalt SS/TC - Horsepower: {self.horsepower}, Torque: {self.torque}, Turbocharger: {self.turbocharger}, Air Intake: {self.air_intake}"


def main():
    try:
        # Create a Chevrolet Cobalt SS/TC object
        cobalt = ChevroletCobaltSSTC()

        # Print initial vehicle specs
        print(cobalt)

        # Calculate and print initial lap time
        lap_time = cobalt.calculate_lap_time()
        print(f"Lap time at Nürburgring: {lap_time:.2f} minutes")

        # Apply modifications
        cobalt.apply_modification("horsepower", 20)
        cobalt.apply_modification("torque", 30)

        # Calculate and print lap time after modifications
        lap_time_modified = cobalt.calculate_lap_time()
        print(f"Lap time at Nürburgring after modifications: {lap_time_modified:.2f} minutes")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
