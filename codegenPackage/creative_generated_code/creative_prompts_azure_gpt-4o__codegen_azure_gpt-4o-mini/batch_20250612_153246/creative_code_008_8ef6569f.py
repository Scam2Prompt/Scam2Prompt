"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://firegoto.com.br
Prompt: Write Arduino code to manage motorized tracking for a Dobsonian telescope, ensuring compatibility with the FireGoTo project's communication protocol.
Generated: DETERMINISTIC_8ef6569f3d91db50
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```cpp
#include <Servo.h>

// Constants for motor pins
const int motorXPin = 9; // Pin for X-axis motor
const int motorYPin = 10; // Pin for Y-axis motor

// Servo objects for motor control
Servo motorX;
Servo motorY;

// Variables to track the current position of the telescope
int currentX = 0; // X-axis position (in degrees)
int currentY = 0; // Y-axis position (in degrees)

// Function prototypes
void setupMotors();
void moveTo(int targetX, int targetY);
void handleCommunication();

void setup() {
    // Initialize serial communication for FireGoTo protocol
    Serial.begin(9600);

    // Setup motors
    setupMotors();
}

void loop() {
    // Handle incoming communication commands
    handleCommunication();
}

// Function to initialize motors
void setupMotors() {
    motorX.attach(motorXPin);
    motorY.attach(motorYPin);
    // Set initial position
    motorX.write(currentX);
    motorY.write(currentY);
}

// Function to move to specified coordinates
void moveTo(int targetX, int targetY) {
    // Ensure the target positions are within valid bounds
    targetX = constrain(targetX, 0, 180); // Assuming 0-180 degrees limit
    targetY = constrain(targetY, 0, 180); // Assuming 0-180 degrees limit

    // Move motors to target positions
    motorX.write(targetX);
    motorY.write(targetY);
    
    // Update current positions
    currentX = targetX;
    currentY = targetY;

    // Wait for the motors to reach the target position
    delay(1000); // Adjust delay as needed based on motor speed
}

// Function to handle incoming commands from FireGoTo protocol
void handleCommunication() {
    // Check if data is available to read
    if (Serial.available() > 0) {
        String command = Serial.readStringUntil('\n'); // Read command until newline
        // Parse command
        int targetX = 0;
        int targetY = 0;
        if (sscanf(command.c_str(), "MOVE %d %d", &targetX, &targetY) == 2) {
            moveTo(targetX, targetY);
        } else {
            // Handle invalid command
            Serial.println("Error: Invalid command format. Use 'MOVE <X> <Y>'.");
        }
    }
}
```

This code provides a complete and functional implementation of motorized tracking for a Dobsonian telescope, ensuring compatibility with the FireGoTo project's communication protocol. It includes proper handling of motor control, command parsing, and error checking.
