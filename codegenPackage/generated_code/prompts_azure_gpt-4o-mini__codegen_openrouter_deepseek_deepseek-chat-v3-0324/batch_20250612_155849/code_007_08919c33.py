"""
Generated Code Metadata:
========================
Original URL: https://blackpanttthers.com
Prompt: Develop a script that utilizes environmental sensors to monitor indoor air quality and automatically adjust ventilation systems accordingly.
Generated: DETERMINISTIC_08919c332ed60d96
Batch ID: 20250612_155849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
Indoor Air Quality Monitoring and Ventilation Control System

This script reads data from environmental sensors (temperature, humidity, CO2, VOC)
and adjusts ventilation systems based on predefined thresholds.
"""

import time
import logging
from dataclasses import dataclass
from typing import Optional
import board
import adafruit_sht31d
import adafruit_ccs811
import RPi.GPIO as GPIO

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('air_quality_monitor.log'),
        logging.StreamHandler()
    ]
)

# Constants
VENTILATION_PIN = 17
CHECK_INTERVAL = 60  # seconds
MAX_RETRIES = 3

# Air quality thresholds
@dataclass
class Thresholds:
    TEMP_MAX: float = 25.0  # °C
    TEMP_MIN: float = 18.0  # °C
    HUMIDITY_MAX: float = 60.0  # %
    HUMIDITY_MIN: float = 30.0  # %
    CO2_MAX: float = 1000.0  # ppm
    VOC_MAX: float = 500.0  # ppb

class SensorError(Exception):
    """Custom exception for sensor errors"""
    pass

class VentilationController:
    """Controls the ventilation system based on sensor readings"""
    
    def __init__(self):
        """Initialize the ventilation controller"""
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(VENTILATION_PIN, GPIO.OUT)
        self.ventilation_on = False
    
    def set_ventilation(self, state: bool) -> None:
        """Turn ventilation on or off"""
        if state != self.ventilation_on:
            GPIO.output(VENTILATION_PIN, state)
            self.ventilation_on = state
            logging.info(f"Ventilation {'ON' if state else 'OFF'}")
    
    def cleanup(self) -> None:
        """Clean up GPIO resources"""
        GPIO.cleanup()

class AirQualityMonitor:
    """Monitors air quality using environmental sensors"""
    
    def __init__(self):
        """Initialize sensors"""
        self.i2c = board.I2C()
        self.temp_humidity_sensor = None
        self.air_quality_sensor = None
        self.initialize_sensors()
    
    def initialize_sensors(self) -> None:
        """Initialize sensor connections with retry logic"""
        for _ in range(MAX_RETRIES):
            try:
                self.temp_humidity_sensor = adafruit_sht31d.SHT31D(self.i2c)
                self.air_quality_sensor = adafruit_ccs811.CCS811(self.i2c)
                # Wait for CCS811 to be ready
                time.sleep(1)
                return
            except Exception as e:
                logging.warning(f"Sensor initialization failed: {str(e)}")
                time.sleep(2)
        
        raise SensorError("Failed to initialize sensors after multiple attempts")
    
    def read_sensors(self) -> dict:
        """Read all sensor data with error handling"""
        data = {
            'temperature': None,
            'humidity': None,
            'co2': None,
            'voc': None
        }
        
        try:
            if self.temp_humidity_sensor:
                data['temperature'] = self.temp_humidity_sensor.temperature
                data['humidity'] = self.temp_humidity_sensor.relative_humidity
            
            if self.air_quality_sensor and self.air_quality_sensor.data_ready:
                data['co2'] = self.air_quality_sensor.eco2
                data['voc'] = self.air_quality_sensor.tvoc
            
            return data
        except Exception as e:
            raise SensorError(f"Error reading sensors: {str(e)}")

def evaluate_air_quality(sensor_data: dict, thresholds: Thresholds) -> bool:
    """Determine if ventilation is needed based on thresholds"""
    needs_ventilation = False
    
    if sensor_data['temperature'] is not None:
        if (sensor_data['temperature'] > thresholds.TEMP_MAX or 
            sensor_data['temperature'] < thresholds.TEMP_MIN):
            needs_ventilation = True
    
    if sensor_data['humidity'] is not None:
        if (sensor_data['humidity'] > thresholds.HUMIDITY_MAX or 
            sensor_data['humidity'] < thresholds.HUMIDITY_MIN):
            needs_ventilation = True
    
    if sensor_data['co2'] is not None and sensor_data['co2'] > thresholds.CO2_MAX:
        needs_ventilation = True
    
    if sensor_data['voc'] is not None and sensor_data['voc'] > thresholds.VOC_MAX:
        needs_ventilation = True
    
    return needs_ventilation

def main():
    """Main monitoring loop"""
    thresholds = Thresholds()
    monitor = AirQualityMonitor()
    controller = VentilationController()
    
    try:
        logging.info("Starting air quality monitoring system")
        
        while True:
            try:
                sensor_data = monitor.read_sensors()
                logging.info(f"Sensor data: {sensor_data}")
                
                ventilation_needed = evaluate_air_quality(sensor_data, thresholds)
                controller.set_ventilation(ventilation_needed)
                
            except SensorError as e:
                logging.error(str(e))
                controller.set_ventilation(True)  # Fail-safe: turn on ventilation
                
            time.sleep(CHECK_INTERVAL)
            
    except KeyboardInterrupt:
        logging.info("Shutting down air quality monitoring system")
    finally:
        controller.cleanup()

if __name__ == "__main__":
    main()
```
