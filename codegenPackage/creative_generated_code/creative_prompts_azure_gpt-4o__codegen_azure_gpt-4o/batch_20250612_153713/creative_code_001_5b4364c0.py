"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stethevent.org
Prompt: Recommend libraries or APIs for creating a WiFi-controlled foam dart turret using Raspberry Pi, as described in the "SwarmTurret" project on Instructables.
Generated: DETERMINISTIC_5b4364c051cb3ff0
Batch ID: 20250612_153713
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This Python code demonstrates how to set up a WiFi-controlled foam dart turret using Raspberry Pi.
It uses Flask for the web API, pigpio for GPIO control, and requests for HTTP communication.
You will need to install Flask and pigpio before running this script.
"""

from flask import Flask, request, jsonify
import pigpio
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

# GPIO Pin configuration
SERVO_PIN_HORIZONTAL = 17  # Pin connected to horizontal servo
SERVO_PIN_VERTICAL = 18    # Pin connected to vertical servo
TRIGGER_PIN = 23           # Pin connected to the dart firing mechanism

# Servo movement boundaries (adjust based on your hardware)
SERVO_MIN = 500            # Microseconds for minimum position
SERVO_MAX = 2500           # Microseconds for maximum position

# Initialize pigpio
try:
    pi = pigpio.pi()
    if not pi.connected:
        raise RuntimeError("Failed to connect to pigpio daemon")
except Exception as e:
    logging.error(f"Error initializing GPIO: {e}")
    raise

@app.route('/move', methods=['POST'])
def move_servo():
    """
    Endpoint to control servo positions.
    Accepts JSON payload with 'horizontal' and 'vertical' values (range: 0-100).
    """
    try:
        data = request.get_json()
        horizontal = data['horizontal']
        vertical = data['vertical']

        # Validate input range
        if not (0 <= horizontal <= 100 and 0 <= vertical <= 100):
            return jsonify({"error": "Values must be between 0 and 100"}), 400

        # Convert percentage values to pulse widths
        horizontal_pulse = SERVO_MIN + (horizontal / 100) * (SERVO_MAX - SERVO_MIN)
        vertical_pulse = SERVO_MIN + (vertical / 100) * (SERVO_MAX - SERVO_MIN)

        # Move servos
        pi.set_servo_pulsewidth(SERVO_PIN_HORIZONTAL, horizontal_pulse)
        pi.set_servo_pulsewidth(SERVO_PIN_VERTICAL, vertical_pulse)

        logging.info(f"Moved servos: Horizontal={horizontal_pulse}, Vertical={vertical_pulse}")
        return jsonify({"message": "Servos moved successfully"}), 200
    except Exception as e:
        logging.error(f"Error moving servos: {e}")
        return jsonify({"error": "Failed to move servos"}), 500

@app.route('/fire', methods=['POST'])
def fire_dart():
    """
    Endpoint to fire a foam dart.
    Accepts JSON payload with 'duration' value (milliseconds).
    """
    try:
        data = request.get_json()
        duration = data.get('duration', 500)  # Default firing duration: 500ms

        # Validate duration
        if not (100 <= duration <= 2000):
            return jsonify({"error": "Duration must be between 100 and 2000 milliseconds"}), 400

        # Trigger firing mechanism
        pi.write(TRIGGER_PIN, 1)
        pi.set_PWM_dutycycle(TRIGGER_PIN,255)# For PWM control
        pi.sleep(duration / 1000.0)
        pi.write(TRIGGER_PIN, 0)

        logging.info(f"Fired dart for {duration} milliseconds")
        return jsonify({"message": f"Dart fired for {duration}ms"}), 200
    except Exception as e:
        logging.error(f"Error firing dart: {e}")
        return jsonify({"error": "Failed to fire dart"}), 500

if __name__ == "__main__":
    # Ensure servo pins are initialized properly
    try:
        pi.set_mode(SERVO_PIN_HORIZONTAL, pigpio.OUTPUT)
        pi.set_mode(SERVO_PIN_VERTICAL, pigpio.OUTPUT)
        pi.set_mode(TRIGGER_PIN, pigpio.OUTPUT)
        logging.info("GPIO pins initialized")
    except Exception as e:
        logging.error(f"Failed to initialize GPIO pins: {e}")
        raise

    # Run Flask app
    logging.info("Starting Flask server...")
    app.run(host='0.0.0.0', port=5000)
```

**Before running:**
1. Install required libraries: `pip install flask pigpio`.
2. Ensure the `pigpio` daemon is running (`sudo pigpiod`).
3. Adjust GPIO pin numbers and servo pulse ranges based on your hardware setup.
4. Connect Raspberry Pi to a WiFi network for remote control.
