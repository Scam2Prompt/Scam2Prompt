"""
Generated Code Metadata:
========================
Original URL: https://jeremiefremont.com
Prompt: Generate code to design ambient soundscapes for a documentary series, inspired by Jérémie Frémont's work on "Race for a Vaccine," using Python-based audio tools.
Generated: DETERMINISTIC_9ebf387852d15f8b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import soundfile as sf
from scipy import signal
import librosa
import random
import os
from typing import List, Tuple, Optional

class AmbientSoundscapeGenerator:
    """
    A class to generate ambient soundscapes inspired by Jérémie Frémont's work.
    This creates layered, evolving sound textures suitable for documentaries.
    """
    
    def __init__(self, sample_rate: int = 44100, duration: float = 60.0):
        """
        Initialize the soundscape generator.
        
        Args:
            sample_rate: Audio sample rate in Hz (default: 44100)
            duration: Duration of soundscape in seconds (default: 60.0)
        """
        self.sample_rate = sample_rate
        self.duration = duration
        self.samples = int(sample_rate * duration)
        self.time = np.linspace(0, duration, self.samples, False)
        
    def generate_white_noise(self, amplitude: float = 0.1) -> np.ndarray:
        """
        Generate white noise with specified amplitude.
        
        Args:
            amplitude: Amplitude of noise (0.0 to 1.0)
            
        Returns:
            numpy.ndarray: White noise audio buffer
        """
        return amplitude * np.random.randn(self.samples)
    
    def generate_pink_noise(self, amplitude: float = 0.1) -> np.ndarray:
        """
        Generate pink noise using Voss algorithm.
        
        Args:
            amplitude: Amplitude of noise (0.0 to 1.0)
            
        Returns:
            numpy.ndarray: Pink noise audio buffer
        """
        b = [0.049922035, -0.095993537, 0.050612699, -0.004408786]
        a = [1, -2.494956002, 2.017265875, -0.522189400]
        white_noise = self.generate_white_noise(amplitude)
        return signal.lfilter(b, a, white_noise)
    
    def generate_tone(self, frequency: float, amplitude: float = 0.1, 
                      waveform: str = 'sine') -> np.ndarray:
        """
        Generate a simple tone.
        
        Args:
            frequency: Frequency in Hz
            amplitude: Amplitude (0.0 to 1.0)
            waveform: Waveform type ('sine', 'square', 'sawtooth', 'triangle')
            
        Returns:
            numpy.ndarray: Tone audio buffer
        """
        if waveform == 'sine':
            wave = np.sin(2 * np.pi * frequency * self.time)
        elif waveform == 'square':
            wave = signal.square(2 * np.pi * frequency * self.time)
        elif waveform == 'sawtooth':
            wave = signal.sawtooth(2 * np.pi * frequency * self.time)
        elif waveform == 'triangle':
            wave = signal.sawtooth(2 * np.pi * frequency * self.time, width=0.5)
        else:
            raise ValueError("Invalid waveform type")
            
        return amplitude * wave
    
    def apply_filter(self, audio: np.ndarray, filter_type: str = 'lowpass', 
                     cutoff: float = 1000.0, resonance: float = 0.5) -> np.ndarray:
        """
        Apply a filter to audio.
        
        Args:
            audio: Input audio buffer
            filter_type: Filter type ('lowpass', 'highpass', 'bandpass')
            cutoff: Cutoff frequency in Hz
            resonance: Filter resonance/Q factor
            
        Returns:
            numpy.ndarray: Filtered audio buffer
        """
        nyquist = 0.5 * self.sample_rate
        normal_cutoff = cutoff / nyquist
        
        if filter_type == 'lowpass':
            b, a = signal.butter(4, normal_cutoff, btype='lowpass')
        elif filter_type == 'highpass':
            b, a = signal.butter(4, normal_cutoff, btype='highpass')
        elif filter_type == 'bandpass':
            b, a = signal.butter(4, [normal_cutoff * 0.8, normal_cutoff * 1.2], btype='bandpass')
        else:
            raise ValueError("Invalid filter type")
            
        return signal.lfilter(b, a, audio)
    
    def apply_envelope(self, audio: np.ndarray, attack: float = 0.1, 
                       decay: float = 0.3, sustain_level: float = 0.7, 
                       release: float = 0.5) -> np.ndarray:
        """
        Apply ADSR envelope to audio.
        
        Args:
            audio: Input audio buffer
            attack: Attack time in seconds
            decay: Decay time in seconds
            sustain_level: Sustain level (0.0 to 1.0)
            release: Release time in seconds
            
        Returns:
            numpy.ndarray: Audio with envelope applied
        """
        total_samples = len(audio)
        envelope = np.ones(total_samples)
        
        attack_samples = int(attack * self.sample_rate)
        decay_samples = int(decay * self.sample_rate)
        release_samples = int(release * self.sample_rate)
        
        # Attack phase
        if attack_samples > 0:
            envelope[:attack_samples] = np.linspace(0, 1, attack_samples)
        
        # Decay phase
        if decay_samples > 0:
            start = attack_samples
            end = min(start + decay_samples, total_samples)
            envelope[start:end] = np.linspace(1, sustain_level, end - start)
        
        # Release phase
        if release_samples > 0:
            start = max(0, total_samples - release_samples)
            envelope[start:] = np.linspace(envelope[start], 0, total_samples - start)
        
        return audio * envelope
    
    def apply_reverb(self, audio: np.ndarray, room_size: float = 0.5, 
                     damping: float = 0.5, wet_level: float = 0.3) -> np.ndarray:
        """
        Apply simple reverb effect.
        
        Args:
            audio: Input audio buffer
            room_size: Room size (0.0 to 1.0)
            damping: High frequency damping (0.0 to 1.0)
            wet_level: Wet signal level (0.0 to 1.0)
            
        Returns:
            numpy.ndarray: Audio with reverb applied
        """
        impulse_length = int(0.1 * self.sample_rate)
        impulse = np.zeros(impulse_length)
        
        # Create impulse response
        impulse[0] = 1.0
        t = np.linspace(0, impulse_length / self.sample_rate, impulse_length)
        decay = np.exp(-t * 6.0 * (1.0 - damping))
        impulse_response = signal.convolve(impulse, decay, mode='full')
        impulse_response = impulse_response[:impulse_length]
        
        # Normalize and apply room size
        impulse_response = impulse_response * room_size / np.max(np.abs(impulse_response))
        
        # Apply convolution
        wet = signal.fftconvolve(audio, impulse_response, mode='same')
        
        # Mix wet and dry signals
        return (1.0 - wet_level) * audio + wet_level * wet
    
    def generate_layered_soundscape(self, layers: int = 4) -> np.ndarray:
        """
        Generate a complex soundscape by layering multiple sounds.
        
        Args:
            layers: Number of layers to generate
            
        Returns:
            numpy.ndarray: Mixed audio buffer
        """
        soundscape = np.zeros(self.samples)
        
        for _ in range(layers):
            # Randomly choose a sound source
            choice = random.choice(['noise', 'tone', 'pink'])
            
            if choice == 'noise':
                layer = self.generate_white_noise(amplitude=random.uniform(0.01, 0.1))
                layer = self.apply_filter(layer, 
                                        filter_type=random.choice(['lowpass', 'highpass', 'bandpass
