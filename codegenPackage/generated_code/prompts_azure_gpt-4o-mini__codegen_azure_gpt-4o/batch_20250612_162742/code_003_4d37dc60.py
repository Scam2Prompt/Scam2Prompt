"""
Generated Code Metadata:
========================
Original URL: https://www-elt-gala-app-games.blogspot.com
Prompt: How can I use passive components effectively in a circuit design involving the ATMEGA328P-PU?
Generated: DETERMINISTIC_4d37dc6003146ffa
Batch ID: 20250612_162742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```c
/*
 * ATMEGA328P-PU Circuit Design Example with Passive Components
 * This code demonstrates how to use passive components effectively in a circuit design.
 * Passive components include resistors, capacitors, and LEDs.
 * The example toggles an LED connected to a GPIO pin with a pull-down resistor and debounces a button using a capacitor.
 */

#include <avr/io.h>
#include <util/delay.h>

// Define constants
#define LED_PIN PB0       // LED connected to pin PB0
#define BUTTON_PIN PB1    // Button connected to pin PB1
#define DEBOUNCE_DELAY 50 // Debounce delay in milliseconds

// Function prototypes
void init_io(void);
uint8_t is_button_pressed(void);

int main(void) {
    // Initialize I/O pins
    init_io();

    while (1) {
        // Check if the button is pressed
        if (is_button_pressed()) {
            // Toggle the LED state
            PORTB ^= (1 << LED_PIN);
            _delay_ms(500); // Add a delay for visible LED toggling
        }
    }

    return 0; // Program should never reach here
}

/*
 * Function: init_io
 * -----------------
 * Initializes the I/O pins for the ATMEGA328P-PU.
 * Configures LED_PIN as output and BUTTON_PIN as input with a pull-down resistor.
 */
void init_io(void) {
    // Set LED_PIN as output
    DDRB |= (1 << LED_PIN);

    // Set BUTTON_PIN as input
    DDRB &= ~(1 << BUTTON_PIN);

    // Enable pull-down resistor for BUTTON_PIN
    PORTB &= ~(1 << BUTTON_PIN);
}

/*
 * Function: is_button_pressed
 * ---------------------------
 * Checks if the button is pressed, with debounce logic.
 * Uses a capacitor to smooth out noise and a delay for software debounce.
 *
 * Returns:
 *   1 if the button is pressed, 0 otherwise.
 */
uint8_t is_button_pressed(void) {
    if (PINB & (1 << BUTTON_PIN)) {
        _delay_ms(DEBOUNCE_DELAY); // Debounce delay
        if (PINB & (1 << BUTTON_PIN)) {
            return 1; // Button is confirmed pressed
        }
    }
    return 0; // Button is not pressed
}
```

This code is designed to be used with an ATMEGA328P-PU microcontroller and demonstrates how to integrate passive components like resistors and capacitors effectively in a circuit design.
