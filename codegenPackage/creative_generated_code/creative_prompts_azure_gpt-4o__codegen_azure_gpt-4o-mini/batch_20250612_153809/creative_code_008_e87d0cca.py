"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chainabusescan.com
Prompt: Develop a browser extension that uses ChainAbuse's API to notify users of potentially risky token approvals when interacting with dApps.
Generated: DETERMINISTIC_e87d0cca1fb9d0b6
Batch ID: 20250612_153809
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.chainabuse.com/v1/check": {
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
  "name": "Token Approval Notifier",
  "version": "1.0",
  "description": "Notify users of potentially risky token approvals when interacting with dApps.",
  "permissions": ["storage", "notifications", "activeTab"],
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
      "16": "icon16.png",
      "48": "icon48.png",
      "128": "icon128.png"
    }
  },
  "icons": {
    "16": "icon16.png",
    "48": "icon48.png",
    "128": "icon128.png"
  }
}

// background.js
const API_URL = "https://api.chainabuse.com/v1/check"; // ChainAbuse API endpoint

// Listen for messages from content scripts
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === "checkApproval") {
    checkTokenApproval(request.tokenAddress, sendResponse);
    return true; // Keep the message channel open for async response
  }
});

// Function to check the token approval using ChainAbuse's API
async function checkTokenApproval(tokenAddress, sendResponse) {
  try {
    const response = await fetch(`${API_URL}?token=${tokenAddress}`);
    if (!response.ok) throw new Error(`Error fetching data: ${response.statusText}`);

    const data = await response.json();
    if (data.isRisky) {
      sendNotification(tokenAddress, data);
    } else {
      console.log(`Token ${tokenAddress} is safe.`);
    }
    sendResponse({ status: "completed" });
  } catch (error) {
    console.error("Error during token approval check:", error);
    sendResponse({ status: "error", message: error.message });
  }
}

// Function to send a notification to the user
function sendNotification(tokenAddress, data) {
  chrome.notifications.create({
    type: "basic",
    iconUrl: "icon48.png",
    title: "Risky Token Approval Detected!",
    message: `The token ${tokenAddress} may be risky. Check ChainAbuse for more details.`,
    priority: 2
  });
}

// content.js
// Listen for user interactions with token approvals on dApps and send messages to the background script
document.addEventListener("click", async (event) => {
  const tokenApprovalElement = event.target.closest(".token-approval"); // Adjust selector as necessary
  if (tokenApprovalElement) {
    const tokenAddress = tokenApprovalElement.dataset.tokenAddress; // Assume the token address is stored in a data attribute
    if (tokenAddress) {
      chrome.runtime.sendMessage({ action: "checkApproval", tokenAddress });
    }
  }
});

// popup.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Token Approval Notifier</title>
    <style>
        body { font-family: Arial, sans-serif; }
        h1 { font-size: 24px; }
        p { font-size: 14px; }
    </style>
</head>
<body>
    <h1>Token Approval Notifier</h1>
    <p>This extension will notify you of potentially risky token approvals.</p>
</body>
</html>
```
