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
/*
 * SkySafari to FireGoTo Interface for Dobsonian Telescope
 * 
 * This code enables communication between SkySafari (via Bluetooth/WiFi)
 * and a FireGoTo system for controlling a Dobsonian telescope.
 * 
 * Features:
 * - Parses SkySafari's LX200 protocol commands
 * - Converts to FireGoTo compatible commands
 * - Handles both azimuth and altitude movements
 * - Includes error checking and safety limits
 */

#include <SoftwareSerial.h>

// Define communication parameters
#define BAUDRATE 9600
#define RX_PIN 10
#define TX_PIN 11

// Define telescope limits (in degrees)
#define MIN_ALTITUDE 5
#define MAX_ALTITUDE 85
#define MIN_AZIMUTH 0
#define MAX_AZIMUTH 360

// Motor control pins
#define AZIMUTH_STEP_PIN 2
#define AZIMUTH_DIR_PIN 3
#define ALTITUDE_STEP_PIN 4
#define ALTITUDE_DIR_PIN 5

// Status LED pins
#define STATUS_LED 13
#define ERROR_LED 12

SoftwareSerial skySafariSerial(RX_PIN, TX_PIN); // RX, TX

// Current telescope position
float currentAzimuth = 0;
float currentAltitude = 0;

// Target position
float targetAzimuth = 0;
float targetAltitude = 0;

// Movement flags
bool isMoving = false;
bool isTracking = false;

void setup() {
  // Initialize serial communication
  Serial.begin(BAUDRATE);
  skySafariSerial.begin(BAUDRATE);
  
  // Initialize motor control pins
  pinMode(AZIMUTH_STEP_PIN, OUTPUT);
  pinMode(AZIMUTH_DIR_PIN, OUTPUT);
  pinMode(ALTITUDE_STEP_PIN, OUTPUT);
  pinMode(ALTITUDE_DIR_PIN, OUTPUT);
  
  // Initialize status LEDs
  pinMode(STATUS_LED, OUTPUT);
  pinMode(ERROR_LED, OUTPUT);
  
  // Home position
  digitalWrite(STATUS_LED, HIGH);
  delay(1000);
  digitalWrite(STATUS_LED, LOW);
  
  Serial.println("FireGoTo Ready");
}

void loop() {
  // Check for incoming commands from SkySafari
  if (skySafariSerial.available()) {
    String command = skySafariSerial.readStringUntil('#');
    processCommand(command);
  }
  
  // Handle movement if needed
  if (isMoving) {
    moveTelescope();
  }
  
  // Handle tracking if enabled
  if (isTracking) {
    updateTracking();
  }
}

void processCommand(String command) {
  command.trim();
  
  if (command.startsWith(":Sr")) {
    // Set target right ascension (converted to azimuth)
    String ra = command.substring(3);
    targetAzimuth = parseCoordinate(ra);
    skySafariSerial.print("1");
    isMoving = true;
  }
  else if (command.startsWith(":Sd")) {
    // Set target declination (converted to altitude)
    String dec = command.substring(3);
    targetAltitude = parseCoordinate(dec);
    if (targetAltitude < MIN_ALTITUDE) targetAltitude = MIN_ALTITUDE;
    if (targetAltitude > MAX_ALTITUDE) targetAltitude = MAX_ALTITUDE;
    skySafariSerial.print("1");
    isMoving = true;
  }
  else if (command.startsWith(":MS")) {
    // Move to target
    skySafariSerial.print("0");
    isMoving = true;
  }
  else if (command.startsWith(":Q")) {
    // Stop movement
    isMoving = false;
    skySafariSerial.print("0");
  }
  else if (command.startsWith(":CM")) {
    // Sync to current position
    skySafariSerial.print("0");
  }
  else if (command.startsWith(":GR")) {
    // Get current RA (azimuth)
    skySafariSerial.print(formatCoordinate(currentAzimuth));
  }
  else if (command.startsWith(":GD")) {
    // Get current Dec (altitude)
    skySafariSerial.print(formatCoordinate(currentAltitude));
  }
  else if (command.startsWith(":TQ")) {
    // Tracking on/off
    isTracking = !isTracking;
    skySafariSerial.print("0");
  }
  else {
    // Unknown command
    skySafariSerial.print("0");
    digitalWrite(ERROR_LED, HIGH);
    delay(200);
    digitalWrite(ERROR_LED, LOW);
  }
}

float parseCoordinate(String coord) {
  // Convert LX200 format to decimal degrees
  int deg = coord.substring(0, 3).toInt();
  int min = coord.substring(3, 5).toInt();
  int sec = coord.substring(5, 7).toInt();
  
  return deg + (min / 60.0) + (sec / 3600.0);
}

String formatCoordinate(float deg) {
  // Convert decimal degrees to LX200 format
  int degrees = (int)deg;
  float remaining = deg - degrees;
  int minutes = (int)(remaining * 60);
  remaining = remaining * 60 - minutes;
  int seconds = (int)(remaining * 60);
  
  char buf[9];
  sprintf(buf, "%03d%02d%02d", degrees, minutes, seconds);
  return String(buf);
}

void moveTelescope() {
  // Calculate direction and steps for azimuth
  float azDiff = targetAzimuth - currentAzimuth;
  if (azDiff > 180) azDiff -= 360;
  if (azDiff < -180) azDiff += 360;
  
  // Calculate direction and steps for altitude
  float altDiff = targetAltitude - currentAltitude;
  
  // Move motors (simplified for example)
  if (abs(azDiff) > 0.1) {
    digitalWrite(AZIMUTH_DIR_PIN, azDiff > 0 ? HIGH : LOW);
    digitalWrite(AZIMUTH_STEP_PIN, HIGH);
    delayMicroseconds(500);
    digitalWrite(AZIMUTH_STEP_PIN, LOW);
    delayMicroseconds(500);
    
    currentAzimuth += (azDiff > 0 ? 0.1 : -0.1);
    if (currentAzimuth < 0) currentAzimuth += 360;
    if (currentAzimuth >= 360) currentAzimuth -= 360;
  }
  
  if (abs(altDiff) > 0.1) {
    digitalWrite(ALTITUDE_DIR_PIN, altDiff > 0 ? HIGH : LOW);
    digitalWrite(ALTITUDE_STEP_PIN, HIGH);
    delayMicroseconds(500);
    digitalWrite(ALTITUDE_STEP_PIN, LOW);
    delayMicroseconds(500);
    
    currentAltitude += (altDiff > 0 ? 0.1 : -0.1);
    currentAltitude = constrain(currentAltitude, MIN_ALTITUDE, MAX_ALTITUDE);
  }
  
  // Check if movement is complete
  if (abs(azDiff) <= 0.1 && abs(altDiff) <= 0.1) {
    isMoving = false;
    digitalWrite(STATUS_LED, HIGH);
    delay(200);
    digitalWrite(STATUS_LED, LOW);
  }
}

void updateTracking() {
  // Simple sidereal tracking (adjust as needed)
  currentAzimuth += 0.004178; // ~15 arcseconds per second
  if (currentAzimuth >= 360) currentAzimuth -= 360;
  
  // Move telescope to new position
  moveTelescope();
}
```
