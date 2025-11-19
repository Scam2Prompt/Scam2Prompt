"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stethevent.org
Prompt: What are some step-by-step instructions for building a WiFi-controlled foam dart turret using Raspberry Pi from Stethevent?
Generated: DETERMINISTIC_6221bd6cd50785e1
Batch ID: 20250612_162548
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is the Python code to control a foam dart turret using a Raspberry Pi over WiFi. It assumes you have a servo motor for aiming, a relay or solenoid for firing, and a web server to handle WiFi commands.

```python
# Import necessary libraries
import RPi.GPIO as GPIO  # Library for GPIO control
from flask import Flask, request, jsonify  # Flask for WiFi-controlled web server

# Setup Flask app
app = Flask(__name__)

# Pin configuration
SERVO_PIN = 18  # GPIO pin for servo motor
FIRE_PIN = 23   # GPIO pin for firing mechanism (relay/solenoid)

# Servo settings
SERVO_PWM_FREQUENCY = 50  # Servo PWM frequency (Hz)
SERVO_MIN_DUTY = 2.5      # Minimum duty cycle for servo (adjust as needed)
SERVO_MAX_DUTY = 12.5     # Maximum duty cycle for servo (adjust as needed)

# Setup GPIO pins
GPIO.setmode(GPIO.BCM)          # Use Broadcom pin numbering
GPIO.setup(SERVO_PIN, GPIO.OUT) # Set SERVO_PIN as output
GPIO.setup(FIRE_PIN, GPIO.OUT)  # Set FIRE_PIN as output
GPIO.output(FIRE_PIN, GPIO.LOW) # Ensure firing mechanism is initially off

# Initialize PWM for servo motor
servo = GPIO.PWM(SERVO_PIN, SERVO_PWM_FREQUENCY)  # Create PWM instance
servo.start(SERVO_MIN_DUTY)  # Start PWM with minimum duty cycle

# Helper function to move the servo motor to a specific angle
def move_servo(angle):
    """
    Move the servo motor to the specified angle.

    :param angle: Desired angle (0 to 180 degrees)
    """
    if 0 <= angle <= 180:
        duty_cycle = SERVO_MIN_DUTY + (angle / 180) * (SERVO_MAX_DUTY - SERVO_MIN_DUTY)
        servo.ChangeDutyCycle(duty_cycle)
    else:
        raise ValueError("Angle must be between 0 and 180 degrees.")

# Helper function to fire dart
def fire_dart():
    """
    Activate the firing mechanism to fire a dart.
    """
    GPIO.output(FIRE_PIN, GPIO.HIGH)  # Turn on firing mechanism
    time.sleep(0.5)                  # Wait 0.5 seconds
    GPIO.output(FIRE_PIN, GPIO.LOW)  # Turn off firing mechanism

# Route to control servo position
@app.route('/move_servo', methods=['POST'])
def handle_move_servo():
    """
    API endpoint to move the servo motor.

    Expected JSON input: {"angle": <desired_angle>}
    """
    try:
        data = request.json
        angle = data.get('angle')
        if angle is None:
            return jsonify({"error": "Missing 'angle' parameter"}), 400
        move_servo(angle)
        return jsonify({"message": f"Servo moved to angle {angle}."}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": f"Failed to move servo: {str(e)}"}), 500

# Route to fire dart
@app.route('/fire', methods=['POST'])
def handle_fire():
    """
    API endpoint to fire the dart.

    No parameters required.
    """
    try:
        fire_dart()
        return jsonify({"message": "Dart fired!"}), 200
    except Exception as e:
        return jsonify({"error": f"Failed to fire dart: {str(e)}"}), 500

# Main function to start the web server
if __name__ == '__main__':
    try:
        print("Starting WiFi-controlled foam dart turret server...")
        app.run(host='0.0.0.0', port=5000)  # Run Flask app on all network interfaces
    except KeyboardInterrupt:
        print("Shutting down server...")
    finally:
        GPIO.cleanup()  # Cleanup GPIO pins
        servo.stop()    # Stop PWM
```

This code sets up a Flask-based web server to control the foam dart turret. You can send POST requests to `/move_servo` with an angle parameter to aim the turret, and to `/fire` to fire a dart. Ensure that hardware components are connected properly, and adjust pin numbers and servo parameters as needed.
