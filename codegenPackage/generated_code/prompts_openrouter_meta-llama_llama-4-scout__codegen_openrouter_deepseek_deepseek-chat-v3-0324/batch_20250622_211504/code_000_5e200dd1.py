"""
Generated Code Metadata:
========================
Original URL: https://aktivrorteknikk.no
Prompt: Write a Python script to detect leaks in a water pipeline network using microphone and correlation techniques, as described by Aktiv Rørteknikk AS.
Generated: DETERMINISTIC_5e200dd1b348f29b
Batch ID: 20250622_211504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import sounddevice as sd
import scipy.signal as signal
import time
import logging
from typing import Tuple, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class PipelineLeakDetector:
    """
    A class to detect leaks in water pipeline networks using microphone and correlation techniques.
    
    Attributes:
        sample_rate (int): Sampling rate in Hz for audio recording.
        duration (float): Duration of each recording in seconds.
        threshold (float): Correlation threshold for leak detection.
        min_delay (float): Minimum expected delay between sensors in seconds.
        max_delay (float): Maximum expected delay between sensors in seconds.
    """
    
    def __init__(
        self,
        sample_rate: int = 44100,
        duration: float = 5.0,
        threshold: float = 0.7,
        min_delay: float = 0.001,
        max_delay: float = 0.1
    ):
        """
        Initialize the leak detector with configuration parameters.
        
        Args:
            sample_rate: Sampling rate in Hz (default: 44100).
            duration: Recording duration in seconds (default: 5.0).
            threshold: Correlation threshold for leak detection (default: 0.7).
            min_delay: Minimum expected delay between sensors in seconds (default: 0.001).
            max_delay: Maximum expected delay between sensors in seconds (default: 0.1).
        """
        self.sample_rate = sample_rate
        self.duration = duration
        self.threshold = threshold
        self.min_delay = min_delay
        self.max_delay = max_delay
        
        # Validate parameters
        if sample_rate <= 0:
            raise ValueError("Sample rate must be positive.")
        if duration <= 0:
            raise ValueError("Duration must be positive.")
        if threshold <= 0 or threshold > 1:
            raise ValueError("Threshold must be between 0 and 1.")
        if min_delay < 0 or max_delay <= min_delay:
            raise ValueError("Invalid delay range.")
    
    def record_audio(self, device: Optional[int] = None) -> np.ndarray:
        """
        Record audio from the specified microphone device.
        
        Args:
            device: Input device ID. If None, uses default device.
            
        Returns:
            A numpy array containing the recorded audio samples.
            
        Raises:
            RuntimeError: If recording fails.
        """
        try:
            logger.info(f"Recording audio for {self.duration} seconds...")
            recording = sd.rec(
                int(self.duration * self.sample_rate),
                samplerate=self.sample_rate,
                channels=1,
                device=device,
                dtype='float32'
            )
            sd.wait()  # Wait until recording is finished
            logger.info("Recording completed.")
            return recording.flatten()
        except Exception as e:
            logger.error(f"Failed to record audio: {e}")
            raise RuntimeError("Audio recording failed.") from e
    
    def cross_correlate(self, x: np.ndarray, y: np.ndarray) -> Tuple[float, float]:
        """
        Compute cross-correlation between two signals and find the delay.
        
        Args:
            x: First signal.
            y: Second signal.
            
        Returns:
            A tuple containing (correlation_coefficient, delay_in_seconds).
            
        Raises:
            ValueError: If signals have different lengths.
        """
        if len(x) != len(y):
            raise ValueError("Signals must have the same length.")
            
        # Compute cross-correlation
        correlation = signal.correlate(x, y, mode='same')
        lags = signal.correlation_lags(len(x), len(y), mode='same')
        
        # Convert lags to time delays
        delays = lags / self.sample_rate
        
        # Find the peak within the expected delay range
        valid_indices = np.where((delays >= self.min_delay) & (delays <= self.max_delay))[0]
        if len(valid_indices) == 0:
            return (0.0, 0.0)
            
        max_index = valid_indices[np.argmax(correlation[valid_indices])]
        max_corr = correlation[max_index] / (np.linalg.norm(x) * np.linalg.norm(y))
        delay = delays[max_index]
        
        return (max_corr, delay)
    
    def detect_leak(
        self,
        sensor1_device: Optional[int] = None,
        sensor2_device: Optional[int] = None
    ) -> Optional[Tuple[float, float]]:
        """
        Detect leaks by comparing signals from two microphones.
        
        Args:
            sensor1_device: Device ID for first microphone.
            sensor2_device: Device ID for second microphone.
            
        Returns:
            A tuple of (correlation_coefficient, delay_in_seconds) if leak is detected,
            None otherwise.
        """
        try:
            # Record from both sensors
            logger.info("Recording from sensor 1...")
            signal1 = self.record_audio(sensor1_device)
            
            logger.info("Recording from sensor 2...")
            signal2 = self.record_audio(sensor2_device)
            
            # Compute cross-correlation
            corr, delay = self.cross_correlate(signal1, signal2)
            
            logger.info(f"Correlation: {corr:.3f}, Delay: {delay:.6f}s")
            
            if corr >= self.threshold:
                logger.info(f"Leak detected with correlation {corr:.3f} and delay {delay:.6f}s")
                return (corr, delay)
            else:
                logger.info("No leak detected.")
                return None
                
        except Exception as e:
            logger.error(f"Leak detection failed: {e}")
            return None

# Example usage
if __name__ == "__main__":
    try:
        # Initialize detector with default parameters
        detector = PipelineLeakDetector()
        
        # List available audio devices
        print("Available audio devices:")
        devices = sd.query_devices()
        for i, dev in enumerate(devices):
            print(f"{i}: {dev['name']}")
        
        # For production, you would specify the correct device IDs
        # Here we use None for default devices
        result = detector.detect_leak()
        
        if result:
            corr, delay = result
            print(f"Leak detected! Correlation: {corr:.3f}, Delay: {delay:.6f}s")
        else:
            print("No leak detected.")
            
    except Exception as e:
        logger.error(f"Pipeline leak detection failed: {e}")
```
