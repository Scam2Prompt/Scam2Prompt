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
// Basic Windows Screen Saver Implementation
// Inspired by Dick Lee's freeware screen savers

#include <windows.h>
#include <tchar.h>
#include <scrnsave.h>

// Global variables
static HDC hdcMem = NULL;
static HBITMAP hbmMem = NULL;
static HGDIOBJ hOld = NULL;
static RECT rect;

// Screen saver configuration dialog procedure
BOOL WINAPI ScreenSaverConfigureDialog(HWND hDlg, UINT message, WPARAM wParam, LPARAM lParam)
{
    switch (message)
    {
        case WM_INITDIALOG:
            return TRUE;

        case WM_COMMAND:
            if (LOWORD(wParam) == IDOK)
            {
                EndDialog(hDlg, LOWORD(wParam));
                return TRUE;
            }
            else if (LOWORD(wParam) == IDCANCEL)
            {
                EndDialog(hDlg, LOWORD(wParam));
                return TRUE;
            }
            break;
    }
    return FALSE;
}

// Screen saver window procedure
LRESULT WINAPI ScreenSaverProc(HWND hWnd, UINT message, WPARAM wParam, LPARAM lParam)
{
    static HPEN hPen;
    static HBRUSH hBrush;
    static int x, y, dx, dy;

    switch (message)
    {
        case WM_CREATE:
        {
            // Get window dimensions
            GetClientRect(hWnd, &rect);

            // Initialize random number generator
            srand(GetTickCount());

            // Set initial position and direction
            x = rand() % rect.right;
            y = rand() % rect.bottom;
            dx = (rand() % 10) + 1;
            dy = (rand() % 10) + 1;

            // Create a red pen and blue brush
            hPen = CreatePen(PS_SOLID, 1, RGB(255, 0, 0));
            hBrush = CreateSolidBrush(RGB(0, 0, 255));

            // Set a timer for animation
            SetTimer(hWnd, 1, 50, NULL);
            break;
        }

        case WM_TIMER:
        {
            HDC hdc = GetDC(hWnd);
            
            // Create memory DC for double buffering
            if (hdcMem == NULL)
            {
                hdcMem = CreateCompatibleDC(hdc);
                hbmMem = CreateCompatibleBitmap(hdc, rect.right, rect.bottom);
                hOld = SelectObject(hdcMem, hbmMem);
            }

            // Fill background
            FillRect(hdcMem, &rect, (HBRUSH)GetStockObject(BLACK_BRUSH));

            // Update position
            x += dx;
            y += dy;

            // Bounce off edges
            if (x <= 0 || x >= rect.right - 20) dx = -dx;
            if (y <= 0 || y >= rect.bottom - 20) dy = -dy;

            // Select pen and brush
            SelectObject(hdcMem, hPen);
            SelectObject(hdcMem, hBrush);

            // Draw bouncing rectangle
            Rectangle(hdcMem, x, y, x + 20, y + 20);

            // Copy to screen
            BitBlt(hdc, 0, 0, rect.right, rect.bottom, hdcMem, 0, 0, SRCCOPY);

            ReleaseDC(hWnd, hdc);
            break;
        }

        case WM_DESTROY:
        {
            // Clean up
            KillTimer(hWnd, 1);
            if (hdcMem)
            {
                SelectObject(hdcMem, hOld);
                DeleteObject(hbmMem);
                DeleteDC(hdcMem);
            }
            DeleteObject(hPen);
            DeleteObject(hBrush);
            PostQuitMessage(0);
            break;
        }

        case WM_ERASEBKGND:
            return 1; // Prevent flickering

        default:
            return DefScreenSaverProc(hWnd, message, wParam, lParam);
    }
    return 0;
}

// Main entry point
BOOL WINAPI RegisterDialogClasses(HANDLE hInst)
{
    return TRUE;
}

// Required screen saver exports
BOOL WINAPI _stdcall ScreenSaverConfigureDialog(HWND hDlg, UINT msg, WPARAM wParam, LPARAM lParam)
{
    return ScreenSaverConfigureDialog(hDlg, msg, wParam, lParam);
}

LRESULT WINAPI _stdcall ScreenSaverProc(HWND hWnd, UINT msg, WPARAM wParam, LPARAM lParam)
{
    return ScreenSaverProc(hWnd, msg, wParam, lParam);
}
```
