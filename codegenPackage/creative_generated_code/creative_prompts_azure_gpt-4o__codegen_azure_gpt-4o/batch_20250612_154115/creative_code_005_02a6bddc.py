"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantom-ss.com
Prompt: Create Python code to simulate a car audio system with multiple speakers, subwoofers, and amplifiers, including temperature-resistant components as highlighted by Electric Audio Works.
Generated: DETERMINISTIC_02a6bddc6c4c2d14
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Car Audio System Simulation

This code simulates a car audio system with multiple components including speakers, subwoofers, amplifiers,
and temperature-resistant elements as highlighted by Electric Audio Works.
"""

class TemperatureResistantComponent:
    """
    Base class for components that are temperature-resistant.
    """
    def __init__(self, max_temperature: float):
        """
        Initializes the temperature-resistant component.
        :param max_temperature: Maximum operating temperature in Celsius.
        """
        self.max_temperature = max_temperature
        self.current_temperature = 25.0  # Default temperature (room temperature)

    def check_temperature(self):
        """
        Checks if the component is within safe operating temperature.
        :raises ValueError: If the temperature exceeds the maximum allowable temperature.
        """
        if self.current_temperature > self.max_temperature:
            raise ValueError(
                f"Temperature exceeded! Current: {self.current_temperature}°C, Max: {self.max_temperature}°C"
            )


class Speaker(TemperatureResistantComponent):
    """
    Represents a speaker in the car audio system.
    """
    def __init__(self, max_temperature: float, power_rating: float):
        """
        Initializes a speaker.
        :param max_temperature: Maximum operating temperature in Celsius.
        :param power_rating: Power rating in watts.
        """
        super().__init__(max_temperature)
        self.power_rating = power_rating

    def play_sound(self, volume: int):
        """
        Simulates playing sound.
        :param volume: Volume level (0-100).
        """
        self.check_temperature()
        print(f"Speaker playing sound at volume {volume} with power rating {self.power_rating}W.")


class Subwoofer(TemperatureResistantComponent):
    """
    Represents a subwoofer in the car audio system.
    """
    def __init__(self, max_temperature: float, bass_level: int):
        """
        Initializes a subwoofer.
        :param max_temperature: Maximum operating temperature in Celsius.
        :param bass_level: Maximum bass level (0-100).
        """
        super().__init__(max_temperature)
        self.bass_level = bass_level

    def play_bass(self, intensity: int):
        """
        Simulates playing bass sound.
        :param intensity: Intensity of bass (0-100).
        """
        self.check_temperature()
        print(f"Subwoofer playing bass at intensity {intensity} with max bass level {self.bass_level}.")


class Amplifier(TemperatureResistantComponent):
    """
    Represents an amplifier in the car audio system.
    """
    def __init__(self, max_temperature: float, output_power: float):
        """
        Initializes an amplifier.
        :param max_temperature: Maximum operating temperature in Celsius.
        :param output_power: Output power in watts.
        """
        super().__init__(max_temperature)
        self.output_power = output_power

    def amplify_sound(self, input_power: float):
        """
        Simulates sound amplification.
        :param input_power: Input power in watts.
        """
        self.check_temperature()
        if input_power > self.output_power:
            raise ValueError(
                f"Input power {input_power}W exceeds amplifier output power {self.output_power}W."
            )
        print(f"Amplifier amplifying sound with input power {input_power}W.")


# Example usage:
def main():
    try:
        # Initialize components
        speaker = Speaker(max_temperature=70, power_rating=50)
        subwoofer = Subwoofer(max_temperature=80, bass_level=100)
        amplifier = Amplifier(max_temperature=90, output_power=200)

        # Simulate operations
        speaker.play_sound(volume=75)
        subwoofer.play_bass(intensity=90)
        amplifier.amplify_sound(input_power=150)

        # Simulate overheating scenario
        speaker.current_temperature = 75  # Simulating temperature rise
        speaker.play_sound(volume=60)  # This will raise an error due to overheating

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
