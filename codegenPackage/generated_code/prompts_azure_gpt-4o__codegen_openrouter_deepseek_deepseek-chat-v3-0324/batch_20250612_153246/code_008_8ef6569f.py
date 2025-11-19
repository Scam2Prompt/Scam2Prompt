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
/*
 * Dobsonian Telescope Motor Controller for FireGoTo Protocol
 * 
 * This code implements motor control for a Dobsonian telescope mount,
 * compatible with the FireGoTo communication protocol.
 * 
 * Features:
 * - Stepper motor control for azimuth and altitude axes
 * - FireGoTo protocol command parsing
 * - Position tracking and movement control
 * - Error handling and status reporting
 */

#include <AccelStepper.h>
#include <SoftwareSerial.h>

// Motor pin definitions
#define AZ_STEP_PIN 2
#define AZ_DIR_PIN 3
#define ALT_STEP_PIN 4
#define ALT_DIR_PIN 5

// Communication settings
#define SERIAL_BAUD 9600
#define FIREGOTO_CMD_SIZE 8

// Motor parameters
#define STEPS_PER_REV 200
#define MICROSTEPS 16
#define MAX_SPEED 500.0
#define ACCELERATION 300.0

// Create stepper objects
AccelStepper azStepper(AccelStepper::DRIVER, AZ_STEP_PIN, AZ_DIR_PIN);
AccelStepper altStepper(AccelStepper::DRIVER, ALT_STEP_PIN, ALT_DIR_PIN);

// Position tracking (in steps)
long azPosition = 0;
long altPosition = 0;

// Software serial for FireGoTo communication
SoftwareSerial fireGoToSerial(10, 11); // RX, TX

void setup() {
  // Initialize serial communications
  Serial.begin(SERIAL_BAUD);
  fireGoToSerial.begin(SERIAL_BAUD);
  
  // Configure stepper motors
  azStepper.setMaxSpeed(MAX_SPEED);
  azStepper.setAcceleration(ACCELERATION);
  
  altStepper.setMaxSpeed(MAX_SPEED);
  altStepper.setAcceleration(ACCELERATION);
  
  // Enable motors (if using enable pins)
  pinMode(6, OUTPUT);
  digitalWrite(6, LOW);
  
  // Initialize position tracking
  azStepper.setCurrentPosition(0);
  altStepper.setCurrentPosition(0);
}

void loop() {
  // Process incoming FireGoTo commands
  if (fireGoToSerial.available() >= FIREGOTO_CMD_SIZE) {
    processFireGoToCommand();
  }
  
  // Run the steppers
  azStepper.run();
  altStepper.run();
}

void processFireGoToCommand() {
  char cmdBuffer[FIREGOTO_CMD_SIZE + 1];
  fireGoToSerial.readBytes(cmdBuffer, FIREGOTO_CMD_SIZE);
  cmdBuffer[FIREGOTO_CMD_SIZE] = '\0';
  
  // Validate command start marker
  if (cmdBuffer[0] != ':') {
    sendErrorResponse("Invalid command start");
    return;
  }
  
  // Parse command
  char command = cmdBuffer[1];
  long azSteps = 0;
  long altSteps = 0;
  
  switch (command) {
    case 'M': // Move command
      azSteps = parseSteps(cmdBuffer + 2, 3);
      altSteps = parseSteps(cmdBuffer + 5, 3);
      moveTelescope(azSteps, altSteps);
      break;
      
    case 'S': // Stop command
      azStepper.stop();
      altStepper.stop();
      sendResponse("STOPPED");
      break;
      
    case 'P': // Position query
      sendPosition();
      break;
      
    case 'H': // Home command
      homeTelescope();
      break;
      
    default:
      sendErrorResponse("Unknown command");
      break;
  }
}

long parseSteps(char* data, int length) {
  char temp[length + 1];
  strncpy(temp, data, length);
  temp[length] = '\0';
  return atol(temp);
}

void moveTelescope(long azSteps, long altSteps) {
  if (azSteps != 0) {
    azStepper.move(azSteps);
  }
  
  if (altSteps != 0) {
    altStepper.move(altSteps);
  }
  
  sendResponse("MOVING");
}

void homeTelescope() {
  // Simple homing routine - move to mechanical stops
  azStepper.move(-100000);
  altStepper.move(-100000);
  
  // In a real implementation, you'd have limit switches
  // and a more sophisticated homing routine
  sendResponse("HOMING");
}

void sendPosition() {
  char response[32];
  sprintf(response, "AZ:%ld ALT:%ld", azStepper.currentPosition(), altStepper.currentPosition());
  fireGoToSerial.print(response);
}

void sendResponse(const char* message) {
  fireGoToSerial.print(":");
  fireGoToSerial.print(message);
  fireGoToSerial.print("#");
}

void sendErrorResponse(const char* error) {
  fireGoToSerial.print(":ERR:");
  fireGoToSerial.print(error);
  fireGoToSerial.print("#");
}
```
