"""
Generated Code Metadata:
========================
Original URL: https://eric-navarro.com
Prompt: Generate a code snippet for a voice recording application that utilizes a Cad E100s microphone and SSL 2 audio interface for high-quality audio capture.
Generated: DETERMINISTIC_3b25b2e9927d5be9
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sounddevice as sd
import numpy as np
import wave
import time
from datetime import datetime
import os

class AudioRecorder:
    """
    A high-quality audio recorder using Cad E100s microphone and SSL 2 audio interface.
    Handles device setup, recording, and file saving with proper error handling.
    """
    
    def __init__(self, sample_rate=48000, channels=1, dtype='int24'):
        """
        Initialize the audio recorder with specified parameters.
        
        Args:
            sample_rate (int): Sample rate in Hz (default: 48000)
            channels (int): Number of audio channels (default: 1 for mono)
            dtype (str): Data type for audio samples (default: 'int24')
        """
        self.sample_rate = sample_rate
        self.channels = channels
        self.dtype = dtype
        self.recording = False
        self.audio_data = None
        self.device_info = None
        
        # Set up audio device
        self._setup_audio_device()
        
    def _setup_audio_device(self):
        """Setup audio device with error handling."""
        try:
            # List all audio devices
            devices = sd.query_devices()
            
            # Find SSL 2 interface (adjust as needed for your system)
            ssl_device = None
            for i, device in enumerate(devices):
                if 'SSL 2' in device['name']:
                    ssl_device = i
                    break
            
            if ssl_device is None:
                raise ValueError("SSL 2 audio interface not found")
            
            # Set as default device
            sd.default.device = ssl_device
            self.device_info = sd.query_devices(ssl_device)
            
            # Verify sample rate is supported
            if self.sample_rate not in self.device_info['default_samplerates']:
                raise ValueError(f"Sample rate {self.sample_rate} not supported by device")
            
            print(f"Audio device setup complete: {self.device_info['name']}")
            
        except Exception as e:
            print(f"Error setting up audio device: {str(e)}")
            raise
    
    def _callback(self, indata, frames, time, status):
        """Callback function for audio stream."""
        if status:
            print(f"Audio stream status: {status}")
        if self.recording:
            if self.audio_data is None:
                self.audio_data = indata.copy()
            else:
                self.audio_data = np.append(self.audio_data, indata, axis=0)
    
    def start_recording(self):
        """Start recording audio."""
        if self.recording:
            print("Already recording")
            return
        
        try:
            self.recording = True
            self.audio_data = None
            
            # Start audio stream
            self.stream = sd.InputStream(
                samplerate=self.sample_rate,
                channels=self.channels,
                dtype=self.dtype,
                callback=self._callback
            )
            self.stream.start()
            
            print("Recording started...")
            
        except Exception as e:
            self.recording = False
            print(f"Error starting recording: {str(e)}")
            raise
    
    def stop_recording(self):
        """Stop recording audio."""
        if not self.recording:
            print("Not currently recording")
            return
        
        try:
            self.recording = False
            self.stream.stop()
            self.stream.close()
            print("Recording stopped")
            
        except Exception as e:
            print(f"Error stopping recording: {str(e)}")
            raise
    
    def save_recording(self, filename=None, directory='recordings'):
        """
        Save the recorded audio to a WAV file.
        
        Args:
            filename (str): Custom filename (optional)
            directory (str): Directory to save recordings (default: 'recordings')
        """
        if self.audio_data is None:
            print("No audio data to save")
            return
        
        try:
            # Create directory if it doesn't exist
            os.makedirs(directory, exist_ok=True)
            
            # Generate filename if not provided
            if filename is None:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"recording_{timestamp}.wav"
            
            filepath = os.path.join(directory, filename)
            
            # Convert audio data to proper format
            if self.dtype == 'int24':
                # For 24-bit audio, we need special handling
                audio_data = (self.audio_data * (2**23 - 1)).astype(np.int32)
            else:
                audio_data = self.audio_data
            
            # Save as WAV file
            with wave.open(filepath, 'wb') as wf:
                wf.setnchannels(self.channels)
                wf.setsampwidth(3 if self.dtype == 'int24' else 2)  # 3 bytes for 24-bit
                wf.setframerate(self.sample_rate)
                wf.writeframes(audio_data.tobytes())
            
            print(f"Recording saved to {filepath}")
            return filepath
            
        except Exception as e:
            print(f"Error saving recording: {str(e)}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        recorder = AudioRecorder()
        
        print("Starting recording for 5 seconds...")
        recorder.start_recording()
        time.sleep(5)
        recorder.stop_recording()
        
        print("Saving recording...")
        recorder.save_recording()
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
