"""
Generated Code Metadata:
========================
Original URL: https://www-elt-gala-app-games.blogspot.com
Prompt: Create a sample code that demonstrates how to read data from a sensor using the ATMEGA328P-AU microcontroller.
Generated: DETERMINISTIC_60c5a6e2e29e3fa1
Batch ID: 20250612_162742
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
#include <stdint.h>
#include <stdio.h>
#include <string.h>
#include <avr/interrupt.h>

// Define ADC prescaler for 16MHz clock (prescaler of 128 gives 125kHz ADC clock)
#define ADC_PRESCALER (_BV(ADPS2) | _BV(ADPS1) | _BV(ADPS0))

// Initialize ADC for reading sensor data
void adc_init() {
    // Set reference voltage to AVCC (5V) and left-adjust result
    ADMUX = _BV(REFS0);
    
    // Enable ADC and set prescaler
    ADCSRA = _BV(ADEN) | ADC_PRESCALER;
}

// Read ADC value from specified channel (0-5)
uint16_t adc_read(uint8_t channel) {
    // Clear channel selection bits and set new channel
    ADMUX = (ADMUX & 0xF0) | (channel & 0x0F);
    
    // Start single conversion
    ADCSRA |= _BV(ADSC);
    
    // Wait for conversion to complete
    while (ADCSRA & _BV(ADSC));
    
    // Return ADC result (10-bit)
    return ADC;
}

// Initialize UART for debugging output (9600 baud at 16MHz)
void uart_init() {
    // Set baud rate
    UBRR0H = 0;
    UBRR0L = 103;
    
    // Enable transmitter
    UCSR0B = _BV(TXEN0);
    
    // Set frame format: 8 data bits, 1 stop bit, no parity
    UCSR0C = _BV(UCSZ01) | _BV(UCSZ00);
}

// Transmit a single character over UART
void uart_transmit(char data) {
    // Wait for empty transmit buffer
    while (!(UCSR0A & _BV(UDRE0)));
    
    // Put data into buffer, sends the data
    UDR0 = data;
}

// Print a string over UART
void uart_print(const char* str) {
    for (size_t i = 0; i < strlen(str); i++) {
        uart_transmit(str[i]);
    }
}

// Print an integer value over UART
void uart_print_int(uint16_t value) {
    char buffer[10];
    snprintf(buffer, sizeof(buffer), "%u", value);
    uart_print(buffer);
}

int main(void) {
    // Initialize peripherals
    adc_init();
    uart_init();
    
    // Enable global interrupts
    sei();
    
    // Main loop
    while (1) {
        // Read sensor value from ADC channel 0
        uint16_t sensor_value = adc_read(0);
        
        // Print sensor value to UART
        uart_print("Sensor Value: ");
        uart_print_int(sensor_value);
        uart_print("\r\n");
        
        // Delay between readings
        _delay_ms(500);
    }
    
    return 0;
}
```
