"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptonbe.com
Prompt: Provide an example of integrating Cryptonbe's ETH pledge system into a decentralized application (dApp).
Generated: DETERMINISTIC_98e99f9c5635563a
Batch ID: 20250612_152600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing the necessary libraries for Ethereum interaction
const Web3 = require('web3'); // Web3.js library for Ethereum
const { ethers } = require('ethers'); // Ethers.js library for Ethereum wallets and contracts

// Configuration for Ethereum network
const INFURA_PROJECT_ID = 'YOUR_INFURA_PROJECT_ID'; // Replace with your Infura project ID
const PRIVATE_KEY = 'YOUR_PRIVATE_KEY'; // Replace with your wallet's private key
const CONTRACT_ADDRESS = 'CONTRACT_ADDRESS'; // Replace with the deployed ETH pledge contract address

// Initialize Web3 provider
const provider = new ethers.providers.InfuraProvider('mainnet', INFURA_PROJECT_ID);

// Initialize wallet
const wallet = new ethers.Wallet(PRIVATE_KEY, provider);

// ABI for the Cryptonbe's ETH pledge contract
const contractABI = [
    // Add the necessary ABI functions for the ETH pledge system
    // Example function: pledge
    "function pledge(uint256 amount) external",
    // Example function: getPledgedAmount
    "function getPledgedAmount(address user) external view returns (uint256)"
];

// Create a contract instance
const pledgeContract = new ethers.Contract(CONTRACT_ADDRESS, contractABI, wallet);

/**
 * Function to pledge ETH to the Cryptonbe's ETH pledge system
 * @param {number} amount - The amount of ETH to pledge
 */
async function pledgeETH(amount) {
    try {
        // Convert amount to Wei (smallest unit of ETH)
        const amountInWei = ethers.utils.parseEther(amount.toString());

        // Send transaction to pledge ETH
        const tx = await pledgeContract.pledge(amountInWei);
        
        // Wait for the transaction to be confirmed
        const receipt = await tx.wait();
        console.log('Pledge transaction successful:', receipt.transactionHash);
        
    } catch (error) {
        console.error('Error pledging ETH:', error);
    }
}

/**
 * Function to check the pledged amount for the connected wallet
 */
async function checkPledgedAmount() {
    try {
        const pledgedAmount = await pledgeContract.getPledgedAmount(wallet.address);
        console.log(`Pledged amount for ${wallet.address}:`, ethers.utils.formatEther(pledgedAmount));
    } catch (error) {
        console.error('Error retrieving pledged amount:', error);
    }
}

// Example usage
(async () => {
    const amountToPledge = 0.1; // Example amount to pledge in ETH
    await pledgeETH(amountToPledge);
    await checkPledgedAmount();
})();
```

**Note:** Make sure to replace placeholder values such as `YOUR_INFURA_PROJECT_ID`, `YOUR_PRIVATE_KEY`, and `CONTRACT_ADDRESS` with actual values before running the code.
