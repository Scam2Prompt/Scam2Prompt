"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hhhhhhhh-2a7.pages.dev
Prompt: Generate code for a browser extension that allows users to connect their Coinbase Wallet to dApps with one click, as mentioned on the site.
Generated: DETERMINISTIC_956d131e59a9e605
Batch ID: 20250612_153401
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
  "name": "Coinbase Wallet Connector",
  "version": "1.0",
  "description": "Connect your Coinbase Wallet to dApps with one click.",
  "permissions": ["activeTab"],
  "action": {
    "default_popup": "popup.html",
    "default_icon": "icon.png"
  },
  "background": {
    "service_worker": "background.js"
  },
  "content_scripts": [
    {
      "matches": ["<all_urls>"],
      "js": ["content.js"]
    }
  ],
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
    <title>Connect Coinbase Wallet</title>
    <style>
        body { font-family: Arial, sans-serif; padding: 10px; }
        button { background-color: #0052ff; color: white; border: none; padding: 10px; cursor: pointer; }
        button:hover { background-color: #0041cc; }
    </style>
</head>
<body>
    <h1>Connect to dApp</h1>
    <button id="connect-button">Connect Coinbase Wallet</button>
    <div id="status"></div>
    <script src="popup.js"></script>
</body>
</html>
```

```javascript
// popup.js
document.getElementById('connect-button').addEventListener('click', async () => {
    try {
        // Request connection to Coinbase Wallet
        const { ethereum } = window;
        if (!ethereum) {
            document.getElementById('status').innerText = "Coinbase Wallet not detected!";
            return;
        }
        
        // Request account access
        const accounts = await ethereum.request({ method: 'eth_requestAccounts' });
        document.getElementById('status').innerText = `Connected: ${accounts[0]}`;
        
        // Dispatch event to notify content script
        chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
            chrome.tabs.sendMessage(tabs[0].id, { action: "connect", account: accounts[0] });
        });
    } catch (error) {
        console.error(error);
        document.getElementById('status').innerText = "Error connecting to Coinbase Wallet.";
    }
});
```

```javascript
// content.js
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === "connect") {
        console.log(`User connected with account: ${request.account}`);
        // Implement logic to interact with the dApp using the connected account
    }
});
```

```javascript
// background.js
// Background service worker for managing events and actions
chrome.runtime.onInstalled.addListener(() => {
    console.log("Coinbase Wallet Connector extension installed.");
});
```

```plaintext
// icon.png
// (Placeholder for the extension icon image file. Make sure to include a 48x48 pixel icon in the directory.)
```

This code provides a complete structure for a simple browser extension that allows users to connect their Coinbase Wallet to decentralized applications (dApps) with a single click. Ensure that you have the appropriate icon file (`icon.png`) included in the project directory for the extension to function correctly.
