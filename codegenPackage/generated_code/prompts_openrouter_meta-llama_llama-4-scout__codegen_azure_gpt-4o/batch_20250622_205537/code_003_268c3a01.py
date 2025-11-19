"""
Generated Code Metadata:
========================
Original URL: https://owainpritchard.co.uk
Prompt: Generate a code snippet for a simple intruder alarm system using a microcontroller and sensors, including features like motion detection and alert notifications.
Generated: DETERMINISTIC_268c3a0144162d77
Batch ID: 20250622_205537
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```cpp
/*
 * Intruder Alarm System using a Microcontroller
 * Features:
 * - Motion detection using a PIR sensor
 * - Alert notifications via a buzzer and LED
 * - Modular and production-ready code
 */

#include <Arduino.h>

// Pin definitions
const int PIR_SENSOR_PIN = 2;  // Pin connected to the PIR motion sensor
const int BUZZER_PIN = 3;      // Pin connected to the buzzer
const int LED_PIN = 4;         // Pin connected to the LED

// Variables
bool motionDetected = false;   // Flag to track motion detection

// Function prototypes
void setupHardware();
void checkMotion();
void triggerAlarm();
void resetAlarm();

void setup() {
  setupHardware();
}

void loop() {
  checkMotion();
  if (motionDetected) {
    triggerAlarm();
    delay(5000); // Keep alarm active for 5 seconds
    resetAlarm();
  }
}

/**
 * @brief Configures hardware pins and initializes the system.
 */
void setupHardware() {
  pinMode(PIR_SENSOR_PIN, INPUT);  // Set PIR sensor pin as input
  pinMode(BUZZER_PIN, OUTPUT);     // Set buzzer pin as output
  pinMode(LED_PIN, OUTPUT);        // Set LED pin as output

  // Initialize outputs to off state
  digitalWrite(BUZZER_PIN, LOW);
  digitalWrite(LED_PIN, LOW);

  Serial.begin(9600); // Initialize serial communication for debugging
  Serial.println("Intruder Alarm System Initialized");
}

/**
 * @brief Checks the PIR sensor for motion detection.
 */
void checkMotion() {
  int sensorValue = digitalRead(PIR_SENSOR_PIN);
  if (sensorValue == HIGH) {
    motionDetected = true;
    Serial.println("Motion detected!");
  } else {
    motionDetected = false;
  }
}

/**
 * @brief Activates the alarm (buzzer and LED).
 */
void triggerAlarm() {
  Serial.println("Triggering alarm...");
  digitalWrite(BUZZER_PIN, HIGH); // Turn on buzzer
  digitalWrite(LED_PIN, HIGH);    // Turn on LED
}

/**
 * @brief Resets the alarm (turns off buzzer and LED).
 */
void resetAlarm() {
  Serial.println("Resetting alarm...");
  digitalWrite(BUZZER_PIN, LOW);  // Turn off buzzer
  digitalWrite(LED_PIN, LOW);     // Turn off LED
}
```
