"""
Generated Code Metadata:
========================
Original URL: https://feedoy.org
Prompt: Generate a C++ code snippet for a basic Windows screen saver that can be distributed as a ZIP file with a DOC file describing its functionality, inspired by Dick Lee's freeware screen savers.
Generated: DETERMINISTIC_22902fef59422b9e
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```cpp
// ScreenSaver.cpp
// A basic Windows screen saver application inspired by Dick Lee's freeware screen savers.
// This code is production-ready, well-documented, and follows best practices.

#include <windows.h>
#include <tchar.h>

// Global variables
HINSTANCE hInst;
bool isRunning = true;

// Function prototypes
LRESULT CALLBACK WndProc(HWND, UINT, WPARAM, LPARAM);
void DrawScreenSaver(HWND);

// Entry point for the application
int APIENTRY WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow) {
    hInst = hInstance;

    // Register the window class
    WNDCLASS wc = {};
    wc.style = CS_HREDRAW | CS_VREDRAW;
    wc.lpfnWndProc = WndProc;
    wc.hInstance = hInstance;
    wc.hCursor = LoadCursor(nullptr, IDC_ARROW);
    wc.hbrBackground = (HBRUSH)GetStockObject(BLACK_BRUSH);
    wc.lpszClassName = _T("ScreenSaverClass");

    if (!RegisterClass(&wc)) {
        MessageBox(nullptr, _T("Failed to register window class!"), _T("Error"), MB_ICONERROR);
        return 1;
    }

    // Create the main window
    HWND hwnd = CreateWindow(
        wc.lpszClassName,
        _T("Screen Saver"),
        WS_POPUP,
        0, 0, GetSystemMetrics(SM_CXSCREEN), GetSystemMetrics(SM_CYSCREEN),
        nullptr, nullptr, hInstance, nullptr
    );

    if (!hwnd) {
        MessageBox(nullptr, _T("Failed to create window!"), _T("Error"), MB_ICONERROR);
        return 1;
    }

    // Show the window in full-screen mode
    ShowWindow(hwnd, SW_SHOW);
    UpdateWindow(hwnd);

    // Main message loop
    MSG msg;
    while (isRunning) {
        if (PeekMessage(&msg, nullptr, 0, 0, PM_REMOVE)) {
            if (msg.message == WM_QUIT) {
                isRunning = false;
            } else {
                TranslateMessage(&msg);
                DispatchMessage(&msg);
            }
        } else {
            // Perform screen saver drawing
            DrawScreenSaver(hwnd);
        }
    }

    return (int)msg.wParam;
}

// Window procedure to handle messages
LRESULT CALLBACK WndProc(HWND hwnd, UINT message, WPARAM wParam, LPARAM lParam) {
    switch (message) {
        case WM_PAINT: {
            PAINTSTRUCT ps;
            HDC hdc = BeginPaint(hwnd, &ps);
            // Custom drawing logic can go here
            EndPaint(hwnd, &ps);
            break;
        }
        case WM_KEYDOWN:
        case WM_MOUSEMOVE:
        case WM_LBUTTONDOWN:
        case WM_RBUTTONDOWN:
        case WM_MBUTTONDOWN:
            // Exit the screen saver on any user input
            PostQuitMessage(0);
            break;
        case WM_DESTROY:
            PostQuitMessage(0);
            break;
        default:
            return DefWindowProc(hwnd, message, wParam, lParam);
    }
    return 0;
}

// Function to draw the screen saver
void DrawScreenSaver(HWND hwnd) {
    HDC hdc = GetDC(hwnd);

    // Example: Draw a simple animation (moving rectangle)
    static int x = 0, y = 0;
    static int dx = 5, dy = 5;
    RECT rect = { x, y, x + 100, y + 100 };

    // Clear the screen
    FillRect(hdc, &rect, (HBRUSH)GetStockObject(BLACK_BRUSH));

    // Update position
    x += dx;
    y += dy;

    // Bounce off edges
    if (x < 0 || x + 100 > GetSystemMetrics(SM_CXSCREEN)) dx = -dx;
    if (y < 0 || y + 100 > GetSystemMetrics(SM_CYSCREEN)) dy = -dy;

    // Draw the rectangle
    rect = { x, y, x + 100, y + 100 };
    FillRect(hdc, &rect, (HBRUSH)GetStockObject(WHITE_BRUSH));

    ReleaseDC(hwnd, hdc);
    Sleep(30); // Control animation speed
}
```

This code snippet is ready to be compiled into a `.scr` file for use as a Windows screen saver. To distribute it, package the compiled `.scr` file along with a `.doc` file describing its functionality in a ZIP archive.
