"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3portal.com
Prompt: Write a script that demonstrates how to integrate a Web3-based decentralized service into a browser extension, specifically referencing the principles of freedom, privacy, and ownership described on Lume Web.
Generated: DETERMINISTIC_455f1b8186d2bcd0
Batch ID: 20250612_154703
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.lumeweb.com/data`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.lumeweb.com/data": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// manifest.json
{
  "manifest_version": 3,
  "name": "Lume Web Integration",
  "version": "1.0",
  "permissions": [
    "storage",
    "activeTab",
    "scripting"
  ],
  "background": {
    "service_worker": "background.js"
  },
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

// background.js
// Background script for handling events and communications
chrome.runtime.onInstalled.addListener(() => {
  console.log("Extension Installed. Ready to integrate with Lume Web.");
});

// Function to fetch data from a decentralized service
async function fetchDataFromDecentralizedService() {
  try {
    const response = await fetch('https://api.lumeweb.com/data');
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Failed to fetch data from decentralized service:", error);
    throw error; // Rethrow error for further handling
  }
}

// popup.js
// Script for handling popup interactions
document.getElementById('fetch-data').addEventListener('click', async () => {
  try {
    const data = await fetchDataFromDecentralizedService();
    document.getElementById('output').innerText = JSON.stringify(data, null, 2);
  } catch (error) {
    document.getElementById('output').innerText = "Error fetching data.";
  }
});

// popup.html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Lume Web Integration</title>
  <script src="popup.js" defer></script>
  <style>
    body { font-family: Arial, sans-serif; }
    #output { white-space: pre-wrap; }
  </style>
</head>
<body>
  <h1>Lume Web Data Fetcher</h1>
  <button id="fetch-data">Fetch Data</button>
  <h2>Output:</h2>
  <pre id="output"></pre>
</body>
</html>
```

### Note:
- Ensure you have an appropriate icon in the `images` directory as referenced in `manifest.json`.
- Update the API endpoint `https://api.lumeweb.com/data` with the correct URL for Lume Web's decentralized service.
- The code adheres to best practices such as error handling, modular design, and clear documentation through comments.
