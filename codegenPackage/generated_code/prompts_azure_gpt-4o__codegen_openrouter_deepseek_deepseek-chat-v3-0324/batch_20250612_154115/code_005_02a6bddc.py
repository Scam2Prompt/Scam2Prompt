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
import random
import time
from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Dict, Optional

class SpeakerType(Enum):
    TWEETER = auto()
    MIDRANGE = auto()
    WOOFER = auto()
    SUBWOOFER = auto()

class AmplifierClass(Enum):
    CLASS_A = auto()
    CLASS_AB = auto()
    CLASS_D = auto()

@dataclass
class Speaker:
    type: SpeakerType
    power_handling: float  # in watts
    impedance: float  # in ohms
    sensitivity: float  # in dB
    is_temperature_resistant: bool

    def play_sound(self, frequency: float, volume: float) -> bool:
        """Simulate playing sound through the speaker."""
        if volume > self.power_handling:
            print(f"Warning: Volume {volume}W exceeds speaker's power handling {self.power_handling}W")
            return False
        
        if self.is_temperature_resistant:
            print(f"Playing {frequency}Hz at {volume}W (Temperature-resistant)")
        else:
            print(f"Playing {frequency}Hz at {volume}W")
        return True

@dataclass
class Amplifier:
    class_type: AmplifierClass
    power_output: float  # in watts
    channels: int
    is_temperature_resistant: bool
    current_temperature: float = 25.0  # in Celsius

    def amplify(self, input_signal: float, channel: int) -> Optional[float]:
        """Amplify the input signal and return the output."""
        if channel >= self.channels:
            print(f"Error: Channel {channel} not available (max {self.channels-1})")
            return None
        
        if self.current_temperature > 80.0 and not self.is_temperature_resistant:
            print("Warning: Amplifier overheating! Performance may degrade.")
            output = input_signal * (self.power_output * 0.7)
        else:
            output = input_signal * self.power_output
        
        self.current_temperature += random.uniform(0.5, 2.0)
        return output

    def cool_down(self, amount: float = 5.0):
        """Reduce the amplifier temperature."""
        self.current_temperature = max(25.0, self.current_temperature - amount)

class CarAudioSystem:
    def __init__(self):
        self.speakers: Dict[str, List[Speaker]] = {
            "front_left": [],
            "front_right": [],
            "rear_left": [],
            "rear_right": [],
        }
        self.subwoofers: List[Speaker] = []
        self.amplifiers: List[Amplifier] = []
        self.temperature: float = 25.0  # ambient temperature in Celsius

    def add_speaker(self, position: str, speaker: Speaker):
        """Add a speaker to a specific position in the car."""
        if position not in self.speakers:
            raise ValueError(f"Invalid speaker position: {position}")
        
        if speaker.type == SpeakerType.SUBWOOFER:
            raise ValueError("Use add_subwoofer() for subwoofers")
            
        self.speakers[position].append(speaker)

    def add_subwoofer(self, subwoofer: Speaker):
        """Add a subwoofer to the system."""
        if subwoofer.type != SpeakerType.SUBWOOFER:
            raise ValueError("Speaker must be a subwoofer")
        self.subwoofers.append(subwoofer)

    def add_amplifier(self, amplifier: Amplifier):
        """Add an amplifier to the system."""
        self.amplifiers.append(amplifier)

    def play_audio(self, frequency: float, volume: float):
        """Play audio through all speakers and subwoofers."""
        if not self.amplifiers:
            raise RuntimeError("No amplifiers in the system")
            
        amplified_signal = self.amplifiers[0].amplify(volume, 0)
        if amplified_signal is None:
            return False

        success = True
        for position, speakers in self.speakers.items():
            for speaker in speakers:
                if not speaker.play_sound(frequency, amplified_signal / len(speakers)):
                    success = False

        for subwoofer in self.subwoofers:
            if frequency < 200:  # Only play low frequencies through subwoofers
                if not subwoofer.play_sound(frequency, amplified_signal / len(self.subwoofers)):
                    success = False

        return success

    def simulate_temperature_change(self, delta: float):
        """Simulate a change in ambient temperature."""
        self.temperature += delta
        for amp in self.amplifiers:
            amp.current_temperature += delta * 0.5  # Amplifiers heat up less than ambient

    def cool_down_system(self):
        """Cool down all components."""
        self.temperature = max(25.0, self.temperature - 10.0)
        for amp in self.amplifiers:
            amp.cool_down()

def create_temperature_resistant_speaker(speaker_type: SpeakerType) -> Speaker:
    """Factory method to create temperature-resistant speakers."""
    specs = {
        SpeakerType.TWEETER: (50, 4, 92),
        SpeakerType.MIDRANGE: (100, 4, 89),
        SpeakerType.WOOFER: (150, 4, 87),
        SpeakerType.SUBWOOFER: (300, 2, 85)
    }
    power, impedance, sensitivity = specs[speaker_type]
    return Speaker(speaker_type, power, impedance, sensitivity, True)

def create_temperature_resistant_amplifier() -> Amplifier:
    """Factory method to create temperature-resistant amplifier."""
    return Amplifier(AmplifierClass.CLASS_D, 500, 4, True)

def demo_car_audio_system():
    """Demonstrate the car audio system functionality."""
    system = CarAudioSystem()
    
    # Add temperature-resistant components
    system.add_speaker("front_left", create_temperature_resistant_speaker(SpeakerType.TWEETER))
    system.add_speaker("front_left", create_temperature_resistant_speaker(SpeakerType.MIDRANGE))
    system.add_speaker("front_right", create_temperature_resistant_speaker(SpeakerType.TWEETER))
    system.add_speaker("front_right", create_temperature_resistant_speaker(SpeakerType.MIDRANGE))
    system.add_speaker("rear_left", create_temperature_resistant_speaker(SpeakerType.WOOFER))
    system.add_speaker("rear_right", create_temperature_resistant_speaker(SpeakerType.WOOFER))
    system.add_subwoofer(create_temperature_resistant_speaker(SpeakerType.SUBWOOFER))
    system.add_amplifier(create_temperature_resistant_amplifier())
    
    # Simulate audio playback
    print("Playing audio at normal temperature:")
    system.play_audio(1000, 50)
    system.play_audio(80, 100)
    
    # Simulate high temperature environment
    print("\nSimulating high temperature environment:")
    system.simulate_temperature_change(40)  # +40°C
    system.play_audio(1000, 50)
    system.play_audio(80, 100)
    
    # Cool down and play again
    print("\nCooling down system and playing again:")
    system.cool_down_system()
    system.play_audio(1000, 50)
    system.play_audio(80, 100)

if __name__ == "__main__":
    demo_car_audio_system()
```
