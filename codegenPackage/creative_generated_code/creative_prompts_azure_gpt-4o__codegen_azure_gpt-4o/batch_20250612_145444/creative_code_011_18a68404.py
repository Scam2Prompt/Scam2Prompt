"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flockerz-claim.web.app
Prompt: Develop a Web3.js-based widget for swapping ETH, BNB, or USDT for $FLOCK tokens, ensuring compatibility with MetaMask and other wallets.
Generated: DETERMINISTIC_18a684045e25c6e2
Batch ID: 20250612_145444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required packages
const Web3 = require('web3');

// Ensure the presence of Web3
if (typeof window.ethereum === 'undefined') {
    throw new Error('MetaMask or compatible wallet is required to use this widget.');
}

// Initialize Web3 instance
const web3 = new Web3(window.ethereum);

// Smart contract details
const FLOCK_TOKEN_CONTRACT_ADDRESS = "0xYourFlockTokenContractAddress"; // Replace with $FLOCK token contract address
const FLOCK_TOKEN_ABI = [ /* ABI Array */ ]; // Replace with $FLOCK token ABI array
const TOKEN_SWAP_CONTRACT_ADDRESS = "0xYourSwapContractAddress"; // Replace with swap contract address
const TOKEN_SWAP_ABI = [ /* Swap Contract ABI */ ]; // Replace with swap contract ABI array

// Connect to wallet and handle interactions
async function connectWallet() {
    try {
        // Request account access if needed
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        console.log('Connected wallet:', accounts[0]);
        return accounts[0]; // Return the connected account
    } catch (err) {
        console.error('Error connecting to wallet:', err);
        throw new Error('Failed to connect MetaMask.');
    }
}

// Swap function for swapping ETH/BNB/USDT to $FLOCK tokens
async function swapTokens(inputToken, amount, account) {
    try {
        // Validate parameters
        if (!inputToken || !['ETH', 'BNB', 'USDT'].includes(inputToken)) {
            throw new Error('Invalid input token. Only ETH, BNB, and USDT are supported.');
        }
        if (!amount || amount <= 0) {
            throw new Error('Invalid amount. Please input a valid amount to swap.');
        }
        if (!web3.utils.isAddress(account)) {
            throw new Error('Invalid wallet address.');
        }

        // Initialize contract instance
        const swapContract = new web3.eth.Contract(TOKEN_SWAP_ABI, TOKEN_SWAP_CONTRACT_ADDRESS);

        // Define parameters for swap
        const valueToSend = inputToken === 'ETH' || inputToken === 'BNB' ? web3.utils.toWei(amount.toString(), 'ether') : 0;

        // Swap logic
        const swapMethod = inputToken === 'USDT' ? 'swapUSDTForFLOCK' : 'swapETHForFLOCK'; // Example function names
        const tx = await swapContract.methods[swapMethod](web3.utils.toWei(amount.toString(), 'ether')).send({
            from: account,
            value: valueToSend,
        });

        console.log('Swap successful:', tx);
        return tx; // Return the transaction object
    } catch (err) {
        console.error('Error swapping tokens:', err);
        throw new Error('Swap failed. Please try again.');
    }
}

// Entry point for the widget interface
async function runWidget() {
    try {
        // Connect to wallet
        const account = await connectWallet();

        // Example usage: Swap 0.1 ETH for FLOCK
        const inputToken = 'ETH'; // ETH, BNB, or USDT
        const amount = 0.1; // Replace with desired swap amount

        const result = await swapTokens(inputToken, amount, account);
        alert(`Swap complete! Transaction hash: ${result.transactionHash}`);
    } catch (err) {
        alert(`Error: ${err.message}`);
    }
}

// Attach the widget functionality to a button
document.getElementById('swapButton').addEventListener('click', runWidget);

// Example HTML for the widget button:
// <button id="swapButton">Swap Tokens</button>
```
