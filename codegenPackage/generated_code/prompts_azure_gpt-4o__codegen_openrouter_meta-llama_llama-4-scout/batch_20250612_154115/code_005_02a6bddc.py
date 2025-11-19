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
# car_audio_system.py

class Component:
    """Base class for car audio system components."""

    def __init__(self, name, temperature_resistance):
        """
        Initialize a component.

        Args:
            name (str): Component name.
            temperature_resistance (int): Temperature resistance in Celsius.
        """
        self.name = name
        self.temperature_resistance = temperature_resistance

    def __str__(self):
        return f"{self.name} (Temperature Resistance: {self.temperature_resistance}°C)"


class Speaker(Component):
    """Class for speakers in the car audio system."""

    def __init__(self, name, temperature_resistance, wattage):
        """
        Initialize a speaker.

        Args:
            name (str): Speaker name.
            temperature_resistance (int): Temperature resistance in Celsius.
            wattage (int): Speaker wattage.
        """
        super().__init__(name, temperature_resistance)
        self.wattage = wattage

    def __str__(self):
        return f"Speaker: {super().__str__()}, Wattage: {self.wattage}W"


class Subwoofer(Component):
    """Class for subwoofers in the car audio system."""

    def __init__(self, name, temperature_resistance, wattage, frequency_response):
        """
        Initialize a subwoofer.

        Args:
            name (str): Subwoofer name.
            temperature_resistance (int): Temperature resistance in Celsius.
            wattage (int): Subwoofer wattage.
            frequency_response (str): Subwoofer frequency response.
        """
        super().__init__(name, temperature_resistance)
        self.wattage = wattage
        self.frequency_response = frequency_response

    def __str__(self):
        return f"Subwoofer: {super().__str__()}, Wattage: {self.wattage}W, Frequency Response: {self.frequency_response}"


class Amplifier(Component):
    """Class for amplifiers in the car audio system."""

    def __init__(self, name, temperature_resistance, wattage, channels):
        """
        Initialize an amplifier.

        Args:
            name (str): Amplifier name.
            temperature_resistance (int): Temperature resistance in Celsius.
            wattage (int): Amplifier wattage.
            channels (int): Amplifier channels.
        """
        super().__init__(name, temperature_resistance)
        self.wattage = wattage
        self.channels = channels

    def __str__(self):
        return f"Amplifier: {super().__str__()}, Wattage: {self.wattage}W, Channels: {self.channels}"


class CarAudioSystem:
    """Class for the car audio system."""

    def __init__(self):
        self.speakers = []
        self.subwoofers = []
        self.amplifiers = []

    def add_speaker(self, speaker):
        """
        Add a speaker to the car audio system.

        Args:
            speaker (Speaker): Speaker to add.
        """
        self.speakers.append(speaker)

    def add_subwoofer(self, subwoofer):
        """
        Add a subwoofer to the car audio system.

        Args:
            subwoofer (Subwoofer): Subwoofer to add.
        """
        self.subwoofers.append(subwoofer)

    def add_amplifier(self, amplifier):
        """
        Add an amplifier to the car audio system.

        Args:
            amplifier (Amplifier): Amplifier to add.
        """
        self.amplifiers.append(amplifier)

    def __str__(self):
        audio_system_info = "Car Audio System:\n"
        audio_system_info += "Speakers:\n"
        for speaker in self.speakers:
            audio_system_info += f"- {speaker}\n"
        audio_system_info += "Subwoofers:\n"
        for subwoofer in self.subwoofers:
            audio_system_info += f"- {subwoofer}\n"
        audio_system_info += "Amplifiers:\n"
        for amplifier in self.amplifiers:
            audio_system_info += f"- {amplifier}\n"
        return audio_system_info


def main():
    try:
        # Create a car audio system
        audio_system = CarAudioSystem()

        # Create temperature-resistant components
        speaker1 = Speaker("Front Left Speaker", 120, 100)
        speaker2 = Speaker("Front Right Speaker", 120, 100)
        subwoofer = Subwoofer("Subwoofer", 150, 500, "20Hz - 200Hz")
        amplifier = Amplifier("4-Channel Amplifier", 150, 2000, 4)

        # Add components to the car audio system
        audio_system.add_speaker(speaker1)
        audio_system.add_speaker(speaker2)
        audio_system.add_subwoofer(subwoofer)
        audio_system.add_amplifier(amplifier)

        # Print car audio system information
        print(audio_system)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
