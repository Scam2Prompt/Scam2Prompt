"""
Generated Code Metadata:
========================
Original URL: https://www.projectortechnology.gr
Prompt: Write code to simulate the acoustic optimization process for audio systems in a room, as required for the sound systems offered by Projector Technology.
Generated: DETERMINISTIC_f585818535ac9116
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
from scipy.signal import windows
import random
from typing import List, Tuple, Dict, Optional

class RoomAcousticsSimulator:
    """
    Simulates and optimizes acoustic properties of a room for audio systems.
    """
    
    def __init__(self, room_dimensions: Tuple[float, float, float], 
                 sampling_rate: int = 44100, 
                 max_frequency: int = 20000):
        """
        Initialize the room acoustics simulator.
        
        Args:
            room_dimensions: Tuple of (length, width, height) in meters
            sampling_rate: Audio sampling rate in Hz
            max_frequency: Maximum frequency to consider in Hz
        """
        self.length, self.width, self.height = room_dimensions
        self.sampling_rate = sampling_rate
        self.max_frequency = max_frequency
        self.absorption_coefficients = self._default_absorption_coefficients()
        self.speaker_positions = []
        self.listener_position = None
        
    def _default_absorption_coefficients(self) -> Dict[str, float]:
        """Return default absorption coefficients for common materials."""
        return {
            'concrete': 0.02,
            'wood': 0.10,
            'glass': 0.04,
            'carpet': 0.30,
            'curtains': 0.50,
            'acoustic_panel': 0.80
        }
    
    def set_surface_materials(self, materials: Dict[str, str]) -> None:
        """
        Set materials for room surfaces.
        
        Args:
            materials: Dict with keys 'floor', 'ceiling', 'front_wall', 
                      'back_wall', 'left_wall', 'right_wall' and values 
                      from absorption_coefficients keys
        """
        self.surface_materials = materials
        
    def add_speaker(self, position: Tuple[float, float, float], 
                   frequency_response: Optional[np.ndarray] = None) -> None:
        """
        Add a speaker to the room.
        
        Args:
            position: (x, y, z) coordinates in meters
            frequency_response: Optional frequency response curve (numpy array)
        """
        self.speaker_positions.append(position)
        if frequency_response is None:
            # Default flat frequency response
            frequency_response = np.ones(self.max_frequency // 100)
        self.speaker_responses = frequency_response
        
    def set_listener_position(self, position: Tuple[float, float, float]) -> None:
        """Set the listener's position in the room."""
        self.listener_position = position
        
    def calculate_room_modes(self) -> Dict[str, List[float]]:
        """
        Calculate room modes (eigenfrequencies) using the room dimensions.
        
        Returns:
            Dictionary with axial, tangential, and oblique modes
        """
        c = 343  # Speed of sound in air (m/s)
        modes = {
            'axial': [],
            'tangential': [],
            'oblique': []
        }
        
        # Calculate axial modes (one dimension)
        for n in range(1, 6):
            modes['axial'].append((n * c) / (2 * self.length))
            modes['axial'].append((n * c) / (2 * self.width))
            modes['axial'].append((n * c) / (2 * self.height))
        
        # Calculate tangential modes (two dimensions)
        for nx in range(1, 4):
            for ny in range(1, 4):
                if nx == 0 and ny == 0:
                    continue
                freq = (c / 2) * np.sqrt((nx / self.length)**2 + (ny / self.width)**2)
                modes['tangential'].append(freq)
                
                freq = (c / 2) * np.sqrt((nx / self.length)**2 + (ny / self.height)**2)
                modes['tangential'].append(freq)
                
                freq = (c / 2) * np.sqrt((nx / self.width)**2 + (ny / self.height)**2)
                modes['tangential'].append(freq)
        
        # Calculate oblique modes (three dimensions)
        for nx in range(1, 3):
            for ny in range(1, 3):
                for nz in range(1, 3):
                    if nx == 0 and ny == 0 and nz == 0:
                        continue
                    freq = (c / 2) * np.sqrt(
                        (nx / self.length)**2 + 
                        (ny / self.width)**2 + 
                        (nz / self.height)**2
                    )
                    modes['oblique'].append(freq)
        
        # Remove duplicates and sort
        for mode_type in modes:
            modes[mode_type] = sorted(list(set(modes[mode_type])))
            
        return modes
    
    def calculate_reverberation_time(self, frequency: float = 1000) -> float:
        """
        Calculate RT60 (reverberation time) using Sabine's formula.
        
        Args:
            frequency: Frequency to calculate RT60 for (Hz)
            
        Returns:
            Reverberation time in seconds
        """
        if not hasattr(self, 'surface_materials'):
            raise ValueError("Surface materials not set. Call set_surface_materials() first.")
        
        # Get absorption coefficient for the given frequency
        alpha = 0
        total_area = 0
        
        # Calculate total absorption in the room
        surfaces = {
            'floor': self.length * self.width,
            'ceiling': self.length * self.width,
            'front_wall': self.width * self.height,
            'back_wall': self.width * self.height,
            'left_wall': self.length * self.height,
            'right_wall': self.length * self.height
        }
        
        total_absorption = 0
        for surface, area in surfaces.items():
            material = self.surface_materials[surface]
            absorption = self.absorption_coefficients[material]
            total_absorption += area * absorption
        
        # Sabine's formula
        volume = self.length * self.width * self.height
        rt60 = (0.161 * volume) / total_absorption
        
        return rt60
    
    def simulate_impulse_response(self, duration: float = 1.0) -> np.ndarray:
        """
        Simulate the room impulse response (RIR).
        
        Args:
            duration: Duration of impulse response in seconds
            
        Returns:
            Numpy array containing the impulse response
        """
        if not self.speaker_positions:
            raise ValueError("No speakers added. Call add_speaker() first.")
        if self.listener_position is None:
            raise ValueError("Listener position not set. Call set_listener_position() first.")
            
        # Basic parameters
        num_samples = int(duration * self.sampling_rate)
        impulse = np.zeros(num_samples)
        
        # Direct sound arrives first
        speaker_pos = np.array(self.speaker_positions[0])
        listener_pos = np.array(self.listener_position)
        distance = np.linalg.norm(speaker_pos - listener_pos)
        delay_samples = int((distance / 343) * self.sampling_rate)
        
        if delay_samples < num_samples:
            impulse[delay_samples] = 1.0
        
        # Add early reflections (simplified)
        reflection_delays = self._calculate_reflection_delays()
        for delay in reflection_delays:
            delay_samples = int(delay * self.sampling_rate)
            if delay_samples < num_samples:
                impulse[delay_samples] = 0.5 * random.uniform(0.7, 0.9)
        
        # Add reverberation tail (exponential decay)
        rt60 = self.calculate_reverberation_time()
        decay_rate = 60.0 / rt60  # dB/s
        decay_per_sample = decay_rate / self.sampling_rate
        
        for i in range(num_samples):
            if impulse[i] > 0:
                continue
            time = i / self.sampling_rate
            if time > 0.05:  # After early reflections
                impulse[i] = np.exp(-decay_per_sample * time) * random.uniform(0, 0.2)
        
        return impulse
    
    def _calculate_reflection_delays(self) -> List[float]:
        """Calculate delays for major early reflections."""
        delays = []
        speaker_pos = np.array(self.speaker_positions[0])
        listener_pos = np.array(self.listener_position)
        
        # Direct path already handled in simulate_impulse_response
        # First-order reflections (6 surfaces)
        for dim in range(3):
            for direction in [-1, 1]:
                # Calculate image source position
                image_pos = speaker_pos.copy()
                room_dim = [self.length, self.width, self.height][dim]
                image_pos[dim] = (2 * room_dim * (direction > 0)) - speaker_pos[dim]
                
                # Calculate distance and delay
                distance = np.linalg.norm(image_pos - listener_pos)
                delays
