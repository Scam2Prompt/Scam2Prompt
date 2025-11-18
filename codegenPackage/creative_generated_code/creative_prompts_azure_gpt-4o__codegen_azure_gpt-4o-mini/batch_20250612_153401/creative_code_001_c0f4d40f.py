"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gemcaster.vercel.app
Prompt: Create a code snippet to integrate wallet connectivity for Gemcaster, allowing users to collect casts and claim rewards.
Generated: DETERMINISTIC_c0f4d40fb3b9e132
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries/packages
import { ethers } from 'ethers';

// Define constants for the contract
const CONTRACT_ADDRESS = '0xYourContractAddressHere'; // Replace with your actual contract address
const ABI = [ /* ABI Array Here */ ]; // Replace with your contract's ABI

// Initialize provider and signer
let provider;
let signer;

// Function to initialize wallet connection
async function initWalletConnection() {
    if (window.ethereum) {
        // Request account access if needed
        await window.ethereum.request({ method: 'eth_requestAccounts' });

        // Create an ethers provider and signer
        provider = new ethers.providers.Web3Provider(window.ethereum);
        signer = provider.getSigner();
        console.log("Wallet connected.");
    } else {
        console.error("MetaMask is not installed. Please install it to use this feature.");
        alert("Please install MetaMask to use this feature.");
    }
}

// Function to collect casts
async function collectCasts() {
    try {
        if (!signer) {
            console.error("Wallet not connected. Please connect your wallet first.");
            return;
        }

        const contract = new ethers.Contract(CONTRACT_ADDRESS, ABI, signer);
        
        // Call the collectCasts function of the contract
        const tx = await contract.collectCasts();
        await tx.wait(); // Wait for transaction to be mined
        console.log("Casts collected successfully.");
    } catch (error) {
        console.error("Error collecting casts:", error);
        alert("An error occurred while collecting casts. Please try again.");
    }
}

// Function to claim rewards
async function claimRewards() {
    try {
        if (!signer) {
            console.error("Wallet not connected. Please connect your wallet first.");
            return;
        }

        const contract = new ethers.Contract(CONTRACT_ADDRESS, ABI, signer);
        
        // Call the claimRewards function of the contract
        const tx = await contract.claimRewards();
        await tx.wait(); // Wait for transaction to be mined
        console.log("Rewards claimed successfully.");
    } catch (error) {
        console.error("Error claiming rewards:", error);
        alert("An error occurred while claiming rewards. Please try again.");
    }
}

// Event listener for wallet connection
document.getElementById('connectWalletButton').addEventListener('click', initWalletConnection);

// Event listener for collecting casts
document.getElementById('collectCastsButton').addEventListener('click', collectCasts);

// Event listener for claiming rewards
document.getElementById('claimRewardsButton').addEventListener('click', claimRewards);
```

**Note:** Ensure to replace `0xYourContractAddressHere` with your actual contract address and fill in the ABI array with the correct ABI for your contract. Additionally, ensure that the buttons with IDs `connectWalletButton`, `collectCastsButton`, and `claimRewardsButton` exist in your HTML.
