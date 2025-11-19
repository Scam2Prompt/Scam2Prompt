"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaskchome.creatorlink.net
Prompt: What steps should I take to connect my MetaMask wallet to a DApp for the first time?
Generated: DETERMINISTIC_cba5b31e9c5fb5b1
Batch ID: 20250612_135105
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Connect MetaMask Wallet to a DApp.
 * This script initializes the connection and retrieves the user's account address.
 * Ensure the DApp is hosted on HTTPS and MetaMask is installed in the browser.
 */

// Check if MetaMask is installed
if (typeof window.ethereum !== 'undefined') {
    console.log('MetaMask is installed!');
} else {
    console.error('MetaMask is not installed. Please install it to continue.');
    alert('MetaMask is not installed. Please install it to connect your wallet.');
}

// Function to connect MetaMask wallet
async function connectMetaMask() {
    try {
        // Request account access
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        
        // Display the connected account address
        const account = accounts[0];
        console.log('Connected account:', account);
        alert(`Wallet connected successfully! Address: ${account}`);

        // Additional code for handling connected account can be added here
        // For example: Save the address in a variable, or interact with smart contracts
    } catch (error) {
        // Handle errors gracefully
        console.error('Error connecting MetaMask wallet:', error);

        if (error.code === 4001) {
            // User rejected the connection request
            alert('Connection request denied by the user.');
        } else {
            alert('An error occurred while connecting to MetaMask. Please try again.');
        }
    }
}

// Function to detect MetaMask account changes
function listenForAccountChanges() {
    window.ethereum.on('accountsChanged', (accounts) => {
        // Handle account change
        if (accounts.length === 0) {
            console.log('MetaMask disconnected.');
            alert('MetaMask wallet has been disconnected.');
        } else {
            console.log('Account changed:', accounts[0]);
            alert(`Account changed to: ${accounts[0]}`);
        }
    });
}

// Example usage: Connect wallet and set up listener for account changes
document.getElementById('connect-wallet-button').addEventListener('click', () => {
    connectMetaMask();
    listenForAccountChanges();
});
```

### HTML Example for the Button
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Connect MetaMask</title>
</head>
<body>
    <button id="connect-wallet-button">Connect Wallet</button>
    <script src="script.js"></script>
</body>
</html>
```

This code connects a MetaMask wallet to a DApp and listens for account changes. To use, save the JavaScript code in a file (`script.js`) and the HTML code above in an `index.html` file in the same directory.
