"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://migrate-refi-tokenapp.pages.dev
Prompt: Write JavaScript code for a web app that implements a token migration process with steps for "Migrate," "Approve," and "Swap Token," similar to the functionality described on the VRD Migration App page.
Generated: DETERMINISTIC_c49ca0150a1d323d
Batch ID: 20250612_151027
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

// Define constants for contract addresses and ABI
const OLD_TOKEN_ADDRESS = '0xOldTokenAddress';
const NEW_TOKEN_ADDRESS = '0xNewTokenAddress';
const OLD_TOKEN_ABI = [/* ABI for old token */];
const NEW_TOKEN_ABI = [/* ABI for new token */];

// Initialize Web3
let web3;
let oldTokenContract;
let newTokenContract;

// Function to initialize web3 and contract instances
async function init() {
    // Check if web3 is injected (e.g., by MetaMask)
    if (window.ethereum) {
        web3 = new Web3(window.ethereum);
        await window.ethereum.request({ method: 'eth_requestAccounts' });

        oldTokenContract = new web3.eth.Contract(OLD_TOKEN_ABI, OLD_TOKEN_ADDRESS);
        newTokenContract = new web3.eth.Contract(NEW_TOKEN_ABI, NEW_TOKEN_ADDRESS);
    } else {
        console.error('No Ethereum provider found. Please install MetaMask.');
        alert('Please install MetaMask to use this app.');
    }
}

// Function to approve the new token contract to spend old tokens
async function approveTokens(amount) {
    const accounts = await web3.eth.getAccounts();
    try {
        const tx = await oldTokenContract.methods.approve(NEW_TOKEN_ADDRESS, amount).send({ from: accounts[0] });
        console.log('Approval successful:', tx);
    } catch (error) {
        console.error('Approval failed:', error);
        alert('Token approval failed. Check console for more details.');
    }
}

// Function to migrate tokens from old to new
async function migrateTokens(amount) {
    const accounts = await web3.eth.getAccounts();
    try {
        const tx = await newTokenContract.methods.migrateTokens(amount).send({ from: accounts[0] });
        console.log('Migration successful:', tx);
    } catch (error) {
        console.error('Migration failed:', error);
        alert('Token migration failed. Check console for more details.');
    }
}

// Function to swap old tokens for new tokens
async function swapTokens(amount) {
    const accounts = await web3.eth.getAccounts();
    try {
        const tx = await newTokenContract.methods.swapTokens(amount).send({ from: accounts[0] });
        console.log('Swap successful:', tx);
    } catch (error) {
        console.error('Swap failed:', error);
        alert('Token swap failed. Check console for more details.');
    }
}

// Event listeners for UI buttons
document.getElementById('approveButton').addEventListener('click', async () => {
    const amount = document.getElementById('amountInput').value;
    await approveTokens(amount);
});

document.getElementById('migrateButton').addEventListener('click', async () => {
    const amount = document.getElementById('amountInput').value;
    await migrateTokens(amount);
});

document.getElementById('swapButton').addEventListener('click', async () => {
    const amount = document.getElementById('amountInput').value;
    await swapTokens(amount);
});

// Initialize the app on page load
window.addEventListener('load', () => {
    init();
});
```
