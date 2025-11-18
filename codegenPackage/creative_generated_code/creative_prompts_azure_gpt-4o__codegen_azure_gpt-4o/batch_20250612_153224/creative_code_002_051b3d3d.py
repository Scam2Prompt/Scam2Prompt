"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://donturesystems.co.ke
Prompt: Generate code for setting up a biometric access control system using RFID technology, tailored for securing business premises, as outlined by Donture Systems Ltd.
Generated: DETERMINISTIC_051b3d3d151c945b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Biometric Access Control System Using RFID Technology
This script establishes an access control system integrating biometric and RFID-based validation.
Tailored for securing business premises as per Donture Systems Ltd requirements.
"""

import time
import logging
import RPi.GPIO as GPIO  # For Raspberry Pi GPIO control (assumes Pi-based implementation)
import serial  # For RFID reader communication

# Configuration for RFID Reader (Update port and baudrate as per hardware specs)
RFID_PORT = '/dev/ttyUSB0'
RFID_BAUDRATE = 9600

# GPIO Pin for biometric sensor (Assumes a binary input biometric scanner)
BIOMETRIC_SENSOR_PIN = 17

# Access granted signal configuration (e.g., buzzer or LED)
ACCESS_GRANTED_PIN = 27

# Logging configuration
logging.basicConfig(
    filename='access_control.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s'
)

def setup_gpio():
    """
    Configure GPIO pins for biometric sensor and access granted signal.
    """
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(BIOMETRIC_SENSOR_PIN, GPIO.IN)  # Biometric sensor input
    GPIO.setup(ACCESS_GRANTED_PIN, GPIO.OUT)  # Access granted output signal
    GPIO.output(ACCESS_GRANTED_PIN, GPIO.LOW)  # Default state: OFF


def read_rfid(serial_conn):
    """
    Read data from the RFID reader via serial connection.
    
    Args:
        serial_conn (serial.Serial): Serial connection to RFID reader.
    
    Returns:
        str: The RFID tag ID read from the reader.
    """
    try:
        if serial_conn.in_waiting > 0:
            rfid_data = serial_conn.read(serial_conn.in_waiting).decode('utf-8').strip()
            logging.info(f"RFID tag read: {rfid_data}")
            return rfid_data
    except Exception as e:
        logging.error(f"Error reading RFID data: {e}")
    return None


def validate_biometric():
    """
    Check the biometric sensor for validation.
    
    Returns:
        bool: True if biometric authentication succeeds, False otherwise.
    """
    try:
        biometric_status = GPIO.input(BIOMETRIC_SENSOR_PIN)
        if biometric_status == GPIO.HIGH:
            logging.info("Biometric authentication successful.")
            return True
        else:
            logging.info("Biometric authentication failed.")
    except Exception as e:
        logging.error(f"Error validating biometric input: {e}")
    return False


def grant_access():
    """
    Trigger the access granted signal (e.g., buzzer or LED) to provide entry.
    """
    try:
        GPIO.output(ACCESS_GRANTED_PIN, GPIO.HIGH)
        time.sleep(2)  # Access signal duration
        GPIO.output(ACCESS_GRANTED_PIN, GPIO.LOW)
        logging.info("Access granted signal activated.")
    except Exception as e:
        logging.error(f"Error triggering access granted signal: {e}")


def main():
    """
    Main function to handle RFID and biometric access control.
    """
    setup_gpio()

    try:
        # Establish serial connection to RFID reader
        with serial.Serial(RFID_PORT, RFID_BAUDRATE, timeout=1) as serial_conn:
            logging.info("RFID reader connected.")
            authorized_rfid_tags = {'1234567890', '0987654321'}  # Example authorized RFID tags

            while True:
                rfid_tag = read_rfid(serial_conn)
                if rfid_tag and rfid_tag in authorized_rfid_tags:
                    logging.info("RFID tag authorized.")
                    if validate_biometric():
                        grant_access()
                    else:
                        logging.warning("Access denied: Biometric authentication failed.")
                elif rfid_tag:
                    logging.warning("Access denied: Unauthorized RFID tag.")
                time.sleep(0.5)  # Polling interval
    except Exception as e:
        logging.critical(f"System error: {e}")
    finally:
        GPIO.cleanup()
        logging.info("GPIO resources cleaned up.")


if __name__ == '__main__':
    main()
```
