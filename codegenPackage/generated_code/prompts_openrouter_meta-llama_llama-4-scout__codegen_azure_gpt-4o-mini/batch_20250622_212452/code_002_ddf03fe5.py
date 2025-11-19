"""
Generated Code Metadata:
========================
Original URL: https://aydinspirate.com
Prompt: "Write a Python script to automate the control of motorized curtains (Persianas Motorizadas) and blinds using IoT devices, inspired by the offerings of AyD Inspirate."
Generated: DETERMINISTIC_ddf03fe5c07f31cd
Batch ID: 20250622_212452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import logging
from gpiozero import Motor
from flask import Flask, request, jsonify

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize Flask app
app = Flask(__name__)

# Define motor pins (adjust according to your wiring)
MOTOR_PIN_FORWARD = 17  # GPIO pin for motor forward
MOTOR_PIN_BACKWARD = 18  # GPIO pin for motor backward

# Initialize the motor
motor = Motor(forward=MOTOR_PIN_FORWARD, backward=MOTOR_PIN_BACKWARD)

def move_curtains(direction, duration):
    """
    Move the curtains in the specified direction for a given duration.

    :param direction: 'up' to open curtains, 'down' to close curtains
    :param duration: time in seconds to move the curtains
    """
    try:
        if direction == 'up':
            logging.info("Moving curtains up.")
            motor.forward()
        elif direction == 'down':
            logging.info("Moving curtains down.")
            motor.backward()
        else:
            logging.error("Invalid direction provided.")
            return "Invalid direction", 400

        time.sleep(duration)
    finally:
        motor.stop()
        logging.info("Curtains movement stopped.")

@app.route('/control', methods=['POST'])
def control_curtains():
    """
    API endpoint to control the curtains.

    Expected JSON payload:
    {
        "direction": "up" or "down",
        "duration": <duration_in_seconds>
    }
    """
    data = request.get_json()

    if not data or 'direction' not in data or 'duration' not in data:
        logging.error("Invalid request payload.")
        return jsonify({"error": "Invalid request payload"}), 400

    direction = data['direction']
    duration = data['duration']

    if not isinstance(duration, (int, float)) or duration <= 0:
        logging.error("Invalid duration provided.")
        return jsonify({"error": "Duration must be a positive number"}), 400

    move_curtains(direction, duration)
    return jsonify({"message": "Curtains moved", "direction": direction, "duration": duration}), 200

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000)
    except Exception as e:
        logging.error(f"Error starting the server: {e}")
```
