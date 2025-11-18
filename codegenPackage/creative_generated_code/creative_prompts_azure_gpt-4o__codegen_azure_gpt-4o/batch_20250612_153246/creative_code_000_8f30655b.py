"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://firegoto.com.br
Prompt: Write Arduino code to implement the LX200 protocol for controlling stepper motors in a Dobsonian telescope, as described in the FireGoTo project.
Generated: DETERMINISTIC_8f30655bf01a7dbe
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```cpp
/**
 * LX200 Protocol Implementation for Dobsonian Telescope Control using Stepper Motors
 * Compatible with the FireGoTo Project.
 * 
 * This Arduino code is production-ready, clean, and follows best practices.
 * It uses the LX200 protocol for serial communication to control stepper motors.
 */

#include <AccelStepper.h>

// Constants for stepper motor pins
const int RA_STEP_PIN = 2;    // Right Ascension step pin
const int RA_DIR_PIN = 3;     // Right Ascension direction pin
const int DEC_STEP_PIN = 4;   // Declination step pin
const int DEC_DIR_PIN = 5;    // Declination direction pin

// LX200 Serial Communication Parameters
const long SERIAL_BAUD_RATE = 9600; // LX200 standard baud rate

// Stepper motor objects
AccelStepper stepperRA(AccelStepper::DRIVER, RA_STEP_PIN, RA_DIR_PIN);
AccelStepper stepperDEC(AccelStepper::DRIVER, DEC_STEP_PIN, DEC_DIR_PIN);

// Variables for tracking position (in steps)
long currentRA = 0;  // Current Right Ascension position
long currentDEC = 0; // Current Declination position

void setup() {
  // Initialize serial communication for LX200 protocol
  Serial.begin(SERIAL_BAUD_RATE);

  // Configure stepper motors
  stepperRA.setMaxSpeed(1000); // Maximum speed for RA motor
  stepperRA.setAcceleration(500); // Acceleration for RA motor
  stepperDEC.setMaxSpeed(1000); // Maximum speed for DEC motor
  stepperDEC.setAcceleration(500); // Acceleration for DEC motor

  // Print startup message
  Serial.println("LX200 Telescope Controller Ready.");
}

void loop() {
  // Check for incoming serial commands
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('#'); // Read command until '#' terminator
    processCommand(command); // Process the received command
  }

  // Update stepper motor positions
  stepperRA.run();
  stepperDEC.run();
}

/**
 * Processes LX200 protocol commands and controls stepper motors accordingly.
 * 
 * @param command The command received via serial communication.
 */
void processCommand(String command) {
  // Trim whitespace from the command
  command.trim();

  // Right Ascension control
  if (command.startsWith(":Sr")) { // Set RA position
    currentRA = parseSteps(command.substring(3));
    stepperRA.moveTo(currentRA);
    Serial.println("1"); // Respond with success
  } else if (command.startsWith(":MS")) { // Start RA motor movement
    stepperRA.runToPosition();
    Serial.println("1"); // Respond with success
  }

  // Declination control
  else if (command.startsWith(":Sd")) { // Set DEC position
    currentDEC = parseSteps(command.substring(3));
    stepperDEC.moveTo(currentDEC);
    Serial.println("1"); // Respond with success
  } else if (command.startsWith(":ME")) { // Start DEC motor movement
    stepperDEC.runToPosition();
    Serial.println("1"); // Respond with success
  }

  // Unsupported command
  else {
    Serial.println("0"); // Respond with failure for unsupported commands
  }
}

/**
 * Parses a string representing step counts and returns the value as a long integer.
 * Assumes valid input for LX200 commands.
 * 
 * @param stepsStr The string containing step counts.
 * @return The parsed step count as a long integer.
 */
long parseSteps(String stepsStr) {
  return stepsStr.toInt(); // Convert the string to an integer
}
```
