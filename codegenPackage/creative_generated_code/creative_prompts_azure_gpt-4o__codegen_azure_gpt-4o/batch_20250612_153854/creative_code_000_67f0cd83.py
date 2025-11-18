"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mestken.top
Prompt: Write a JavaScript script that integrates the MetaMask browser extension to connect to a blockchain application and fetch the user's wallet address.
Generated: DETERMINISTIC_67f0cd83f9a99563
Batch ID: 20250612_153854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// MetaMask Integration Script: Connect to a blockchain application and fetch the user's wallet address

// Ensure the code runs only after the DOM is fully loaded
document.addEventListener('DOMContentLoaded', () => {
    // UI Elements
    const connectButton = document.getElementById('connectWallet');
    const walletAddressDisplay = document.getElementById('walletAddress');

    // Check if MetaMask is installed
    function isMetaMaskInstalled() {
        return typeof window.ethereum !== 'undefined' && window.ethereum.isMetaMask;
    }

    // Connect to MetaMask and fetch the wallet address
    async function connectWallet() {
        try {
            // Check if MetaMask is installed
            if (!isMetaMaskInstalled()) {
                alert('MetaMask is not installed. Please install MetaMask to connect.');
                return;
            }

            // Request account access from MetaMask
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });

            // Handle case where no accounts are returned
            if (accounts.length === 0) {
                alert('No wallet address found. Please ensure your MetaMask is set up correctly.');
                return;
            }

            // Display the connected wallet address
            const walletAddress = accounts[0];
            walletAddressDisplay.textContent = `Connected Wallet Address: ${walletAddress}`;
        } catch (error) {
            // Handle errors during the connection process
            console.error('Error connecting to MetaMask:', error);
            alert('An error occurred while connecting to MetaMask. Please try again.');
        }
    }

    // Add click event listener to the "Connect Wallet" button
    connectButton.addEventListener('click', connectWallet);
});
```

### Example HTML for UI elements:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MetaMask Integration</title>
</head>
<body>
    <button id="connectWallet">Connect Wallet</button>
    <p id="walletAddress">Wallet Address will appear here after connection.</p>
    <script src="script.js"></script>
</body>
</html>
```
