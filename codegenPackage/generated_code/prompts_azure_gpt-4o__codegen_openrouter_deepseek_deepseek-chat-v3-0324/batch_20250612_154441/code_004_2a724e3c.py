"""
Generated Code Metadata:
========================
Original URL: https://ironpickle.com
Prompt: Provide code to analyze the audio features (e.g., tempo, mood) of Iron Pickle's "Strange Cargo - Space Ambient Music" using the librosa Python library.
Generated: DETERMINISTIC_2a724e3ca1b0f600
Batch ID: 20250612_154441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import librosa
import numpy as np
import matplotlib.pyplot as plt
import warnings

def analyze_audio_features(file_path):
    """
    Analyze audio features of a given audio file using librosa.
    
    Args:
        file_path (str): Path to the audio file.
        
    Returns:
        dict: Dictionary containing various audio features.
    """
    # Suppress librosa warnings
    warnings.filterwarnings('ignore')
    
    try:
        # Load audio file
        y, sr = librosa.load(file_path)
        
        # Extract features
        features = {}
        
        # Basic features
        features['duration'] = librosa.get_duration(y=y, sr=sr)
        features['tempo'], _ = librosa.beat.beat_track(y=y, sr=sr)
        
        # Spectral features
        features['spectral_centroid'] = np.mean(librosa.feature.spectral_centroid(y=y, sr=sr))
        features['spectral_bandwidth'] = np.mean(librosa.feature.spectral_bandwidth(y=y, sr=sr))
        features['spectral_rolloff'] = np.mean(librosa.feature.spectral_rolloff(y=y, sr=sr))
        
        # MFCC features
        mfcc = librosa.feature.mfcc(y=y, sr=sr)
        features['mfcc_mean'] = np.mean(mfcc, axis=1)
        
        # Chroma features
        chroma = librosa.feature.chroma_stft(y=y, sr=sr)
        features['chroma_mean'] = np.mean(chroma, axis=1)
        
        # Harmonic and percussive components
        y_harmonic, y_percussive = librosa.effects.hpss(y)
        features['harmonic_ratio'] = np.mean(y_harmonic / (y_harmonic + y_percussive + 1e-6))
        
        # Zero-crossing rate
        features['zero_crossing_rate'] = np.mean(librosa.feature.zero_crossing_rate(y))
        
        # RMS energy
        features['rms_energy'] = np.mean(librosa.feature.rms(y=y))
        
        # Mood estimation (valence and energy approximation)
        features['valence'] = (features['harmonic_ratio'] + 
                              (1 - features['zero_crossing_rate']) + 
                              np.mean(features['chroma_mean'])) / 3
        features['energy'] = (features['rms_energy'] + 
                             features['spectral_centroid'] + 
                             features['tempo'] / 250) / 3
        
        return features
        
    except Exception as e:
        print(f"Error analyzing audio file: {e}")
        return None

def visualize_features(features):
    """
    Visualize the extracted audio features.
    
    Args:
        features (dict): Dictionary containing audio features.
    """
    if not features:
        return
        
    plt.figure(figsize=(12, 8))
    
    # Plot basic features
    plt.subplot(2, 2, 1)
    plt.bar(['Tempo', 'Duration'], [features['tempo'], features['duration']])
    plt.title('Basic Features')
    
    # Plot spectral features
    plt.subplot(2, 2, 2)
    spectral_features = ['Centroid', 'Bandwidth', 'Rolloff']
    values = [features['spectral_centroid'], 
              features['spectral_bandwidth'], 
              features['spectral_rolloff']]
    plt.bar(spectral_features, values)
    plt.title('Spectral Features')
    
    # Plot mood features
    plt.subplot(2, 2, 3)
    plt.bar(['Valence', 'Energy'], [features['valence'], features['energy']])
    plt.ylim(0, 1)
    plt.title('Mood Estimation')
    
    # Plot MFCC heatmap
    plt.subplot(2, 2, 4)
    plt.imshow(np.expand_dims(features['mfcc_mean'], 0), 
               aspect='auto', origin='lower', cmap='viridis')
    plt.colorbar()
    plt.title('MFCC Mean Coefficients')
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Example usage
    audio_file = "Strange Cargo - Space Ambient Music.mp3"  # Replace with actual file path
    
    # Analyze audio features
    features = analyze_audio_features(audio_file)
    
    if features:
        print("Audio Features Analysis:")
        for key, value in features.items():
            if isinstance(value, np.ndarray):
                print(f"{key}: array of shape {value.shape}")
            else:
                print(f"{key}: {value:.2f}")
        
        # Visualize features
        visualize_features(features)
```
