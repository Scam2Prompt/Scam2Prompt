"""
Generated Code Metadata:
========================
Original URL: https://jeremiefremont.com
Prompt: Suggest tools or libraries for creating unique sound textures by combining acoustic and electronic elements, as Jérémie Frémont does in his compositions.
Generated: DETERMINISTIC_d00afb23ec7f1c9f
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
import librosa
import soundfile as sf
from scipy import signal
import pyo

# Initialize pyo server
s = pyo.Server().boot()

def load_audio(file_path):
    """Load audio file using librosa."""
    try:
        y, sr = librosa.load(file_path, sr=None)
        return y, sr
    except Exception as e:
        print(f"Error loading audio file: {e}")
        return None, None

def apply_granular_synthesis(input_signal, sr, grain_size=0.1, overlap=0.5):
    """Apply granular synthesis to audio signal."""
    try:
        grain_samples = int(grain_size * sr)
        hop_samples = int(grain_samples * (1 - overlap))
        
        grains = []
        for i in range(0, len(input_signal) - grain_samples, hop_samples):
            grain = input_signal[i:i+grain_samples]
            window = signal.windows.hann(len(grain))
            grains.append(grain * window)
        
        output = np.zeros(len(input_signal))
        for i, grain in enumerate(grains):
            start = i * hop_samples
            end = start + len(grain)
            if end > len(output):
                end = len(output)
                grain = grain[:end-start]
            output[start:end] += grain
        
        return output
    except Exception as e:
        print(f"Error in granular synthesis: {e}")
        return None

def create_fm_synth(freq, ratio=1.5, index=5, dur=5.0):
    """Create FM synthesis sound using pyo."""
    try:
        fm = pyo.FM(carrier=freq, ratio=ratio, index=index, mul=0.3)
        env = pyo.Adsr(attack=0.1, decay=0.2, sustain=0.5, release=0.3, dur=dur, mul=0.5)
        return fm * env
    except Exception as e:
        print(f"Error creating FM synth: {e}")
        return None

def mix_signals(signal1, signal2, sr, mix_ratio=0.5):
    """Mix two audio signals with specified ratio."""
    try:
        min_len = min(len(signal1), len(signal2))
        mixed = (signal1[:min_len] * mix_ratio) + (signal2[:min_len] * (1 - mix_ratio))
        return mixed
    except Exception as e:
        print(f"Error mixing signals: {e}")
        return None

def apply_convolution(signal1, signal2, sr):
    """Apply convolution between two signals."""
    try:
        conv = signal.fftconvolve(signal1, signal2, mode='same')
        return conv / np.max(np.abs(conv))
    except Exception as e:
        print(f"Error in convolution: {e}")
        return None

def save_audio(output_path, signal, sr):
    """Save audio signal to file."""
    try:
        sf.write(output_path, signal, sr)
        print(f"Audio saved to {output_path}")
    except Exception as e:
        print(f"Error saving audio: {e}")

# Example usage
if __name__ == "__main__":
    # Load acoustic sample
    acoustic, sr = load_audio("acoustic_sample.wav")
    
    # Process acoustic sample
    if acoustic is not None:
        granular = apply_granular_synthesis(acoustic, sr)
        
        # Create electronic element
        fm_synth = create_fm_synth(440)
        if fm_synth is not None:
            s.start()
            fm_synth.out()
            s.recstart("fm_synth.wav")
            pyo.time.sleep(5)
            s.recstop()
            s.stop()
            
            # Load FM synth recording
            electronic, _ = load_audio("fm_synth.wav")
            
            # Mix signals
            if electronic is not None and granular is not None:
                mixed = mix_signals(granular, electronic, sr)
                
                # Apply convolution
                convolved = apply_convolution(mixed, acoustic, sr)
                
                # Save result
                if convolved is not None:
                    save_audio("hybrid_texture.wav", convolved, sr)
```
