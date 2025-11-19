"""
Generated Code Metadata:
========================
Original URL: https://soundsource.tn
Prompt: Provide code to model the acoustic design of a nightclub, incorporating the expertise described in Sound Source's portfolio.
Generated: DETERMINISTIC_8774ce7b37a5489a
Batch ID: 20250612_153225
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
from scipy.signal import fftconvolve
from scipy.io import wavfile

class NightclubAcousticModel:
    """
    A class to model the acoustic properties of a nightclub space.
    Incorporates room geometry, material properties, and sound system characteristics.
    """
    
    def __init__(self, room_dimensions, materials, sound_system):
        """
        Initialize the acoustic model with room parameters.
        
        Args:
            room_dimensions (tuple): (length, width, height) in meters
            materials (dict): Dictionary of material properties {'wall': absorption_coeff, ...}
            sound_system (dict): Speaker system parameters {'position': (x,y,z), 'power': dB, ...}
        """
        self.length, self.width, self.height = room_dimensions
        self.materials = materials
        self.sound_system = sound_system
        self.sample_rate = 44100  # Standard audio sample rate
        
        # Validate inputs
        if any(dim <= 0 for dim in room_dimensions):
            raise ValueError("Room dimensions must be positive values")
        if not all(0 <= coeff <= 1 for coeff in materials.values()):
            raise ValueError("Material coefficients must be between 0 and 1")
            
    def calculate_reverb_time(self, frequency):
        """
        Calculate RT60 reverberation time using Sabine's formula.
        
        Args:
            frequency (float): Frequency band to calculate for (Hz)
            
        Returns:
            float: Reverberation time in seconds
        """
        try:
            # Calculate total absorption
            surface_areas = {
                'wall': 2 * (self.length * self.height + self.width * self.height),
                'floor': self.length * self.width,
                'ceiling': self.length * self.width
            }
            
            total_absorption = sum(
                area * self.materials[material] 
                for material, area in surface_areas.items()
            )
            
            # Sabine's formula (simplified)
            volume = self.length * self.width * self.height
            rt60 = (0.161 * volume) / total_absorption
            
            return rt60
        except Exception as e:
            print(f"Error calculating reverb time: {e}")
            return None
    
    def generate_impulse_response(self, listener_position, max_reflections=10):
        """
        Generate room impulse response using image source method.
        
        Args:
            listener_position (tuple): (x,y,z) position of listener
            max_reflections (int): Maximum number of reflections to consider
            
        Returns:
            ndarray: Impulse response as numpy array
        """
        try:
            # Source and listener positions
            source_pos = np.array(self.sound_system['position'])
            listener_pos = np.array(listener_position)
            
            # Initialize impulse response
            duration = 2.0  # seconds
            impulse_length = int(duration * self.sample_rate)
            impulse_response = np.zeros(impulse_length)
            
            # Direct sound
            direct_dist = np.linalg.norm(source_pos - listener_pos)
            direct_delay = int((direct_dist / 343) * self.sample_rate)
            if direct_delay < impulse_length:
                impulse_response[direct_delay] = 1.0
            
            # Early reflections
            for reflection_order in range(1, max_reflections + 1):
                for dim in range(3):  # x, y, z dimensions
                    for sign in [-1, 1]:
                        # Image source method
                        image_source = source_pos.copy()
                        image_source[dim] = sign * (2 * (self.length if dim == 0 else 
                                                       (self.width if dim == 1 else self.height)) - 
                                                  source_pos[dim])
                        
                        dist = np.linalg.norm(image_source - listener_pos)
                        delay = int((dist / 343) * self.sample_rate)
                        
                        if delay < impulse_length:
                            # Apply attenuation based on distance and materials
                            attenuation = 1.0 / (1.0 + dist)
                            material_attenuation = np.prod([self.materials[m] for m in self.materials])
                            total_attenuation = attenuation * (material_attenuation ** reflection_order)
                            
                            impulse_response[delay] += total_attenuation
            
            return impulse_response
        except Exception as e:
            print(f"Error generating impulse response: {e}")
            return None
    
    def apply_room_acoustics(self, audio_file):
        """
        Apply the room acoustics to an input audio file.
        
        Args:
            audio_file (str): Path to input audio file
            
        Returns:
            ndarray: Processed audio signal
        """
        try:
            # Load audio file
            sample_rate, audio = wavfile.read(audio_file)
            if sample_rate != self.sample_rate:
                raise ValueError("Input audio sample rate must match model sample rate (44100)")
                
            if audio.ndim > 1:  # Convert to mono if stereo
                audio = np.mean(audio, axis=1)
                
            # Generate impulse response at center of dance floor
            dance_floor_center = (self.length/2, self.width/2, 1.5)  # 1.5m height
            impulse_response = self.generate_impulse_response(dance_floor_center)
            
            if impulse_response is None:
                raise RuntimeError("Failed to generate impulse response")
                
            # Convolve audio with impulse response
            processed_audio = fftconvolve(audio, impulse_response, mode='same')
            
            # Normalize to prevent clipping
            processed_audio = processed_audio / np.max(np.abs(processed_audio))
            
            return processed_audio
        except Exception as e:
            print(f"Error processing audio: {e}")
            return None
    
    def plot_frequency_response(self, listener_position):
        """
        Plot the frequency response at a given listener position.
        
        Args:
            listener_position (tuple): (x,y,z) position to analyze
        """
        try:
            impulse_response = self.generate_impulse_response(listener_position)
            if impulse_response is None:
                return
                
            # Compute frequency response
            freq_response = np.abs(np.fft.rfft(impulse_response))
            freqs = np.fft.rfftfreq(len(impulse_response), 1/self.sample_rate)
            
            # Plot
            plt.figure(figsize=(10, 6))
            plt.semilogx(freqs, 20 * np.log10(freq_response))
            plt.xlim(20, 20000)
            plt.ylim(-60, 0)
            plt.xlabel('Frequency (Hz)')
            plt.ylabel('Amplitude (dB)')
            plt.title('Frequency Response at Listener Position')
            plt.grid(True)
            plt.show()
        except Exception as e:
            print(f"Error plotting frequency response: {e}")

# Example usage
if __name__ == "__main__":
    # Define room parameters
    room_dim = (15, 10, 4)  # 15m x 10m x 4m
    materials = {
        'wall': 0.3,    # Brick with plaster
        'floor': 0.15,  # Concrete
        'ceiling': 0.8  # Acoustic panels
    }
    sound_system = {
        'position': (2, 2, 3),  # Speaker position
        'power': 100            # dB SPL
    }
    
    # Create model
    try:
        club_model = NightclubAcousticModel(room_dim, materials, sound_system)
        
        # Calculate and print reverb time
        rt60 = club_model.calculate_reverb_time(1000)  # 1kHz
        print(f"Reverberation time at 1kHz: {rt60:.2f} seconds")
        
        # Plot frequency response
        listener_pos = (8, 5, 1.7)  # Typical standing listener height
        club_model.plot_frequency_response(listener_pos)
        
        # Process audio sample (uncomment to use with actual audio file)
        # processed_audio = club_model.apply_room_acoustics("input_audio.wav")
        # if processed_audio is not None:
        #     wavfile.write("processed_audio.wav", club_model.sample_rate, processed_audio)
            
    except Exception as e:
        print(f"Error in model setup: {e}")
```
