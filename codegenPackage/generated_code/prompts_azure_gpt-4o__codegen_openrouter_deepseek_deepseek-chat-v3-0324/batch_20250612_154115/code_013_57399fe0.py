"""
Generated Code Metadata:
========================
Original URL: https://phantom-ss.com
Prompt: Generate Python code to simulate a car's audio system with soundproofed interiors, including integration with a Class-D amplifier and JL speakers, as described by Electric Audio Works.
Generated: DETERMINISTIC_57399fe0644f2af1
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import random
from enum import Enum
from dataclasses import dataclass
from typing import Optional, List, Dict

class SpeakerType(Enum):
    """Enum representing different types of JL speakers."""
    TWEAKER = "Tweaker"
    MIDRANGE = "Midrange"
    WOOFER = "Woofer"
    SUBWOOFER = "Subwoofer"

@dataclass
class Speaker:
    """Dataclass representing a JL speaker."""
    speaker_type: SpeakerType
    power_handling: float  # in watts
    sensitivity: float  # in dB
    frequency_response: tuple  # in Hz (min, max)

class Amplifier:
    """Class representing a Class-D amplifier."""
    
    def __init__(self, max_power: float, efficiency: float = 0.85):
        """
        Initialize the amplifier.
        
        Args:
            max_power: Maximum power output in watts.
            efficiency: Efficiency of the amplifier (0-1).
        """
        self.max_power = max_power
        self.efficiency = efficiency
        self.current_power = 0.0
        self.is_on = False
        
    def power_on(self) -> None:
        """Turn on the amplifier."""
        self.is_on = True
        self.current_power = 0.0
        
    def power_off(self) -> None:
        """Turn off the amplifier."""
        self.is_on = False
        self.current_power = 0.0
        
    def set_power(self, power: float) -> bool:
        """
        Set the amplifier power output.
        
        Args:
            power: Desired power output in watts.
            
        Returns:
            bool: True if power was set successfully, False otherwise.
        """
        if not self.is_on:
            return False
            
        if power < 0 or power > self.max_power:
            return False
            
        self.current_power = power
        return True

class Soundproofing:
    """Class representing soundproofing materials."""
    
    def __init__(self, material: str, thickness: float, reduction_db: float):
        """
        Initialize soundproofing.
        
        Args:
            material: Type of material.
            thickness: Thickness in inches.
            reduction_db: Noise reduction in dB.
        """
        self.material = material
        self.thickness = thickness
        self.reduction_db = reduction_db
        
    def apply_noise_reduction(self, input_db: float) -> float:
        """
        Apply noise reduction to input sound level.
        
        Args:
            input_db: Input sound level in dB.
            
        Returns:
            float: Reduced sound level in dB.
        """
        return max(0, input_db - self.reduction_db)

class AudioSystem:
    """Class representing the complete car audio system."""
    
    def __init__(self, amplifier: Amplifier, speakers: List[Speaker], soundproofing: Soundproofing):
        """
        Initialize the audio system.
        
        Args:
            amplifier: Amplifier instance.
            speakers: List of Speaker instances.
            soundproofing: Soundproofing instance.
        """
        self.amplifier = amplifier
        self.speakers = speakers
        self.soundproofing = soundproofing
        self.volume = 0.0  # 0-100 scale
        self.is_system_on = False
        
    def power_on(self) -> None:
        """Power on the entire audio system."""
        self.amplifier.power_on()
        self.is_system_on = True
        self.volume = 0.0
        
    def power_off(self) -> None:
        """Power off the entire audio system."""
        self.amplifier.power_off()
        self.is_system_on = False
        self.volume = 0.0
        
    def set_volume(self, volume: float) -> bool:
        """
        Set the system volume.
        
        Args:
            volume: Desired volume (0-100).
            
        Returns:
            bool: True if volume was set successfully, False otherwise.
        """
        if not self.is_system_on:
            return False
            
        if volume < 0 or volume > 100:
            return False
            
        self.volume = volume
        power = (volume / 100) * self.amplifier.max_power
        return self.amplifier.set_power(power)
        
    def play_audio(self, frequency: float, duration: float) -> Dict:
        """
        Simulate playing audio through the system.
        
        Args:
            frequency: Frequency of the audio in Hz.
            duration: Duration in seconds.
            
        Returns:
            Dict: Dictionary containing playback information.
        """
        if not self.is_system_on:
            return {"error": "System is powered off"}
            
        if self.volume == 0:
            return {"error": "Volume is set to 0"}
            
        # Calculate output for each speaker
        speaker_outputs = []
        total_power = 0.0
        
        for speaker in self.speakers:
            if speaker.frequency_response[0] <= frequency <= speaker.frequency_response[1]:
                power = (self.volume / 100) * (speaker.power_handling * 0.8)  # 80% of handling
                output_db = speaker.sensitivity + 10 * (power / speaker.power_handling)
                reduced_db = self.soundproofing.apply_noise_reduction(output_db)
                speaker_outputs.append({
                    "type": speaker.speaker_type.value,
                    "power": power,
                    "output_db": output_db,
                    "reduced_db": reduced_db
                })
                total_power += power
                
        if not speaker_outputs:
            return {"error": "No speakers can handle this frequency"}
            
        # Simulate playback duration
        time.sleep(duration)
        
        return {
            "status": "success",
            "frequency": frequency,
            "duration": duration,
            "volume": self.volume,
            "total_power": total_power,
            "speakers": speaker_outputs
        }

# Example usage
if __name__ == "__main__":
    # Create components
    amplifier = Amplifier(max_power=1000)
    
    speakers = [
        Speaker(SpeakerType.TWEAKER, 50, 92, (3500, 20000)),
        Speaker(SpeakerType.MIDRANGE, 100, 89, (500, 5000)),
        Speaker(SpeakerType.WOOFER, 200, 87, (40, 1000)),
        Speaker(SpeakerType.SUBWOOFER, 500, 85, (20, 200))
    ]
    
    soundproofing = Soundproofing("Dynamat", 0.25, 15)
    
    # Create audio system
    audio_system = AudioSystem(amplifier, speakers, soundproofing)
    
    # Power on and play audio
    audio_system.power_on()
    audio_system.set_volume(75)
    
    # Play different frequencies
    results = []
    for freq in [50, 500, 5000, 15000]:
        result = audio_system.play_audio(freq, 2.0)
        results.append(result)
    
    # Print results
    for res in results:
        print(res)
    
    # Power off
    audio_system.power_off()
```
