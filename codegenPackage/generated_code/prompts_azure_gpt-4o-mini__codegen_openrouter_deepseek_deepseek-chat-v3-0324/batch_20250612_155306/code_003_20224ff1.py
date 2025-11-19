"""
Generated Code Metadata:
========================
Original URL: https://delsolmontessorihn.com
Prompt: Develop a simple robotics project for elementary students that fosters logical thinking and creativity, inspired by the robotics program at Del Sol Montessori.
Generated: DETERMINISTIC_20224ff1e30b17b5
Batch ID: 20250612_155306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
Simple Robotics Project for Elementary Students
Inspired by Del Sol Montessori Robotics Program

This program controls a basic robot using a Raspberry Pi and GPIO pins.
It includes simple movements and sensor interactions to foster logical thinking.
"""

import RPi.GPIO as GPIO
import time
import random

# Set up GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Motor pins
LEFT_MOTOR_FORWARD = 17
LEFT_MOTOR_BACKWARD = 18
RIGHT_MOTOR_FORWARD = 22
RIGHT_MOTOR_BACKWARD = 23

# Sensor pins
ULTRASONIC_TRIGGER = 5
ULTRASONIC_ECHO = 6
BUTTON_PIN = 24

# LED pins
LED_RED = 12
LED_GREEN = 13
LED_BLUE = 19

# Setup motor pins as output
for pin in [LEFT_MOTOR_FORWARD, LEFT_MOTOR_BACKWARD, 
            RIGHT_MOTOR_FORWARD, RIGHT_MOTOR_BACKWARD]:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

# Setup sensor pins
GPIO.setup(ULTRASONIC_TRIGGER, GPIO.OUT)
GPIO.setup(ULTRASONIC_ECHO, GPIO.IN)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Setup LED pins
for led in [LED_RED, LED_GREEN, LED_BLUE]:
    GPIO.setup(led, GPIO.OUT)
    GPIO.output(led, GPIO.LOW)

def move_forward(duration=1):
    """Move robot forward for specified duration"""
    GPIO.output(LEFT_MOTOR_FORWARD, GPIO.HIGH)
    GPIO.output(RIGHT_MOTOR_FORWARD, GPIO.HIGH)
    time.sleep(duration)
    stop_motors()

def move_backward(duration=1):
    """Move robot backward for specified duration"""
    GPIO.output(LEFT_MOTOR_BACKWARD, GPIO.HIGH)
    GPIO.output(RIGHT_MOTOR_BACKWARD, GPIO.HIGH)
    time.sleep(duration)
    stop_motors()

def turn_left(duration=0.5):
    """Turn robot left for specified duration"""
    GPIO.output(RIGHT_MOTOR_FORWARD, GPIO.HIGH)
    GPIO.output(LEFT_MOTOR_BACKWARD, GPIO.HIGH)
    time.sleep(duration)
    stop_motors()

def turn_right(duration=0.5):
    """Turn robot right for specified duration"""
    GPIO.output(LEFT_MOTOR_FORWARD, GPIO.HIGH)
    GPIO.output(RIGHT_MOTOR_BACKWARD, GPIO.HIGH)
    time.sleep(duration)
    stop_motors()

def stop_motors():
    """Stop all motors"""
    for pin in [LEFT_MOTOR_FORWARD, LEFT_MOTOR_BACKWARD, 
                RIGHT_MOTOR_FORWARD, RIGHT_MOTOR_BACKWARD]:
        GPIO.output(pin, GPIO.LOW)

def get_distance():
    """Measure distance using ultrasonic sensor"""
    GPIO.output(ULTRASONIC_TRIGGER, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(ULTRASONIC_TRIGGER, GPIO.LOW)

    start_time = time.time()
    stop_time = time.time()

    while GPIO.input(ULTRASONIC_ECHO) == 0:
        start_time = time.time()

    while GPIO.input(ULTRASONIC_ECHO) == 1:
        stop_time = time.time()

    time_elapsed = stop_time - start_time
    distance = (time_elapsed * 34300) / 2  # Speed of sound in cm/s

    return distance

def set_led(color, state):
    """Control LED colors"""
    if color.lower() == 'red':
        GPIO.output(LED_RED, state)
    elif color.lower() == 'green':
        GPIO.output(LED_GREEN, state)
    elif color.lower() == 'blue':
        GPIO.output(LED_BLUE, state)

def dance_routine():
    """Perform a fun dance routine"""
    moves = [move_forward, move_backward, turn_left, turn_right]
    colors = ['red', 'green', 'blue']
    
    for _ in range(5):
        move = random.choice(moves)
        color = random.choice(colors)
        
        set_led(color, GPIO.HIGH)
        move(duration=random.uniform(0.3, 1.0))
        set_led(color, GPIO.LOW)
        time.sleep(0.2)

def obstacle_avoidance():
    """Simple obstacle avoidance behavior"""
    try:
        while True:
            distance = get_distance()
            
            if distance < 20:  # 20 cm threshold
                set_led('red', GPIO.HIGH)
                move_backward(0.5)
                turn_choice = random.choice([turn_left, turn_right])
                turn_choice(0.7)
                set_led('red', GPIO.LOW)
            else:
                set_led('green', GPIO.HIGH)
                move_forward(0.3)
                set_led('green', GPIO.LOW)
                
    except KeyboardInterrupt:
        stop_motors()
        GPIO.cleanup()

def main():
    """Main program with simple menu"""
    print("Simple Robotics Program")
    print("1. Move Forward")
    print("2. Move Backward")
    print("3. Turn Left")
    print("4. Turn Right")
    print("5. Dance Routine")
    print("6. Obstacle Avoidance")
    print("7. Exit")
    
    try:
        while True:
            choice = input("Enter your choice (1-7): ")
            
            if choice == '1':
                move_forward()
            elif choice == '2':
                move_backward()
            elif choice == '3':
                turn_left()
            elif choice == '4':
                turn_right()
            elif choice == '5':
                dance_routine()
            elif choice == '6':
                obstacle_avoidance()
            elif choice == '7':
                break
            else:
                print("Invalid choice. Please try again.")
                
    except KeyboardInterrupt:
        print("\nProgram stopped by user")
    finally:
        stop_motors()
        GPIO.cleanup()
        print("Robot stopped and GPIO cleaned up")

if __name__ == "__main__":
    main()
```
