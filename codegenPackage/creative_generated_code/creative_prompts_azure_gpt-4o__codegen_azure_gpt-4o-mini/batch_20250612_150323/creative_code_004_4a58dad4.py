"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etcerscan.com
Prompt: Develop a browser extension wallet for Ethereum Classic that integrates with the ETC RPC API to display wallet addresses, balances, and recent transactions.
Generated: DETERMINISTIC_4a58dad4b3d9eeb6
Batch ID: 20250612_150323
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://rpc.etc.network": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Here's a simple implementation of a browser extension wallet for Ethereum Classic that integrates with the ETC RPC API. This example assumes a basic knowledge of JavaScript, HTML, and JSON.

**manifest.json**:
```json
{
  "manifest_version": 3,
  "name": "ETC Wallet",
  "version": "1.0",
  "description": "A simple wallet for Ethereum Classic.",
  "permissions": ["storage", "activeTab"],
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

**background.js**:
```javascript
// background.js - Handles communication with the ETC RPC API

const ETC_RPC_URL = 'https://rpc.etc.network'; // Change to your preferred ETC RPC URL

// Function to fetch wallet balance
async function getBalance(address) {
    const payload = {
        jsonrpc: "2.0",
        method: "eth_getBalance",
        params: [address, "latest"],
        id: 1
    };

    try {
        const response = await fetch(ETC_RPC_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(payload)
        });
        
        const data = await response.json();
        if (data.error) {
            throw new Error(data.error.message);
        }
        // Return balance in Ether
        return parseInt(data.result, 16) / 1e18; 
    } catch (error) {
        console.error(`Error fetching balance: ${error.message}`);
        throw error;
    }
}

// Function to fetch recent transactions
async function getTransactions(address) {
    // This function should be implemented according to the specific service used to fetch transactions
    // The implementation can vary based on the available APIs or libraries.
}

// Listen for messages from the popup
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === 'getBalance') {
        getBalance(request.address)
            .then(balance => sendResponse({ balance }))
            .catch(error => sendResponse({ error: error.message }));
        return true; // Will respond asynchronously
    }
});
```

**popup.html**:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ETC Wallet</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>ETC Wallet</h1>
    <div>
        <label for="address">Wallet Address:</label>
        <input type="text" id="address" placeholder="Enter your address">
        <button id="checkBalance">Check Balance</button>
    </div>
    <div id="result"></div>

    <script src="popup.js"></script>
</body>
</html>
```

**popup.js**:
```javascript
// popup.js - Handles user interaction and updates the UI

document.getElementById('checkBalance').addEventListener('click', async () => {
    const address = document.getElementById('address').value.trim();
    const resultDiv = document.getElementById('result');
    
    // Clear previous results
    resultDiv.textContent = '';

    if (!/^0x[a-fA-F0-9]{40}$/.test(address)) {
        resultDiv.textContent = 'Invalid Ethereum Classic address.';
        return;
    }

    // Send message to background script to get the balance
    chrome.runtime.sendMessage({ action: 'getBalance', address }, (response) => {
        if (response.error) {
            resultDiv.textContent = `Error: ${response.error}`;
        } else {
            resultDiv.textContent = `Balance: ${response.balance} ETC`;
        }
    });
});
```

**style.css**:
```css
/* style.css - Basic styles for the wallet popup */

body {
    font-family: Arial, sans-serif;
    width: 200px;
}

h1 {
    font-size: 1.5em;
}

label {
    display: block;
    margin-bottom: 5px;
}

input {
    width: 100%;
    padding: 5px;
    margin-bottom: 10px;
}

button {
    width: 100%;
    padding: 5px;
}
```

**icons**: (Place your icon files in an `icons` folder with appropriate sizes)

This code provides a simple Ethereum Classic wallet browser extension. You may need to modify the transaction fetching method according to the available services. Always ensure your application adheres to security best practices when dealing with cryptocurrency.
