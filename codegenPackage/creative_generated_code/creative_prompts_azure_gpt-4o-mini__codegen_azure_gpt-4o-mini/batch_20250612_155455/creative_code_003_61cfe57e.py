"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask.godaddysites.com
Prompt: Generate a sample code for a customizable theme feature in a Chrome extension, taking cues from the Metamak Chrome Extension's personalization options.
Generated: DETERMINISTIC_61cfe57e0ed99c86
Batch ID: 20250612_155455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// popup.js - This script manages the customizable theme feature for the Chrome extension

// Function to apply the selected theme to the extension
function applyTheme(theme) {
    // Define a mapping of themes to CSS variables
    const themes = {
        light: {
            '--background-color': '#ffffff',
            '--text-color': '#000000',
            '--button-color': '#007bff',
        },
        dark: {
            '--background-color': '#333333',
            '--text-color': '#ffffff',
            '--button-color': '#007bff',
        },
        custom: {
            '--background-color': '#ffcc00',
            '--text-color': '#0000ff',
            '--button-color': '#ff5722',
        },
    };

    // Check if the selected theme is valid
    if (themes[theme]) {
        // Apply CSS variables for the selected theme
        const root = document.documentElement;
        Object.keys(themes[theme]).forEach((key) => {
            root.style.setProperty(key, themes[theme][key]);
        });
    } else {
        console.error(`Theme "${theme}" is not defined.`);
    }
}

// Function to save the selected theme to local storage
function saveTheme(theme) {
    try {
        // Save the theme to Chrome's storage
        chrome.storage.local.set({ selectedTheme: theme }, () => {
            if (chrome.runtime.lastError) {
                console.error("Error saving theme:", chrome.runtime.lastError);
            } else {
                console.log(`Theme "${theme}" saved successfully.`);
            }
        });
    } catch (error) {
        console.error("Error in saveTheme function:", error);
    }
}

// Function to load the theme from local storage
function loadTheme() {
    try {
        // Retrieve the theme from Chrome's storage
        chrome.storage.local.get('selectedTheme', (data) => {
            if (chrome.runtime.lastError) {
                console.error("Error loading theme:", chrome.runtime.lastError);
                return;
            }

            // Apply the loaded theme if it exists
            if (data.selectedTheme) {
                applyTheme(data.selectedTheme);
            } else {
                // Default to light theme if no theme is saved
                applyTheme('light');
            }
        });
    } catch (error) {
        console.error("Error in loadTheme function:", error);
    }
}

// Event listener for theme selection
document.addEventListener('DOMContentLoaded', () => {
    // Load the theme when the popup is opened
    loadTheme();

    // Add event listeners for theme selection buttons
    document.getElementById('light-theme').addEventListener('click', () => {
        applyTheme('light');
        saveTheme('light');
    });

    document.getElementById('dark-theme').addEventListener('click', () => {
        applyTheme('dark');
        saveTheme('dark');
    });

    document.getElementById('custom-theme').addEventListener('click', () => {
        applyTheme('custom');
        saveTheme('custom');
    });
});
```

```html
<!-- popup.html - This is the popup interface for the Chrome extension -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Theme Customization</title>
    <link rel="stylesheet" href="popup.css">
    <script src="popup.js" defer></script>
</head>
<body>
    <h1>Choose a Theme</h1>
    <button id="light-theme">Light Theme</button>
    <button id="dark-theme">Dark Theme</button>
    <button id="custom-theme">Custom Theme</button>
</body>
</html>
```

```css
/* popup.css - Basic styling for the popup interface */
body {
    background-color: var(--background-color);
    color: var(--text-color);
    font-family: Arial, sans-serif;
    padding: 20px;
}

button {
    background-color: var(--button-color);
    color: var(--text-color);
    border: none;
    padding: 10px 15px;
    margin: 5px;
    cursor: pointer;
}

button:hover {
    opacity: 0.9;
}
```

```json
// manifest.json - Manifest file for the Chrome extension
{
    "manifest_version": 3,
    "name": "Custom Theme Extension",
    "version": "1.0",
    "description": "A Chrome extension that allows users to customize themes.",
    "action": {
        "default_popup": "popup.html",
        "default_icon": {
            "16": "icon16.png",
            "48": "icon48.png",
            "128": "icon128.png"
        }
    },
    "permissions": [
        "storage"
    ],
    "icons": {
        "16": "icon16.png",
        "48": "icon48.png",
        "128": "icon128.png"
    }
}
```
