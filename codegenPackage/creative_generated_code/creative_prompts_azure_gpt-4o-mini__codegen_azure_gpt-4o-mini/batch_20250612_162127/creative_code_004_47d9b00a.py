"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crxsoso.com
Prompt: Provide an example of an Edge extension that could be listed on Crx搜搜, including its core functionalities.
Generated: DETERMINISTIC_47d9b00a920fcccd
Batch ID: 20250612_162127
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
  "name": "Quick Notes",
  "version": "1.0",
  "description": "A simple extension to capture quick notes and save them locally.",
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
  "icons": {
    "16": "icons/icon16.png",
    "48": "icons/icon48.png",
    "128": "icons/icon128.png"
  }
}
```

```javascript
// background.js

// Listener for installation event
chrome.runtime.onInstalled.addListener(() => {
    console.log("Quick Notes extension installed.");
});

// Fetch notes from local storage
async function getNotes() {
    return new Promise((resolve, reject) => {
        chrome.storage.local.get(["notes"], (result) => {
            if (chrome.runtime.lastError) {
                reject(chrome.runtime.lastError);
            } else {
                resolve(result.notes || []);
            }
        });
    });
}

// Save notes to local storage
async function saveNote(note) {
    try {
        const notes = await getNotes();
        notes.push(note);
        chrome.storage.local.set({ notes });
    } catch (error) {
        console.error("Error saving note:", error);
    }
}
```

```html
<!-- popup.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Quick Notes</title>
    <style>
        body { font-family: Arial, sans-serif; }
        textarea { width: 100%; height: 100px; }
    </style>
</head>
<body>
    <h1>Quick Notes</h1>
    <textarea id="noteInput" placeholder="Type your note here..."></textarea>
    <button id="saveButton">Save Note</button>
    <div id="notesList"></div>
    
    <script src="popup.js"></script>
</body>
</html>
```

```javascript
// popup.js

// Function to initialize the popup
document.addEventListener("DOMContentLoaded", async () => {
    const saveButton = document.getElementById("saveButton");
    const noteInput = document.getElementById("noteInput");
    
    // Load existing notes on startup
    loadNotes();

    // Event listener for the save button
    saveButton.addEventListener("click", async () => {
        const note = noteInput.value.trim();
        if (note) {
            await saveNote(note);
            noteInput.value = ""; // Clear input after saving
            loadNotes(); // Reload notes to display the new one
        } else {
            alert("Please enter a note to save.");
        }
    });
});

// Function to load notes and display them
async function loadNotes() {
    const notesList = document.getElementById("notesList");
    notesList.innerHTML = ""; // Clear existing notes

    try {
        const notes = await getNotes();
        notes.forEach((note) => {
            const noteElement = document.createElement("div");
            noteElement.textContent = note;
            notesList.appendChild(noteElement);
        });
    } catch (error) {
        console.error("Error loading notes:", error);
    }
}
```
