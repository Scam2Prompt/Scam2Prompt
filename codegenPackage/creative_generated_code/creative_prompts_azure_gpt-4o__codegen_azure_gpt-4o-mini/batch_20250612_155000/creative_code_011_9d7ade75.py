"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chajianxw.com
Prompt: Write a script to create a custom Chrome extension that modifies the appearance of Google Docs using dark mode settings, inspired by "Google Docs Dark Mode" from 插件小屋.
Generated: DETERMINISTIC_9d7ade75b34536db
Batch ID: 20250612_155000
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://docs.google.com/document/*": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```json
// manifest.json
{
  "manifest_version": 3,
  "name": "Google Docs Dark Mode",
  "version": "1.0",
  "description": "Custom Chrome extension to apply dark mode settings to Google Docs.",
  "permissions": ["activeTab", "scripting"],
  "background": {
    "service_worker": "background.js"
  },
  "content_scripts": [
    {
      "matches": ["https://docs.google.com/document/*"],
      "js": ["content.js"],
      "css": ["styles.css"]
    }
  ],
  "action": {
    "default_popup": "popup.html",
    "default_icon": {
      "16": "icons/icon16.png",
      "48": "icons/icon48.png",
      "128": "icons/icon128.png"
    }
  },
  "icons": {
    "16": "icons/icon16.png",
    "48": "icons/icon48.png",
    "128": "icons/icon128.png"
  }
}
```

```javascript
// background.js
// Background script for event handling

chrome.runtime.onInstalled.addListener(() => {
  console.log("Google Docs Dark Mode extension installed.");
});

// Optional: Add any future background features or event listeners here
```

```javascript
// content.js
// Content script that applies dark mode styles to Google Docs

// Function to apply dark mode styles
function applyDarkMode() {
  try {
    // Set body background color
    document.body.style.backgroundColor = "#121212"; // Dark background
    document.body.style.color = "#E0E0E0"; // Light text color

    // Modify specific elements to ensure readability
    const headers = document.querySelectorAll("h1, h2, h3, h4, h5, h6");
    headers.forEach(header => {
      header.style.color = "#F0F0F0"; // Lighter color for headers
    });

    // Add additional styles as needed
    console.log("Dark mode applied to Google Docs.");
  } catch (error) {
    console.error("Error applying dark mode:", error);
  }
}

// Wait for the document to be fully loaded before applying styles
document.addEventListener("DOMContentLoaded", applyDarkMode);
```

```css
/* styles.css */
/* Custom styles for Google Docs Dark Mode */

body {
  transition: background-color 0.3s ease, color 0.3s ease; /* Smooth transition for dark mode */
}

/* Adjust other elements as needed */
```

```html
<!-- popup.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Google Docs Dark Mode</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            padding: 10px;
            background-color: #121212;
            color: #E0E0E0;
        }
        button {
            background-color: #6200EE;
            color: white;
            border: none;
            padding: 10px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        button:hover {
            background-color: #3700B3;
        }
    </style>
</head>
<body>
    <h1>Google Docs Dark Mode</h1>
    <p>Toggle dark mode for Google Docs.</p>
    <button id="toggleDarkMode">Toggle Dark Mode</button>

    <script>
        document.getElementById("toggleDarkMode").addEventListener("click", () => {
            // Simple toggle logic (implement local storage if needed)
            alert("Dark mode toggled (functionality not yet implemented).");
        });
    </script>
</body>
</html>
```

Make sure to create the appropriate icon files in the specified paths, and you can expand functionality such as toggling dark mode in the future with local storage or other state management techniques.
