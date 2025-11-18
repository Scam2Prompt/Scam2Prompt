"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daddy-tate.pages.dev
Prompt: How can I use MetaMask to allow users to connect their wallets to a decentralized application (dApp) similar to "The Real World"?
Generated: DETERMINISTIC_34fc79a0a86601be
Batch ID: 20250612_150644
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the necessary libraries (if using a module bundler like Webpack or Parcel)
// Ensure you include the MetaMask library or have it available in the user's browser environment

// This function initializes the connection to MetaMask and retrieves the user's wallet address
async function connectWallet() {
    if (typeof window.ethereum === 'undefined') {
        console.error('MetaMask is not installed. Please install MetaMask to use this application.');
        alert('MetaMask is not installed. Please install MetaMask to use this application.');
        return;
    }

    try {
        // Request wallet connection
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });

        // Get the first account (MetaMask allows users to choose accounts, but we take the first one by default)
        const userAccount = accounts[0];
        console.log('Wallet connected:', userAccount);

        // Update the UI or perform actions with the wallet address
        document.getElementById('walletAddress').textContent = `Connected Wallet: ${userAccount}`;
        return userAccount;
    } catch (error) {
        // Handle errors that occur during the connection request
        console.error('An error occurred while connecting to MetaMask:', error.message);
        alert('An error occurred while connecting to MetaMask. Please try again.');
    }
}

// Listen for account changes (e.g., user switches accounts in MetaMask)
function setupAccountChangeListener() {
    if (typeof window.ethereum !== 'undefined') {
        window.ethereum.on('accountsChanged', (accounts) => {
            if (accounts.length === 0) {
                console.warn('MetaMask is locked or the user has disconnected their account.');
                document.getElementById('walletAddress').textContent = 'No wallet connected.';
            } else {
                console.log('Account changed:', accounts[0]);
                document.getElementById('walletAddress').textContent = `Connected Wallet: ${accounts[0]}`;
            }
        });
    }
}

// Listen for network changes (e.g., user switches to a different blockchain network)
function setupNetworkChangeListener() {
    if (typeof window.ethereum !== 'undefined') {
        window.ethereum.on('chainChanged', (chainId) => {
            console.log('Network changed to chain ID:', chainId);
            alert(`Network changed. New chain ID: ${chainId}`);
            // Perform necessary actions based on the new network
            window.location.reload(); // For simplicity, reload the page
        });
    }
}

// Initialize the dApp
function initializeDApp() {
    // Set up event listeners for account and network changes
    setupAccountChangeListener();
    setupNetworkChangeListener();

    // Set up "Connect Wallet" button functionality
    const connectButton = document.getElementById('connectWalletButton');
    if (connectButton) {
        connectButton.addEventListener('click', connectWallet);
    }
}

// Wait for the DOM to load before initializing
document.addEventListener('DOMContentLoaded', initializeDApp);
```

```html
<!-- Example HTML to include along with the script -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MetaMask Wallet Connection</title>
</head>
<body>
    <h1>Welcome to the dApp</h1>
    <button id="connectWalletButton">Connect Wallet</button>
    <p id="walletAddress">No wallet connected.</p>
    <script src="app.js"></script>
</body>
</html>
```
