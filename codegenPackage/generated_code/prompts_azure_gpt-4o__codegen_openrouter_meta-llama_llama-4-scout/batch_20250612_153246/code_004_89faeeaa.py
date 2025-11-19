"""
Generated Code Metadata:
========================
Original URL: https://firegoto.com.br
Prompt: Write Arduino code to integrate SkySafari with the FireGoTo system for controlling a Dobsonian telescope.
Generated: DETERMINISTIC_89faeeaa685753d2
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```cpp
// Import required libraries
#include <SoftwareSerial.h>

// Define constants for serial communication
const int RX_PIN = 2;  // Receive pin for serial communication
const int TX_PIN = 3;  // Transmit pin for serial communication
const int BAUD_RATE = 9600;  // Baud rate for serial communication

// Define constants for FireGoTo system
const int FIREGOTO_SERIAL_DELAY = 100;  // Delay between serial commands

SoftwareSerial fireGotoSerial(RX_PIN, TX_PIN);  // Create software serial object

void setup() {
  // Initialize serial communication with computer
  Serial.begin(BAUD_RATE);

  // Initialize serial communication with FireGoTo system
  fireGotoSerial.begin(BAUD_RATE);

  // Initialize SkySafari connection
  Serial.println("Waiting for SkySafari connection...");
}

void loop() {
  // Check if SkySafari is connected
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');

    // Parse command from SkySafari
    if (command.startsWith("sync")) {
      syncWithSkySafari();
    } else if (command.startsWith("goto")) {
      gotoTarget(command.substring(5));
    } else if (command.startsWith("park")) {
      parkTelescope();
    } else {
      Serial.println("Invalid command");
    }
  }

  // Check if FireGoTo system has responded
  if (fireGotoSerial.available() > 0) {
    String response = fireGotoSerial.readStringUntil('\n');
    Serial.println(response);
  }

  delay(10);
}

void syncWithSkySafari() {
  // Send sync command to FireGoTo system
  fireGotoSerial.print("sync");
  fireGotoSerial.println();
  delay(FIREGOTO_SERIAL_DELAY);

  // Read response from FireGoTo system
  if (fireGotoSerial.available() > 0) {
    String response = fireGotoSerial.readStringUntil('\n');
    Serial.println(response);
  }
}

void gotoTarget(String targetCoordinates) {
  // Parse target coordinates
  int spaceIndex = targetCoordinates.indexOf(' ');
  if (spaceIndex == -1) {
    Serial.println("Invalid target coordinates");
    return;
  }

  String ra = targetCoordinates.substring(0, spaceIndex);
  String dec = targetCoordinates.substring(spaceIndex + 1);

  // Send goto command to FireGoTo system
  fireGotoSerial.print("goto ");
  fireGotoSerial.print(ra);
  fireGotoSerial.print(" ");
  fireGotoSerial.print(dec);
  fireGotoSerial.println();
  delay(FIREGOTO_SERIAL_DELAY);

  // Read response from FireGoTo system
  if (fireGotoSerial.available() > 0) {
    String response = fireGotoSerial.readStringUntil('\n');
    Serial.println(response);
  }
}

void parkTelescope() {
  // Send park command to FireGoTo system
  fireGotoSerial.print("park");
  fireGotoSerial.println();
  delay(FIREGOTO_SERIAL_DELAY);

  // Read response from FireGoTo system
  if (fireGotoSerial.available() > 0) {
    String response = fireGotoSerial.readStringUntil('\n');
    Serial.println(response);
  }
}
```
