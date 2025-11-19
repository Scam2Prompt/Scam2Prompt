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
# Interactive Art Installation inspired by Olaf Schirm's 'Interference'
# Uses ultrasonic sensors to detect proximity and generates sound interference patterns

import time
import math
import random
import pygame
import RPi.GPIO as GPIO
from threading import Thread

# Configuration
SENSOR_COUNT = 4
TRIGGER_PINS = [23, 24, 25, 8]  # GPIO pins for ultrasonic sensors
ECHO_PINS = [17, 27, 22, 7]     # GPIO pins for echo
MAX_DISTANCE = 200              # Max distance in cm
SOUND_DURATION = 0.5            # Duration of each sound in seconds
BASE_FREQUENCY = 220            # Base frequency in Hz

# Initialize pygame for sound generation
pygame.mixer.init(frequency=44100, size=-16, channels=2)
pygame.init()

class SoundGenerator:
    def __init__(self):
        self.sounds = []
        self.active = False
        
    def generate_sine_wave(self, frequency, duration, volume=0.1):
        sample_rate = 44100
        samples = int(sample_rate * duration)
        buffer = numpy.zeros((samples, 2), dtype=numpy.int16)
        amplitude = 32767 * volume
        
        for i in range(samples):
            t = float(i) / sample_rate
            wave = amplitude * math.sin(2 * math.pi * frequency * t)
            buffer[i][0] = buffer[i][1] = wave
            
        sound = pygame.sndarray.make_sound(buffer)
        return sound
    
    def play_interference(self, frequencies):
        if self.active:
            return
            
        self.active = True
        self.sounds = []
        
        for freq in frequencies:
            sound = self.generate_sine_wave(freq, SOUND_DURATION)
            sound.play()
            self.sounds.append(sound)
            
        Thread(target=self._monitor_sounds).start()
        
    def _monitor_sounds(self):
        time.sleep(SOUND_DURATION)
        self.active = False

class SensorController:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        self.setup_sensors()
        self.last_distances = [0] * SENSOR_COUNT
        self.sound_gen = SoundGenerator()
        
    def setup_sensors(self):
        for trig, echo in zip(TRIGGER_PINS, ECHO_PINS):
            GPIO.setup(trig, GPIO.OUT)
            GPIO.setup(echo, GPIO.IN)
            GPIO.output(trig, False)
            
    def get_distance(self, sensor_idx):
        trig = TRIGGER_PINS[sensor_idx]
        echo = ECHO_PINS[sensor_idx]
        
        GPIO.output(trig, True)
        time.sleep(0.00001)
        GPIO.output(trig, False)
        
        pulse_start = time.time()
        pulse_end = time.time()
        
        while GPIO.input(echo) == 0:
            pulse_start = time.time()
            
        while GPIO.input(echo) == 1:
            pulse_end = time.time()
            
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance, 2)
        
        if distance > MAX_DISTANCE:
            distance = MAX_DISTANCE
            
        return distance
    
    def update_distances(self):
        for i in range(SENSOR_COUNT):
            self.last_distances[i] = self.get_distance(i)
            
    def calculate_frequencies(self):
        frequencies = []
        for dist in self.last_distances:
            if dist < MAX_DISTANCE * 0.1:  # Minimum threshold
                freq = BASE_FREQUENCY
            else:
                ratio = dist / MAX_DISTANCE
                freq = BASE_FREQUENCY * (1 + ratio)
            frequencies.append(freq)
        return frequencies
    
    def run(self):
        try:
            while True:
                self.update_distances()
                frequencies = self.calculate_frequencies()
                self.sound_gen.play_interference(frequencies)
                time.sleep(0.1)
                
        except KeyboardInterrupt:
            GPIO.cleanup()
            print("\nExiting...")

if __name__ == "__main__":
    import numpy  # Import here to avoid pygame init issues
    
    print("Starting Interactive Art Installation")
    print("Press Ctrl+C to exit")
    
    controller = SensorController()
    controller.run()
```
