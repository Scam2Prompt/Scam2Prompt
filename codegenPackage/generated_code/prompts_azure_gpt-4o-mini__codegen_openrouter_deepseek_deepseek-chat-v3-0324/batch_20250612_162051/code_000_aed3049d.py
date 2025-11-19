"""
Generated Code Metadata:
========================
Original URL: https://jeremiefremont.com
Prompt: Generate a code snippet for a sound design tool that can blend acoustic and electronic sounds, inspired by Jérémie Frémont's unique approach to composition.
Generated: DETERMINISTIC_aed3049d3351a17d
Batch ID: 20250612_162051
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
from scipy.io import wavfile
import os
import random
import logging
from typing import Tuple, List, Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class SoundBlender:
    """
    A tool for blending acoustic and electronic sounds with various processing techniques.
    Inspired by Jérémie Frémont's unique approach to composition.
    """
    
    def __init__(self, sample_rate: int = 44100):
        """
        Initialize the SoundBlender with a default sample rate.
        
        Args:
            sample_rate: The sample rate to use for audio processing (default: 44100 Hz)
        """
        self.sample_rate = sample_rate
        self.max_amplitude = 0.9  # To prevent clipping
        
    def load_audio(self, file_path: str) -> Tuple[np.ndarray, int]:
        """
        Load an audio file and return its data and sample rate.
        
        Args:
            file_path: Path to the audio file
            
        Returns:
            Tuple of (audio_data, sample_rate)
            
        Raises:
            FileNotFoundError: If file doesn't exist
            ValueError: If file format is unsupported
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Audio file not found: {file_path}")
            
        try:
            audio_data, sample_rate = sf.read(file_path, always_2d=True)
            if audio_data.ndim > 2:
                raise ValueError("Only mono or stereo files are supported")
            return audio_data, sample_rate
        except Exception as e:
            raise ValueError(f"Error loading audio file: {str(e)}")
    
    def normalize(self, audio_data: np.ndarray) -> np.ndarray:
        """
        Normalize audio data to prevent clipping.
        
        Args:
            audio_data: Input audio data
            
        Returns:
            Normalized audio data
        """
        max_val = np.max(np.abs(audio_data))
        if max_val > 0:
            return audio_data * (self.max_amplitude / max_val)
        return audio_data
    
    def blend_sounds(
        self,
        acoustic_path: str,
        electronic_path: str,
        blend_ratio: float = 0.5,
        time_stretch: Optional[float] = None,
        pitch_shift: Optional[float] = None,
        output_path: str = "blended_output.wav"
    ) -> None:
        """
        Blend acoustic and electronic sounds with optional processing.
        
        Args:
            acoustic_path: Path to acoustic sound file
            electronic_path: Path to electronic sound file
            blend_ratio: Ratio of blending (0.0 = all acoustic, 1.0 = all electronic)
            time_stretch: Optional time stretch factor (None for no stretching)
            pitch_shift: Optional pitch shift in semitones (None for no shift)
            output_path: Path to save the blended output
            
        Raises:
            ValueError: If blend_ratio is not between 0 and 1
        """
        if not 0 <= blend_ratio <= 1:
            raise ValueError("Blend ratio must be between 0 and 1")
            
        try:
            # Load both audio files
            acoustic, ac_sr = self.load_audio(acoustic_path)
            electronic, el_sr = self.load_audio(electronic_path)
            
            # Resample if needed to match sample rates
            if ac_sr != self.sample_rate:
                acoustic = signal.resample(acoustic, int(len(acoustic) * self.sample_rate / ac_sr))
            if el_sr != self.sample_rate:
                electronic = signal.resample(electronic, int(len(electronic) * self.sample_rate / el_sr))
            
            # Apply time stretching if requested
            if time_stretch is not None:
                acoustic = self._time_stretch(acoustic, time_stretch)
                electronic = self._time_stretch(electronic, time_stretch)
            
            # Apply pitch shifting if requested
            if pitch_shift is not None:
                acoustic = self._pitch_shift(acoustic, pitch_shift)
                electronic = self._pitch_shift(electronic, pitch_shift)
            
            # Match lengths by zero-padding the shorter one
            max_len = max(len(acoustic), len(electronic))
            if len(acoustic) < max_len:
                acoustic = np.pad(acoustic, ((0, max_len - len(acoustic)), (0, 0)), mode='constant')
            if len(electronic) < max_len:
                electronic = np.pad(electronic, ((0, max_len - len(electronic)), (0, 0)), mode='constant')
            
            # Blend the sounds
            blended = (1 - blend_ratio) * acoustic + blend_ratio * electronic
            
            # Normalize and save
            blended = self.normalize(blended)
            sf.write(output_path, blended, self.sample_rate)
            logger.info(f"Successfully saved blended audio to {output_path}")
            
        except Exception as e:
            logger.error(f"Error blending sounds: {str(e)}")
            raise
    
    def _time_stretch(self, audio_data: np.ndarray, factor: float) -> np.ndarray:
        """
        Simple time stretching using resampling.
        
        Args:
            audio_data: Input audio data
            factor: Stretch factor (>1 slows down, <1 speeds up)
            
        Returns:
            Time-stretched audio data
        """
        num_samples = int(len(audio_data) * factor)
        return signal.resample(audio_data, num_samples)
    
    def _pitch_shift(self, audio_data: np.ndarray, semitones: float) -> np.ndarray:
        """
        Simple pitch shifting using resampling.
        
        Args:
            audio_data: Input audio data
            semitones: Number of semitones to shift
            
        Returns:
            Pitch-shifted audio data
        """
        factor = 2 ** (semitones / 12)
        return signal.resample(audio_data, int(len(audio_data) / factor))
    
    def granular_synthesis(
        self,
        audio_path: str,
        grain_size_ms: int = 50,
        density: float = 0.5,
        randomness: float = 0.3,
        output_path: str = "granular_output.wav"
    ) -> None:
        """
        Apply granular synthesis to an audio file.
        
        Args:
            audio_path: Path to input audio file
            grain_size_ms: Size of each grain in milliseconds
            density: Density of grains (0-1)
            randomness: Randomness in grain placement (0-1)
            output_path: Path to save the output
        """
        try:
            audio_data, sr = self.load_audio(audio_path)
            if sr != self.sample_rate:
                audio_data = signal.resample(audio_data, int(len(audio_data) * self.sample_rate / sr))
            
            grain_size = int(self.sample_rate * grain_size_ms / 1000)
            output_length = len(audio_data)
            output = np.zeros_like(audio_data)
            
            # Calculate number of grains based on density
            num_grains = int(density * (output_length / grain_size))
            
            for _ in range(num_grains):
                # Random position with some randomness
                pos = int(random.uniform(0, 1) * randomness * output_length)
                pos = min(pos, output_length - grain_size - 1)
                
                # Extract grain
                grain = audio_data[pos:pos+grain_size]
                
                # Apply window function
                window = np.hanning(grain_size)
                if grain.ndim == 2:  # stereo
                    window = window[:, np.newaxis]
                grain = grain * window
                
                # Random output position
                out_pos = int(random.uniform(0, 1) * output_length)
                out_pos = min(out_pos, output_length - grain_size - 1)
                
                # Overlap-add the grain
                output[out_pos:out_pos+grain_size] += grain
            
            # Normalize and save
            output = self.normalize(output)
            sf.write(output_path, output, self.sample_rate)
            logger.info(f"Successfully saved granular synthesis output to {output_path}")
            
        except Exception as e:
            logger.error(f"Error in granular synthesis: {str(e)}")
            raise

# Example usage
if __name__ == "__main__":
    blender = SoundBlender()
    
    try:
        # Blend acoustic and electronic sounds
        blender.blend_sounds(
            acoustic_path="acoustic.wav",
            electronic_path="electronic.wav",
            blend_ratio=0.6,
            time_stretch=1.1,
            pitch_shift=2.0,
            output_path="blended.wav"
        )
        
        # Apply granular synthesis
        blender.granular_synthesis(
            audio_path="input.wav",
            grain_size_ms=30,
