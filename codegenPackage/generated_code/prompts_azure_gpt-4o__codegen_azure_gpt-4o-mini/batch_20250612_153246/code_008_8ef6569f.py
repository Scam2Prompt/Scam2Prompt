"""
Generated Code Metadata:
========================
Original URL: https://firegoto.com.br
Prompt: Write Arduino code to manage motorized tracking for a Dobsonian telescope, ensuring compatibility with the FireGoTo project's communication protocol.
Generated: DETERMINISTIC_8ef6569f3d91db50
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```cpp
#include <Servo.h>

// Constants for motor control
const int azimuthMotorPin = 9;  // Pin for azimuth motor
const int altitudeMotorPin = 10; // Pin for altitude motor

// Servo objects for controlling motors
Servo azimuthMotor;
Servo altitudeMotor;

// Variables to store target positions
float targetAzimuth = 0.0;   // Target azimuth angle in degrees
float targetAltitude = 0.0;  // Target altitude angle in degrees

// Function to initialize motors
void setup() {
    Serial.begin(9600); // Start serial communication at 9600 baud
    azimuthMotor.attach(azimuthMotorPin); // Attach azimuth motor to pin
    altitudeMotor.attach(altitudeMotorPin); // Attach altitude motor to pin

    // Initialize motors to a default position
    azimuthMotor.write(90); // Set azimuth to 90 degrees (center)
    altitudeMotor.write(90); // Set altitude to 90 degrees (center)
}

// Function to read incoming commands
void loop() {
    if (Serial.available() > 0) {
        String command = Serial.readStringUntil('\n'); // Read command until newline
        processCommand(command); // Process the received command
    }
}

// Function to process received commands
void processCommand(String command) {
    // Example command format: "GOTO 180 45"
    if (command.startsWith("GOTO")) {
        int spaceIndex1 = command.indexOf(' ', 5);
        int spaceIndex2 = command.indexOf(' ', spaceIndex1 + 1);

        if (spaceIndex1 > 0 && spaceIndex2 > spaceIndex1) {
            // Extract azimuth and altitude values
            String azimuthStr = command.substring(5, spaceIndex1);
            String altitudeStr = command.substring(spaceIndex1 + 1, spaceIndex2);

            // Convert strings to float
            targetAzimuth = azimuthStr.toFloat();
            targetAltitude = altitudeStr.toFloat();

            // Validate angles
            if (isValidAngle(targetAzimuth) && isValidAngle(targetAltitude)) {
                moveToTarget(targetAzimuth, targetAltitude); // Move to target position
            } else {
                Serial.println("Error: Invalid angle values.");
            }
        } else {
            Serial.println("Error: Command format is incorrect.");
        }
    } else {
        Serial.println("Error: Unknown command.");
    }
}

// Function to validate angle values
bool isValidAngle(float angle) {
    return (angle >= 0 && angle <= 360); // Valid range for angles
}

// Function to move motors to target positions
void moveToTarget(float azimuth, float altitude) {
    // Move azimuth motor
    int azimuthPosition = map(azimuth, 0, 360, 0, 180); // Map to servo range
    azimuthMotor.write(azimuthPosition); // Set azimuth motor position

    // Move altitude motor
    int altitudePosition = map(altitude, 0, 90, 0, 180); // Map to servo range
    altitudeMotor.write(altitudePosition); // Set altitude motor position

    // Provide feedback
    Serial.print("Moving to Azimuth: ");
    Serial.print(azimuth);
    Serial.print(", Altitude: ");
    Serial.println(altitude);
}
```
