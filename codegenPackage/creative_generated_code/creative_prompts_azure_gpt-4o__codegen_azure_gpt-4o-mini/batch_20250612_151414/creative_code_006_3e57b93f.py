"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://peetdecentralized.finance
Prompt: Write a tutorial for setting up a decentralized staking system using Peet's platform and wallets like Metamask or TrustWallet.
Generated: DETERMINISTIC_3e57b93f1139d47c
Batch ID: 20250612_151414
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
const Web3 = require('web3'); // Web3.js library for Ethereum blockchain interaction
const { abi: stakingContractABI } = require('./StakingContract.json'); // ABI for the staking contract

// Initialize Web3 with Metamask or TrustWallet provider
if (typeof window.ethereum !== 'undefined') {
    var web3 = new Web3(window.ethereum);
} else {
    console.error("Please install Metamask or TrustWallet to use this application.");
}

// Address of the deployed staking contract
const stakingContractAddress = '0xYourStakingContractAddress'; // Replace with your contract address

// Create an instance of the staking contract
const stakingContract = new web3.eth.Contract(stakingContractABI, stakingContractAddress);

// Function to connect to user's wallet
async function connectWallet() {
    try {
        // Request account access
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        const userAddress = accounts[0];
        console.log("Connected account:", userAddress);
        return userAddress;
    } catch (error) {
        console.error("Error connecting to wallet:", error);
    }
}

// Function to stake tokens
async function stakeTokens(amount, userAddress) {
    try {
        // Convert amount to Wei (smallest unit of Ether)
        const amountInWei = web3.utils.toWei(amount.toString(), 'ether');

        // Send transaction to stake tokens
        const transaction = await stakingContract.methods.stake(amountInWei).send({ from: userAddress });
        console.log("Transaction successful:", transaction);
    } catch (error) {
        console.error("Error staking tokens:", error);
    }
}

// Function to unstake tokens
async function unstakeTokens(amount, userAddress) {
    try {
        // Convert amount to Wei
        const amountInWei = web3.utils.toWei(amount.toString(), 'ether');

        // Send transaction to unstake tokens
        const transaction = await stakingContract.methods.unstake(amountInWei).send({ from: userAddress });
        console.log("Transaction successful:", transaction);
    } catch (error) {
        console.error("Error unstaking tokens:", error);
    }
}

// Function to check staked balance
async function getStakedBalance(userAddress) {
    try {
        const balance = await stakingContract.methods.balanceOf(userAddress).call();
        // Convert balance from Wei to Ether
        const balanceInEther = web3.utils.fromWei(balance, 'ether');
        console.log("Staked balance:", balanceInEther);
        return balanceInEther;
    } catch (error) {
        console.error("Error fetching staked balance:", error);
    }
}

// Example usage of the functions
async function main() {
    const userAddress = await connectWallet();

    // Stake tokens
    await stakeTokens(1, userAddress); // Staking 1 token

    // Get staked balance
    await getStakedBalance(userAddress);

    // Unstake tokens
    await unstakeTokens(1, userAddress); // Unstaking 1 token
}

// Execute the main function to run the example
main();
```
