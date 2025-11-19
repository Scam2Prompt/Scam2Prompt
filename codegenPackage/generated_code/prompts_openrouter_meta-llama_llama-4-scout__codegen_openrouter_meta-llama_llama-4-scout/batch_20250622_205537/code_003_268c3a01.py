"""
Generated Code Metadata:
========================
Original URL: https://owainpritchard.co.uk
Prompt: Generate a code snippet for a simple intruder alarm system using a microcontroller and sensors, including features like motion detection and alert notifications.
Generated: DETERMINISTIC_268c3a0144162d77
Batch ID: 20250622_205537
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```c
/**
 * @file intruder_alarm_system.c
 * @brief Simple intruder alarm system using a microcontroller and sensors.
 * @author [Your Name]
 * @date [Today's Date]
 */

#include <stdio.h>
#include <stdbool.h>
#include <stdint.h>
#include <avr/io.h>
#include <avr/interrupt.h>

// Define sensor pin connections
#define MOTION_SENSOR_PIN PB0
#define DOOR_SENSOR_PIN PB1
#define BUZZER_PIN PB2
#define LED_PIN PB3

// Define alert notification pins
#define SMS_MODULE_TX_PIN PD0
#define SMS_MODULE_RX_PIN PD1

// Define system states
typedef enum {
    SYSTEM_IDLE,
    MOTION_DETECTED,
    DOOR_OPENED,
    ALERT_SENT
} system_state_t;

// Global system state
system_state_t system_state = SYSTEM_IDLE;

// Interrupt Service Routine (ISR) for motion sensor
ISR(INT0_vect) {
    // Check if motion is detected
    if (bit_is_set(PINB, MOTION_SENSOR_PIN)) {
        system_state = MOTION_DETECTED;
    }
}

// Interrupt Service Routine (ISR) for door sensor
ISR(INT1_vect) {
    // Check if door is opened
    if (bit_is_set(PINB, DOOR_SENSOR_PIN)) {
        system_state = DOOR_OPENED;
    }
}

int main(void) {
    // Initialize microcontroller pins
    DDRB = 0xFF;  // Set all PORTB pins as output
    DDRD = 0xFF;  // Set all PORTD pins as output

    // Initialize sensor pins as input
    PORTB |= (1 << MOTION_SENSOR_PIN) | (1 << DOOR_SENSOR_PIN);

    // Enable interrupts
    EIMSK |= (1 << INT0) | (1 << INT1);  // Enable INT0 and INT1
    EICRA |= (1 << ISC01) | (1 << ISC11);  // Set interrupt sense control

    // Initialize system
    sei();  // Enable global interrupts

    while (1) {
        switch (system_state) {
            case SYSTEM_IDLE:
                // Check sensor states
                if (bit_is_clear(PINB, MOTION_SENSOR_PIN)) {
                    // Motion detected, trigger alert
                    system_state = MOTION_DETECTED;
                } else if (bit_is_clear(PINB, DOOR_SENSOR_PIN)) {
                    // Door opened, trigger alert
                    system_state = DOOR_OPENED;
                }
                break;

            case MOTION_DETECTED:
                // Trigger buzzer and LED
                PORTB |= (1 << BUZZER_PIN) | (1 << LED_PIN);
                // Send alert notification via SMS
                send_sms_alert();
                system_state = ALERT_SENT;
                break;

            case DOOR_OPENED:
                // Trigger buzzer and LED
                PORTB |= (1 << BUZZER_PIN) | (1 << LED_PIN);
                // Send alert notification via SMS
                send_sms_alert();
                system_state = ALERT_SENT;
                break;

            case ALERT_SENT:
                // Wait for a short period before resetting
                _delay_ms(5000);
                // Reset system state and buzzer/LED
                system_state = SYSTEM_IDLE;
                PORTB &= ~((1 << BUZZER_PIN) | (1 << LED_PIN));
                break;
        }
    }

    return 0;
}

// Function to send SMS alert
void send_sms_alert() {
    // Initialize SMS module
    uart_init();

    // Send SMS using AT commands
    uart_send_string("AT+CMGF=1\r");  // Set SMS mode to text
    uart_send_string("AT+CMGS=\"+1234567890\"\r");  // Set recipient number
    uart_send_string("Intruder alert!\r");  // Send SMS message
    uart_send_string("\x1a");  // Send SMS termination character

    // Wait for SMS to be sent
    _delay_ms(1000);
}

// UART initialization function
void uart_init() {
    // Set baud rate
    UBRR0H = 0x00;
    UBRR0L = 0x05;  // 9600 bps

    // Enable UART transmitter and receiver
    UCSR0B |= (1 << RXEN0) | (1 << TXEN0);

    // Set frame format: 8 data, 1 stop bit
    UCSR0C |= (1 << UCSZ01) | (1 << UCSZ00);
}

// UART send string function
void uart_send_string(char *str) {
    while (*str) {
        uart_send_char(*str++);
    }
}

// UART send character function
void uart_send_char(char c) {
    while (!(UCSR0A & (1 << UDRE0)));  // Wait for empty transmit buffer
    UDR0 = c;  // Send character
}
```
