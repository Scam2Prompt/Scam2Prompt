"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdccash.xyz
Prompt: Provide a step-by-step guide to integrate the $UPRINT token with a MetaMask wallet, including how to add the token address `0x7a553dec67ea2cdd9350e3205f0faadb5c45434a` and track USDC rewards.
Generated: DETERMINISTIC_7ad0c1f866389a1c
Batch ID: 20250612_154728
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
import { ethers } from 'ethers';

// Define the token contract address and ABI
const UPRINT_TOKEN_ADDRESS = '0x7a553dec67ea2cdd9350e3205f0faadb5c45434a';
const UPRINT_ABI = [ /* Add the token's ABI here */ ];

// Initialize web3
let web3;

// Function to connect to MetaMask
async function connectMetaMask() {
    // Check if MetaMask is installed
    if (typeof window.ethereum !== 'undefined') {
        web3 = new Web3(window.ethereum);

        try {
            // Request account access
            await window.ethereum.request({ method: 'eth_requestAccounts' });
            console.log('MetaMask connected!');
        } catch (error) {
            console.error('User denied account access:', error);
            throw new Error('Connection to MetaMask failed');
        }
    } else {
        console.error('MetaMask is not installed. Please install it to continue.');
        throw new Error('MetaMask not found');
    }
}

// Function to add UPRINT token to MetaMask
async function addTokenToMetaMask() {
    const tokenAddress = UPRINT_TOKEN_ADDRESS;
    const tokenSymbol = 'UPRINT';
    const tokenDecimals = 18;

    // Call the MetaMask API to add the token
    const wasAdded = await window.ethereum.request({
        method: 'wallet_watchAsset',
        params: {
            type: 'ERC20',
            options: {
                address: tokenAddress,
                symbol: tokenSymbol,
                decimals: tokenDecimals,
            },
        },
    });

    if (wasAdded) {
        console.log(`${tokenSymbol} token added to MetaMask!`);
    } else {
        console.log(`Failed to add ${tokenSymbol} token.`);
    }
}

// Function to track USDC rewards
async function trackUSDCRewards() {
    const account = (await web3.eth.getAccounts())[0];
    const tokenContract = new web3.eth.Contract(UPRINT_ABI, UPRINT_TOKEN_ADDRESS);

    try {
        // Assuming 'getRewards' is a function on the contract that returns USDC rewards
        const rewards = await tokenContract.methods.getRewards(account).call();
        console.log(`USDC Rewards for ${account}: ${web3.utils.fromWei(rewards, 'ether')} USDC`);
    } catch (error) {
        console.error('Error fetching USDC rewards:', error);
    }
}

// Main function to execute the steps
async function main() {
    try {
        await connectMetaMask();
        await addTokenToMetaMask();
        await trackUSDCRewards();
    } catch (error) {
        console.error('An error occurred in the process:', error);
    }
}

// Execute the main function
main();
```
