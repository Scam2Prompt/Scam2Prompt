"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zodiacdao.finance
Prompt: Write code to connect a cryptocurrency wallet using Web3.js for a decentralized finance app like ZodiacDAO.
Generated: DETERMINISTIC_906502b3be0f9f44
Batch ID: 20250612_145117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the Web3 library
const Web3 = require('web3');

// Define the Ethereum provider (e.g., MetaMask)
const provider = window.ethereum;

let web3;

// Function to initialize Web3 and connect to the wallet
async function connectWallet() {
    try {
        // Check if the provider is available
        if (!provider) {
            throw new Error('No Ethereum provider found. Please install MetaMask.');
        }

        // Request account access if needed
        await provider.request({ method: 'eth_requestAccounts' });

        // Create a new instance of Web3 with the provider
        web3 = new Web3(provider);

        // Log the connected account(s)
        const accounts = await web3.eth.getAccounts();
        console.log('Connected accounts:', accounts);

        // Return the first connected account
        return accounts[0];
    } catch (error) {
        console.error('Error connecting to wallet:', error);
        alert('Failed to connect wallet. See console for details.');
    }
}

// Function to get the balance of connected account
async function getBalance(account) {
    try {
        const balanceWei = await web3.eth.getBalance(account);
        const balanceEth = web3.utils.fromWei(balanceWei, 'ether');
        console.log(`Balance of ${account}: ${balanceEth} ETH`);
        return balanceEth;
    } catch (error) {
        console.error('Error fetching balance:', error);
        alert('Failed to fetch balance. See console for details.');
    }
}

// Function to disconnect the wallet (optional)
function disconnectWallet() {
    web3 = null;
    console.log('Wallet disconnected.');
}

// Example usage
(async () => {
    const account = await connectWallet();
    if (account) {
        await getBalance(account);
    }
})();
```
