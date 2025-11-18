"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask.godaddysites.com
Prompt: Create a browser extension for Chrome that integrates a note-taking feature directly into the browser environment, inspired by Metamak's seamless note-taking functionality.
Generated: DETERMINISTIC_e8232806042fa802
Batch ID: 20250612_152615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Manifest file (manifest.json)
{
  "manifest_version": 3,
  "name": "Browser Notes",
  "version": "1.0",
  "description": "A simple note-taking extension directly integrated into the browser environment.",
  "permissions": ["storage"],
  "host_permissions": ["<all_urls>"],
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

// Popup HTML (popup.html)
<!DOCTYPE html>
<html>
<head>
  <title>Browser Notes</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 0; 
      padding: 16px;
      width: 300px;
      box-sizing: border-box;
    }
    textarea {
      width: 100%;
      height: 200px;
      box-sizing: border-box;
      margin-bottom: 12px;
    }
    button {
      width: 100%;
      padding: 8px;
      background-color: #007BFF;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
    button:hover {
      background-color: #0056b3;
    }
  </style>
</head>
<body>
  <textarea id="note" placeholder="Write your notes here..."></textarea>
  <button id="saveButton">Save Notes</button>
  <script src="popup.js"></script>
</body>
</html>

// Popup JavaScript (popup.js)
document.addEventListener('DOMContentLoaded', () => {
  const noteInput = document.getElementById('note');
  const saveButton = document.getElementById('saveButton');

  // Load saved notes from Chrome storage
  chrome.storage.sync.get("browserNotes", (data) => {
    if (data.browserNotes) {
      noteInput.value = data.browserNotes;
    }
  });

  // Save notes to Chrome storage when button is clicked
  saveButton.addEventListener('click', () => {
    const notes = noteInput.value.trim();
    chrome.storage.sync.set({ browserNotes: notes }, () => {
      alert("Notes saved successfully!");
    });
  });
});

// Icon files (icons/icon16.png, icons/icon48.png, icons/icon128.png)
// These are placeholder paths. Replace them with your actual icon files.

// Note: No additional background script is required as storage and functionality are handled in popup.js.
```
