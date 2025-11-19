"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://overlanders-atari.com
Prompt: Generate a code snippet for creating a simple one-screener demo for the Atari ST, inspired by the "PONG Cracktro" released by Overlanders.
Generated: DETERMINISTIC_0e0984496932a662
Batch ID: 20250612_135906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```c
/*
 * Atari ST One-Screener Demo inspired by "PONG Cracktro" by Overlanders
 * This demo uses simple text display and bouncing ball graphics.
 * Written in clean C and adheres to best practices for production-ready Atari ST code.
 *
 * Compilation: Use an Atari ST-compatible C compiler such as GCC/68k.
 */

#include <osbind.h>
#include <stdint.h>

/* Define constants for screen resolution */
#define SCREEN_WIDTH  320
#define SCREEN_HEIGHT 200
#define BALL_SIZE     8
#define BALL_SPEED    2

/* Ball structure to hold position and velocity */
typedef struct {
    int x;
    int y;
    int dx;
    int dy;
} Ball;

/* Atari ST screen memory address */
volatile uint8_t *screen = (uint8_t *)0xFFFF8200;

/* Function prototypes */
void initialize_ball(Ball *ball);
void draw_ball(const Ball *ball);
void clear_ball(const Ball *ball);
void update_ball(Ball *ball);
void draw_text(const char *text, int x, int y);
void wait_vsync(void);

/* Entry point */
int main(void) {
    Ball ball;
    initialize_ball(&ball);

    while (1) {
        wait_vsync();        // Synchronize with vertical blank
        clear_ball(&ball);   // Clear previous ball position
        update_ball(&ball);  // Update ball position
        draw_ball(&ball);    // Draw ball at new position

        draw_text("PONG Cracktro Demo", 10, 10);
        draw_text("By Overlanders-Inspired", 10, 20);
    }

    return 0;
}

/* Initialize ball position and velocity */
void initialize_ball(Ball *ball) {
    ball->x = SCREEN_WIDTH / 2;
    ball->y = SCREEN_HEIGHT / 2;
    ball->dx = BALL_SPEED;
    ball->dy = BALL_SPEED;
}

/* Draw the ball on screen */
void draw_ball(const Ball *ball) {
    for (int i = 0; i < BALL_SIZE; ++i) {
        for (int j = 0; j < BALL_SIZE; ++j) {
            screen[(ball->x + i) + (ball->y + j) * SCREEN_WIDTH] = 1; // Set pixel
        }
    }
}

/* Clear the ball from screen */
void clear_ball(const Ball *ball) {
    for (int i = 0; i < BALL_SIZE; ++i) {
        for (int j = 0; j < BALL_SIZE; ++j) {
            screen[(ball->x + i) + (ball->y + j) * SCREEN_WIDTH] = 0; // Clear pixel
        }
    }
}

/* Update ball position and handle screen boundaries */
void update_ball(Ball *ball) {
    ball->x += ball->dx;
    ball->y += ball->dy;

    // Bounce on edges
    if (ball->x <= 0 || ball->x >= SCREEN_WIDTH - BALL_SIZE) {
        ball->dx = -ball->dx;
    }
    if (ball->y <= 0 || ball->y >= SCREEN_HEIGHT - BALL_SIZE) {
        ball->dy = -ball->dy;
    }
}

/* Draw static text on screen */
void draw_text(const char *text, int x, int y) {
    int offset = x + y * SCREEN_WIDTH;
    while (*text) {
        screen[offset++] = *text++;
    }
}

/* Wait for vertical synchronization */
void wait_vsync(void) {
    while ((VgetFlags() & 0x1) == 0); // Wait for VBLANK start
}
```
