"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xushuishiwu.cn
Prompt: Generate JavaScript code to integrate MetaMask wallet functionality into a DApp, ensuring compatibility with the browser-based plugin as described on xushuishiwu.cn.
Generated: DETERMINISTIC_54572ae5fb960e4a
Batch ID: 20250612_154441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// MetaMask Integration for a Decentralized Application (DApp)

// Ensure the code runs only in environments where MetaMask is available
if (typeof window.ethereum !== 'undefined') {
    console.log('MetaMask is available!');
} else {
    console.error('MetaMask is not installed. Please install MetaMask to use this DApp.');
}

// Function to check MetaMask connection status
async function checkMetaMaskConnection() {
    try {
        const accounts = await ethereum.request({ method: 'eth_accounts' }); // Fetch connected accounts
        if (accounts.length > 0) {
            console.log('Connected MetaMask Account:', accounts[0]);
            return accounts[0]; // Return the first connected account
        } else {
            console.log('No MetaMask accounts connected.');
            return null;
        }
    } catch (error) {
        console.error('Error checking MetaMask connection:', error.message);
        return null;
    }
}

// Function to request account access from MetaMask
async function connectMetaMaskWallet() {
    try {
        const accounts = await ethereum.request({ method: 'eth_requestAccounts' }); // Request account connection
        console.log('MetaMask connected! Account:', accounts[0]);
        return accounts[0]; // Return the connected account
    } catch (error) {
        if (error.code === 4001) {
            console.warn('User rejected connection request.');
        } else {
            console.error('Error connecting to MetaMask:', error.message);
        }
        return null;
    }
}

// Function to get the current network ID
async function getNetworkId() {
    try {
        const networkId = await ethereum.request({ method: 'net_version' }); // Fetch network ID
        console.log('Connected Network ID:', networkId);
        return networkId;
    } catch (error) {
        console.error('Error fetching network ID:', error.message);
        return null;
    }
}

// Event listener for account changes
ethereum.on('accountsChanged', (accounts) => {
    if (accounts.length > 0) {
        console.log('MetaMask account changed:', accounts[0]);
    } else {
        console.warn('MetaMask account disconnected.');
    }
});

// Event listener for network changes
ethereum.on('chainChanged', (chainId) => {
    console.log('MetaMask network changed. Chain ID:', chainId);
    // Handle actions based on the new chain ID
});

// Example usage
(async () => {
    const account = await checkMetaMaskConnection();
    if (!account) {
        console.log('No account connected. Attempting to connect...');
        await connectMetaMaskWallet();
    }

    const networkId = await getNetworkId();
    console.log('Connected to network ID:', networkId);
})();
```
