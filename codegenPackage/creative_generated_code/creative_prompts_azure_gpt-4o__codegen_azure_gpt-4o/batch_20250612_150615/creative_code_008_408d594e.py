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
/*
 * Title: I2C Communication Between ATMEGA328P-AU and a Sensor Module
 * Description: This code demonstrates how to set up I2C communication
 *              between an ATMEGA328P-AU microcontroller and a sensor module.
 *              The implementation includes I2C initialization, data transmission,
 *              and data reception.
 * Author: Professional Software Developer
 */

#include <avr/io.h>
#include <util/twi.h>

#define F_CPU 16000000UL      // Define CPU frequency for delay calculations
#define SCL_CLOCK 100000L     // Define I2C clock frequency (100kHz)

// I2C Status Codes for Error Handling
#define I2C_START_SUCCESS 0x08
#define I2C_REP_START_SUCCESS 0x10
#define I2C_MT_SLA_ACK 0x18
#define I2C_MT_DATA_ACK 0x28
#define I2C_MR_SLA_ACK 0x40
#define I2C_MR_DATA_ACK 0x50
#define I2C_MR_DATA_NACK 0x58

// Function Prototypes
void I2C_Init(void);
uint8_t I2C_Start(void);
void I2C_Stop(void);
uint8_t I2C_Write(uint8_t data);
uint8_t I2C_Read_ACK(void);
uint8_t I2C_Read_NACK(void);

int main(void) {
    uint8_t sensor_data;
    uint8_t sensor_address = 0x40; // Replace with your sensor's I2C address

    // Initialize I2C
    I2C_Init();

    // Start the I2C communication
    if (I2C_Start() != I2C_START_SUCCESS) {
        // Handle start error (e.g., blink an LED or reset the microcontroller)
        while (1);
    }

    // Send sensor address with write bit (0)
    if (I2C_Write(sensor_address << 1) != I2C_MT_SLA_ACK) {
        // Handle error in sending address
        while (1);
    }

    // Send register address or control byte to the sensor
    if (I2C_Write(0x00) != I2C_MT_DATA_ACK) {
        // Handle error in sending register address
        while (1);
    }

    // Restart to switch to read mode
    if (I2C_Start() != I2C_REP_START_SUCCESS) {
        // Handle repeated start error
        while (1);
    }

    // Send sensor address with read bit (1)
    if (I2C_Write((sensor_address << 1) | 1) != I2C_MR_SLA_ACK) {
        // Handle error in sending read address
        while (1);
    }

    // Read data from the sensor with NACK (last byte)
    sensor_data = I2C_Read_NACK();

    // Stop the I2C communication
    I2C_Stop();

    // Sensor data can now be used as needed
    while (1) {
        // Infinite loop (e.g., process sensor data or send it elsewhere)
    }
}

// Initialize I2C (TWI) with the specified clock frequency
void I2C_Init(void) {
    TWSR = 0x00;                           // Set prescaler bits to 0
    TWBR = ((F_CPU / SCL_CLOCK) - 16) / 2; // Set bit rate register
    TWCR = (1 << TWEN);                    // Enable TWI
}

// Send Start Condition
uint8_t I2C_Start(void) {
    TWCR = (1 << TWSTA) | (1 << TWEN) | (1 << TWINT); // Send START condition
    while (!(TWCR & (1 << TWINT)));                   // Wait for TWINT flag to set
    return (TWSR & 0xF8);                             // Return status code
}

// Send Stop Condition
void I2C_Stop(void) {
    TWCR = (1 << TWSTO) | (1 << TWEN) | (1 << TWINT); // Send STOP condition
    while (TWCR & (1 << TWSTO));                      // Wait for STOP to complete
}

// Write a byte of data to the I2C bus
uint8_t I2C_Write(uint8_t data) {
    TWDR = data;                      // Load data into TWDR register
    TWCR = (1 << TWEN) | (1 << TWINT); // Start data transmission
    while (!(TWCR & (1 << TWINT)));   // Wait for TWINT flag to set
    return (TWSR & 0xF8);             // Return status code
}

// Read a byte of data from the I2C bus and acknowledge it (ACK)
uint8_t I2C_Read_ACK(void) {
    TWCR = (1 << TWEN) | (1 << TWINT) | (1 << TWEA); // Enable ACK and start reception
    while (!(TWCR & (1 << TWINT)));                 // Wait for TWINT flag to set
    return TWDR;                                    // Return received data
}

// Read a byte of data from the I2C bus without acknowledging it (NACK)
uint8_t I2C_Read_NACK(void) {
    TWCR = (1 << TWEN) | (1 << TWINT); // Start reception without ACK
    while (!(TWCR & (1 << TWINT)));    // Wait for TWINT flag to set
    return TWDR;                       // Return received data
}
```
