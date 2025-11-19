"""
Generated Code Metadata:
========================
Original URL: https://www-elt-gala-app-games.blogspot.com
Prompt: Write code to implement I2C communication between an ATMEGA328P-AU microcontroller and a sensor module.
Generated: DETERMINISTIC_408d594efc4318da
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

// I2C definitions
#define F_SCL 100000UL // SCL frequency (100kHz)
#define PRESCALER 1    // I2C prescaler
#define TWBR_VALUE ((F_CPU/F_SCL)-16)/(2*PRESCALER)

// Sensor address (7-bit)
#define SENSOR_ADDRESS 0x68

// Status codes
#define I2C_START 0x08
#define I2C_REP_START 0x10
#define I2C_MT_SLA_ACK 0x18
#define I2C_MT_DATA_ACK 0x28
#define I2C_MR_SLA_ACK 0x40
#define I2C_MR_DATA_ACK 0x50
#define I2C_MR_DATA_NACK 0x58

// Initialize I2C (TWI) interface
void i2c_init(void) {
    // Set SCL frequency
    TWBR = (uint8_t)TWBR_VALUE;
    
    // No prescaler
    TWSR &= ~((1<<TWPS1) | (1<<TWPS0));
}

// Send I2C start condition
uint8_t i2c_start(void) {
    // Send START condition
    TWCR = (1<<TWINT) | (1<<TWSTA) | (1<<TWEN);
    
    // Wait for TWINT flag set
    while (!(TWCR & (1<<TWINT)));
    
    // Return status code
    return (TWSR & 0xF8);
}

// Send I2C stop condition
void i2c_stop(void) {
    // Send STOP condition
    TWCR = (1<<TWINT) | (1<<TWSTO) | (1<<TWEN);
    
    // Wait until STOP condition is executed
    while (TWCR & (1<<TWSTO));
}

// Write one byte to I2C bus
uint8_t i2c_write(uint8_t data) {
    // Load data into TWDR
    TWDR = data;
    
    // Start transmission
    TWCR = (1<<TWINT) | (1<<TWEN);
    
    // Wait for TWINT flag set
    while (!(TWCR & (1<<TWINT)));
    
    // Return status code
    return (TWSR & 0xF8);
}

// Read one byte from I2C bus (ack = 1 for ACK, 0 for NACK)
uint8_t i2c_read(uint8_t ack) {
    // Start read operation
    if (ack) {
        TWCR = (1<<TWINT) | (1<<TWEN) | (1<<TWEA);
    } else {
        TWCR = (1<<TWINT) | (1<<TWEN);
    }
    
    // Wait for TWINT flag set
    while (!(TWCR & (1<<TWINT)));
    
    // Return received data
    return TWDR;
}

// Write to sensor register
uint8_t sensor_write_register(uint8_t reg, uint8_t data) {
    uint8_t status;
    
    // Send START condition
    status = i2c_start();
    if (status != I2C_START && status != I2C_REP_START) {
        return 1; // Error
    }
    
    // Send sensor address with write bit
    status = i2c_write((SENSOR_ADDRESS << 1) | 0);
    if (status != I2C_MT_SLA_ACK) {
        i2c_stop();
        return 2; // Error
    }
    
    // Send register address
    status = i2c_write(reg);
    if (status != I2C_MT_DATA_ACK) {
        i2c_stop();
        return 3; // Error
    }
    
    // Send data
    status = i2c_write(data);
    if (status != I2C_MT_DATA_ACK) {
        i2c_stop();
        return 4; // Error
    }
    
    // Send STOP condition
    i2c_stop();
    
    return 0; // Success
}

// Read from sensor register
uint8_t sensor_read_register(uint8_t reg, uint8_t *data) {
    uint8_t status;
    
    // Send START condition
    status = i2c_start();
    if (status != I2C_START && status != I2C_REP_START) {
        return 1; // Error
    }
    
    // Send sensor address with write bit
    status = i2c_write((SENSOR_ADDRESS << 1) | 0);
    if (status != I2C_MT_SLA_ACK) {
        i2c_stop();
        return 2; // Error
    }
    
    // Send register address
    status = i2c_write(reg);
    if (status != I2C_MT_DATA_ACK) {
        i2c_stop();
        return 3; // Error
    }
    
    // Send repeated START condition
    status = i2c_start();
    if (status != I2C_REP_START) {
        i2c_stop();
        return 4; // Error
    }
    
    // Send sensor address with read bit
    status = i2c_write((SENSOR_ADDRESS << 1) | 1);
    if (status != I2C_MR_SLA_ACK) {
        i2c_stop();
        return 5; // Error
    }
    
    // Read data with NACK (last byte)
    *data = i2c_read(0);
    status = TWSR & 0xF8;
    if (status != I2C_MR_DATA_NACK) {
        i2c_stop();
        return 6; // Error
    }
    
    // Send STOP condition
    i2c_stop();
    
    return 0; // Success
}

// Example usage
int main(void) {
    uint8_t error;
    uint8_t sensor_data;
    
    // Initialize I2C
    i2c_init();
    
    // Example: Write 0x0F to register 0x1A
    error = sensor_write_register(0x1A, 0x0F);
    if (error) {
        // Handle error
    }
    
    // Example: Read from register 0x1B
    error = sensor_read_register(0x1B, &sensor_data);
    if (error) {
        // Handle error
    }
    
    while (1) {
        // Main program loop
    }
    
    return 0;
}
```
