"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chaingpt-airdrop.pages.dev
Prompt: Write a JavaScript script to connect a wallet and interact with the ChainGPT Airdrop system, ensuring users can claim their $CGPT tokens based on activity.
Generated: DETERMINISTIC_b749d7b06275e2bd
Batch ID: 20250612_152526
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

// Airdrop contract address and ABI (Application Binary Interface)
const AIRDROP_CONTRACT_ADDRESS = '0xYourAirdropContractAddress';
const AIRDROP_CONTRACT_ABI = [
    // Replace with the actual ABI of the airdrop contract
];

// Initialize Web3
const web3 = new Web3(window.ethereum);

// Function to connect the user's wallet
async function connectWallet() {
    try {
        // Request account access
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        console.log('Wallet connected');
    } catch (error) {
        console.error('User denied account access or error occurred:', error);
        alert('Could not connect your wallet. Please check your browser console for details.');
    }
}

// Function to claim $CGPT tokens
async function claimTokens() {
    try {
        // Get user's accounts
        const accounts = await web3.eth.getAccounts();
        const userAddress = accounts[0];

        // Create contract instance
        const airdropContract = new web3.eth.Contract(AIRDROP_CONTRACT_ABI, AIRDROP_CONTRACT_ADDRESS);

        // Call claim function from the contract
        const tx = await airdropContract.methods.claimTokens().send({ from: userAddress });
        console.log('Tokens claimed successfully:', tx);
        alert('You have successfully claimed your $CGPT tokens!');
    } catch (error) {
        console.error('Error claiming tokens:', error);
        alert('An error occurred while claiming your tokens. Please try again.');
    }
}

// Event listener for the connect button
document.getElementById('connectButton').addEventListener('click', async () => {
    await connectWallet();
});

// Event listener for the claim button
document.getElementById('claimButton').addEventListener('click', async () => {
    await claimTokens();
});

// Check if MetaMask is installed
if (typeof window.ethereum === 'undefined') {
    alert('MetaMask is not installed. Please install it to interact with the airdrop system.');
}
```
