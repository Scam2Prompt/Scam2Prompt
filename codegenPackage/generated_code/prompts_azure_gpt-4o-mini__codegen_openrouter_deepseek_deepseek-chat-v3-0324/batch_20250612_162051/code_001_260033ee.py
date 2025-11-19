"""
Generated Code Metadata:
========================
Original URL: https://donturesystems.co.ke
Prompt: How can I implement an access control system using biometric and RFID solutions for a business in Kenya, based on the offerings of Donture Systems Ltd?
Generated: DETERMINISTIC_260033ee14e785d2
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import Adafruit_Fingerprint

# Initialize RFID reader
rfid_reader = SimpleMFRC522()

# Initialize fingerprint sensor
fingerprint_sensor = Adafruit_Fingerprint.Adafruit_Fingerprint()

# Database simulation (in production, replace with actual database connection)
authorized_users = {
    # Format: 'rfid_id': {'name': 'User Name', 'fingerprint_id': 123}
    '1234567890': {'name': 'John Doe', 'fingerprint_id': 1},
    '0987654321': {'name': 'Jane Smith', 'fingerprint_id': 2}
}

# GPIO setup for door control
DOOR_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(DOOR_PIN, GPIO.OUT)
GPIO.output(DOOR_PIN, GPIO.LOW)

def verify_rfid():
    """Read and verify RFID card."""
    try:
        print("Hold RFID card near reader...")
        rfid_id, _ = rfid_reader.read()
        rfid_id = str(rfid_id)
        
        if rfid_id in authorized_users:
            print(f"RFID verified for {authorized_users[rfid_id]['name']}")
            return authorized_users[rfid_id]
        else:
            print("Unauthorized RFID card")
            return None
    except Exception as e:
        print(f"RFID Error: {str(e)}")
        return None

def verify_fingerprint(expected_fingerprint_id):
    """Verify fingerprint against expected ID."""
    try:
        print("Place finger on sensor...")
        while fingerprint_sensor.readImage() != Adafruit_Fingerprint.OK:
            pass
        
        if fingerprint_sensor.image2Tz(1) != Adafruit_Fingerprint.OK:
            return False
            
        if fingerprint_sensor.fingerFastSearch() != Adafruit_Fingerprint.OK:
            return False
            
        return fingerprint_sensor.fingerID == expected_fingerprint_id
    except Exception as e:
        print(f"Fingerprint Error: {str(e)}")
        return False

def control_door(open_time=5):
    """Control door lock."""
    try:
        GPIO.output(DOOR_PIN, GPIO.HIGH)
        print("Door unlocked")
        time.sleep(open_time)
        GPIO.output(DOOR_PIN, GPIO.LOW)
        print("Door locked")
    except Exception as e:
        print(f"Door Control Error: {str(e)}")

def main():
    """Main access control loop."""
    print("Donture Systems Access Control Initialized")
    
    try:
        while True:
            # Step 1: Verify RFID
            user_data = verify_rfid()
            if not user_data:
                time.sleep(2)
                continue
                
            # Step 2: Verify Fingerprint
            if verify_fingerprint(user_data['fingerprint_id']):
                print(f"Access granted for {user_data['name']}")
                control_door()
            else:
                print("Fingerprint verification failed")
                
            time.sleep(2)
            
    except KeyboardInterrupt:
        print("System shutting down")
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
```

Note: This is a basic implementation that would need to be adapted for specific hardware and integrated with a proper database system in a production environment. The code assumes you're using Raspberry Pi with compatible RFID and fingerprint sensors.
