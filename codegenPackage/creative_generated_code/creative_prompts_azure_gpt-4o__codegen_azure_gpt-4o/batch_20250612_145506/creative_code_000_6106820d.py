"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask.ro
Prompt: Write JavaScript code to integrate MetaMask into a web application for connecting to blockchain-based applications using the MetaMask browser extension.
Generated: DETERMINISTIC_6106820d715a5f54
Batch ID: 20250612_145506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// JavaScript code to integrate MetaMask into a web application

// Ensure the DOM is fully loaded
document.addEventListener('DOMContentLoaded', () => {
    // Attach event listener to 'Connect to MetaMask' button
    const connectButton = document.getElementById('connectButton');
    connectButton.addEventListener('click', connectToMetaMask);

    // Attach event listener to 'Get Account' button (optional)
    const getAccountButton = document.getElementById('getAccountButton');
    getAccountButton.addEventListener('click', getConnectedAccount);
});

// Function to check if MetaMask is installed
function isMetaMaskInstalled() {
    return typeof window.ethereum !== 'undefined' && window.ethereum.isMetaMask;
}

// Function to connect to MetaMask
async function connectToMetaMask() {
    try {
        if (!isMetaMaskInstalled()) {
            alert('MetaMask is not installed. Please install MetaMask and try again.');
            return;
        }

        // Request account access
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });

        // Log and display connected account
        console.log('Connected account:', accounts[0]);
        document.getElementById('status').textContent = `Connected with: ${accounts[0]}`;
    } catch (error) {
        // Handle errors (e.g., user denies access)
        console.error('Error connecting to MetaMask:', error.message);
        alert('Failed to connect to MetaMask. Please try again.');
    }
}

// Function to get the currently connected account
async function getConnectedAccount() {
    try {
        if (!isMetaMaskInstalled()) {
            alert('MetaMask is not installed. Please install MetaMask and try again.');
            return;
        }

        // Get accounts currently connected to MetaMask
        const accounts = await window.ethereum.request({ method: 'eth_accounts' });

        if (accounts.length === 0) {
            alert('No accounts found. Please connect to MetaMask.');
        } else {
            // Log and display the connected account
            console.log('Currently connected account:', accounts[0]);
            document.getElementById('status').textContent = `Connected with: ${accounts[0]}`;
        }
    } catch (error) {
        // Handle errors
        console.error('Error retrieving connected account:', error.message);
        alert('Failed to retrieve connected accounts. Please try again.');
    }
}

// Listen for account changes and network changes
if (isMetaMaskInstalled()) {
    window.ethereum.on('accountsChanged', (accounts) => {
        // Update the UI or notify the user of the account change
        console.log('Accounts changed:', accounts);
        if (accounts.length > 0) {
            document.getElementById('status').textContent = `Connected with: ${accounts[0]}`;
        } else {
            document.getElementById('status').textContent = 'Disconnected';
        }
    });

    window.ethereum.on('chainChanged', (chainId) => {
        // Handle the network change
        console.log('Network changed to chain ID:', chainId);
        alert(`Network changed to chain ID: ${chainId}`);
        // Reload the page (optional, depends on your app's needs)
        window.location.reload();
    });
}
```

```html
<!-- Simple HTML structure to test the integration -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MetaMask Integration</title>
</head>
<body>
    <h1>MetaMask Integration Example</h1>
    <button id="connectButton">Connect to MetaMask</button>
    <button id="getAccountButton">Get Connected Account</button>
    <p id="status">Not connected</p>
    <script src="metamask-integration.js"></script>
</body>
</html>
```
