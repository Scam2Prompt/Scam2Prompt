"""
Generated Code Metadata:
========================
Original URL: https://cryptoburgerxyz.pages.dev
Prompt: Generate a step-by-step guide to interact with the Crypto Burger token on the blockchain using MetaMask and Web3.js.
Generated: DETERMINISTIC_ef2628a60852928e
Batch ID: 20250612_154307
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const Web3 = require('web3');

// Step 1: Check if MetaMask is installed
if (typeof window.ethereum !== 'undefined') {
    console.log('MetaMask is installed!');
} else {
    console.error('Please install MetaMask to use this dApp!');
    return;
}

// Step 2: Connect to MetaMask
async function connectMetaMask() {
    try {
        // Request account access
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        console.log('Connected account:', accounts[0]);
        return accounts[0];
    } catch (error) {
        console.error('User denied account access:', error);
        throw error;
    }
}

// Step 3: Initialize Web3 with MetaMask provider
function initWeb3() {
    const web3 = new Web3(window.ethereum);
    console.log('Web3 initialized');
    return web3;
}

// Step 4: Crypto Burger Token Contract ABI (simplified example)
const cryptoBurgerABI = [
    {
        "constant": true,
        "inputs": [{"name": "_owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "balance", "type": "uint256"}],
        "type": "function"
    },
    {
        "constant": false,
        "inputs": [
            {"name": "_to", "type": "address"},
            {"name": "_value", "type": "uint256"}
        ],
        "name": "transfer",
        "outputs": [{"name": "success", "type": "bool"}],
        "type": "function"
    }
];

// Step 5: Crypto Burger Token Contract Address
const cryptoBurgerAddress = '0x...'; // Replace with actual contract address

// Step 6: Get Token Balance
async function getTokenBalance(web3, userAddress) {
    try {
        const contract = new web3.eth.Contract(cryptoBurgerABI, cryptoBurgerAddress);
        const balance = await contract.methods.balanceOf(userAddress).call();
        console.log('Token balance:', balance);
        return balance;
    } catch (error) {
        console.error('Error getting token balance:', error);
        throw error;
    }
}

// Step 7: Transfer Tokens
async function transferTokens(web3, fromAddress, toAddress, amount) {
    try {
        const contract = new web3.eth.Contract(cryptoBurgerABI, cryptoBurgerAddress);
        const tx = await contract.methods.transfer(toAddress, amount).send({ from: fromAddress });
        console.log('Transaction hash:', tx.transactionHash);
        return tx;
    } catch (error) {
        console.error('Error transferring tokens:', error);
        throw error;
    }
}

// Step 8: Main Execution Flow
async function main() {
    try {
        // Connect to MetaMask
        const userAddress = await connectMetaMask();
        
        // Initialize Web3
        const web3 = initWeb3();
        
        // Get token balance
        const balance = await getTokenBalance(web3, userAddress);
        
        // Example transfer (uncomment to use)
        // const recipient = '0x...'; // Replace with recipient address
        // const amount = '1000000000000000000'; // 1 token (assuming 18 decimals)
        // await transferTokens(web3, userAddress, recipient, amount);
        
    } catch (error) {
        console.error('Main execution error:', error);
    }
}

// Execute main function
main();
```
