"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepeunchained-as.web.app
Prompt: Write a tutorial on creating a browser extension for Pepe Unchained that interacts with MetaMask to facilitate $PEPU token staking and purchasing.
Generated: DETERMINISTIC_866d6f32efacaa4e
Batch ID: 20250612_152727
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// content.js

// This script will be injected into the web pages the user visits.
// It listens for messages from the popup to interact with the MetaMask wallet.

const pepeContractAddress = '0xYourPepeContractAddressHere'; // Replace with your contract address
const pepeTokenABI = [ /* Your ABI here */ ];  // Replace with your ABI

// Function to initialize web3 and connect to MetaMask
async function initWeb3() {
    if (typeof window.ethereum !== 'undefined') {
        try {
            // Request account access
            await window.ethereum.request({ method: 'eth_requestAccounts' });
            const web3 = new Web3(window.ethereum);
            return web3;
        } catch (error) {
            console.error('User denied account access:', error);
        }
    } else {
        console.error('MetaMask is not installed');
    }
}

// Function to stake $PEPU tokens
async function stakeTokens(amount) {
    const web3 = await initWeb3();
    if (!web3) return;

    const accounts = await web3.eth.getAccounts();
    const contract = new web3.eth.Contract(pepeTokenABI, pepeContractAddress);

    try {
        // Call the stake function in your smart contract
        await contract.methods.stake(web3.utils.toWei(amount, 'ether')).send({ from: accounts[0] });
        console.log(`Successfully staked ${amount} $PEPU tokens`);
    } catch (error) {
        console.error('Error staking tokens:', error);
    }
}

// Function to purchase $PEPU tokens
async function purchaseTokens(amount) {
    const web3 = await initWeb3();
    if (!web3) return;

    const accounts = await web3.eth.getAccounts();
    const contract = new web3.eth.Contract(pepeTokenABI, pepeContractAddress);

    try {
        // Call the purchase function in your smart contract
        await contract.methods.purchase(web3.utils.toWei(amount, 'ether')).send({ from: accounts[0] });
        console.log(`Successfully purchased ${amount} $PEPU tokens`);
    } catch (error) {
        console.error('Error purchasing tokens:', error);
    }
}

// Listen for messages from the popup
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === 'stake') {
        stakeTokens(request.amount);
    } else if (request.action === 'purchase') {
        purchaseTokens(request.amount);
    }
});
```

```javascript
// popup.js

// This script runs in the popup window of the browser extension.
// It handles user interactions and sends requests to the content script.

document.getElementById('stake-button').addEventListener('click', async () => {
    const amount = document.getElementById('stake-amount').value;
    
    // Send message to content script to stake tokens
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
        chrome.tabs.sendMessage(tabs[0].id, { action: 'stake', amount: amount });
    });
});

document.getElementById('purchase-button').addEventListener('click', async () => {
    const amount = document.getElementById('purchase-amount').value;
    
    // Send message to content script to purchase tokens
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
        chrome.tabs.sendMessage(tabs[0].id, { action: 'purchase', amount: amount });
    });
});
```

```html
<!-- popup.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pepe Unchained</title>
    <script src="popup.js" defer></script>
</head>
<body>
    <h1>Pepe Unchained</h1>
    
    <div>
        <h2>Stake $PEPU</h2>
        <input type="text" id="stake-amount" placeholder="Amount" />
        <button id="stake-button">Stake Tokens</button>
    </div>
    
    <div>
        <h2>Purchase $PEPU</h2>
        <input type="text" id="purchase-amount" placeholder="Amount" />
        <button id="purchase-button">Purchase Tokens</button>
    </div>
</body>
</html>
```

```json
// manifest.json

{
    "manifest_version": 3,
    "name": "Pepe Unchained",
    "version": "1.0",
    "description": "A browser extension for staking and purchasing $PEPU tokens.",
    "permissions": [
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
    "content_scripts": [
        {
            "matches": ["<all_urls>"],
            "js": ["content.js"]
        }
    ],
    "icons": {
        "16": "images/icon16.png",
        "48": "images/icon48.png",
        "128": "images/icon128.png"
    }
}
```

This code represents a simple browser extension for interacting with a smart contract to stake and purchase $PEPU tokens via MetaMask. Make sure to replace placeholders such as contract address and ABI with actual values.
