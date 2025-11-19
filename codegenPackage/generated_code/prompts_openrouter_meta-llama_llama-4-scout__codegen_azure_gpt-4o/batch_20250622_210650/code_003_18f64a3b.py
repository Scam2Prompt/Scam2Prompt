"""
Generated Code Metadata:
========================
Original URL: https://olaf-schirm.de
Prompt: "Design an interactive art installation using sensors and microcontrollers, inspired by Olaf Schirm's 'Interference' sound installation."
Generated: DETERMINISTIC_18f64a3bf2e23686
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is the code for an interactive art installation using an Arduino microcontroller and sensors. This example uses a distance sensor (e.g., HC-SR04) and a piezo buzzer to create sound effects based on proximity, inspired by Olaf Schirm's "Interference" sound installation.

```cpp
/*
  Interactive Art Installation: Inspired by Olaf Schirm's "Interference"
  Author: [Your Name]
  Date: [Insert Date]

  Description:
  This code creates an interactive sound installation using an ultrasonic distance sensor
  and a piezo buzzer. The sound frequency changes based on the proximity of the user to the sensor.

  Components:
  - HC-SR04 Ultrasonic Distance Sensor
  - Piezo Buzzer
  - Arduino Microcontroller

  Wiring:
  - HC-SR04: VCC to 5V, GND to GND, Trig to Pin 9, Echo to Pin 10
  - Piezo Buzzer: Positive to Pin 3, Negative to GND
*/

#define TRIG_PIN 9  // Pin connected to the Trig pin of the HC-SR04
#define ECHO_PIN 10 // Pin connected to the Echo pin of the HC-SR04
#define BUZZER_PIN 3 // Pin connected to the piezo buzzer

// Constants for the HC-SR04 sensor
const int MAX_DISTANCE = 200; // Maximum distance to measure (in cm)
const int MIN_DISTANCE = 2;   // Minimum distance to measure (in cm)

// Function to measure distance using the HC-SR04 sensor
long measureDistance() {
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  // Calculate the duration of the echo pulse
  long duration = pulseIn(ECHO_PIN, HIGH);

  // Convert the duration to distance (in cm)
  long distance = duration * 0.034 / 2;

  // Return the measured distance
  return distance;
}

// Function to generate sound based on distance
void generateSound(long distance) {
  if (distance >= MIN_DISTANCE && distance <= MAX_DISTANCE) {
    // Map the distance to a frequency range (e.g., 200 Hz to 2000 Hz)
    int frequency = map(distance, MIN_DISTANCE, MAX_DISTANCE, 200, 2000);

    // Play the sound on the buzzer
    tone(BUZZER_PIN, frequency);
  } else {
    // Stop the buzzer if the distance is out of range
    noTone(BUZZER_PIN);
  }
}

void setup() {
  // Initialize the serial communication for debugging
  Serial.begin(9600);

  // Set up the pins for the HC-SR04 sensor
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);

  // Set up the pin for the piezo buzzer
  pinMode(BUZZER_PIN, OUTPUT);

  // Print a startup message
  Serial.println("Interactive Art Installation Initialized");
}

void loop() {
  // Measure the distance from the sensor
  long distance = measureDistance();

  // Print the measured distance to the serial monitor
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");

  // Generate sound based on the measured distance
  generateSound(distance);

  // Add a short delay to avoid excessive polling
  delay(100);
}
```

This code is ready to be uploaded to an Arduino board. Ensure the wiring matches the pin assignments in the code.
