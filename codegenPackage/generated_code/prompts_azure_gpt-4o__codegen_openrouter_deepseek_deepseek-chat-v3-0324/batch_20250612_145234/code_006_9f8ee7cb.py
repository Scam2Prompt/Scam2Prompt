"""
Generated Code Metadata:
========================
Original URL: https://www.prointegrationfuture.asia
Prompt: Create a Python program to simulate a connected sensory journey using AV and lighting systems, inspired by the demonstrations at Pro Integration Future Asia.
Generated: DETERMINISTIC_9f8ee7cbf3ae40ab
Batch ID: 20250612_145234
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
import threading
from enum import Enum
import logging
from dataclasses import dataclass

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class AVSystemState(Enum):
    """Enum representing possible states of the AV system."""
    IDLE = 0
    PLAYING = 1
    PAUSED = 2
    STOPPED = 3

class LightingSystemState(Enum):
    """Enum representing possible states of the lighting system."""
    OFF = 0
    AMBIENT = 1
    DYNAMIC = 2
    STROBE = 3

@dataclass
class SensoryJourneyConfig:
    """Configuration for the sensory journey simulation."""
    duration: float = 60.0  # in seconds
    av_intensity: float = 0.5  # 0.0 to 1.0
    lighting_intensity: float = 0.5  # 0.0 to 1.0
    transition_speed: float = 1.0  # 0.1 to 5.0

class AVSystem:
    """Class representing the AV system."""
    def __init__(self):
        self.state = AVSystemState.IDLE
        self.current_content = None
        self.volume = 0.5
        
    def play(self, content: str):
        """Play the specified content."""
        if self.state == AVSystemState.PLAYING:
            logger.warning("AV system is already playing content")
            return
            
        self.current_content = content
        self.state = AVSystemState.PLAYING
        logger.info(f"AV system playing: {content}")
        
    def stop(self):
        """Stop the current playback."""
        if self.state == AVSystemState.STOPPED:
            logger.warning("AV system is already stopped")
            return
            
        self.state = AVSystemState.STOPPED
        self.current_content = None
        logger.info("AV system stopped")
        
    def set_volume(self, volume: float):
        """Set the volume level (0.0 to 1.0)."""
        if not 0.0 <= volume <= 1.0:
            raise ValueError("Volume must be between 0.0 and 1.0")
            
        self.volume = volume
        logger.info(f"AV volume set to {volume:.2f}")
        
    def get_state(self) -> AVSystemState:
        """Get the current state of the AV system."""
        return self.state

class LightingSystem:
    """Class representing the lighting system."""
    def __init__(self):
        self.state = LightingSystemState.OFF
        self.brightness = 0.0
        self.color = (1.0, 1.0, 1.0)  # RGB
        
    def set_state(self, state: LightingSystemState):
        """Set the lighting system state."""
        self.state = state
        logger.info(f"Lighting system state changed to {state.name}")
        
    def set_brightness(self, brightness: float):
        """Set the brightness level (0.0 to 1.0)."""
        if not 0.0 <= brightness <= 1.0:
            raise ValueError("Brightness must be between 0.0 and 1.0")
            
        self.brightness = brightness
        logger.info(f"Lighting brightness set to {brightness:.2f}")
        
    def set_color(self, r: float, g: float, b: float):
        """Set the color (RGB values 0.0 to 1.0)."""
        if not all(0.0 <= val <= 1.0 for val in (r, g, b)):
            raise ValueError("Color values must be between 0.0 and 1.0")
            
        self.color = (r, g, b)
        logger.info(f"Lighting color set to R:{r:.2f} G:{g:.2f} B:{b:.2f}")
        
    def get_state(self) -> LightingSystemState:
        """Get the current state of the lighting system."""
        return self.state

class SensoryJourney:
    """Main class for the sensory journey simulation."""
    def __init__(self):
        self.av_system = AVSystem()
        self.lighting_system = LightingSystem()
        self.is_running = False
        self.thread = None
        
    def start(self, config: SensoryJourneyConfig):
        """Start the sensory journey with the given configuration."""
        if self.is_running:
            logger.warning("Sensory journey is already running")
            return
            
        self.is_running = True
        self.thread = threading.Thread(
            target=self._run_journey,
            args=(config,),
            daemon=True
        )
        self.thread.start()
        logger.info("Sensory journey started")
        
    def stop(self):
        """Stop the sensory journey."""
        if not self.is_running:
            logger.warning("Sensory journey is not running")
            return
            
        self.is_running = False
        if self.thread and self.thread.is_alive():
            self.thread.join(timeout=2.0)
            
        self.av_system.stop()
        self.lighting_system.set_state(LightingSystemState.OFF)
        logger.info("Sensory journey stopped")
        
    def _run_journey(self, config: SensoryJourneyConfig):
        """Internal method to run the sensory journey."""
        try:
            # Initialize systems
            self.av_system.play("Ambient Soundscape")
            self.av_system.set_volume(config.av_intensity)
            
            self.lighting_system.set_state(LightingSystemState.AMBIENT)
            self.lighting_system.set_brightness(config.lighting_intensity)
            
            start_time = time.time()
            elapsed = 0.0
            
            while elapsed < config.duration and self.is_running:
                elapsed = time.time() - start_time
                progress = elapsed / config.duration
                
                # Dynamic adjustments based on journey progress
                self._adjust_av(progress, config)
                self._adjust_lighting(progress, config)
                
                time.sleep(0.1)  # Control update rate
                
        except Exception as e:
            logger.error(f"Error during sensory journey: {str(e)}")
            self.stop()
            
    def _adjust_av(self, progress: float, config: SensoryJourneyConfig):
        """Adjust AV system based on journey progress."""
        # Example: Vary volume and content based on progress
        if progress < 0.3:
            volume = config.av_intensity * 0.7
            if self.av_system.current_content != "Ambient Soundscape":
                self.av_system.play("Ambient Soundscape")
        elif progress < 0.7:
            volume = config.av_intensity * 1.2
            if self.av_system.current_content != "Rhythmic Patterns":
                self.av_system.play("Rhythmic Patterns")
        else:
            volume = config.av_intensity * 0.9
            if self.av_system.current_content != "Crescendo Finale":
                self.av_system.play("Crescendo Finale")
                
        self.av_system.set_volume(min(1.0, volume))
        
    def _adjust_lighting(self, progress: float, config: SensoryJourneyConfig):
        """Adjust lighting system based on journey progress."""
        # Example: Vary lighting based on progress
        if progress < 0.2:
            self.lighting_system.set_state(LightingSystemState.AMBIENT)
            self.lighting_system.set_brightness(config.lighting_intensity * 0.6)
            self.lighting_system.set_color(0.8, 0.6, 0.9)  # Soft purple
        elif progress < 0.5:
            self.lighting_system.set_state(LightingSystemState.DYNAMIC)
            self.lighting_system.set_brightness(config.lighting_intensity * 0.9)
            self.lighting_system.set_color(0.2, 0.8, 0.9)  # Cool blue
        elif progress < 0.8:
            self.lighting_system.set_state(LightingSystemState.DYNAMIC)
            self.lighting_system.set_brightness(config.lighting_intensity * 1.1)
            self.lighting_system.set_color(0.9, 0.7, 0.2)  # Warm orange
        else:
            self.lighting_system.set_state(LightingSystemState.STROBE)
            self.lighting_system.set_brightness(config.lighting_intensity * 1.3)
            self.lighting_system.set_color(1.0, 1.0, 1.0)  # Bright white

def main():
    """Main function to demonstrate the sensory journey."""
    try:
        # Create and configure the sensory journey
        journey = SensoryJourney()
        config = SensoryJourneyConfig(
            duration=30.0,  # Shorter
