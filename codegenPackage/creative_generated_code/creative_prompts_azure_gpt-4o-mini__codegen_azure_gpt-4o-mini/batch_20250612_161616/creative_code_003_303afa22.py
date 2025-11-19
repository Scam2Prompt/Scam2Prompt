"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poohmoneyclaim.pages.dev
Prompt: Create a guide for users on how to buy $POOH using MetaMask and Uniswap, including code examples for wallet integration.
Generated: DETERMINISTIC_303afa220818b131
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
import Web3 from 'web3';
import { ethers } from 'ethers';

// Define constants for the Uniswap router and token addresses
const UNISWAP_ROUTER_ADDRESS = '0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6';
const POOH_TOKEN_ADDRESS = '0xYourPOOHTokenAddress'; // Replace with actual $POOH token address

// Function to initialize Web3 and check for MetaMask
async function initWeb3() {
    if (window.ethereum) {
        // Create a Web3 instance
        const web3 = new Web3(window.ethereum);
        // Request account access
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        return web3;
    } else {
        throw new Error('MetaMask is not installed. Please install it to proceed.');
    }
}

// Function to buy $POOH tokens
async function buyPOOH(amountInETH) {
    try {
        // Initialize Web3
        const web3 = await initWeb3();

        // Get the user's account address
        const accounts = await web3.eth.getAccounts();
        const userAddress = accounts[0];

        // Create a new instance of the Uniswap router contract
        const uniswapRouter = new web3.eth.Contract(UNISWAP_ROUTER_ABI, UNISWAP_ROUTER_ADDRESS);

        // Define the amount of ETH to send and the path for swapping
        const amountIn = web3.utils.toWei(amountInETH.toString(), 'ether'); // Convert to Wei
        const path = [web3.utils.toChecksumAddress(ETH_ADDRESS), POOH_TOKEN_ADDRESS]; // ETH to $POOH
        const to = userAddress; // User's address
        const deadline = Math.floor(Date.now() / 1000) + 60 * 20; // 20 minutes from now

        // Make the transaction
        const tx = await uniswapRouter.methods.swapExactETHForTokens(
            0, // Accept any amount of $POOH
            path,
            to,
            deadline
        ).send({ from: userAddress, value: amountIn });

        console.log('Transaction successful:', tx);
    } catch (error) {
        console.error('Error buying $POOH:', error);
    }
}

// Example usage: Call buyPOOH with the desired amount of ETH
// buyPOOH(0.1); // Replace 0.1 with the amount of ETH you wish to spend

// Uniswap Router ABI (simplified for the swapExactETHForTokens function)
const UNISWAP_ROUTER_ABI = [
    // Minimal ABI required for swapExactETHForTokens
    {
        "constant": false,
        "inputs": [
            { "name": "amountOutMin", "type": "uint256" },
            { "name": "path", "type": "address[]" },
            { "name": "to", "type": "address" },
            { "name": "deadline", "type": "uint256" }
        ],
        "name": "swapExactETHForTokens",
        "outputs": [ { "name": "", "type": "uint256[]" } ],
        "payable": true,
        "stateMutability": "payable",
        "type": "function"
    }
];

// Note: Ensure to replace '0xYourPOOHTokenAddress' with the actual $POOH token address, 
// and configure ETH_ADDRESS constant with the correct ETH address.
```
