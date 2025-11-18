"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://help-metmschrxtnsg.gitbook.io
Prompt: Provide code to enable seamless integration of MetaMask with a browser-based blockchain game, ensuring secure asset management and transactions.
Generated: DETERMINISTIC_d426475ae205cb10
Batch ID: 20250612_153925
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import Web3 from 'web3';

// Define the game contract's address and ABI (Application Binary Interface)
const contractAddress = 'YOUR_CONTRACT_ADDRESS_HERE';
const contractABI = [
    // Replace with your contract's ABI
];

// Create a Web3 instance
let web3;

async function initializeWeb3() {
    // Check if MetaMask is installed
    if (window.ethereum) {
        // Request account access if needed
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        // Initialize Web3
        web3 = new Web3(window.ethereum);
    } else {
        alert('MetaMask is not installed. Please install MetaMask to play the game.');
        throw new Error('MetaMask not found');
    }
}

// Create an instance of the contract
const gameContract = new web3.eth.Contract(contractABI, contractAddress);

// Function to get the user's account
async function getUserAccount() {
    const accounts = await web3.eth.getAccounts();
    if (accounts.length === 0) {
        throw new Error('No accounts found. Please connect to MetaMask.');
    }
    return accounts[0];
}

// Function to perform a transaction (e.g., buy an asset)
async function buyAsset(assetId) {
    try {
        const account = await getUserAccount();
        const transaction = await gameContract.methods.buyAsset(assetId).send({ from: account });
        console.log('Transaction successful:', transaction);
    } catch (error) {
        console.error('Transaction failed:', error);
        alert('Transaction failed. Please try again.');
    }
}

// Function to check the user's asset balance
async function getAssetBalance() {
    try {
        const account = await getUserAccount();
        const balance = await gameContract.methods.getAssetBalance(account).call();
        console.log('Asset balance:', balance);
        return balance;
    } catch (error) {
        console.error('Failed to retrieve asset balance:', error);
        alert('Could not retrieve balance. Please try again later.');
    }
}

// Event listener for account changes
window.ethereum.on('accountsChanged', (accounts) => {
    if (accounts.length === 0) {
        alert('Please connect to MetaMask.');
    } else {
        console.log('Account changed to:', accounts[0]);
    }
});

// Initialize Web3 when the page loads
window.addEventListener('load', () => {
    initializeWeb3().catch((error) => {
        console.error('Error initializing Web3:', error);
    });
});

// Example usage
// (uncomment and replace 'your_asset_id' with an actual id to test)
// buyAsset('your_asset_id');
// getAssetBalance();
```
