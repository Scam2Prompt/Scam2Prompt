"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getgrass-claim.pages.dev
Prompt: Develop a code snippet using JavaScript to create a browser extension that mimics the functionality of Grass, allowing users to share unused internet bandwidth securely for AI data collection.
Generated: DETERMINISTIC_dfafe9182a5830fd
Batch ID: 20250612_151246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// manifest.json
{
  "manifest_version": 3,
  "name": "Grass-like Bandwidth Sharing Extension",
  "version": "1.0",
  "description": "Share unused internet bandwidth securely for AI data collection.",
  "permissions": ["storage", "webRequest", "webRequestBlocking", "tabs"],
  "host_permissions": ["<all_urls>"],
  "background": {
    "service_worker": "background.js"
  },
  "action": {
    "default_popup": "popup.html",
    "default_icon": "icon.png"
  },
  "icons": {
    "48": "icon.png"
  }
}
```

```javascript
// background.js

// This script handles the background logic for bandwidth sharing

// Store user preferences and bandwidth usage state
let userPreferences = {
  enabled: false, // Whether the bandwidth sharing is turned on
  maxBandwidth: 1024 // Maximum bandwidth to use in KB/s
};

// Listen for messages from the popup or other parts of the extension
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.type === "toggleBandwidthSharing") {
    userPreferences.enabled = message.enabled;
    console.log(`Bandwidth sharing ${userPreferences.enabled ? "enabled" : "disabled"}`);
    sendResponse({ success: true });
  } else if (message.type === "updatePreferences") {
    userPreferences = { ...userPreferences, ...message.preferences };
    console.log("User preferences updated:", userPreferences);
    sendResponse({ success: true });
  }
});

// Function to securely share bandwidth
async function shareBandwidth(requestDetails) {
  if (!userPreferences.enabled) {
    return { cancel: false };
  }

  // Example logic: simulate bandwidth throttling
  // TODO: Replace with actual secure sharing logic as required by the service
  const bandwidthUsage = Math.random() * userPreferences.maxBandwidth;
  console.log(`Bandwidth usage: ${bandwidthUsage} KB/s`);

  // Ensure sharing complies with security and privacy standards
  // For demonstration, let the request proceed without modification
  return { cancel: false };
}

// Attach the secure sharing function to web requests
chrome.webRequest.onBeforeRequest.addListener(
  shareBandwidth,
  { urls: ["<all_urls>"] },
  ["blocking"]
);
```

```html
<!-- popup.html -->

<!DOCTYPE html>
<html>
<head>
  <title>Grass-like Extension</title>
  <script src="popup.js" defer></script>
  <style>
    body {
      font-family: Arial, sans-serif;
      padding: 10px;
    }
    .container {
      display: flex;
      flex-direction: column;
      align-items: center;
    }
    .button {
      background-color: #4CAF50;
      color: white;
      border: none;
      padding: 10px 20px;
      margin: 10px;
      cursor: pointer;
      border-radius: 5px;
    }
    .button:hover {
      background-color: #45a049;
    }
  </style>
</head>
<body>
<div class="container">
  <h1>Bandwidth Sharing</h1>
  <button id="toggleButton" class="button">Enable Sharing</button>
  <label for="maxBandwidth">Max Bandwidth (KB/s):</label>
  <input type="number" id="maxBandwidth" value="1024" />
  <button id="saveButton" class="button">Save Preferences</button>
</div>
</body>
</html>
```

```javascript
// popup.js

// DOM Elements
const toggleButton = document.getElementById("toggleButton");
const maxBandwidthInput = document.getElementById("maxBandwidth");

// State variable for tracking enabled/disabled status
let enabled = false;

// Handle toggle button click
toggleButton.addEventListener("click", () => {
  enabled = !enabled;
  toggleButton.textContent = enabled ? "Disable Sharing" : "Enable Sharing";

  // Communicate with the background script
  chrome.runtime.sendMessage(
    { type: "toggleBandwidthSharing", enabled },
    (response) => {
      if (response.success) {
        console.log("Bandwidth sharing toggled successfully.");
      }
    }
  );
});

// Handle save preferences button click
document.getElementById("saveButton").addEventListener("click", () => {
  const maxBandwidth = parseInt(maxBandwidthInput.value, 10);

  if (isNaN(maxBandwidth) || maxBandwidth <= 0) {
    alert("Please enter a valid bandwidth amount.");
    return;
  }

  // Save preferences via background script
  chrome.runtime.sendMessage(
    { type: "updatePreferences", preferences: { maxBandwidth } },
    (response) => {
      if (response.success) {
        alert("Preferences saved successfully!");
      }
    }
  );
});
```

```plaintext
// icon.png
// Use any 48x48 pixel icon image for the extension logo.
```

This code snippet creates a basic browser extension that mimics the functionality of bandwidth sharing securely. It includes a manifest file, background script, popup HTML for user interaction, and accompanying JavaScript for UI logic. Adjustments may be required to implement actual secure bandwidth sharing functionality.
