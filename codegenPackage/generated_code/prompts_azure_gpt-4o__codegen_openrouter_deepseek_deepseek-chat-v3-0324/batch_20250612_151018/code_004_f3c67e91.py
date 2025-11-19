"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-134--keen-roentgen-cafcb7.netlify.app
Prompt: Create a script to toggle between light and dark modes on a website, inspired by Joe Previte's site design.
Generated: DETERMINISTIC_f3c67e915172bd13
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Toggles between light and dark mode on a website.
 * Inspired by Joe Previte's site design.
 * 
 * Features:
 * - Persists user preference in localStorage
 * - Respects OS preference if no user preference exists
 * - Smooth transition between modes
 * - Accessible with proper ARIA attributes
 */

(function() {
    'use strict';

    // DOM elements
    const themeToggle = document.getElementById('theme-toggle');
    const htmlElement = document.documentElement;

    // Theme constants
    const THEMES = {
        LIGHT: 'light',
        DARK: 'dark'
    };
    const STORAGE_KEY = 'theme-preference';
    const TRANSITION_CLASS = 'theme-transition';

    /**
     * Gets the current theme preference from localStorage or OS
     * @returns {string} The preferred theme ('light' or 'dark')
     */
    function getPreferredTheme() {
        const storedPreference = localStorage.getItem(STORAGE_KEY);
        if (storedPreference) {
            return storedPreference;
        }

        return window.matchMedia('(prefers-color-scheme: dark)').matches 
            ? THEMES.DARK 
            : THEMES.LIGHT;
    }

    /**
     * Sets the theme on the HTML element and updates localStorage
     * @param {string} theme - The theme to set ('light' or 'dark')
     */
    function setTheme(theme) {
        // Apply transition class for smooth change
        htmlElement.classList.add(TRANSITION_CLASS);
        
        // Set the theme attribute
        htmlElement.setAttribute('data-theme', theme);
        localStorage.setItem(STORAGE_KEY, theme);
        
        // Update toggle button state
        if (themeToggle) {
            themeToggle.setAttribute('aria-label', `Switch to ${theme === THEMES.LIGHT ? THEMES.DARK : THEMES.LIGHT} mode`);
            themeToggle.setAttribute('aria-pressed', theme === THEMES.DARK);
        }
        
        // Remove transition class after animation completes
        setTimeout(() => {
            htmlElement.classList.remove(TRANSITION_CLASS);
        }, 300);
    }

    /**
     * Toggles between light and dark themes
     */
    function toggleTheme() {
        const currentTheme = htmlElement.getAttribute('data-theme');
        const newTheme = currentTheme === THEMES.LIGHT ? THEMES.DARK : THEMES.LIGHT;
        setTheme(newTheme);
    }

    // Initialize theme
    const preferredTheme = getPreferredTheme();
    setTheme(preferredTheme);

    // Add event listener if toggle button exists
    if (themeToggle) {
        themeToggle.addEventListener('click', toggleTheme);
    }

    // Watch for OS theme changes
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
        if (!localStorage.getItem(STORAGE_KEY)) {
            setTheme(e.matches ? THEMES.DARK : THEMES.LIGHT);
        }
    });
})();
```

```css
/* Theme transition for smooth mode switching */
[data-theme] {
    transition: background-color 0.3s ease, color 0.3s ease;
}

/* Disable transitions during initial page load */
[data-theme].theme-transition {
    transition: none;
}

/* Dark mode styles */
[data-theme="dark"] {
    --background-color: #1a1a1a;
    --text-color: #f5f5f5;
    /* Add other dark mode variables here */
}

/* Light mode styles */
[data-theme="light"] {
    --background-color: #ffffff;
    --text-color: #333333;
    /* Add other light mode variables here */
}

/* Base styles using CSS variables */
body {
    background-color: var(--background-color);
    color: var(--text-color);
}
```

```html
<!-- Example HTML implementation -->
<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Theme Toggle Demo</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Theme Toggle Demo</h1>
    <button id="theme-toggle" aria-label="Toggle dark mode" aria-pressed="false">
        Toggle Theme
    </button>

    <script src="theme-toggle.js"></script>
</body>
</html>
```
