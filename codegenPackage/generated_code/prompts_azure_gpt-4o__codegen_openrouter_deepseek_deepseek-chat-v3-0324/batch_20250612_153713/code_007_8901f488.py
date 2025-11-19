"""
Generated Code Metadata:
========================
Original URL: https://stethevent.org
Prompt: Develop an Arduino sketch for building a quadcopter landing pad with telescoping legs for uneven ground, as described in the "Quadcopter Landing Pad With Telescoping Legs" project on Instructables.
Generated: DETERMINISTIC_8901f488c00621c8
Batch ID: 20250612_153713
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```arduino
/*
 * Quadcopter Landing Pad With Telescoping Legs
 * 
 * This sketch controls a quadcopter landing pad with telescoping legs
 * that automatically adjust to uneven ground using servo motors and
 * ultrasonic distance sensors.
 * 
 * Components:
 * - 4x Servo motors (for leg adjustment)
 * - 4x Ultrasonic sensors (HC-SR04)
 * - Arduino board (Uno/Mega)
 * - Power supply
 */

#include <Servo.h>

// Constants
const int NUM_LEGS = 4;
const int MIN_SERVO_ANGLE = 0;
const int MAX_SERVO_ANGLE = 180;
const int LEG_EXTEND_THRESHOLD = 30; // cm
const int LEG_RETRACT_THRESHOLD = 50; // cm
const int STABILIZATION_DELAY = 500; // ms between adjustments
const int SENSOR_TIMEOUT = 10000; // microseconds

// Servo objects
Servo legServos[NUM_LEGS];

// Ultrasonic sensor pins
const int trigPins[NUM_LEGS] = {2, 4, 6, 8}; // Trigger pins
const int echoPins[NUM_LEGS] = {3, 5, 7, 9}; // Echo pins

// Current servo positions
int currentPositions[NUM_LEGS] = {90, 90, 90, 90}; // Start at midpoint

void setup() {
  Serial.begin(9600);
  
  // Initialize servos
  for (int i = 0; i < NUM_LEGS; i++) {
    legServos[i].attach(10 + i); // Servos on pins 10-13
    legServos[i].write(currentPositions[i]);
  }
  
  // Initialize ultrasonic sensors
  for (int i = 0; i < NUM_LEGS; i++) {
    pinMode(trigPins[i], OUTPUT);
    pinMode(echoPins[i], INPUT);
  }
  
  Serial.println("Landing pad initialized");
}

void loop() {
  int distances[NUM_LEGS];
  
  // Measure distances for all legs
  for (int i = 0; i < NUM_LEGS; i++) {
    distances[i] = measureDistance(i);
    Serial.print("Leg ");
    Serial.print(i);
    Serial.print(" distance: ");
    Serial.print(distances[i]);
    Serial.println(" cm");
  }
  
  // Adjust legs based on measurements
  adjustLegs(distances);
  
  delay(STABILIZATION_DELAY);
}

int measureDistance(int legIndex) {
  // Ensure trigger is low
  digitalWrite(trigPins[legIndex], LOW);
  delayMicroseconds(2);
  
  // Send 10 microsecond pulse
  digitalWrite(trigPins[legIndex], HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPins[legIndex], LOW);
  
  // Measure echo pulse duration
  long duration = pulseIn(echoPins[legIndex], HIGH, SENSOR_TIMEOUT);
  
  // Calculate distance (cm)
  int distance = duration * 0.034 / 2;
  
  // Handle timeout or invalid readings
  if (distance <= 0 || distance > 300) {
    distance = -1; // Error value
    Serial.print("Error reading sensor for leg ");
    Serial.println(legIndex);
  }
  
  return distance;
}

void adjustLegs(int distances[]) {
  for (int i = 0; i < NUM_LEGS; i++) {
    if (distances[i] == -1) {
      continue; // Skip if sensor error
    }
    
    if (distances[i] < LEG_EXTEND_THRESHOLD && currentPositions[i] < MAX_SERVO_ANGLE) {
      // Extend leg (increase angle)
      currentPositions[i] += 5;
      legServos[i].write(currentPositions[i]);
      Serial.print("Extending leg ");
      Serial.println(i);
    }
    else if (distances[i] > LEG_RETRACT_THRESHOLD && currentPositions[i] > MIN_SERVO_ANGLE) {
      // Retract leg (decrease angle)
      currentPositions[i] -= 5;
      legServos[i].write(currentPositions[i]);
      Serial.print("Retracting leg ");
      Serial.println(i);
    }
  }
}
```
