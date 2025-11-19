"""
Generated Code Metadata:
========================
Original URL: https://overlanders-atari.com
Prompt: Create an example of a 4K intro demo code that could compete in a demoscene event, taking cues from the '4K-Memory' demo by Overlanders.
Generated: DETERMINISTIC_d0e7620dff75cee5
Batch ID: 20250612_135906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**4K Intro Demo Code**
```c
// 4K Intro Demo Code
// Inspired by '4K-Memory' demo by Overlanders

#include <windows.h>
#include <math.h>
#include <stdint.h>

// Constants
#define WIDTH  640
#define HEIGHT 480
#define FRAMERATE 60

// Global variables
static uint8_t *vram;
static float angle = 0.0f;

// Vertex structure
typedef struct {
    float x, y, z;
    float r, g, b;
} vertex_t;

// Initialize graphics
void init_graphics() {
    // Create a window
    HWND hwnd = CreateWindowEx(0, "STATIC", "4K Intro Demo", WS_OVERLAPPEDWINDOW, CW_USEDEFAULT, CW_USEDEFAULT, WIDTH, HEIGHT, NULL, NULL, GetModuleHandle(NULL), NULL);
    ShowWindow(hwnd, SW_SHOW);

    // Create a DC and a bitmap
    HDC hdc = GetDC(hwnd);
    HDC memdc = CreateCompatibleDC(hdc);
    HBITMAP bitmap = CreateCompatibleBitmap(hdc, WIDTH, HEIGHT);
    HGDIOBJ oldobj = SelectObject(memdc, bitmap);
    vram = (uint8_t *)malloc(WIDTH * HEIGHT * 4);

    // Set up pixel format
    for (int y = 0; y < HEIGHT; y++) {
        for (int x = 0; x < WIDTH; x++) {
            uint32_t *pixel = (uint32_t *)(vram + (y * WIDTH * 4) + (x * 4));
            *pixel = 0xFF000000; // Clear screen to black
        }
    }
}

// Render a frame
void render_frame() {
    // Clear screen
    for (int y = 0; y < HEIGHT; y++) {
        for (int x = 0; x < WIDTH; x++) {
            uint32_t *pixel = (uint32_t *)(vram + (y * WIDTH * 4) + (x * 4));
            *pixel = 0xFF000000; // Clear screen to black
        }
    }

    // Draw a rotating cube
    vertex_t vertices[] = {
        {-1.0f, -1.0f,  1.0f, 1.0f, 0.0f, 0.0f},
        { 1.0f, -1.0f,  1.0f, 0.0f, 1.0f, 0.0f},
        { 1.0f,  1.0f,  1.0f, 0.0f, 0.0f, 1.0f},
        {-1.0f,  1.0f,  1.0f, 1.0f, 1.0f, 0.0f},
        {-1.0f, -1.0f, -1.0f, 1.0f, 0.0f, 1.0f},
        { 1.0f, -1.0f, -1.0f, 0.0f, 1.0f, 1.0f},
        { 1.0f,  1.0f, -1.0f, 1.0f, 1.0f, 1.0f},
        {-1.0f,  1.0f, -1.0f, 0.0f, 0.0f, 0.0f}
    };

    int edges[] = {0, 1, 1, 2, 2, 3, 3, 0, 4, 5, 5, 6, 6, 7, 7, 4, 0, 4, 1, 5, 2, 6, 3, 7};

    for (int i = 0; i < 24; i += 2) {
        vertex_t v1 = vertices[edges[i]];
        vertex_t v2 = vertices[edges[i + 1]];

        // Rotate vertices
        float rx1 = v1.x * cos(angle) - v1.z * sin(angle);
        float rz1 = v1.x * sin(angle) + v1.z * cos(angle);
        float rx2 = v2.x * cos(angle) - v2.z * sin(angle);
        float rz2 = v2.x * sin(angle) + v2.z * cos(angle);

        v1.x = rx1;
        v1.z = rz1;
        v2.x = rx2;
        v2.z = rz2;

        // Project vertices
        int x1 = (int)(v1.x * 200 / (4 - v1.z) + WIDTH / 2);
        int y1 = (int)(v1.y * 200 / (4 - v1.z) + HEIGHT / 2);
        int x2 = (int)(v2.x * 200 / (4 - v2.z) + WIDTH / 2);
        int y2 = (int)(v2.y * 200 / (4 - v2.z) + HEIGHT / 2);

        // Draw line
        int dx = x2 - x1;
        int dy = y2 - y1;
        int steps = abs(dx) > abs(dy) ? abs(dx) : abs(dy);

        for (int j = 0; j <= steps; j++) {
            int x = x1 + (dx * j) / steps;
            int y = y1 + (dy * j) / steps;
            uint32_t *pixel = (uint32_t *)(vram + (y * WIDTH * 4) + (x * 4));
            *pixel = 0xFFFFFFFF; // White color
        }
    }

    // Update angle
    angle += 0.01f;
}

// Main loop
int main() {
    init_graphics();

    // Main loop
    MSG msg;
    while (GetMessage(&msg, NULL, 0, 0)) {
        render_frame();

        // Update window
        HDC hdc = GetDC(msg.hwnd);
        HDC memdc = CreateCompatibleDC(hdc);
        HBITMAP bitmap = CreateCompatibleBitmap(hdc, WIDTH, HEIGHT);
        HGDIOBJ oldobj = SelectObject(memdc, bitmap);
        SetBitmapBits(bitmap, WIDTH * HEIGHT * 4, vram, DIB_RGB_COLORS);
        BitBlt(hdc, 0, 0, WIDTH, HEIGHT, memdc, 0, 0, SRCCOPY);
        ReleaseDC(msg.hwnd, hdc);
        DeleteDC(memdc);
        DeleteObject(bitmap);

        // Cap framerate
        Sleep(1000 / FRAMERATE);
    }

    return 0;
}
```
