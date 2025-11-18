"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantomchromeextension.flazio.com
Prompt: Generate code to interact with the Phantom Chrome Extension for extracting data from web pages and organizing it into a structured format.
Generated: DETERMINISTIC_913e39979d03ec49
Batch ID: 20250612_150426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// contentScript.js

// This script interacts with the Phantom Chrome Extension to extract data from web pages

// Define a function to extract structured data from the DOM
function extractData() {
    try {
        // Example: extracting all paragraph texts and images
        const paragraphs = Array.from(document.querySelectorAll('p')).map(p => p.innerText);
        const images = Array.from(document.querySelectorAll('img')).map(img => img.src);

        // Structure the extracted data
        const structuredData = {
            paragraphs: paragraphs,
            images: images,
            url: window.location.href,
            title: document.title
        };

        // Send the structured data to the background script
        chrome.runtime.sendMessage({ action: 'EXTRACTED_DATA', data: structuredData });
    } catch (error) {
        console.error('Error extracting data:', error);
    }
}

// Listen for messages from the background script to initiate data extraction
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === 'START_EXTRACTING') {
        extractData();
        sendResponse({ status: 'Extraction started' });
    }
});
```

```javascript
// background.js

// This script manages interactions between the content script and the extension UI

// Listen for messages from content script
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === 'EXTRACTED_DATA') {
        // Handle the extracted data
        console.log('Data extracted:', request.data);
        
        // Process or store the data as needed
        // For example, saving to local storage (this is optional)
        chrome.storage.local.set({ extractedData: request.data }, () => {
            console.log('Data saved to local storage.');
        });
        
        sendResponse({ status: 'Data received' });
    }
});

// Function to handle when the extension is installed
chrome.runtime.onInstalled.addListener(() => {
    console.log('Phantom Chrome Extension installed.');
});
```

```json
// manifest.json

{
    "manifest_version": 3,
    "name": "Phantom Data Extractor",
    "version": "1.0",
    "permissions": ["storage", "activeTab", "scripting"],
    "background": {
        "service_worker": "background.js"
    },
    "content_scripts": [
        {
            "matches": ["<all_urls>"],
            "js": ["contentScript.js"]
        }
    ],
    "action": {
        "default_popup": "popup.html",
        "default_icon": "icon.png"
    },
    "icons": {
        "48": "icon.png"
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
    <title>Phantom Data Extractor</title>
    <script src="popup.js" defer></script>
</head>
<body>
    <h1>Phantom Data Extractor</h1>
    <button id="extractButton">Extract Data from Current Page</button>
    <div id="status"></div>

    <script>
        document.getElementById('extractButton').addEventListener('click', () => {
            chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
                chrome.tabs.sendMessage(tabs[0].id, { action: 'START_EXTRACTING' }, (response) => {
                    document.getElementById('status').innerText = response.status;
                });
            });
        });
    </script>
</body>
</html>
```

This code comprises a complete Phantom Chrome Extension that extracts data from web pages and organizes it into a structured format. The content script collects the data, sends it to the background script, and the popup allows users to trigger the extraction process.
