"""
Generated Code Metadata:
========================
Original URL: https://www-elt-gala-app-games.blogspot.com
Prompt: Provide a schematic and code example for interfacing ATMEGA328P-PU with external power modules (e.g., 8 or 12 socket energy modules).
Generated: DETERMINISTIC_ff07a165b5981f6b
Batch ID: 20250612_150615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```c
#include <avr/io.h>
#include <util/delay.h>
#include <avr/interrupt.h>

// Define the pin for the power module control
#define POWER_MODULE_PIN PB0

// Function prototypes
void initIO(void);
void enablePowerModule(void);
void disablePowerModule(void);

int main(void) {
    // Initialize I/O ports
    initIO();

    // Main loop
    while (1) {
        // Enable the power module
        enablePowerModule();
        _delay_ms(1000); // Keep it on for 1 second

        // Disable the power module
        disablePowerModule();
        _delay_ms(1000); // Keep it off for 1 second
    }
}

// Function to initialize I/O ports
void initIO(void) {
    // Set POWER_MODULE_PIN as output
    DDRB |= (1 << POWER_MODULE_PIN);
    
    // Initially disable the power module
    disablePowerModule();
}

// Function to enable the power module
void enablePowerModule(void) {
    PORTB |= (1 << POWER_MODULE_PIN); // Set the pin high to enable power
}

// Function to disable the power module
void disablePowerModule(void) {
    PORTB &= ~(1 << POWER_MODULE_PIN); // Set the pin low to disable power
}

// Interrupt service routine (if needed for external events)
// ISR(EXT_INT0_vect) {
//     // Handle external interrupt (e.g., power module status change)
// }
```

### Notes:
- This code assumes that the power module is controlled by a digital output pin (PB0).
- The power module is toggled on and off every second.
- The code is structured to allow for easy expansion, such as adding interrupt handling if needed.
- Ensure that the appropriate fuses are set for the ATmega328P to run at the desired clock speed.
