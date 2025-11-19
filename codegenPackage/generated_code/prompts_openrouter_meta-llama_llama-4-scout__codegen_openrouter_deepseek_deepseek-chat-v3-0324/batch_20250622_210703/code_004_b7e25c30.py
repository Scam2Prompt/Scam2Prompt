"""
Generated Code Metadata:
========================
Original URL: https://sincresisarquitectos.com
Prompt: "Develop a code snippet for simulating and visualizing the acoustic properties of a space, similar to those discussed in Sincresis's approach to creating immersive environments."
Generated: DETERMINISTIC_b7e25c306b87afe2
Batch ID: 20250622_210703
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
from mpl_toolkits.mplot3d import Axes3D
from scipy.io import wavfile
from scipy.signal import fftconvolve
import soundfile as sf
import os

class AcousticSimulator:
    """
    Simulates and visualizes acoustic properties of a space.
    Models reflections, reverberation, and spatial characteristics.
    """
    
    def __init__(self, room_dimensions, fs=44100, rt60=1.0, absorption=0.5):
        """
        Initialize acoustic simulator with room parameters.
        
        Args:
            room_dimensions (tuple): (length, width, height) in meters
            fs (int): Sampling frequency (Hz)
            rt60 (float): Reverberation time (seconds)
            absorption (float): Wall absorption coefficient (0-1)
        """
        self.room_dim = np.array(room_dimensions)
        self.fs = fs
        self.rt60 = rt60
        self.absorption = absorption
        self.max_reflections = 10  # Maximum order of reflections to simulate
        
    def generate_rir(self, source_pos, receiver_pos):
        """
        Generate room impulse response using image source method.
        
        Args:
            source_pos (array): [x,y,z] coordinates of sound source
            receiver_pos (array): [x,y,z] coordinates of receiver
            
        Returns:
            ndarray: Room impulse response
        """
        source_pos = np.array(source_pos)
        receiver_pos = np.array(receiver_pos)
        
        # Initialize impulse response
        max_delay = int(self.rt60 * self.fs)
        rir = np.zeros(max_delay)
        
        # Direct sound
        dist = np.linalg.norm(source_pos - receiver_pos)
        delay = int(dist / 343.0 * self.fs)  # Speed of sound = 343 m/s
        if delay < max_delay:
            rir[delay] = 1.0 / (dist + 1e-10)  # Avoid division by zero
            
        # Early reflections
        for order in range(1, self.max_reflections + 1):
            # Generate image sources (simplified for demo)
            for dim in range(3):
                for _ in range(2**order):
                    # Simplified reflection calculation
                    image_pos = source_pos.copy()
                    image_pos[dim] = 2 * (order % 2) * self.room_dim[dim] - image_pos[dim]
                    
                    dist = np.linalg.norm(image_pos - receiver_pos)
                    delay = int(dist / 343.0 * self.fs)
                    if delay < max_delay:
                        attenuation = (self.absorption ** order) / (dist + 1e-10)
                        rir[delay] += attenuation
        
        # Late reverberation (exponential decay)
        t = np.arange(max_delay) / self.fs
        late_reverb = np.exp(-3 * np.log(10) * t / self.rt60)
        rir += late_reverb * np.random.normal(0, 0.1, size=max_delay)
        
        # Normalize
        rir /= np.max(np.abs(rir))
        return rir
    
    def apply_reverb(self, dry_signal, rir):
        """
        Convolve dry signal with room impulse response.
        
        Args:
            dry_signal (ndarray): Input audio signal
            rir (ndarray): Room impulse response
            
        Returns:
            ndarray: Reverberant signal
        """
        return fftconvolve(dry_signal, rir)
    
    def visualize_rir(self, rir, title="Room Impulse Response"):
        """
        Plot room impulse response.
        
        Args:
            rir (ndarray): Room impulse response to visualize
            title (str): Plot title
        """
        plt.figure(figsize=(10, 4))
        plt.plot(np.arange(len(rir)) / self.fs, rir)
        plt.title(title)
        plt.xlabel("Time (s)")
        plt.ylabel("Amplitude")
        plt.grid(True)
        plt.show()
    
    def visualize_room(self, source_pos, receiver_pos):
        """
        3D visualization of room with source and receiver positions.
        
        Args:
            source_pos (array): [x,y,z] coordinates of sound source
            receiver_pos (array): [x,y,z] coordinates of receiver
        """
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')
        
        # Draw room
        x, y, z = self.room_dim
        vertices = [
            [0, 0, 0], [x, 0, 0], [x, y, 0], [0, y, 0],
            [0, 0, z], [x, 0, z], [x, y, z], [0, y, z]
        ]
        edges = [
            [0,1], [1,2], [2,3], [3,0],
            [4,5], [5,6], [6,7], [7,4],
            [0,4], [1,5], [2,6], [3,7]
        ]
        
        for edge in edges:
            ax.plot3D(*zip(vertices[edge[0]], vertices[edge[1]]), color='gray', alpha=0.5)
        
        # Plot source and receiver
        ax.scatter(*source_pos, c='r', s=100, label='Source')
        ax.scatter(*receiver_pos, c='b', s=100, label='Receiver')
        
        ax.set_xlabel('X (m)')
        ax.set_ylabel('Y (m)')
        ax.set_zlabel('Z (m)')
        ax.set_title('Room Acoustics Simulation')
        ax.legend()
        plt.show()
    
    def process_audio_file(self, input_path, output_path, source_pos, receiver_pos):
        """
        Process audio file through simulated room acoustics.
        
        Args:
            input_path (str): Path to input audio file
            output_path (str): Path to save processed audio
            source_pos (array): [x,y,z] coordinates of sound source
            receiver_pos (array): [x,y,z] coordinates of receiver
        """
        try:
            # Load audio file
            dry_signal, fs = sf.read(input_path)
            if fs != self.fs:
                raise ValueError(f"Sample rate mismatch: expected {self.fs}, got {fs}")
            
            # Generate RIR and apply reverb
            rir = self.generate_rir(source_pos, receiver_pos)
            wet_signal = self.apply_reverb(dry_signal, rir)
            
            # Normalize and save
            wet_signal = wet_signal / np.max(np.abs(wet_signal))
            sf.write(output_path, wet_signal, self.fs)
            
        except Exception as e:
            print(f"Error processing audio file: {str(e)}")
            raise

# Example usage
if __name__ == "__main__":
    # Initialize simulator
    room_dim = (10, 8, 3)  # Length, width, height in meters
    simulator = AcousticSimulator(room_dim, rt60=1.5, absorption=0.7)
    
    # Define positions
    source_pos = [2, 2, 1.5]
    receiver_pos = [8, 6, 1.5]
    
    # Generate and visualize RIR
    rir = simulator.generate_rir(source_pos, receiver_pos)
    simulator.visualize_rir(rir)
    simulator.visualize_room(source_pos, receiver_pos)
    
    # Process audio file (example - uncomment to use)
    # simulator.process_audio_file("input.wav", "output.wav", source_pos, receiver_pos)
```
