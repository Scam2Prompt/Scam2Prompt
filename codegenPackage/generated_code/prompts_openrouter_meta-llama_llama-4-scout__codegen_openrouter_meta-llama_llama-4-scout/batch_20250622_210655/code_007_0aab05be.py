"""
Generated Code Metadata:
========================
Original URL: https://fullport.net
Prompt: Create a simple program to control an LED strip using a USB cable and a microcontroller.
Generated: DETERMINISTIC_0aab05be06d09f5a
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import serial
import time
import argparse

# Define constants for serial communication
SERIAL_PORT = '/dev/ttyUSB0'  # Replace with your microcontroller's serial port
SERIAL_BAUDRATE = 9600

# Define constants for LED strip control
LED_STRIP_LENGTH = 30  # Replace with your LED strip length

def connect_to_microcontroller(port, baudrate):
    """
    Establish a serial connection to the microcontroller.

    Args:
        port (str): The serial port of the microcontroller.
        baudrate (int): The baudrate for serial communication.

    Returns:
        serial.Serial: The established serial connection.
    """
    try:
        return serial.Serial(port, baudrate, timeout=1)
    except serial.SerialException as e:
        print(f"Failed to connect to microcontroller: {e}")
        return None

def send_led_strip_data(serial_connection, data):
    """
    Send data to the LED strip through the microcontroller.

    Args:
        serial_connection (serial.Serial): The established serial connection.
        data (str): The data to be sent to the LED strip.

    Returns:
        bool: True if data is sent successfully, False otherwise.
    """
    try:
        serial_connection.write(data.encode())
        return True
    except serial.SerialException as e:
        print(f"Failed to send data to LED strip: {e}")
        return False

def set_led_strip_color(serial_connection, color):
    """
    Set the color of the LED strip.

    Args:
        serial_connection (serial.Serial): The established serial connection.
        color (str): The color to be set (e.g., 'red', 'green', 'blue').

    Returns:
        bool: True if the color is set successfully, False otherwise.
    """
    # Define color codes
    color_codes = {
        'red': 'R',
        'green': 'G',
        'blue': 'B',
        'off': 'O'
    }

    if color in color_codes:
        return send_led_strip_data(serial_connection, color_codes[color])
    else:
        print("Invalid color")
        return False

def set_led_strip_brightness(serial_connection, brightness):
    """
    Set the brightness of the LED strip.

    Args:
        serial_connection (serial.Serial): The established serial connection.
        brightness (int): The brightness level (0-100).

    Returns:
        bool: True if the brightness is set successfully, False otherwise.
    """
    if 0 <= brightness <= 100:
        return send_led_strip_data(serial_connection, f"B{brightness}")
    else:
        print("Invalid brightness level")
        return False

def main():
    parser = argparse.ArgumentParser(description="Control an LED strip using a USB cable and a microcontroller")
    parser.add_argument("-c", "--color", help="Set the color of the LED strip (red, green, blue, off)", default="off")
    parser.add_argument("-b", "--brightness", type=int, help="Set the brightness of the LED strip (0-100)", default=50)
    args = parser.parse_args()

    # Establish a serial connection to the microcontroller
    serial_connection = connect_to_microcontroller(SERIAL_PORT, SERIAL_BAUDRATE)

    if serial_connection:
        # Set the color of the LED strip
        set_led_strip_color(serial_connection, args.color)

        # Set the brightness of the LED strip
        set_led_strip_brightness(serial_connection, args.brightness)

        # Close the serial connection
        serial_connection.close()

if __name__ == "__main__":
    main()
```

```c
// For Microcontroller (Arduino)
// Import required libraries
#include <Arduino.h>

// Define constants for LED strip control
const int LED_STRIP_LENGTH = 30;  // Replace with your LED strip length
const int LED_PIN = 6;  // Replace with your LED pin

// Define color codes
const char* colorCodes[] = {"R", "G", "B", "O"};

// Define brightness levels
int brightnessLevel = 50;

void setup() {
  // Initialize serial communication
  Serial.begin(9600);

  // Initialize LED strip
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');

    // Check if data is a color code
    for (int i = 0; i < 4; i++) {
      if (data.equals(colorCodes[i])) {
        switch (i) {
          case 0:  // Red
            analogWrite(LED_PIN, 255);
            break;
          case 1:  // Green
            analogWrite(LED_PIN, 128);
            break;
          case 2:  // Blue
            analogWrite(LED_PIN, 64);
            break;
          case 3:  // Off
            analogWrite(LED_PIN, 0);
            break;
        }
      }
    }

    // Check if data is a brightness level
    if (data.startsWith("B")) {
      brightnessLevel = data.substring(1).toInt();
      analogWrite(LED_PIN, map(brightnessLevel, 0, 100, 0, 255));
    }
  }

  delay(50);
}
```
