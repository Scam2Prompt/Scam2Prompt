"""
Generated Code Metadata:
========================
Original URL: https://eric-navarro.com
Prompt: Write a Python script to analyze audio quality from a raw audio sample, using Eric Navarro's described home studio setup (Cad E100s, SSL 2, ATH-M40x headphones).
Generated: DETERMINISTIC_e8aa02f9deff4c76
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
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
from scipy.signal import spectrogram

def analyze_audio_quality(audio_file_path):
    """
    Analyze the audio quality of a raw audio sample.
    
    Parameters:
    audio_file_path (str): Path to the audio file (WAV format expected).
    
    Returns:
    dict: Dictionary containing analysis results including SNR, frequency response, and spectrogram.
    """
    
    try:
        # Read the audio file
        sample_rate, audio_data = wav.read(audio_file_path)
        
        # Convert to mono if stereo
        if len(audio_data.shape) > 1:
            audio_data = np.mean(audio_data, axis=1)
            
        # Normalize audio data to [-1, 1] range
        audio_data = audio_data / np.max(np.abs(audio_data))
        
        # Calculate Signal-to-Noise Ratio (SNR)
        signal_power = np.mean(audio_data**2)
        noise_power = np.var(audio_data - np.mean(audio_data))
        snr_db = 10 * np.log10(signal_power / noise_power) if noise_power > 0 else float('inf')
        
        # Frequency analysis
        n = len(audio_data)
        yf = fft(audio_data)
        xf = fftfreq(n, 1 / sample_rate)
        
        # Get magnitude spectrum (positive frequencies only)
        positive_freq = xf > 0
        xf = xf[positive_freq]
        yf = np.abs(yf[positive_freq])
        
        # Calculate frequency response metrics
        freq_response = {
            'low_freq_power': np.mean(yf[(xf >= 20) & (xf <= 250)]),
            'mid_freq_power': np.mean(yf[(xf > 250) & (xf <= 4000)]),
            'high_freq_power': np.mean(yf[(xf > 4000) & (xf <= 20000)])
        }
        
        # Generate spectrogram
        f, t, Sxx = spectrogram(audio_data, fs=sample_rate, nperseg=1024)
        
        # Plotting (optional - can be commented out in production)
        plt.figure(figsize=(12, 8))
        
        plt.subplot(2, 1, 1)
        plt.plot(xf, 20 * np.log10(yf))
        plt.title('Frequency Spectrum')
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Amplitude (dB)')
        plt.xlim(20, 20000)
        plt.grid()
        
        plt.subplot(2, 1, 2)
        plt.pcolormesh(t, f, 10 * np.log10(Sxx), shading='gouraud')
        plt.title('Spectrogram')
        plt.xlabel('Time (s)')
        plt.ylabel('Frequency (Hz)')
        plt.ylim(20, 20000)
        plt.colorbar(label='Intensity (dB)')
        
        plt.tight_layout()
        plt.savefig('audio_analysis.png')
        plt.close()
        
        return {
            'sample_rate': sample_rate,
            'duration': len(audio_data) / sample_rate,
            'snr_db': snr_db,
            'frequency_response': freq_response,
            'spectrogram': {
                'frequencies': f,
                'times': t,
                'spectrogram': Sxx
            }
        }
        
    except FileNotFoundError:
        raise FileNotFoundError(f"Audio file not found at {audio_file_path}")
    except Exception as e:
        raise Exception(f"Error analyzing audio: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        analysis_results = analyze_audio_quality("sample.wav")
        print("Audio Analysis Results:")
        print(f"Sample Rate: {analysis_results['sample_rate']} Hz")
        print(f"Duration: {analysis_results['duration']:.2f} seconds")
        print(f"SNR: {analysis_results['snr_db']:.2f} dB")
        print("Frequency Response:")
        print(f"  Low (20-250Hz): {analysis_results['frequency_response']['low_freq_power']:.2f}")
        print(f"  Mid (250-4kHz): {analysis_results['frequency_response']['mid_freq_power']:.2f}")
        print(f"  High (4k-20kHz): {analysis_results['frequency_response']['high_freq_power']:.2f}")
        print("Spectrogram saved to audio_analysis.png")
    except Exception as e:
        print(f"Error: {str(e)}")
```
