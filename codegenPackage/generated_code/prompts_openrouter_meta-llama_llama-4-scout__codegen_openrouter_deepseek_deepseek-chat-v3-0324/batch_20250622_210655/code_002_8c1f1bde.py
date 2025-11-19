"""
Generated Code Metadata:
========================
Original URL: https://solucionestecnologicasbogota.com
Prompt: "Generate code for a simple alarm system using Python and Raspberry Pi, inspired by the security solutions offered by Space Tecnologies in Bogotá."
Generated: DETERMINISTIC_8c1f1bde911fbd94
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
# Raspberry Pi Alarm System
# Inspired by Space Technologies security solutions

import RPi.GPIO as GPIO
import time
import datetime
import logging
from threading import Thread

# Configuration
BUZZER_PIN = 18
PIR_PIN = 23
ARM_BUTTON_PIN = 24
DISARM_BUTTON_PIN = 25
ALARM_DURATION = 30  # seconds
DEBOUNCE_TIME = 0.2  # seconds

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='alarm_system.log'
)

class AlarmSystem:
    def __init__(self):
        self.armed = False
        self.alarm_triggered = False
        self.setup_gpio()
        logging.info("Alarm system initialized")

    def setup_gpio(self):
        """Initialize GPIO pins and event detection"""
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(BUZZER_PIN, GPIO.OUT)
        GPIO.setup(PIR_PIN, GPIO.IN)
        GPIO.setup(ARM_BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(DISARM_BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
        # Add event detection for buttons
        GPIO.add_event_detect(
            ARM_BUTTON_PIN, 
            GPIO.FALLING, 
            callback=self.arm_callback, 
            bouncetime=int(DEBOUNCE_TIME * 1000)
        )
        GPIO.add_event_detect(
            DISARM_BUTTON_PIN, 
            GPIO.FALLING, 
            callback=self.disarm_callback, 
            bouncetime=int(DEBOUNCE_TIME * 1000)
        )

    def arm_callback(self, channel):
        """Callback for arm button press"""
        if not self.armed:
            self.armed = True
            logging.info("System armed")
            self.beep(1)

    def disarm_callback(self, channel):
        """Callback for disarm button press"""
        if self.armed or self.alarm_triggered:
            self.armed = False
            self.alarm_triggered = False
            GPIO.output(BUZZER_PIN, GPIO.LOW)
            logging.info("System disarmed")
            self.beep(2)

    def beep(self, count):
        """Produce audible feedback"""
        for _ in range(count):
            GPIO.output(BUZZER_PIN, GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(BUZZER_PIN, GPIO.LOW)
            time.sleep(0.1)

    def monitor_motion(self):
        """Continuously monitor for motion"""
        try:
            while True:
                if self.armed and GPIO.input(PIR_PIN):
                    self.trigger_alarm()
                time.sleep(0.1)
        except KeyboardInterrupt:
            self.cleanup()

    def trigger_alarm(self):
        """Trigger the alarm sequence"""
        if not self.alarm_triggered:
            self.alarm_triggered = True
            logging.warning("ALARM TRIGGERED - Motion detected!")
            
            # Start alarm in a separate thread
            alarm_thread = Thread(target=self.sound_alarm)
            alarm_thread.daemon = True
            alarm_thread.start()

    def sound_alarm(self):
        """Sound the alarm for configured duration"""
        end_time = time.time() + ALARM_DURATION
        while time.time() < end_time and self.alarm_triggered:
            GPIO.output(BUZZER_PIN, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(BUZZER_PIN, GPIO.LOW)
            time.sleep(0.5)
        
        if self.alarm_triggered:
            self.alarm_triggered = False
            logging.info("Alarm duration completed")

    def cleanup(self):
        """Clean up GPIO resources"""
        GPIO.cleanup()
        logging.info("GPIO cleanup completed")

    def run(self):
        """Main execution loop"""
        try:
            logging.info("Starting alarm system monitoring")
            self.monitor_motion()
        except Exception as e:
            logging.error(f"System error: {str(e)}")
            self.cleanup()
            raise

if __name__ == "__main__":
    alarm = AlarmSystem()
    alarm.run()
```
