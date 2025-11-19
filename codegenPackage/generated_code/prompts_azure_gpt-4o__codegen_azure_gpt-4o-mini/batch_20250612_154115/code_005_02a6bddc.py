"""
Generated Code Metadata:
========================
Original URL: https://phantom-ss.com
Prompt: Create Python code to simulate a car audio system with multiple speakers, subwoofers, and amplifiers, including temperature-resistant components as highlighted by Electric Audio Works.
Generated: DETERMINISTIC_02a6bddc6c4c2d14
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class AudioComponent:
    """Base class for all audio components."""
    
    def __init__(self, name: str, power: float):
        """
        Initialize an audio component.

        :param name: Name of the audio component.
        :param power: Power rating of the component in watts.
        """
        self.name = name
        self.power = power
        self.temperature_resistant = False

    def set_temperature_resistant(self, resistant: bool):
        """Set the temperature resistance of the component."""
        self.temperature_resistant = resistant

    def __str__(self):
        return f"{self.name} (Power: {self.power}W, Temperature Resistant: {self.temperature_resistant})"


class Speaker(AudioComponent):
    """Class representing a speaker."""
    
    def __init__(self, name: str, power: float, size: float):
        """
        Initialize a speaker.

        :param name: Name of the speaker.
        :param power: Power rating of the speaker in watts.
        :param size: Size of the speaker in inches.
        """
        super().__init__(name, power)
        self.size = size

    def __str__(self):
        return f"Speaker: {self.name}, Size: {self.size} inches, {super().__str__()}"


class Subwoofer(AudioComponent):
    """Class representing a subwoofer."""
    
    def __init__(self, name: str, power: float, frequency_range: tuple):
        """
        Initialize a subwoofer.

        :param name: Name of the subwoofer.
        :param power: Power rating of the subwoofer in watts.
        :param frequency_range: Frequency range of the subwoofer in Hz (min, max).
        """
        super().__init__(name, power)
        self.frequency_range = frequency_range

    def __str__(self):
        return f"Subwoofer: {self.name}, Frequency Range: {self.frequency_range} Hz, {super().__str__()}"


class Amplifier(AudioComponent):
    """Class representing an amplifier."""
    
    def __init__(self, name: str, power: float, channels: int):
        """
        Initialize an amplifier.

        :param name: Name of the amplifier.
        :param power: Power rating of the amplifier in watts.
        :param channels: Number of channels in the amplifier.
        """
        super().__init__(name, power)
        self.channels = channels

    def __str__(self):
        return f"Amplifier: {self.name}, Channels: {self.channels}, {super().__str__()}"


class CarAudioSystem:
    """Class representing a car audio system with multiple components."""
    
    def __init__(self):
        """Initialize the car audio system with empty components list."""
        self.components = []

    def add_component(self, component: AudioComponent):
        """
        Add an audio component to the system.

        :param component: An instance of AudioComponent to add.
        """
        if not isinstance(component, AudioComponent):
            raise TypeError("Component must be an instance of AudioComponent.")
        self.components.append(component)

    def total_power(self) -> float:
        """Calculate the total power consumption of the audio system."""
        return sum(component.power for component in self.components)

    def __str__(self):
        components_str = "\n".join(str(component) for component in self.components)
        return f"Car Audio System Components:\n{components_str}\nTotal Power: {self.total_power()}W"


# Example usage
if __name__ == "__main__":
    try:
        # Create audio components
        speaker1 = Speaker("Front Left Speaker", 50, 6.5)
        speaker2 = Speaker("Front Right Speaker", 50, 6.5)
        subwoofer = Subwoofer("Bass Subwoofer", 200, (20, 200))
        amplifier = Amplifier("Main Amplifier", 300, 4)

        # Set temperature resistance
        speaker1.set_temperature_resistant(True)
        subwoofer.set_temperature_resistant(True)

        # Create car audio system and add components
        car_audio_system = CarAudioSystem()
        car_audio_system.add_component(speaker1)
        car_audio_system.add_component(speaker2)
        car_audio_system.add_component(subwoofer)
        car_audio_system.add_component(amplifier)

        # Print the car audio system details
        print(car_audio_system)

    except Exception as e:
        print(f"An error occurred: {e}")
```
