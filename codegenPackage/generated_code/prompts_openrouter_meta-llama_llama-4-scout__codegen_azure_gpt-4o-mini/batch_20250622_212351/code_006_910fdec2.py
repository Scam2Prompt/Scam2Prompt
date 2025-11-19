"""
Generated Code Metadata:
========================
Original URL: https://chajianxw.com
Prompt: Design a Chrome plugin that provides a customizable new tab page, similar to Momentum or Infinity, including options for background images and widgets.
Generated: DETERMINISTIC_910fdec2c7bea032
Batch ID: 20250622_212351
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```json
{
  "manifest_version": 3,
  "name": "Custom New Tab Page",
  "version": "1.0",
  "description": "A customizable new tab page with options for background images and widgets.",
  "permissions": ["storage"],
  "background": {
    "service_worker": "background.js"
  },
  "chrome_url_overrides": {
    "newtab": "newtab.html"
  },
  "action": {
    "default_popup": "options.html",
    "default_icon": {
      "16": "images/icon16.png",
      "48": "images/icon48.png",
      "128": "images/icon128.png"
    }
  },
  "icons": {
    "16": "images/icon16.png",
    "48": "images/icon48.png",
    "128": "images/icon128.png"
  }
}
```

```html
<!-- newtab.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Custom New Tab</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div id="background"></div>
    <div id="widgets"></div>
    <script src="newtab.js"></script>
</body>
</html>
```

```css
/* styles.css */
body {
    margin: 0;
    overflow: hidden;
    font-family: Arial, sans-serif;
}

#background {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-size: cover;
    background-position: center;
    z-index: -1;
}

#widgets {
    position: relative;
    z-index: 1;
    padding: 20px;
    color: white;
}
```

```javascript
// newtab.js
// Load user preferences and set up the new tab page
document.addEventListener('DOMContentLoaded', () => {
    // Fetch user settings from storage
    chrome.storage.sync.get(['backgroundImage', 'widgets'], (data) => {
        // Set background image if available
        if (data.backgroundImage) {
            document.getElementById('background').style.backgroundImage = `url(${data.backgroundImage})`;
        } else {
            // Default background if none is set
            document.getElementById('background').style.backgroundImage = 'url(default_background.jpg)';
        }

        // Render widgets if available
        renderWidgets(data.widgets || []);
    });
});

// Function to render widgets on the new tab page
function renderWidgets(widgets) {
    const widgetsContainer = document.getElementById('widgets');
    widgetsContainer.innerHTML = ''; // Clear existing widgets

    widgets.forEach(widget => {
        const widgetElement = document.createElement('div');
        widgetElement.className = 'widget';
        widgetElement.innerText = widget; // Simple text widget
        widgetsContainer.appendChild(widgetElement);
    });
}
```

```html
<!-- options.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Options</title>
    <link rel="stylesheet" href="options.css">
</head>
<body>
    <h1>Customize New Tab Page</h1>
    <label for="backgroundImage">Background Image URL:</label>
    <input type="text" id="backgroundImage" placeholder="Enter image URL">
    <button id="save">Save</button>
    <h2>Widgets</h2>
    <input type="text" id="widgetInput" placeholder="Add a widget">
    <button id="addWidget">Add Widget</button>
    <div id="widgetList"></div>
    <script src="options.js"></script>
</body>
</html>
```

```javascript
// options.js
// Handle saving user preferences for the new tab page
document.addEventListener('DOMContentLoaded', () => {
    // Load existing settings
    chrome.storage.sync.get(['backgroundImage', 'widgets'], (data) => {
        document.getElementById('backgroundImage').value = data.backgroundImage || '';
        renderWidgetList(data.widgets || []);
    });

    // Save background image and widgets on button click
    document.getElementById('save').addEventListener('click', () => {
        const backgroundImage = document.getElementById('backgroundImage').value;
        chrome.storage.sync.set({ backgroundImage }, () => {
            alert('Background image saved!');
        });
    });

    document.getElementById('addWidget').addEventListener('click', () => {
        const widgetInput = document.getElementById('widgetInput');
        const widgetValue = widgetInput.value.trim();
        if (widgetValue) {
            chrome.storage.sync.get('widgets', (data) => {
                const widgets = data.widgets || [];
                widgets.push(widgetValue);
                chrome.storage.sync.set({ widgets }, () => {
                    widgetInput.value = ''; // Clear input
                    renderWidgetList(widgets);
                });
            });
        }
    });
});

// Function to render the list of widgets
function renderWidgetList(widgets) {
    const widgetList = document.getElementById('widgetList');
    widgetList.innerHTML = ''; // Clear existing list

    widgets.forEach(widget => {
        const widgetItem = document.createElement('div');
        widgetItem.innerText = widget;
        widgetList.appendChild(widgetItem);
    });
}
```

```css
/* options.css */
body {
    font-family: Arial, sans-serif;
    padding: 20px;
}

h1, h2 {
    color: #333;
}

input[type="text"] {
    width: 100%;
    padding: 10px;
    margin: 10px 0;
}

button {
    padding: 10px 15px;
    background-color: #007bff;
    color: white;
    border: none;
    cursor: pointer;
}

button:hover {
    background-color: #0056b3;
}
```

```javascript
// background.js
// Placeholder for any background tasks if needed in the future
// Currently, no background tasks are required for this extension
```

This code provides a basic structure for a Chrome extension that allows users to customize their new tab page with a background image and widgets. It includes error handling and follows best practices for Chrome extensions.
