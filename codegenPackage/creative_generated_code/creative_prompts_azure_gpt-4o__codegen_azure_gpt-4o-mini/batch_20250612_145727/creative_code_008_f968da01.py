"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://onlytest.cc
Prompt: Develop a feature for customizable themes with light and dark modes, ensuring easy integration into a social media platform like Lovr.
Generated: DETERMINISTIC_f968da01345cb958
Batch ID: 20250612_145727
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// themeManager.js

/**
 * ThemeManager class to handle customizable themes with light and dark modes.
 */
class ThemeManager {
    constructor() {
        this.theme = 'light'; // Default theme
        this.init(); // Initialize theme on load
    }

    /**
     * Initialize the theme by checking localStorage.
     */
    init() {
        const savedTheme = localStorage.getItem('theme');
        if (savedTheme) {
            this.setTheme(savedTheme);
        } else {
            this.setTheme(this.theme); // Default to light theme if none saved
        }
    }

    /**
     * Sets the theme for the application.
     * @param {string} theme - The theme to set ('light' or 'dark').
     */
    setTheme(theme) {
        if (theme !== 'light' && theme !== 'dark') {
            console.error(`Invalid theme: ${theme}. Defaulting to light.`);
            theme = 'light';
        }
        this.theme = theme;
        document.body.className = theme; // Update body class
        localStorage.setItem('theme', theme); // Save theme to localStorage
    }

    /**
     * Toggles between light and dark themes.
     */
    toggleTheme() {
        const newTheme = this.theme === 'light' ? 'dark' : 'light';
        this.setTheme(newTheme);
    }
}

// Instantiate the ThemeManager
const themeManager = new ThemeManager();

// Event listener for theme toggle button
document.getElementById('theme-toggle').addEventListener('click', () => {
    themeManager.toggleTheme();
});
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Customizable Themes</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <button id="theme-toggle">Toggle Theme</button>
    <script src="themeManager.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* Light Theme Styles */
body.light {
    background-color: #ffffff;
    color: #000000;
}

/* Dark Theme Styles */
body.dark {
    background-color: #000000;
    color: #ffffff;
}

/* Button Styles */
button {
    padding: 10px 15px;
    font-size: 16px;
    cursor: pointer;
    margin-top: 20px;
}
```
