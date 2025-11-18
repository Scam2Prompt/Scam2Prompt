"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://portal-sso-rabby-wallet-auth.bravesites.com
Prompt: Create code for detecting and interacting with DeFi protocols and NFT marketplaces within a browser extension, similar to Rabby Wallet's seamless dApp integration.
Generated: DETERMINISTIC_410e380e79a1f7cc
Batch ID: 20250612_153848
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
  "name": "DeFi & NFT Interaction Extension",
  "version": "1.0",
  "permissions": [
    "activeTab",
    "scripting"
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
  }
}

// background.js
// Background service worker to manage the extension's lifecycle and messaging
chrome.runtime.onInstalled.addListener(() => {
  console.log('DeFi & NFT Interaction Extension installed.');
});

// content.js
// Content script for detecting dApps and interacting with them
const dAppPatterns = [
  /uniswap/i, 
  /sushi/i, 
  /opensea/i,
  /rarible/i
];

// Function to detect if the current site is a dApp or NFT marketplace
function detectDApp() {
  const url = window.location.href;
  const matchedDApp = dAppPatterns.find(pattern => pattern.test(url));

  if (matchedDApp) {
    console.log(`Detected dApp: ${matchedDApp}`);
    // Inject UI or functionality here
    injectDAppUI(matchedDApp);
  }
}

// Function to inject UI elements into the dApp
function injectDAppUI(dAppName) {
  const button = document.createElement('button');
  button.innerText = `Interact with ${dAppName}`;
  button.style.position = 'fixed';
  button.style.bottom = '20px';
  button.style.right = '20px';
  button.style.zIndex = '9999';

  button.addEventListener('click', () => {
    handleInteraction(dAppName);
  });

  document.body.appendChild(button);
}

// Function to handle interaction with the dApp
async function handleInteraction(dAppName) {
  try {
    // Here you can include specific logic for each dApp
    if (dAppName.includes("uniswap")) {
      // Example: Interact with Uniswap
      console.log("Interacting with Uniswap...");
      // Add your Uniswap interaction logic here
    } else if (dAppName.includes("opensea")) {
      // Example: Interact with OpenSea
      console.log("Interacting with OpenSea...");
      // Add your OpenSea interaction logic here
    }
  } catch (error) {
    console.error(`Error interacting with ${dAppName}:`, error);
    alert('An error occurred while interacting with the dApp.');
  }
}

// Start detecting dApps on page load
window.onload = detectDApp;

// popup.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DeFi & NFT Extension</title>
    <style>
        body { font-family: Arial, sans-serif; }
        #status { margin: 20px; }
    </style>
</head>
<body>
    <h1>DeFi & NFT Extension</h1>
    <div id="status">Ready to interact!</div>
    <script src="popup.js"></script>
</body>
</html>

// popup.js
// Script for handling popup interactions
document.addEventListener('DOMContentLoaded', () => {
    const status = document.getElementById('status');
    status.innerText = 'Extension is ready. Click on a dApp to interact!';
});
```

Note: This code represents a basic structure and setup for the browser extension. Actual interaction logic with smart contracts and NFTs, as well as proper web3 provider integration (like MetaMask), would need to be added based on the specific APIs and SDKs for the corresponding DeFi protocols and NFT marketplaces. Be sure to follow security best practices when handling user data and ensuring secure interactions with smart contracts.
