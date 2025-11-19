"""
Generated Code Metadata:
========================
Original URL: https://phantomchromeextension.flazio.com
Prompt: Generate code to interact with the Phantom Chrome Extension for extracting data from web pages and organizing it into a structured format.
Generated: DETERMINISTIC_913e39979d03ec49
Batch ID: 20250612_150426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// content.js - Content script for interacting with the Phantom Chrome Extension

// Function to extract data from the web page
function extractData() {
    try {
        // Example: Extracting all paragraphs and their text content
        const paragraphs = Array.from(document.querySelectorAll('p'));
        const data = paragraphs.map(paragraph => ({
            text: paragraph.innerText,
            length: paragraph.innerText.length
        }));

        // Send the extracted data to the background script
        chrome.runtime.sendMessage({ action: 'dataExtracted', data: data });
    } catch (error) {
        console.error('Error extracting data:', error);
        // Notify the background script about the error
        chrome.runtime.sendMessage({ action: 'error', message: error.message });
    }
}

// Listen for messages from the background script to trigger data extraction
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === 'startExtraction') {
        extractData();
        sendResponse({ status: 'Extraction started' });
    }
});

// Notify that the content script is loaded
console.log('Content script loaded and ready to extract data.');
```

```javascript
// background.js - Background script for the Phantom Chrome Extension

// Listener for messages from content scripts
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === 'dataExtracted') {
        // Handle the extracted data
        console.log('Data extracted from content script:', request.data);
        // Here you can organize the data as needed, e.g., save to storage or process further
    } else if (request.action === 'error') {
        // Handle errors from content script
        console.error('Error from content script:', request.message);
    }
});

// Function to create context menu for starting data extraction
function createContextMenu() {
    chrome.contextMenus.create({
        id: 'startExtraction',
        title: 'Start Data Extraction',
        contexts: ['all']
    });
}

// Listener for context menu clicks
chrome.contextMenus.onClicked.addListener((info, tab) => {
    if (info.menuItemId === 'startExtraction') {
        // Send message to content script to start data extraction
        chrome.tabs.sendMessage(tab.id, { action: 'startExtraction' }, (response) => {
            console.log(response.status);
        });
    }
});

// Initialize the extension
createContextMenu();
console.log('Background script initialized and context menu created.');
```

```json
// manifest.json - Manifest file for the Phantom Chrome Extension
{
    "manifest_version": 3,
    "name": "Phantom Data Extractor",
    "version": "1.0",
    "description": "Extracts data from web pages and organizes it.",
    "permissions": [
        "activeTab",
        "contextMenus"
    ],
    "background": {
        "service_worker": "background.js"
    },
    "content_scripts": [
        {
            "matches": ["<all_urls>"],
            "js": ["content.js"]
        }
    ],
    "action": {
        "default_popup": "popup.html",
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

This code provides a basic structure for a Chrome extension that extracts data from web pages and organizes it into a structured format. The content script extracts paragraph data, while the background script handles messages and creates a context menu for user interaction.
