"""
Generated Code Metadata:
========================
Original URL: https://marchigue.cl
Prompt: Write a CSS style sheet that implements high contrast and low saturation themes for a tourism website, enhancing readability for users with different visual needs, as outlined in the accessibility features of Marchigüe.
Generated: DETERMINISTIC_8ba9bb7b05628a5e
Batch ID: 20250612_155250
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* Base styles for the tourism website */
:root {
    --primary-color: #4a6fa5;
    --secondary-color: #166088;
    --accent-color: #4fc3f7;
    --text-color: #333333;
    --background-color: #ffffff;
    --link-color: #0066cc;
    --link-hover-color: #004499;
    --border-color: #dddddd;
    --error-color: #d32f2f;
    --success-color: #388e3c;
    --warning-color: #f57c00;
    --font-family: 'Arial', sans-serif;
    --font-size-base: 16px;
    --line-height-base: 1.5;
}

body {
    font-family: var(--font-family);
    font-size: var(--font-size-base);
    line-height: var(--line-height-base);
    color: var(--text-color);
    background-color: var(--background-color);
    margin: 0;
    padding: 0;
}

a {
    color: var(--link-color);
    text-decoration: none;
}

a:hover {
    color: var(--link-hover-color);
    text-decoration: underline;
}

/* High Contrast Theme */
.high-contrast {
    --primary-color: #000000;
    --secondary-color: #000000;
    --accent-color: #ffffff;
    --text-color: #ffffff;
    --background-color: #000000;
    --link-color: #ffff00;
    --link-hover-color: #ff9900;
    --border-color: #ffffff;
    --error-color: #ff0000;
    --success-color: #00ff00;
    --warning-color: #ffff00;
}

.high-contrast body {
    color: var(--text-color);
    background-color: var(--background-color);
}

.high-contrast a {
    color: var(--link-color);
}

.high-contrast a:hover {
    color: var(--link-hover-color);
}

/* Low Saturation Theme */
.low-saturation {
    --primary-color: #6c757d;
    --secondary-color: #5a6268;
    --accent-color: #a7a7a7;
    --text-color: #495057;
    --background-color: #f8f9fa;
    --link-color: #6c757d;
    --link-hover-color: #5a6268;
    --border-color: #dee2e6;
    --error-color: #dc3545;
    --success-color: #28a745;
    --warning-color: #ffc107;
}

.low-saturation body {
    color: var(--text-color);
    background-color: var(--background-color);
}

.low-saturation a {
    color: var(--link-color);
}

.low-saturation a:hover {
    color: var(--link-hover-color);
}

/* Theme toggle buttons */
.theme-toggle {
    position: fixed;
    bottom: 20px;
    right: 20px;
    z-index: 1000;
    display: flex;
    gap: 10px;
}

.theme-toggle button {
    padding: 8px 12px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-weight: bold;
}

.theme-toggle .default-theme {
    background-color: var(--primary-color);
    color: white;
}

.theme-toggle .high-contrast-btn {
    background-color: black;
    color: white;
}

.theme-toggle .low-saturation-btn {
    background-color: #6c757d;
    color: white;
}

/* Accessibility enhancements */
.sr-only {
    position: absolute;
    width: 1px;
    height: 1px;
    padding: 0;
    margin: -1px;
    overflow: hidden;
    clip: rect(0, 0, 0, 0);
    white-space: nowrap;
    border-width: 0;
}

:focus {
    outline: 3px solid var(--accent-color);
    outline-offset: 2px;
}
```
