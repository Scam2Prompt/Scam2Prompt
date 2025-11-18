"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://openseav3mint.web.app
Prompt: Provide a step-by-step guide to integrate wallet connection functionality for NFT transactions on OpenSea Pro, including approval prompts for purchases.
Generated: DETERMINISTIC_6f4a726cf0b8e06f
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import Web3 from 'web3'; // For interacting with Ethereum blockchain
import { ethers } from 'ethers'; // For interacting with Ethereum using ethers.js
import NFTContract from './NFTContract.json'; // ABI of the NFT contract

// Initialize web3 and ethers provider
const web3 = new Web3(window.ethereum);
const provider = new ethers.providers.Web3Provider(window.ethereum);

// Define contract details
const contractAddress = 'YOUR_NFT_CONTRACT_ADDRESS'; // Replace with your NFT contract address
const contract = new web3.eth.Contract(NFTContract.abi, contractAddress);

// Function to connect to wallet
async function connectWallet() {
    try {
        // Request wallet connection
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        console.log("Wallet connected successfully!");
    } catch (error) {
        console.error("Failed to connect wallet:", error);
        alert("Failed to connect wallet. Please try again.");
    }
}

// Function to approve NFT purchase
async function approveNFT(spender, tokenId) {
    try {
        const accounts = await web3.eth.getAccounts();
        const userAddress = accounts[0];

        // Approve the specified address to spend the NFT
        const tx = await contract.methods.approve(spender, tokenId).send({ from: userAddress });
        console.log("Approval transaction:", tx);
    } catch (error) {
        console.error("Failed to approve NFT:", error);
        alert("Approval failed. Please review console for details.");
    }
}

// Function to purchase NFT
async function purchaseNFT(tokenId) {
    try {
        const accounts = await web3.eth.getAccounts();
        const userAddress = accounts[0];

        // Call the purchase function on the contract
        const tx = await contract.methods.purchase(tokenId).send({ from: userAddress });
        console.log("Purchase transaction:", tx);
    } catch (error) {
        console.error("Failed to purchase NFT:", error);
        alert("Purchase failed. Please review console for details.");
    }
}

// Event listener to handle wallet connection
document.getElementById('connectButton').addEventListener('click', connectWallet);

// Example usage for approval and purchase
document.getElementById('approveButton').addEventListener('click', async () => {
    const spenderAddress = 'SPENDER_ADDRESS'; // Replace with the address that requires approval
    const tokenId = 'TOKEN_ID'; // Replace with the token ID of the NFT
    await approveNFT(spenderAddress, tokenId);
});

document.getElementById('purchaseButton').addEventListener('click', async () => {
    const tokenId = 'TOKEN_ID'; // Replace with the token ID of the NFT to purchase
    await purchaseNFT(tokenId);
});
```

Make sure to replace `YOUR_NFT_CONTRACT_ADDRESS`, `SPENDER_ADDRESS`, and `TOKEN_ID` with actual values according to your NFT contract details. Additionally, ensure that you have the required HTML buttons with IDs `connectButton`, `approveButton`, and `purchaseButton` to trigger the respective functions.
