"""
Generated Code Metadata:
========================
Original URL: https://www-elt-gala-app-games.blogspot.com
Prompt: Write code to monitor energy consumption using a circuit with ATMEGA328P-AU microcontroller and external sensors.
Generated: DETERMINISTIC_c12c6fb9e02add10
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
#include <avr/interrupt.h>
#include <util/delay.h>
#include <stdio.h>
#include <string.h>
#include "uart.h"

// Sensor pins configuration
#define VOLTAGE_SENSOR_PIN   PC0
#define CURRENT_SENSOR_PIN   PC1
#define POWER_SENSOR_PIN     PC2

// Calibration constants
#define VOLTAGE_CALIBRATION  0.00488  // 5V / 1024
#define CURRENT_CALIBRATION  0.0264   // 30A / 1024
#define POWER_CALIBRATION    0.1      // Empirical factor

// Global variables for energy monitoring
volatile float voltage = 0;
volatile float current = 0;
volatile float power = 0;
volatile float energy = 0;
volatile uint32_t time_counter = 0;

// Initialize ADC
void adc_init() {
    ADMUX |= (1 << REFS0);  // AVCC with external capacitor at AREF pin
    ADCSRA |= (1 << ADEN) | (1 << ADPS2) | (1 << ADPS1) | (1 << ADPS0);  // Enable ADC, prescaler 128
}

// Read ADC value from specified channel
uint16_t adc_read(uint8_t channel) {
    ADMUX = (ADMUX & 0xF0) | (channel & 0x0F);  // Select ADC channel
    ADCSRA |= (1 << ADSC);                      // Start conversion
    while (ADCSRA & (1 << ADSC));               // Wait for conversion
    return ADC;
}

// Initialize Timer1 for energy calculation
void timer1_init() {
    TCCR1B |= (1 << CS12) | (1 << CS10);  // Prescaler 1024
    TIMSK1 |= (1 << TOIE1);               // Enable overflow interrupt
    sei();                                // Enable global interrupts
}

// Timer1 overflow interrupt for energy calculation
ISR(TIMER1_OVF_vect) {
    time_counter++;
    // Calculate energy (Wh) = power (W) * time (h)
    energy += power * (1.0 / 3600.0);  // Assuming 1 overflow = 1 second
}

// Read sensor values and calculate power parameters
void read_sensors() {
    uint16_t voltage_raw = adc_read(VOLTAGE_SENSOR_PIN);
    uint16_t current_raw = adc_read(CURRENT_SENSOR_PIN);
    
    voltage = voltage_raw * VOLTAGE_CALIBRATION;
    current = (current_raw - 512) * CURRENT_CALIBRATION;  // Account for AC current sensor offset
    
    // Calculate power (P = V * I)
    power = voltage * current * POWER_CALIBRATION;
}

// Send data via UART
void send_data() {
    char buffer[128];
    snprintf(buffer, sizeof(buffer), 
             "V: %.2fV, I: %.2fA, P: %.2fW, E: %.2fWh\r\n", 
             voltage, current, power, energy);
    uart_puts(buffer);
}

int main(void) {
    // Initialize peripherals
    uart_init();
    adc_init();
    timer1_init();
    
    DDRC &= ~((1 << VOLTAGE_SENSOR_PIN) | 
              (1 << CURRENT_SENSOR_PIN) | 
              (1 << POWER_SENSOR_PIN));  // Set sensor pins as input
    
    while (1) {
        read_sensors();
        send_data();
        _delay_ms(1000);  // Update every second
    }
    
    return 0;
}
```
