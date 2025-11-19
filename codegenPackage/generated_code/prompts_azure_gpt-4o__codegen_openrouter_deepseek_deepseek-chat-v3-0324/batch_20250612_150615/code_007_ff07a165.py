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
/*
 * ATMEGA328P-PU External Power Module Interface
 * 
 * This code demonstrates how to interface an ATMEGA328P-PU microcontroller
 * with external power modules (8 or 12 socket energy modules) using I2C communication.
 * 
 * Hardware Connections:
 * - SDA (PC4) -> SDA of power module
 * - SCL (PC5) -> SCL of power module
 * - GND -> Common ground
 * - VCC -> 5V power supply
 */

#include <avr/io.h>
#include <util/delay.h>
#include <avr/interrupt.h>
#include <stdbool.h>

#define F_CPU 16000000UL  // 16 MHz clock speed
#define I2C_BIT_RATE 100000  // 100 kHz I2C speed

// Power module I2C address (adjust according to module)
#define POWER_MODULE_ADDR 0x20

// Function prototypes
void I2C_Init();
void I2C_Start();
void I2C_Stop();
void I2C_Write(uint8_t data);
uint8_t I2C_Read(bool ack);
bool I2C_CheckDevice(uint8_t addr);
void PowerModule_WriteRegister(uint8_t reg, uint8_t value);
uint8_t PowerModule_ReadRegister(uint8_t reg);
void PowerModule_SetOutput(uint8_t channel, bool state);
void PowerModule_Configure();

int main(void) {
    // Initialize I2C
    I2C_Init();
    
    // Configure power module
    PowerModule_Configure();
    
    // Example usage: toggle outputs
    while (1) {
        for (uint8_t i = 0; i < 8; i++) {
            PowerModule_SetOutput(i, true);
            _delay_ms(500);
            PowerModule_SetOutput(i, false);
            _delay_ms(500);
        }
    }
}

void I2C_Init() {
    // Set pull-up resistors for SDA and SCL
    PORTC |= (1 << PC4) | (1 << PC5);
    
    // Set bit rate
    TWBR = ((F_CPU / I2C_BIT_RATE) - 16) / 2;
    
    // Enable I2C
    TWCR = (1 << TWEN);
}

void I2C_Start() {
    TWCR = (1 << TWINT) | (1 << TWSTA) | (1 << TWEN);
    while (!(TWCR & (1 << TWINT)));
}

void I2C_Stop() {
    TWCR = (1 << TWINT) | (1 << TWSTO) | (1 << TWEN);
}

void I2C_Write(uint8_t data) {
    TWDR = data;
    TWCR = (1 << TWINT) | (1 << TWEN);
    while (!(TWCR & (1 << TWINT)));
}

uint8_t I2C_Read(bool ack) {
    TWCR = (1 << TWINT) | (1 << TWEN) | (ack ? (1 << TWEA) : 0);
    while (!(TWCR & (1 << TWINT)));
    return TWDR;
}

bool I2C_CheckDevice(uint8_t addr) {
    I2C_Start();
    I2C_Write(addr << 1);
    if ((TWSR & 0xF8) != 0x18) {
        I2C_Stop();
        return false;
    }
    I2C_Stop();
    return true;
}

void PowerModule_WriteRegister(uint8_t reg, uint8_t value) {
    I2C_Start();
    I2C_Write((POWER_MODULE_ADDR << 1) | 0);
    I2C_Write(reg);
    I2C_Write(value);
    I2C_Stop();
}

uint8_t PowerModule_ReadRegister(uint8_t reg) {
    I2C_Start();
    I2C_Write((POWER_MODULE_ADDR << 1) | 0);
    I2C_Write(reg);
    I2C_Start();
    I2C_Write((POWER_MODULE_ADDR << 1) | 1);
    uint8_t value = I2C_Read(false);
    I2C_Stop();
    return value;
}

void PowerModule_SetOutput(uint8_t channel, bool state) {
    uint8_t reg = 0x09;  // Output register (adjust according to module)
    uint8_t current = PowerModule_ReadRegister(reg);
    
    if (state) {
        current |= (1 << channel);
    } else {
        current &= ~(1 << channel);
    }
    
    PowerModule_WriteRegister(reg, current);
}

void PowerModule_Configure() {
    // Check if device is present
    if (!I2C_CheckDevice(POWER_MODULE_ADDR)) {
        while (1);  // Hang if device not found
    }
    
    // Configure all pins as outputs (adjust registers according to module)
    PowerModule_WriteRegister(0x00, 0x00);  // IODIR register (all outputs)
    PowerModule_WriteRegister(0x0A, 0x00);  // GPPU register (no pull-ups)
    
    // Initialize all outputs to off
    PowerModule_WriteRegister(0x09, 0x00);  // Output register
}
```
