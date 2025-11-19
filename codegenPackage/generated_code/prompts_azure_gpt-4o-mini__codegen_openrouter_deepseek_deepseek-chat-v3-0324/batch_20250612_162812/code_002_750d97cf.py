"""
Generated Code Metadata:
========================
Original URL: https://en.clark-zapper.com
Prompt: Provide a code example for an Arduino project that mimics the functionality of the Hulda Clark Zapper, focusing on generating positive voltage pulses to target parasites.
Generated: DETERMINISTIC_750d97cf2f1932a0
Batch ID: 20250612_162812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, well-commented Arduino implementation for a Zapper device:

```arduino
/*
 * Hulda Clark Zapper Simulation
 * Generates positive voltage pulses at specific frequencies to target parasites
 * 
 * Features:
 * - 30kHz square wave output (common zapper frequency)
 * - Adjustable duty cycle (typically 50% for zappers)
 * - Safety timer to limit session duration
 * - Output enable/disable control
 */

// Pin definitions
const uint8_t OUTPUT_PIN = 9;      // PWM capable pin for signal generation
const uint8_t ENABLE_PIN = 2;      // Pin to enable/disable output
const uint8_t STATUS_LED = 13;     // Built-in LED for status indication

// Zapper parameters
const uint32_t ZAPPER_FREQ = 30000;  // 30 kHz frequency
const uint8_t DUTY_CYCLE = 50;       // 50% duty cycle
const uint32_t MAX_SESSION_TIME = 180000; // 3 minute safety limit (in ms)

// Runtime variables
volatile bool outputEnabled = false;
uint32_t sessionStartTime = 0;

void setup() {
  // Initialize pins
  pinMode(OUTPUT_PIN, OUTPUT);
  pinMode(ENABLE_PIN, INPUT_PULLUP);  // Use internal pullup
  pinMode(STATUS_LED, OUTPUT);
  
  // Attach interrupt for enable/disable control
  attachInterrupt(digitalPinToInterrupt(ENABLE_PIN), toggleOutput, FALLING);
  
  // Initialize serial for debugging
  Serial.begin(9600);
  Serial.println("Zapper Initialized");
  
  // Start with output disabled
  disableOutput();
}

void loop() {
  // Check session time if output is active
  if (outputEnabled) {
    uint32_t currentTime = millis();
    
    // Automatic shutoff after max session time
    if (currentTime - sessionStartTime >= MAX_SESSION_TIME) {
      disableOutput();
      Serial.println("Session completed automatically");
    }
    
    // Blink status LED during operation
    digitalWrite(STATUS_LED, (currentTime / 500) % 2);
  }
}

// ISR for enable/disable toggle
void toggleOutput() {
  static uint32_t lastInterruptTime = 0;
  uint32_t interruptTime = millis();
  
  // Debounce check
  if (interruptTime - lastInterruptTime > 200) {
    if (outputEnabled) {
      disableOutput();
    } else {
      enableOutput();
    }
  }
  lastInterruptTime = interruptTime;
}

// Enable zapper output
void enableOutput() {
  if (!outputEnabled) {
    // Configure Timer1 for 30kHz PWM
    TCCR1A = _BV(COM1A1) | _BV(WGM11) | _BV(WGM10);
    TCCR1B = _BV(WGM13) | _BV(WGM12) | _BV(CS10);
    ICR1 = (F_CPU / (2 * ZAPPER_FREQ)) - 1;
    OCR1A = (ICR1 * DUTY_CYCLE) / 100;
    
    outputEnabled = true;
    sessionStartTime = millis();
    digitalWrite(STATUS_LED, HIGH);
    Serial.println("Output Enabled");
  }
}

// Disable zapper output
void disableOutput() {
  if (outputEnabled) {
    // Stop PWM output
    TCCR1A = 0;
    TCCR1B = 0;
    digitalWrite(OUTPUT_PIN, LOW);
    
    outputEnabled = false;
    digitalWrite(STATUS_LED, LOW);
    Serial.println("Output Disabled");
  }
}
```
