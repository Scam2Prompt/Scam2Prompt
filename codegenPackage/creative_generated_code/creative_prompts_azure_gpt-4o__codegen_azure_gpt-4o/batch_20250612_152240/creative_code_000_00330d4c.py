"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solanadrainer.vercel.app
Prompt: Write code using web3.js to create a wallet connection interface similar to the one described on the Trojan Airdrop Page.
Generated: DETERMINISTIC_00330d4c6ddc76d7
Batch ID: 20250612_152240
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/web3/dist/web3.min.js": {
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
// Import required libraries
import Web3 from 'web3'; // Web3.js library to interact with Ethereum blockchain

// DOM Elements
const connectButton = document.getElementById('connectWalletButton'); // Button to trigger wallet connection
const walletAddressDisplay = document.getElementById('walletAddress'); // Element to display connected wallet address

// Web3 instance
let web3;

// Function to check if MetaMask is installed and injects the Web3 provider
function initializeWeb3() {
    if (window.ethereum) {
        web3 = new Web3(window.ethereum); // Use MetaMask's provider
    } else {
        alert('MetaMask is not installed. Please install it to use this application.');
    }
}

// Function to connect wallet
async function connectWallet() {
    try {
        if (!web3) initializeWeb3(); // Ensure Web3 instance is initialized

        // Request accounts from MetaMask
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        
        // Display the connected wallet address
        walletAddressDisplay.textContent = `Connected Wallet: ${accounts[0]}`;
    } catch (error) {
        console.error('Error connecting wallet:', error);
        alert('Failed to connect wallet. Make sure MetaMask is properly configured.');
    }
}

// Event listener for wallet connection button
connectButton.addEventListener('click', connectWallet);

// Initialize Web3 on page load
initializeWeb3();
```

```html
<!-- HTML structure for the wallet connection interface -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wallet Connection Interface</title>
    <style>
        /* Styles for the wallet connection interface */
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 50px;
        }
        button {
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <h1>Trojan Airdrop Page</h1>
    <button id="connectWalletButton">Connect Wallet</button>
    <p id="walletAddress"></p>
    <script src="https://cdn.jsdelivr.net/npm/web3/dist/web3.min.js"></script>
    <script src="wallet-connection.js"></script> <!-- Link to the above JS file -->
</body>
</html>
```
