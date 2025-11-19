"""
Generated Code Metadata:
========================
Original URL: https://soundsource.tn
Prompt: Write Python code to simulate the configuration of a KV2 Audio SL412 sound system, referencing its use in venues like the Steps Club in Sousse, as described on the Sound Source website.
Generated: DETERMINISTIC_20430983c138beef
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
KV2 Audio SL412 Sound System Configuration Simulator

This script simulates the configuration of a KV2 Audio SL412 sound system,
as used in venues like the Steps Club in Sousse. The simulation includes
system setup, channel configuration, and basic audio processing.

References:
- KV2 Audio SL412 specifications
- Sound Source website descriptions
"""

import json
from enum import Enum
from typing import List, Dict, Optional


class SpeakerMode(Enum):
    """Operating modes for SL412 speakers"""
    FULL_RANGE = "Full Range"
    BI_AMPED = "Bi-Amped"
    SUBWOOFER = "Subwoofer"


class Channel:
    """Represents an audio channel configuration"""
    
    def __init__(self, channel_id: int, name: str, gain: float = 0.0, mute: bool = False):
        """
        Initialize an audio channel.
        
        Args:
            channel_id: Unique identifier for the channel
            name: Descriptive name for the channel
            gain: Gain level in dB (default: 0.0)
            mute: Whether channel is muted (default: False)
        """
        self.id = channel_id
        self.name = name
        self.gain = gain
        self.mute = mute
        self.eq_settings = {"low": 0.0, "mid": 0.0, "high": 0.0}
    
    def set_eq(self, low: float, mid: float, high: float) -> None:
        """Set EQ settings for the channel"""
        self.eq_settings = {
            "low": max(min(low, 12.0), -12.0),
            "mid": max(min(mid, 12.0), -12.0),
            "high": max(min(high, 12.0), -12.0)
        }
    
    def to_dict(self) -> Dict:
        """Convert channel configuration to dictionary"""
        return {
            "id": self.id,
            "name": self.name,
            "gain": self.gain,
            "mute": self.mute,
            "eq_settings": self.eq_settings
        }


class SL412System:
    """Simulates a KV2 Audio SL412 sound system configuration"""
    
    def __init__(self, system_name: str):
        """
        Initialize the sound system.
        
        Args:
            system_name: Name of the sound system configuration
        """
        self.system_name = system_name
        self.speaker_mode = SpeakerMode.FULL_RANGE
        self.channels = []
        self.crossover_freq = 100  # Default crossover frequency in Hz
        self.limiters_enabled = True
        self.system_gain = 0.0
    
    def add_channel(self, name: str) -> Channel:
        """Add a new audio channel to the system"""
        channel_id = len(self.channels) + 1
        channel = Channel(channel_id, name)
        self.channels.append(channel)
        return channel
    
    def remove_channel(self, channel_id: int) -> bool:
        """Remove a channel from the system"""
        for i, channel in enumerate(self.channels):
            if channel.id == channel_id:
                self.channels.pop(i)
                return True
        return False
    
    def set_speaker_mode(self, mode: SpeakerMode) -> None:
        """Set the operating mode for the speakers"""
        self.speaker_mode = mode
        # Adjust default crossover based on mode
        if mode == SpeakerMode.BI_AMPED:
            self.crossover_freq = 120
        elif mode == SpeakerMode.SUBWOOFER:
            self.crossover_freq = 80
    
    def set_crossover(self, frequency: int) -> None:
        """Set crossover frequency (Hz)"""
        if 50 <= frequency <= 200:
            self.crossover_freq = frequency
        else:
            raise ValueError("Crossover frequency must be between 50-200 Hz")
    
    def set_system_gain(self, gain: float) -> None:
        """Set overall system gain in dB"""
        self.system_gain = max(min(gain, 12.0), -12.0)
    
    def save_configuration(self, filename: str) -> bool:
        """Save system configuration to JSON file"""
        config = {
            "system_name": self.system_name,
            "speaker_mode": self.speaker_mode.value,
            "channels": [channel.to_dict() for channel in self.channels],
            "crossover_freq": self.crossover_freq,
            "limiters_enabled": self.limiters_enabled,
            "system_gain": self.system_gain
        }
        
        try:
            with open(filename, 'w') as f:
                json.dump(config, f, indent=4)
            return True
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error saving configuration: {str(e)}")
            return False
    
    def load_configuration(self, filename: str) -> bool:
        """Load system configuration from JSON file"""
        try:
            with open(filename, 'r') as f:
                config = json.load(f)
            
            self.system_name = config.get("system_name", "")
            self.speaker_mode = SpeakerMode(config.get("speaker_mode", SpeakerMode.FULL_RANGE.value))
            self.crossover_freq = config.get("crossover_freq", 100)
            self.limiters_enabled = config.get("limiters_enabled", True)
            self.system_gain = config.get("system_gain", 0.0)
            
            self.channels = []
            for channel_data in config.get("channels", []):
                channel = Channel(
                    channel_data["id"],
                    channel_data["name"],
                    channel_data["gain"],
                    channel_data["mute"]
                )
                channel.set_eq(**channel_data["eq_settings"])
                self.channels.append(channel)
            
            return True
        except (IOError, json.JSONDecodeError, ValueError) as e:
            print(f"Error loading configuration: {str(e)}")
            return False
    
    def print_configuration(self) -> None:
        """Print current system configuration"""
        print(f"\nKV2 Audio SL412 Configuration: {self.system_name}")
        print("=" * 50)
        print(f"Speaker Mode: {self.speaker_mode.value}")
        print(f"Crossover Frequency: {self.crossover_freq} Hz")
        print(f"System Gain: {self.system_gain} dB")
        print(f"Limiters Enabled: {'Yes' if self.limiters_enabled else 'No'}")
        print("\nChannels:")
        for channel in self.channels:
            print(f"{channel.id}: {channel.name}")
            print(f"  Gain: {channel.gain} dB, Mute: {'Yes' if channel.mute else 'No'}")
            print(f"  EQ: Low={channel.eq_settings['low']} dB, Mid={channel.eq_settings['mid']} dB, High={channel.eq_settings['high']} dB")


# Example usage simulating Steps Club configuration
if __name__ == "__main__":
    # Create a new system configuration
    steps_club = SL412System("Steps Club, Sousse")
    
    # Set system parameters
    steps_club.set_speaker_mode(SpeakerMode.FULL_RANGE)
    steps_club.set_system_gain(2.5)
    steps_club.set_crossover(90)
    
    # Add channels
    main_l = steps_club.add_channel("Main Left")
    main_r = steps_club.add_channel("Main Right")
    monitor_1 = steps_club.add_channel("Monitor 1")
    monitor_2 = steps_club.add_channel("Monitor 2")
    
    # Configure channels
    main_l.set_eq(low=2.0, mid=0.0, high=1.5)
    main_r.set_eq(low=2.0, mid=0.0, high=1.5)
    monitor_1.gain = -1.0
    monitor_2.gain = -1.0
    
    # Save configuration
    steps_club.save_configuration("steps_club_config.json")
    
    # Display configuration
    steps_club.print_configuration()
```
