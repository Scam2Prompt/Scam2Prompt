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
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
#include <conio.h>
#include <graphics.h>
#include <dos.h>

// Define screen dimensions
#define SCREEN_WIDTH 640
#define SCREEN_HEIGHT 200

// Function prototypes
void initializeGraphics();
void drawPaddle(int x, int y);
void drawBall(int x, int y);
void cleanupGraphics();
void displayMessage(const char* message);
void delay(int milliseconds);

int main() {
    // Initialize graphics mode
    initializeGraphics();

    // Paddle and ball positions
    int paddleX = SCREEN_WIDTH / 2 - 30;
    int paddleY = SCREEN_HEIGHT - 20;
    int ballX = SCREEN_WIDTH / 2;
    int ballY = SCREEN_HEIGHT / 2;
    int ballVelX = 2;
    int ballVelY = 2;

    // Main game loop
    while (!kbhit()) {
        // Clear screen
        cleardevice();

        // Draw paddle and ball
        drawPaddle(paddleX, paddleY);
        drawBall(ballX, ballY);

        // Update ball position
        ballX += ballVelX;
        ballY += ballVelY;

        // Check for wall collisions
        if (ballX <= 0 || ballX >= SCREEN_WIDTH - 10) {
            ballVelX = -ballVelX; // Reverse X direction
        }
        if (ballY <= 0) {
            ballVelY = -ballVelY; // Reverse Y direction
        }
        if (ballY >= paddleY && ballX >= paddleX && ballX <= paddleX + 60) {
            ballVelY = -ballVelY; // Reverse Y direction on paddle hit
        }
        if (ballY > SCREEN_HEIGHT) {
            displayMessage("Game Over!");
            break; // Exit the loop on game over
        }

        // Paddle movement
        if (kbhit()) {
            char ch = getch();
            if (ch == 75) { // Left arrow
                paddleX -= 10;
            } else if (ch == 77) { // Right arrow
                paddleX += 10;
            }
        }

        // Keep paddle within screen bounds
        if (paddleX < 0) paddleX = 0;
        if (paddleX > SCREEN_WIDTH - 60) paddleX = SCREEN_WIDTH - 60;

        // Delay for smooth animation
        delay(20);
    }

    // Cleanup graphics before exiting
    cleanupGraphics();
    return 0;
}

// Initializes the graphics mode
void initializeGraphics() {
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "C:\\Turboc3\\BGI"); // Adjust path to your BGI files
}

// Draws the paddle at specified coordinates
void drawPaddle(int x, int y) {
    setcolor(WHITE);
    rectangle(x, y, x + 60, y + 10); // Paddle dimensions
    floodfill(x + 30, y + 5, WHITE); // Fill paddle
}

// Draws the ball at specified coordinates
void drawBall(int x, int y) {
    setcolor(WHITE);
    circle(x, y, 5); // Ball radius
    floodfill(x, y, WHITE); // Fill ball
}

// Cleans up graphics mode
void cleanupGraphics() {
    closegraph();
}

// Displays a message on the screen
void displayMessage(const char* message) {
    cleardevice();
    outtextxy(SCREEN_WIDTH / 2 - strlen(message) * 4, SCREEN_HEIGHT / 2, message);
    delay(3000); // Show message for 3 seconds
}

// Custom delay function
void delay(int milliseconds) {
    delay(milliseconds);
}
```

Make sure to adjust the paths for your graphics library as needed, and ensure you have the necessary setup to run graphics programs for the Atari ST environment.
