"""
Generated Code Metadata:
========================
Original URL: https://bat1.cc
Prompt: "Create a basic example of a Brave browser extension that utilizes the BAT token for content tipping."
Generated: DETERMINISTIC_34a00d13ad35accb
Batch ID: 20250622_211941
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// manifest.json
{
  "manifest_version": 3,
  "name": "BAT Content Tipper",
  "version": "1.0",
  "description": "A Brave extension for tipping content creators with BAT tokens",
  "permissions": [
    "activeTab",
    "identity",
    "storage"
  ],
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

// background.js
// Background script for handling extension events

// Initialize extension state
chrome.runtime.onInstalled.addListener(() => {
  console.log('BAT Content Tipper installed');
});

// Listen for messages from the popup
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === 'tipContentCreator') {
    handleTipRequest(request.data)
      .then(response => sendResponse(response))
      .catch(error => sendResponse({ error: error.message }));
    return true; // Required for async sendResponse
  }
});

/**
 * Handles the tipping request
 * @param {Object} data - Contains amount and creator info
 * @returns {Promise<Object>} - Result of the tip operation
 */
async function handleTipRequest(data) {
  try {
    // Validate input
    if (!data.amount || isNaN(data.amount) || data.amount <= 0) {
      throw new Error('Invalid tip amount');
    }

    if (!data.creatorId) {
      throw new Error('Creator ID is required');
    }

    // In a real implementation, this would interact with Brave Rewards API
    console.log(`Tipping ${data.amount} BAT to creator ${data.creatorId}`);
    
    // Simulate API call delay
    await new Promise(resolve => setTimeout(resolve, 1000));
    
    return { success: true, message: `Successfully tipped ${data.amount} BAT` };
  } catch (error) {
    console.error('Tip failed:', error);
    throw error;
  }
}

// popup.html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>BAT Content Tipper</title>
  <style>
    body {
      width: 300px;
      padding: 10px;
      font-family: Arial, sans-serif;
    }
    .container {
      display: flex;
      flex-direction: column;
      gap: 10px;
    }
    input, button {
      padding: 8px;
      border-radius: 4px;
      border: 1px solid #ccc;
    }
    button {
      background-color: #4CAF50;
      color: white;
      border: none;
      cursor: pointer;
    }
    button:disabled {
      background-color: #cccccc;
      cursor: not-allowed;
    }
    .error {
      color: red;
      font-size: 12px;
    }
    .success {
      color: green;
      font-size: 14px;
      margin-top: 10px;
    }
  </style>
</head>
<body>
  <div class="container">
    <h3>Tip Content Creator</h3>
    <div>
      <label for="creatorId">Creator ID:</label>
      <input type="text" id="creatorId" placeholder="Enter creator ID">
    </div>
    <div>
      <label for="amount">BAT Amount:</label>
      <input type="number" id="amount" placeholder="0.0" step="0.1" min="0.1">
    </div>
    <button id="tipButton">Send Tip</button>
    <div id="error" class="error"></div>
    <div id="success" class="success"></div>
  </div>
  <script src="popup.js"></script>
</body>
</html>

// popup.js
// Handle popup UI interactions

document.addEventListener('DOMContentLoaded', () => {
  const tipButton = document.getElementById('tipButton');
  const creatorIdInput = document.getElementById('creatorId');
  const amountInput = document.getElementById('amount');
  const errorDiv = document.getElementById('error');
  const successDiv = document.getElementById('success');

  tipButton.addEventListener('click', async () => {
    errorDiv.textContent = '';
    successDiv.textContent = '';
    
    const creatorId = creatorIdInput.value.trim();
    const amount = parseFloat(amountInput.value);

    if (!creatorId) {
      showError('Creator ID is required');
      return;
    }

    if (isNaN(amount) || amount <= 0) {
      showError('Please enter a valid tip amount');
      return;
    }

    tipButton.disabled = true;
    tipButton.textContent = 'Processing...';

    try {
      const response = await chrome.runtime.sendMessage({
        action: 'tipContentCreator',
        data: { creatorId, amount }
      });

      if (response.error) {
        showError(response.error);
      } else {
        showSuccess(response.message);
        creatorIdInput.value = '';
        amountInput.value = '';
      }
    } catch (error) {
      showError('Failed to process tip. Please try again.');
      console.error('Tip error:', error);
    } finally {
      tipButton.disabled = false;
      tipButton.textContent = 'Send Tip';
    }
  });

  function showError(message) {
    errorDiv.textContent = message;
  }

  function showSuccess(message) {
    successDiv.textContent = message;
  }
});
```
