"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www-elt-gala-app-games.blogspot.com
Prompt: Write code to implement I2C communication between an ATMEGA328P-AU microcontroller and a sensor module.
Generated: DETERMINISTIC_408d594efc4318da
Batch ID: 20250612_150615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```c
#include <avr/io.h>
#include <util/twi.h>
#include <avr/interrupt.h>
#include <stdbool.h>

/* I2C Configuration */
#define F_SCL 100000UL // I2C frequency 100kHz
#define Prescaler 1
#define TWBR_VALUE ((F_CPU / F_SCL) - 16) / (2 * Prescaler)

// I2C Initialize Function
void I2C_Init(void) {
    TWSR = 0; // Set prescaler to 1
    TWBR = TWBR_VALUE; // Set bit rate
}

// I2C Start Condition Function
bool I2C_Start(void) {
    // Transmit start condition
    TWCR = (1 << TWSTA) | (1 << TWEN) | (1 << TWINT);
    while (!(TWCR & (1 << TWINT))); // Wait for TWINT flag
    return (TWSR & 0xF8) == TW_START; // Check if start condition was transmitted
}

// I2C Stop Condition Function
void I2C_Stop(void) {
    // Transmit stop condition
    TWCR = (1 << TWSTO) | (1 << TWEN) | (1 << TWINT);
    while (TWCR & (1 << TWSTO)); // Wait until stop condition is executed
}

// I2C Write Byte Function
bool I2C_Write(uint8_t data) {
    TWDR = data; // Load data into TWI data register
    TWCR = (1 << TWINT) | (1 << TWEN); // Start transmission
    while (!(TWCR & (1 << TWINT))); // Wait for TWINT flag
    return (TWSR & 0xF8) != TW_MT_DATA_ACK; // Check for ACK
}

// I2C Read Byte Function
uint8_t I2C_Read(bool ack) {
    if (ack) {
        TWCR = (1 << TWINT) | (1 << TWEN) | (1 << TWEA); // Enable ACK
    } else {
        TWCR = (1 << TWINT) | (1 << TWEN); // No ACK
    }
    while (!(TWCR & (1 << TWINT))); // Wait for TWINT flag
    return TWDR; // Return received data
}

// Example usage of I2C communication
int main(void) {
    I2C_Init(); // Initialize I2C
    uint8_t sensor_address = 0x48; // Example sensor address
    uint8_t data_to_write = 0x01; // Example data to write

    // Start I2C communication
    if (I2C_Start()) {
        // Send sensor address for writing
        if (!I2C_Write(sensor_address << 1)) {
            // Write data to sensor
            if (!I2C_Write(data_to_write)) {
                // Data written successfully
            }
        }
        // Stop I2C communication
        I2C_Stop();
    } else {
        // Handle start condition error
    }

    // Read data from sensor
    if (I2C_Start()) {
        // Send sensor address for reading
        if (!I2C_Write((sensor_address << 1) | 0x01)) {
            uint8_t received_data = I2C_Read(false); // Read without ACK
            // Process received data
        }
        I2C_Stop();
    } else {
        // Handle start condition error
    }

    while (1) {
        // Main loop
    }
}
```
