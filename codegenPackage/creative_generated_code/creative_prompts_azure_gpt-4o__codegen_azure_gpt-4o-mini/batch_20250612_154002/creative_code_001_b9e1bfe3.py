"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dcqqx.com
Prompt: Recommend libraries or APIs for building decentralized applications (dApps) on Ethereum that require JavaScript for proper functionality.
Generated: DETERMINISTIC_b9e1bfe382f91232
Batch ID: 20250612_154002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries for building Ethereum dApps
const Web3 = require('web3'); // A library to interact with the Ethereum blockchain
const { ethers } = require('ethers'); // A library for Ethereum wallet and contract interaction
const dotenv = require('dotenv'); // A module to load environment variables from a .env file

// Load environment variables from .env file
dotenv.config();

// Initialize Web3 with an Ethereum provider (like Infura or Alchemy)
const web3 = new Web3(new Web3.providers.HttpProvider(process.env.INFURA_URL));

// Function to connect to an Ethereum wallet
async function connectWallet() {
    // Check if the window object is available (for browser environment)
    if (typeof window.ethereum !== 'undefined') {
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        await provider.send("eth_requestAccounts", []); // Request user accounts
        const signer = provider.getSigner(); // Get the signer
        console.log("Wallet connected:", await signer.getAddress());
    } else {
        throw new Error("Ethereum wallet not found. Please install MetaMask.");
    }
}

// Function to get the balance of an Ethereum account
async function getBalance(address) {
    try {
        const balance = await web3.eth.getBalance(address); // Get balance in Wei
        console.log(`Balance of ${address}: ${web3.utils.fromWei(balance, 'ether')} ETH`);
        return balance;
    } catch (error) {
        console.error("Error fetching balance:", error);
        throw new Error("Failed to fetch balance.");
    }
}

// Function to deploy a smart contract
async function deployContract(abi, bytecode) {
    const accounts = await web3.eth.getAccounts(); // Get accounts
    const contract = new web3.eth.Contract(abi); // Create contract instance

    try {
        const deployedContract = await contract.deploy({ data: bytecode }) // Deploy contract
            .send({ from: accounts[0], gas: 3000000 });
        console.log("Contract deployed at address:", deployedContract.options.address);
        return deployedContract;
    } catch (error) {
        console.error("Error deploying contract:", error);
        throw new Error("Contract deployment failed.");
    }
}

// Example usage
(async () => {
    try {
        await connectWallet(); // Connect to user's wallet
        const userAddress = await web3.eth.getAccounts()[0]; // Get the user's Ethereum address
        await getBalance(userAddress); // Fetch and log user's balance
    } catch (error) {
        console.error("An error occurred:", error.message);
    }
})();

// Exporting functions for external use
module.exports = {
    connectWallet,
    getBalance,
    deployContract
};
```
