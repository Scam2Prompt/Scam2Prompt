"""
Generated Code Metadata:
========================
Original URL: https://overlanders-atari.com
Prompt: Generate a code snippet for creating a simple one-screener demo for the Atari ST, inspired by the "PONG Cracktro" released by Overlanders.
Generated: DETERMINISTIC_0e0984496932a662
Batch ID: 20250612_135906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```c
/*
 * Atari ST One-Screener Demo inspired by "PONG Cracktro" by Overlanders
 * This code creates a simple bouncing ball animation with text on the screen.
 * Written in C for the Atari ST platform.
 */

#include <osbind.h>  // Atari ST system calls
#include <stdlib.h>  // Standard library for random numbers

#define SCREEN_WIDTH  320
#define SCREEN_HEIGHT 200
#define BALL_SIZE     8
#define TEXT_Y_POS    180

// Ball structure to hold position and velocity
typedef struct {
    int x, y;       // Position
    int dx, dy;     // Velocity
} Ball;

// Function prototypes
void draw_ball(int x, int y);
void erase_ball(int x, int y);
void draw_text(const char *text, int x, int y);
void delay(int ms);

int main() {
    Ball ball = {SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 2, 2};
    const char *message = "PONG Cracktro Demo!";
    int running = 1;

    // Set video mode to low resolution (320x200, 16 colors)
    int old_mode = VsetMode(0);

    while (running) {
        // Erase the ball at its current position
        erase_ball(ball.x, ball.y);

        // Update ball position
        ball.x += ball.dx;
        ball.y += ball.dy;

        // Check for collisions with screen edges
        if (ball.x <= 0 || ball.x >= SCREEN_WIDTH - BALL_SIZE) {
            ball.dx = -ball.dx;  // Reverse horizontal direction
        }
        if (ball.y <= 0 || ball.y >= SCREEN_HEIGHT - BALL_SIZE) {
            ball.dy = -ball.dy;  // Reverse vertical direction
        }

        // Draw the ball at its new position
        draw_ball(ball.x, ball.y);

        // Draw the text message
        draw_text(message, (SCREEN_WIDTH - 8 * strlen(message)) / 2, TEXT_Y_POS);

        // Delay to control animation speed
        delay(50);

        // Check for user input to exit (e.g., pressing a key)
        if (Cconis()) {  // Check if a key is pressed
            running = 0; // Exit the loop
        }
    }

    // Restore the original video mode
    VsetMode(old_mode);

    return 0;
}

/*
 * Draws a ball at the specified position.
 * Uses a simple filled rectangle to represent the ball.
 */
void draw_ball(int x, int y) {
    for (int i = 0; i < BALL_SIZE; i++) {
        for (int j = 0; j < BALL_SIZE; j++) {
            *(unsigned short *)(0xFFFF8200 + (y + j) * SCREEN_WIDTH + (x + i)) = 0xFFFF;  // White pixel
        }
    }
}

/*
 * Erases the ball at the specified position.
 * Fills the area with black pixels.
 */
void erase_ball(int x, int y) {
    for (int i = 0; i < BALL_SIZE; i++) {
        for (int j = 0; j < BALL_SIZE; j++) {
            *(unsigned short *)(0xFFFF8200 + (y + j) * SCREEN_WIDTH + (x + i)) = 0x0000;  // Black pixel
        }
    }
}

/*
 * Draws text at the specified position.
 * Uses the system console for simplicity.
 */
void draw_text(const char *text, int x, int y) {
    Cconws("\033Y");  // Move cursor to position
    Cconws(text);     // Output text
}

/*
 * Delays execution for the specified number of milliseconds.
 * Uses a busy-wait loop for simplicity.
 */
void delay(int ms) {
    long end = ms * 1000;
    for (long i = 0; i < end; i++) {
        // Busy-wait loop
    }
}
```

Note: This code is a simplified example and assumes direct memory access for drawing pixels, which may not work on all Atari ST systems. Proper hardware-specific libraries should be used for production-ready code.
