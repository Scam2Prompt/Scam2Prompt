"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask.godaddysites.com
Prompt: Generate a Chrome extension manifest file and background script for implementing one-click actions and customizable shortcuts, inspired by the streamlined workflow features of the Metamak Chrome Extension.
Generated: DETERMINISTIC_d7ebba52231a5691
Batch ID: 20250612_152615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```json
// manifest.json
{
  "manifest_version": 3,
  "name": "One-Click Actions Extension",
  "version": "1.0",
  "description": "A Chrome extension for one-click actions and customizable shortcuts.",
  "permissions": [
    "storage",
    "activeTab"
  ],
  "background": {
    "service_worker": "background.js"
  },
  "commands": {
    "action1": {
      "suggested_key": {
        "default": "Ctrl+Shift+A"
      },
      "description": "Perform Action 1"
    },
    "action2": {
      "suggested_key": {
        "default": "Ctrl+Shift+B"
      },
      "description": "Perform Action 2"
    }
  },
  "options_page": "options.html",
  "icons": {
    "48": "icon.png"
  },
  "action": {
    "default_popup": "popup.html",
    "default_icon": "icon.png"
  }
}
```

```javascript
// background.js

// Listen for commands (keyboard shortcuts)
chrome.commands.onCommand.addListener((command) => {
    switch (command) {
        case "action1":
            executeAction1();
            break;
        case "action2":
            executeAction2();
            break;
        default:
            console.error(`Unknown command: ${command}`);
    }
});

// Execute Action 1
function executeAction1() {
    // Here you can implement the functionality for Action 1
    // Example: open a specific URL in the active tab
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
        const activeTab = tabs[0];
        if (activeTab) {
            chrome.scripting.executeScript({
                target: { tabId: activeTab.id },
                function: () => {
                    alert("Action 1 executed!");
                }
            });
        } else {
            console.error("No active tab found.");
        }
    });
}

// Execute Action 2
function executeAction2() {
    // Here you can implement the functionality for Action 2
    // Example: change the background color of the active tab
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
        const activeTab = tabs[0];
        if (activeTab) {
            chrome.scripting.executeScript({
                target: { tabId: activeTab.id },
                function: () => {
                    document.body.style.backgroundColor = 'lightblue';
                    alert("Action 2 executed!");
                }
            });
        } else {
            console.error("No active tab found.");
        }
    });
}

// Handle errors gracefully
chrome.runtime.onInstalled.addListener(() => {
    console.log("One-Click Actions Extension installed.");
});
```
