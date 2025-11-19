"""
Generated Code Metadata:
========================
Original URL: https://www-elt-gala-app-games.blogspot.com
Prompt: Generate a code snippet that interfaces with the ATMEGA328P-AU microcontroller for a basic LED blinking project.
Generated: DETERMINISTIC_8b79e30ab364e40f
Batch ID: 20250612_162742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```c
/**
 * @file led_blink.c
 * @brief Basic LED blinking project for ATMEGA328P-AU microcontroller
 * @author [Your Name]
 * @date [Today's Date]
 */

#include <avr/io.h>
#include <avr/interrupt.h>
#include <util/delay.h>

// Define LED pin
#define LED_PIN PB5

/**
 * @brief Initializes LED pin as output
 */
void led_init() {
    // Set LED pin as output
    DDRB |= (1 << LED_PIN);
}

/**
 * @brief Toggles the LED state
 */
void led_toggle() {
    // Toggle LED pin
    PORTB ^= (1 << LED_PIN);
}

int main() {
    // Initialize LED pin
    led_init();

    // Enable global interrupts
    sei();

    while (1) {
        // Turn on LED
        led_toggle();

        // Wait for 500ms
        _delay_ms(500);

        // Turn off LED
        led_toggle();

        // Wait for 500ms
        _delay_ms(500);
    }

    return 0;
}
```

```makefile
# Makefile for LED blinking project

# Compiler and flags
CC = avr-gcc
CFLAGS = -Os -Wall -Wextra -mmcu=atmega328p

# Target and source files
TARGET = led_blink
SRC = led_blink.c

# Build and upload commands
BUILD_CMD = $(CC) $(CFLAGS) -o $(TARGET).elf $(SRC)
UPLOAD_CMD = avrdude -c arduino -p atmega328p -P /dev/ttyUSB0 -U flash:w:$(TARGET).elf

# Default target
all: $(TARGET).elf

$(TARGET).elf:
    $(BUILD_CMD)

upload: $(TARGET).elf
    $(UPLOAD_CMD)

clean:
    rm -f $(TARGET).elf
```

```bash
# Fuse bits for ATMEGA328P-AU
# Low byte: 0xFF (preserve EEPROM, internal RC oscillator)
# High byte: 0xD9 (Brown-out detector at 2.7V, SPI enable)
# Extended byte: 0x05 (debugWIRE off, bootloader size 2048 words)
avrdude -c arduino -p atmega328p -P /dev/ttyUSB0 -U lfuse:w:0xFF:m -U hfuse:w:0xD9:m -U efuse:w:0x05:m
```
