"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mixswap.finance
Prompt: Write code to integrate a cryptocurrency wallet connection feature using Web3.js, similar to the functionality described on MixSwap Finance.
Generated: DETERMINISTIC_4b738cbdb310e55f
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the Web3 library
import Web3 from 'web3';

// Check if the browser has a Web3 provider (like MetaMask)
const hasWeb3 = () => typeof window.ethereum !== 'undefined';

// Initialize Web3 instance
let web3;

// Function to connect to the user's wallet
async function connectWallet() {
    if (!hasWeb3()) {
        alert('Please install a Web3 wallet like MetaMask to use this feature.');
        return;
    }

    try {
        // Request account access
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        
        // Initialize Web3 with the provider
        web3 = new Web3(window.ethereum);

        // Display connected account
        console.log('Connected account:', accounts[0]);
        return accounts[0];
    } catch (error) {
        console.error('Error connecting to wallet:', error);
        alert('Failed to connect to wallet. Please try again.');
    }
}

// Function to get the connected account's balance
async function getBalance(account) {
    try {
        const balance = await web3.eth.getBalance(account);
        // Convert balance from Wei to Ether
        const balanceInEther = web3.utils.fromWei(balance, 'ether');
        console.log(`Balance of ${account}: ${balanceInEther} ETH`);
        return balanceInEther;
    } catch (error) {
        console.error('Error fetching balance:', error);
        alert('Failed to fetch balance. Please try again.');
    }
}

// Function to disconnect the wallet (optional)
function disconnectWallet() {
    web3 = null;
    console.log('Wallet disconnected.');
}

// Event listener for wallet connection button
document.getElementById('connect-button').addEventListener('click', async () => {
    const account = await connectWallet();
    if (account) {
        await getBalance(account);
    }
});

// Optional: Listen for account changes (e.g., user switching accounts in MetaMask)
window.ethereum.on('accountsChanged', (accounts) => {
    if (accounts.length === 0) {
        disconnectWallet();
        alert('Please connect to a wallet.');
    } else {
        console.log('Account changed to:', accounts[0]);
        getBalance(accounts[0]);
    }
});

// Optional: Listen for network changes
window.ethereum.on('chainChanged', (chainId) => {
    console.log('Network changed to:', chainId);
    // Handle network change logic here (e.g., update UI or reconnect)
});

// Export functions for use in other modules
export { connectWallet, getBalance, disconnectWallet };
```

```html
<!-- HTML structure for the wallet connection button -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Crypto Wallet Connection</title>
</head>
<body>
    <button id="connect-button">Connect Wallet</button>
    <script type="module" src="path/to/your/javascript/file.js"></script>
</body>
</html>
```

Ensure you include the Web3.js library in your project by installing it via npm or adding it via a CDN in your HTML file.
