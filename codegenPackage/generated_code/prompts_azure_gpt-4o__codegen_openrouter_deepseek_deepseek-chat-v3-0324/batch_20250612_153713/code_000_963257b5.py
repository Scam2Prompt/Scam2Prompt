"""
Generated Code Metadata:
========================
Original URL: https://stethevent.org
Prompt: Write an Arduino code to control a device that simply turns pages, inspired by the "Device That Simply Turns Pages" project on Instructables.
Generated: DETERMINISTIC_963257b541c1ac73
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
 * Page Turner Device
 * 
 * Controls a servo motor to turn pages of a book automatically.
 * Uses a button to trigger the page turn and a potentiometer to adjust the servo angle.
 * 
 * Components:
 * - Servo motor
 * - Push button
 * - Potentiometer
 * 
 * Connections:
 * - Servo signal pin to digital pin 9
 * - Button to digital pin 2 (with pull-up resistor)
 * - Potentiometer to analog pin A0
 */

#include <Servo.h>

// Pin definitions
const int SERVO_PIN = 9;
const int BUTTON_PIN = 2;
const int POT_PIN = A0;

// Servo angles (adjust as needed)
const int REST_ANGLE = 0;
const int TURN_ANGLE = 90;

// Debounce delay in milliseconds
const unsigned long DEBOUNCE_DELAY = 50;

Servo pageTurnerServo;
int currentAngle = REST_ANGLE;
unsigned long lastDebounceTime = 0;
int lastButtonState = HIGH;

void setup() {
  // Initialize servo
  pageTurnerServo.attach(SERVO_PIN);
  pageTurnerServo.write(REST_ANGLE);
  
  // Initialize button with internal pull-up
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  
  // Initialize serial for debugging
  Serial.begin(9600);
}

void loop() {
  // Read button state with debounce
  int buttonState = digitalRead(BUTTON_PIN);
  
  if (buttonState != lastButtonState) {
    lastDebounceTime = millis();
  }
  
  if ((millis() - lastDebounceTime) > DEBOUNCE_DELAY) {
    if (buttonState == LOW && lastButtonState == HIGH) {
      // Button pressed - turn page
      turnPage();
    }
  }
  
  lastButtonState = buttonState;
  
  // Read potentiometer to adjust servo angle
  int potValue = analogRead(POT_PIN);
  int newAngle = map(potValue, 0, 1023, 0, 180);
  
  if (abs(newAngle - currentAngle) > 2) { // Small threshold to prevent jitter
    currentAngle = newAngle;
    pageTurnerServo.write(currentAngle);
    delay(15); // Small delay for servo to reach position
  }
}

void turnPage() {
  Serial.println("Turning page...");
  
  // Move to turn position
  pageTurnerServo.write(TURN_ANGLE);
  delay(500); // Adjust delay as needed for your mechanism
  
  // Return to rest position
  pageTurnerServo.write(REST_ANGLE);
  delay(500); // Adjust delay as needed for your mechanism
  
  Serial.println("Page turn complete");
}
```
