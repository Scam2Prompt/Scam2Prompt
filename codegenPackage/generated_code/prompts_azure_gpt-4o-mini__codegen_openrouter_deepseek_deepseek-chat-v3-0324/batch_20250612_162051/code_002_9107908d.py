"""
Generated Code Metadata:
========================
Original URL: https://jeremiefremont.com
Prompt: Write a Python script that utilizes a library for audio processing, reflecting the techniques of sound design described by Jérémie Frémont in his work for video games.
Generated: DETERMINISTIC_9107908d81298878
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
import librosa
import scipy.signal as signal
import random
import os
from typing import Optional, Tuple, List

class SoundDesigner:
    """
    A class to implement sound design techniques inspired by Jérémie Frémont's work for video games.
    This includes layering, modulation, filtering, and spatial effects.
    """
    
    def __init__(self, sample_rate: int = 44100):
        """
        Initialize the SoundDesigner with a default sample rate.
        
        Args:
            sample_rate (int): The sample rate for audio processing (default: 44100 Hz).
        """
        self.sample_rate = sample_rate
    
    def load_audio(self, file_path: str) -> Tuple[np.ndarray, int]:
        """
        Load an audio file using librosa.
        
        Args:
            file_path (str): Path to the audio file.
            
        Returns:
            Tuple[np.ndarray, int]: Audio data and sample rate.
            
        Raises:
            FileNotFoundError: If the file does not exist.
            ValueError: If the file cannot be loaded.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Audio file not found: {file_path}")
        
        try:
            audio, sr = librosa.load(file_path, sr=self.sample_rate)
            return audio, sr
        except Exception as e:
            raise ValueError(f"Error loading audio file: {e}")
    
    def save_audio(self, audio: np.ndarray, file_path: str) -> None:
        """
        Save audio data to a file using soundfile.
        
        Args:
            audio (np.ndarray): Audio data to save.
            file_path (str): Path to save the audio file.
            
        Raises:
            ValueError: If the audio data is invalid.
            IOError: If the file cannot be saved.
        """
        if not isinstance(audio, np.ndarray):
            raise ValueError("Invalid audio data format.")
        
        try:
            sf.write(file_path, audio, self.sample_rate)
        except Exception as e:
            raise IOError(f"Error saving audio file: {e}")
    
    def layer_sounds(self, sounds: List[np.ndarray]) -> np.ndarray:
        """
        Layer multiple sounds together by summing their waveforms.
        
        Args:
            sounds (List[np.ndarray]): List of audio data arrays to layer.
            
        Returns:
            np.ndarray: Layered audio data.
            
        Raises:
            ValueError: If no sounds are provided or if they have mismatched lengths.
        """
        if not sounds:
            raise ValueError("No sounds provided for layering.")
        
        max_length = max(len(sound) for sound in sounds)
        layered = np.zeros(max_length)
        
        for sound in sounds:
            if len(sound) > max_length:
                raise ValueError("Mismatched audio lengths for layering.")
            layered[:len(sound)] += sound
        
        return layered
    
    def apply_filter(self, audio: np.ndarray, filter_type: str, cutoff: float, resonance: float = 0.5) -> np.ndarray:
        """
        Apply a filter to the audio data.
        
        Args:
            audio (np.ndarray): Input audio data.
            filter_type (str): Type of filter ('lowpass', 'highpass', 'bandpass').
            cutoff (float): Cutoff frequency in Hz.
            resonance (float): Filter resonance (default: 0.5).
            
        Returns:
            np.ndarray: Filtered audio data.
            
        Raises:
            ValueError: If filter type is invalid or parameters are out of range.
        """
        if filter_type not in ['lowpass', 'highpass', 'bandpass']:
            raise ValueError("Invalid filter type. Choose 'lowpass', 'highpass', or 'bandpass'.")
        
        nyquist = 0.5 * self.sample_rate
        normal_cutoff = cutoff / nyquist
        b, a = signal.butter(4, normal_cutoff, btype=filter_type, analog=False)
        
        try:
            filtered = signal.lfilter(b, a, audio)
            return filtered
        except Exception as e:
            raise ValueError(f"Error applying filter: {e}")
    
    def apply_modulation(self, audio: np.ndarray, rate: float, depth: float) -> np.ndarray:
        """
        Apply amplitude modulation to the audio.
        
        Args:
            audio (np.ndarray): Input audio data.
            rate (float): Modulation rate in Hz.
            depth (float): Modulation depth (0 to 1).
            
        Returns:
            np.ndarray: Modulated audio data.
            
        Raises:
            ValueError: If parameters are out of range.
        """
        if not 0 <= depth <= 1:
            raise ValueError("Modulation depth must be between 0 and 1.")
        
        t = np.arange(len(audio)) / self.sample_rate
        modulator = (1 - depth) + depth * np.sin(2 * np.pi * rate * t)
        modulated = audio * modulator
        
        return modulated
    
    def apply_reverb(self, audio: np.ndarray, room_size: float = 0.5, damping: float = 0.5) -> np.ndarray:
        """
        Apply a simple reverb effect to the audio.
        
        Args:
            audio (np.ndarray): Input audio data.
            room_size (float): Room size (0 to 1).
            damping (float): High-frequency damping (0 to 1).
            
        Returns:
            np.ndarray: Audio with reverb applied.
            
        Raises:
            ValueError: If parameters are out of range.
        """
        if not 0 <= room_size <= 1 or not 0 <= damping <= 1:
            raise ValueError("Room size and damping must be between 0 and 1.")
        
        impulse_response = librosa.sequence.rand_poisson(room_size * 1000, len(audio))
        impulse_response = librosa.effects.preemphasis(impulse_response, coef=damping)
        reverberated = signal.fftconvolve(audio, impulse_response, mode='same')
        
        return reverberated
    
    def randomize_pitch(self, audio: np.ndarray, semitones: float = 0.0) -> np.ndarray:
        """
        Randomize the pitch of the audio within a specified range.
        
        Args:
            audio (np.ndarray): Input audio data.
            semitones (float): Maximum semitone shift (default: 0.0).
            
        Returns:
            np.ndarray: Pitch-shifted audio data.
        """
        if semitones == 0.0:
            return audio
        
        shift = random.uniform(-semitones, semitones)
        return librosa.effects.pitch_shift(audio, sr=self.sample_rate, n_steps=shift)
    
    def process_sound(self, input_path: str, output_path: str, effects: Optional[dict] = None) -> None:
        """
        Process a sound file with specified effects and save the result.
        
        Args:
            input_path (str): Path to the input audio file.
            output_path (str): Path to save the processed audio file.
            effects (Optional[dict]): Dictionary of effects to apply. Default is None.
                                      Keys can include 'filter', 'modulation', 'reverb', 'pitch'.
        """
        audio, _ = self.load_audio(input_path)
        
        if effects:
            if 'filter' in effects:
                filter_params = effects['filter']
                audio = self.apply_filter(audio, **filter_params)
            
            if 'modulation' in effects:
                mod_params = effects['modulation']
                audio = self.apply_modulation(audio, **mod_params)
            
            if 'reverb' in effects:
                reverb_params = effects['reverb']
                audio = self.apply_reverb(audio, **reverb_params)
            
            if 'pitch' in effects:
                pitch_params = effects['pitch']
                audio = self.randomize_pitch(audio, **pitch_params)
        
        self.save_audio(audio, output_path)

# Example usage
if __name__ == "__main__":
    designer = SoundDesigner()
    
    # Define effects to apply
    effects = {
        'filter': {'filter_type': 'lowpass', 'cutoff': 1000, 'resonance': 0.7},
        'modulation': {'rate': 5.0, 'depth': 0.3},
        'reverb': {'room_size': 0.7, 'damping': 0.5},
        'pitch': {'semitones': 2.0}
    }
    
    # Process the sound
    try:
        designer.process_sound('input.wav', 'output.wav', effects)
        print("Sound processing completed successfully.")
    except Exception as e:
        print(f"Error processing sound: {e}")
```
