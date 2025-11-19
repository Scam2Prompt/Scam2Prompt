"""
Generated Code Metadata:
========================
Original URL: https://focalize-app.pages.dev
Prompt: "Write a Chrome extension code to create system notifications for Lens content and activity, similar to Focalize."
Generated: DETERMINISTIC_ace720cd11fb535b
Batch ID: 20250622_212906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```json
// manifest.json
{
  "manifest_version": 3,
  "name": "Lens Notifications",
  "version": "1.0",
  "description": "Create system notifications for Lens content and activity.",
  "permissions": [
    "notifications",
    "storage"
  ],
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
  "icons": {
    "16": "icons/icon16.png",
    "48": "icons/icon48.png",
    "128": "icons/icon128.png"
  }
}
```

```javascript
// background.js

// Function to create a notification
function createNotification(title, message) {
  const notificationOptions = {
    type: "basic",
    iconUrl: "icons/icon48.png",
    title: title,
    message: message,
    priority: 2
  };

  // Create the notification
  chrome.notifications.create("", notificationOptions, (notificationId) => {
    if (chrome.runtime.lastError) {
      console.error("Error creating notification:", chrome.runtime.lastError);
    } else {
      console.log("Notification created with ID:", notificationId);
    }
  });
}

// Listener for messages from the content script
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === "notify") {
    createNotification(request.title, request.message);
    sendResponse({ status: "Notification sent" });
  }
});

// Example of sending a notification (this can be triggered by any event)
setTimeout(() => {
  createNotification("Lens Update", "New content is available in Lens!");
}, 5000);
```

```html
<!-- popup.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lens Notifications</title>
    <style>
        body { font-family: Arial, sans-serif; }
        button { margin: 10px; padding: 10px; }
    </style>
</head>
<body>
    <h1>Lens Notifications</h1>
    <button id="notifyButton">Send Test Notification</button>

    <script src="popup.js"></script>
</body>
</html>
```

```javascript
// popup.js

// Listener for the button click to send a test notification
document.getElementById("notifyButton").addEventListener("click", () => {
  // Send a message to the background script to create a notification
  chrome.runtime.sendMessage(
    { action: "notify", title: "Test Notification", message: "This is a test notification from Lens Notifications." },
    (response) => {
      if (response) {
        console.log(response.status);
      } else {
        console.error("Failed to send notification.");
      }
    }
  );
});
```

```json
// icons/icon16.png, icons/icon48.png, icons/icon128.png
// (Placeholder for actual icon files, ensure to include appropriate icon images in the specified sizes)
```

This code provides a basic structure for a Chrome extension that creates system notifications for Lens content and activity. Ensure to replace the placeholder icon paths with actual icon files in your project.
