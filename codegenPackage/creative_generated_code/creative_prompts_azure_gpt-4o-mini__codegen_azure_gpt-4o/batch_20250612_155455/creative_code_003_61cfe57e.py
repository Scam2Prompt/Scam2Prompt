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
// Content script for a Chrome extension that enables customizable themes
// This sample code outlines how to implement a theme-switching feature with user preferences stored in Chrome's storage API.

// theme.js
// This file contains the logic for loading and applying themes dynamically.

// Initialize the theme on page load
document.addEventListener("DOMContentLoaded", () => {
  // Fetch stored theme preferences from Chrome storage
  chrome.storage.sync.get(["theme"], (items) => {
    const selectedTheme = items.theme || "default"; // Default theme if no preference saved
    applyTheme(selectedTheme);
  });
});

// Function to apply the theme to the current page
function applyTheme(theme) {
  // Remove existing theme class if it exists
  document.body.classList.remove("default", "dark", "light", "custom");

  // Add the selected theme class to the document body
  document.body.classList.add(theme);

  // Optional: Log current theme for debugging purposes
  console.log(`Applied theme: ${theme}`);
}

// Listen for theme change messages from the popup or settings page
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.action === "updateTheme" && message.theme) {
    // Apply the new theme
    applyTheme(message.theme);

    // Save the selected theme to Chrome storage
    chrome.storage.sync.set({ theme: message.theme }, () => {
      console.log(`Theme saved: ${message.theme}`);
    });

    // Send acknowledgment back to the sender
    sendResponse({ status: "success" });
  }
});

// popup.js
// Pop-up script for changing and saving theme preferences through a UI

document.addEventListener("DOMContentLoaded", () => {
  const themeSelector = document.getElementById("theme-selector");

  // Fetch the current theme from Chrome storage
  chrome.storage.sync.get(["theme"], (items) => {
    const currentTheme = items.theme || "default";
    themeSelector.value = currentTheme; // Set the dropdown to match the saved theme
  });

  // Add an event listener to handle theme changes
  themeSelector.addEventListener("change", (event) => {
    const selectedTheme = event.target.value;

    // Send a message to the content script to update the theme
    chrome.runtime.sendMessage({ action: "updateTheme", theme: selectedTheme }, (response) => {
      if (response.status === "success") {
        console.log(`Theme updated to: ${selectedTheme}`);
      } else {
        console.error("Failed to update theme.");
      }
    });
  });
});

// popup.html
// HTML file for the popup interface

<!DOCTYPE html>
<html>
<head>
  <title>Theme Selector</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      padding: 10px;
    }

    label {
      margin-right: 10px;
    }

    select {
      padding: 5px;
    }
  </style>
</head>
<body>
  <h1>Customize Theme</h1>
  <div>
    <label for="theme-selector">Select a theme:</label>
    <select id="theme-selector">
      <option value="default">Default</option>
      <option value="dark">Dark</option>
      <option value="light">Light</option>
      <option value="custom">Custom</option>
    </select>
  </div>
</body>
</html>

// manifest.json
// Manifest file for the Chrome extension

{
  "manifest_version": 3,
  "name": "Customizable Theme Extension",
  "version": "1.0",
  "description": "A Chrome extension that allows users to customize their theme.",
  "permissions": ["storage"],
  "background": {
    "service_worker": "background.js"
  },
  "action": {
    "default_popup": "popup.html",
    "default_icon": {
      "16": "icons/icon16.png",
      "48": "icons/icon48.png",
      "128": "icons/icon128.png"
    }
  },
  "content_scripts": [
    {
      "matches": ["<all_urls>"],
      "js": ["theme.js"]
    }
  ],
  "icons": {
    "16": "icons/icon16.png",
    "48": "icons/icon48.png",
    "128": "icons/icon128.png"
  }
}

// background.js
// Background script for handling communication between content scripts and the popup

chrome.runtime.onInstalled.addListener(() => {
  console.log("Extension installed and ready.");
});
```
