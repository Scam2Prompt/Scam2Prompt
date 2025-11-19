"""
Generated Code Metadata:
========================
Original URL: https://soundsource.tn
Prompt: "Develop a system configuration for enhancing the sound experience at a bar or club, similar to the improvements made by Sound Source at CozyBar Club."
Generated: DETERMINISTIC_b96f3eb26947079a
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from dataclasses import dataclass
from typing import Dict, List, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class Speaker:
    """Represents a speaker in the sound system."""
    id: str
    model: str
    power_watts: int
    frequency_range: tuple
    position: tuple  # (x, y, z) coordinates
    channel: int
    is_active: bool = True

@dataclass
class AudioZone:
    """Represents an audio zone with specific sound settings."""
    id: str
    name: str
    speakers: List[str]  # List of speaker IDs
    volume: float  # 0.0 to 1.0
    eq_settings: Dict[str, float]  # EQ bands and their gains
    delay_ms: float = 0.0

class SoundSystemConfig:
    """Main configuration class for the sound enhancement system."""
    
    def __init__(self):
        self.speakers: Dict[str, Speaker] = {}
        self.audio_zones: Dict[str, AudioZone] = {}
        self.global_eq: Dict[str, float] = {
            'low': 0.0,
            'mid': 0.0,
            'high': 0.0
        }
        self.global_volume: float = 0.7
        self.crossover_freq: int = 80  # Hz
    
    def add_speaker(self, speaker: Speaker) -> None:
        """Add a speaker to the system."""
        if speaker.id in self.speakers:
            raise ValueError(f"Speaker with ID {speaker.id} already exists")
        self.speakers[speaker.id] = speaker
        logger.info(f"Added speaker {speaker.id} to the system")
    
    def add_audio_zone(self, zone: AudioZone) -> None:
        """Add an audio zone to the system."""
        if zone.id in self.audio_zones:
            raise ValueError(f"Zone with ID {zone.id} already exists")
        
        # Validate speaker references
        for speaker_id in zone.speakers:
            if speaker_id not in self.speakers:
                raise ValueError(f"Speaker {speaker_id} not found in system")
        
        self.audio_zones[zone.id] = zone
        logger.info(f"Added audio zone {zone.id} to the system")
    
    def remove_speaker(self, speaker_id: str) -> None:
        """Remove a speaker from the system."""
        if speaker_id not in self.speakers:
            raise ValueError(f"Speaker {speaker_id} not found")
        
        # Check if speaker is used in any zones
        for zone in self.audio_zones.values():
            if speaker_id in zone.speakers:
                raise ValueError(
                    f"Cannot remove speaker {speaker_id} as it's used in zone {zone.id}"
                )
        
        del self.speakers[speaker_id]
        logger.info(f"Removed speaker {speaker_id} from the system")
    
    def update_zone_eq(self, zone_id: str, eq_settings: Dict[str, float]) -> None:
        """Update EQ settings for a zone."""
        if zone_id not in self.audio_zones:
            raise ValueError(f"Zone {zone_id} not found")
        self.audio_zones[zone_id].eq_settings = eq_settings
        logger.info(f"Updated EQ settings for zone {zone_id}")
    
    def set_global_volume(self, volume: float) -> None:
        """Set global volume level (0.0 to 1.0)."""
        if not 0.0 <= volume <= 1.0:
            raise ValueError("Volume must be between 0.0 and 1.0")
        self.global_volume = volume
        logger.info(f"Set global volume to {volume}")
    
    def to_json(self) -> str:
        """Serialize configuration to JSON."""
        config_dict = {
            'speakers': {k: v.__dict__ for k, v in self.speakers.items()},
            'audio_zones': {k: v.__dict__ for k, v in self.audio_zones.items()},
            'global_eq': self.global_eq,
            'global_volume': self.global_volume,
            'crossover_freq': self.crossover_freq
        }
        return json.dumps(config_dict, indent=2)
    
    @classmethod
    def from_json(cls, json_str: str) -> 'SoundSystemConfig':
        """Deserialize configuration from JSON."""
        config = cls()
        data = json.loads(json_str)
        
        # Recreate speakers
        for speaker_id, speaker_data in data.get('speakers', {}).items():
            speaker = Speaker(
                id=speaker_id,
                model=speaker_data['model'],
                power_watts=speaker_data['power_watts'],
                frequency_range=tuple(speaker_data['frequency_range']),
                position=tuple(speaker_data['position']),
                channel=speaker_data['channel'],
                is_active=speaker_data.get('is_active', True)
            )
            config.speakers[speaker_id] = speaker
        
        # Recreate audio zones
        for zone_id, zone_data in data.get('audio_zones', {}).items():
            zone = AudioZone(
                id=zone_id,
                name=zone_data['name'],
                speakers=zone_data['speakers'],
                volume=zone_data['volume'],
                eq_settings=zone_data['eq_settings'],
                delay_ms=zone_data.get('delay_ms', 0.0)
            )
            config.audio_zones[zone_id] = zone
        
        # Set global settings
        config.global_eq = data.get('global_eq', config.global_eq)
        config.global_volume = data.get('global_volume', config.global_volume)
        config.crossover_freq = data.get('crossover_freq', config.crossover_freq)
        
        return config

def create_cozybar_config() -> SoundSystemConfig:
    """Create a configuration similar to CozyBar Club's setup."""
    config = SoundSystemConfig()
    
    # Main speakers
    config.add_speaker(Speaker(
        id="main_left",
        model="JBL PRX815",
        power_watts=1500,
        frequency_range=(45, 20000),
        position=(2.5, 0, 2.5),
        channel=1
    ))
    
    config.add_speaker(Speaker(
        id="main_right",
        model="JBL PRX815",
        power_watts=1500,
        frequency_range=(45, 20000),
        position=(7.5, 0, 2.5),
        channel=2
    ))
    
    # Subwoofers
    config.add_speaker(Speaker(
        id="sub1",
        model="JBL PRX818XLF",
        power_watts=2000,
        frequency_range=(30, 120),
        position=(5.0, 0, 1.0),
        channel=3
    ))
    
    # Lounge area speakers
    config.add_speaker(Speaker(
        id="lounge1",
        model="Bose F1 Model 812",
        power_watts=1000,
        frequency_range=(60, 20000),
        position=(1.0, 8.0, 2.0),
        channel=4
    ))
    
    config.add_speaker(Speaker(
        id="lounge2",
        model="Bose F1 Model 812",
        power_watts=1000,
        frequency_range=(60, 20000),
        position=(9.0, 8.0, 2.0),
        channel=5
    ))
    
    # Create audio zones
    config.add_audio_zone(AudioZone(
        id="dance_floor",
        name="Dance Floor",
        speakers=["main_left", "main_right", "sub1"],
        volume=0.8,
        eq_settings={'low': 2.0, 'mid': 0.5, 'high': 1.0},
        delay_ms=5.0
    ))
    
    config.add_audio_zone(AudioZone(
        id="lounge",
        name="Lounge Area",
        speakers=["lounge1", "lounge2"],
        volume=0.6,
        eq_settings={'low': 1.0, 'mid': 0.0, 'high': 0.5}
    ))
    
    # Set global settings
    config.set_global_volume(0.7)
    config.global_eq = {'low': 1.0, 'mid': 0.0, 'high': 0.5}
    config.crossover_freq = 80
    
    return config

# Example usage
if __name__ == "__main__":
    try:
        system_config = create_cozybar_config()
        print("Sound System Configuration:")
        print(system_config
