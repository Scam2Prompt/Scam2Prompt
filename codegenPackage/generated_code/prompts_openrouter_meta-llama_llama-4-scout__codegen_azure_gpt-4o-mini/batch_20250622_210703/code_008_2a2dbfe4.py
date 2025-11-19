"""
Generated Code Metadata:
========================
Original URL: https://spmepl.com
Prompt: "Design a pipe handling equipment, including pipe rollers and rotators, for a pipeline construction project."
Generated: DETERMINISTIC_2a2dbfe44c1f8ad7
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PipeRoller:
    """
    A class to represent a pipe roller used in pipeline construction.
    """

    def __init__(self, roller_diameter: float, load_capacity: float):
        """
        Initializes a PipeRoller instance.

        :param roller_diameter: Diameter of the roller in meters.
        :param load_capacity: Maximum load capacity of the roller in kilograms.
        """
        self.roller_diameter = roller_diameter
        self.load_capacity = load_capacity
        self.current_load = 0.0

    def load_pipe(self, weight: float):
        """
        Loads a pipe onto the roller.

        :param weight: Weight of the pipe in kilograms.
        :raises ValueError: If the weight exceeds the load capacity.
        """
        if weight > self.load_capacity:
            raise ValueError("Weight exceeds load capacity of the roller.")
        self.current_load += weight

    def unload_pipe(self, weight: float):
        """
        Unloads a pipe from the roller.

        :param weight: Weight of the pipe in kilograms.
        :raises ValueError: If the weight to unload exceeds the current load.
        """
        if weight > self.current_load:
            raise ValueError("Cannot unload more than the current load.")
        self.current_load -= weight

    def get_current_load(self) -> float:
        """
        Returns the current load on the roller.

        :return: Current load in kilograms.
        """
        return self.current_load


class PipeRotator:
    """
    A class to represent a pipe rotator used in pipeline construction.
    """

    def __init__(self, rotation_speed: float):
        """
        Initializes a PipeRotator instance.

        :param rotation_speed: Speed of rotation in degrees per second.
        """
        self.rotation_speed = rotation_speed
        self.is_rotating = False

    def start_rotation(self):
        """
        Starts the rotation of the pipe.
        """
        if not self.is_rotating:
            self.is_rotating = True
            print("Pipe rotation started.")

    def stop_rotation(self):
        """
        Stops the rotation of the pipe.
        """
        if self.is_rotating:
            self.is_rotating = False
            print("Pipe rotation stopped.")

    def get_rotation_status(self) -> bool:
        """
        Returns the current rotation status.

        :return: True if rotating, False otherwise.
        """
        return self.is_rotating


class PipelineConstruction:
    """
    A class to manage the pipeline construction process using pipe rollers and rotators.
    """

    def __init__(self):
        """
        Initializes the PipelineConstruction instance with empty equipment lists.
        """
        self.rollers = []
        self.rotators = []

    def add_roller(self, roller: PipeRoller):
        """
        Adds a PipeRoller to the construction equipment.

        :param roller: An instance of PipeRoller.
        """
        self.rollers.append(roller)

    def add_rotator(self, rotator: PipeRotator):
        """
        Adds a PipeRotator to the construction equipment.

        :param rotator: An instance of PipeRotator.
        """
        self.rotators.append(rotator)

    def load_pipe_to_roller(self, roller_index: int, weight: float):
        """
        Loads a pipe onto a specified roller.

        :param roller_index: Index of the roller in the rollers list.
        :param weight: Weight of the pipe in kilograms.
        :raises IndexError: If the roller index is out of range.
        """
        try:
            self.rollers[roller_index].load_pipe(weight)
        except IndexError:
            print("Error: Roller index out of range.")
        except ValueError as e:
            print(f"Error: {e}")

    def unload_pipe_from_roller(self, roller_index: int, weight: float):
        """
        Unloads a pipe from a specified roller.

        :param roller_index: Index of the roller in the rollers list.
        :param weight: Weight of the pipe in kilograms.
        :raises IndexError: If the roller index is out of range.
        """
        try:
            self.rollers[roller_index].unload_pipe(weight)
        except IndexError:
            print("Error: Roller index out of range.")
        except ValueError as e:
            print(f"Error: {e}")

    def start_rotator(self, rotator_index: int):
        """
        Starts the rotation of a specified rotator.

        :param rotator_index: Index of the rotator in the rotators list.
        :raises IndexError: If the rotator index is out of range.
        """
        try:
            self.rotators[rotator_index].start_rotation()
        except IndexError:
            print("Error: Rotator index out of range.")

    def stop_rotator(self, rotator_index: int):
        """
        Stops the rotation of a specified rotator.

        :param rotator_index: Index of the rotator in the rotators list.
        :raises IndexError: If the rotator index is out of range.
        """
        try:
            self.rotators[rotator_index].stop_rotation()
        except IndexError:
            print("Error: Rotator index out of range.")


# Example usage
if __name__ == "__main__":
    # Create pipeline construction instance
    pipeline = PipelineConstruction()

    # Create and add pipe rollers
    roller1 = PipeRoller(0.5, 1000)
    roller2 = PipeRoller(0.6, 1200)
    pipeline.add_roller(roller1)
    pipeline.add_roller(roller2)

    # Create and add pipe rotators
    rotator1 = PipeRotator(30)
    rotator2 = PipeRotator(45)
    pipeline.add_rotator(rotator1)
    pipeline.add_rotator(rotator2)

    # Load and unload pipes
    pipeline.load_pipe_to_roller(0, 800)
    pipeline.unload_pipe_from_roller(0, 300)

    # Start and stop rotation
    pipeline.start_rotator(0)
    pipeline.stop_rotator(0)
```
