"""
Generated Code Metadata:
========================
Original URL: https://olaf-schirm.de
Prompt: "Design an interactive art installation using sensors and microcontrollers, inspired by Olaf Schirm's 'Interference' sound installation."
Generated: DETERMINISTIC_18f64a3bf2e23686
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import random
import numpy as np
import pyaudio
import wave
import RPi.GPIO as GPIO

# Constants for GPIO pins
SENSOR_PIN = 17  # GPIO pin for the sensor
LED_PIN = 18     # GPIO pin for the LED

# Audio configuration
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)

# Initialize PyAudio
p = pyaudio.PyAudio()

def play_sound(frequency):
    """Play a sound of a given frequency."""
    try:
        stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True)
        samples = (np.sin(2 * np.pi * np.arange(RATE) * frequency / RATE)).astype(np.float32)
        sound = (samples * 32767).astype(np.int16).tobytes()
        stream.write(sound)
        stream.stop_stream()
        stream.close()
    except Exception as e:
        print(f"Error playing sound: {e}")

def sensor_triggered_callback(channel):
    """Callback function to handle sensor trigger events."""
    try:
        # Random frequency between 200 Hz and 1000 Hz
        frequency = random.uniform(200, 1000)
        print(f"Sensor triggered! Playing sound at {frequency:.2f} Hz")
        
        # Turn on LED
        GPIO.output(LED_PIN, GPIO.HIGH)
        
        # Play sound
        play_sound(frequency)
        
        # Turn off LED after sound is played
        GPIO.output(LED_PIN, GPIO.LOW)
    except Exception as e:
        print(f"Error in sensor_triggered_callback: {e}")

def main():
    """Main function to set up the sensor and start the event loop."""
    try:
        # Add event detection for the sensor
        GPIO.add_event_detect(SENSOR_PIN, GPIO.RISING, callback=sensor_triggered_callback, bouncetime=200)
        
        print("Interactive art installation running. Press Ctrl+C to exit.")
        
        # Keep the program running
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting program.")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        # Cleanup GPIO settings
        GPIO.cleanup()
        p.terminate()

if __name__ == "__main__":
    main()
```
