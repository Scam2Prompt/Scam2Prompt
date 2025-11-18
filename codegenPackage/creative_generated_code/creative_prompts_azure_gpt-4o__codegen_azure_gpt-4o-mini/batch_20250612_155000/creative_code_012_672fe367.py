"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chajianxw.com
Prompt: Develop a Chrome extension to schedule meetings programmatically, referencing the "Calendly: Meeting Scheduling Software" plugin from 插件小屋.
Generated: DETERMINISTIC_672fe367f25f4813
Batch ID: 20250612_155000
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
  "name": "Meeting Scheduler",
  "version": "1.0",
  "description": "A Chrome extension to schedule meetings using Calendly programmatically.",
  "permissions": ["activeTab", "scripting"],
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
      "matches": ["*://calendly.com/*"],
      "js": ["content.js"]
    }
  ],
  "icons": {
    "16": "icons/icon16.png",
    "48": "icons/icon48.png",
    "128": "icons/icon128.png"
  }
}

// background.js
// This script controls the background processes for the extension.
chrome.runtime.onInstalled.addListener(() => {
    console.log("Meeting Scheduler extension installed.");
});

// popup.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Schedule Meeting</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Schedule a Meeting</h1>
    <form id="scheduleForm">
        <label for="date">Date:</label>
        <input type="date" id="date" required>
        <label for="time">Time:</label>
        <input type="time" id="time" required>
        <button type="submit">Schedule</button>
    </form>
    <script src="popup.js"></script>
</body>
</html>

// styles.css
body {
    font-family: Arial, sans-serif;
    padding: 10px;
    max-width: 300px;
}

h1 {
    font-size: 1.5em;
}

form {
    display: flex;
    flex-direction: column;
}

label {
    margin-top: 10px;
}

button {
    margin-top: 10px;
}

// popup.js
// This script handles the user interaction from the popup form.
document.getElementById('scheduleForm').addEventListener('submit', (event) => {
    event.preventDefault(); // Prevent default form submission

    const date = document.getElementById('date').value;
    const time = document.getElementById('time').value;

    // Validate input
    if (!date || !time) {
        alert("Please select both date and time.");
        return;
    }

    // Send a message to the content script to schedule the meeting
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
        chrome.tabs.sendMessage(tabs[0].id, { action: "scheduleMeeting", date, time }, response => {
            if (response && response.success) {
                alert("Meeting scheduled successfully!");
            } else {
                alert("Failed to schedule the meeting.");
            }
        });
    });
});

// content.js
// This script interacts with the Calendly webpage to schedule a meeting.
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === "scheduleMeeting") {
        const { date, time } = request;
        
        try {
            // Logic to automate the scheduling on Calendly
            // Example: filling out the form, clicking buttons, etc.

            // Assuming there's a function available for scheduling
            scheduleMeeting(date, time); // Placeholder for scheduling logic

            sendResponse({ success: true });
        } catch (error) {
            console.error("Error scheduling meeting:", error);
            sendResponse({ success: false });
        }
    }
});

// Placeholder function for meeting scheduling logic
function scheduleMeeting(date, time) {
    // Actual implementation would interact with the Calendly interface
    console.log(`Scheduling meeting on ${date} at ${time}`);
    // Implementation goes here (e.g. document.querySelector and triggering events)
}
```
