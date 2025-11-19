"""
Generated Code Metadata:
========================
Original URL: https://shibuya-git-website-redesign-landing-page-pleasrdevs.vercel.app
Prompt: Generate JavaScript code for a simple NFT claim page that checks if a user has voted and then allows them to claim an NFT, inspired by Shibuya's claim system.
Generated: DETERMINISTIC_bb2b186f6ed8c6ea
Batch ID: 20250622_205335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// NFT Claim Page Script

// Import necessary libraries
import Web3 from 'web3'; // Web3.js for Ethereum interaction
import { ethers } from 'ethers'; // Ethers.js for wallet connection

// Constants
const NFT_CONTRACT_ADDRESS = '0xYourNFTContractAddress'; // Replace with your NFT contract address
const VOTING_CONTRACT_ADDRESS = '0xYourVotingContractAddress'; // Replace with your voting contract address
const ABI_NFT = [ /* NFT Contract ABI */ ]; // Replace with your NFT contract ABI
const ABI_VOTING = [ /* Voting Contract ABI */ ]; // Replace with your Voting contract ABI

// Initialize Web3
const web3 = new Web3(window.ethereum);

// Function to check if the user has voted
async function hasUserVoted(userAddress) {
    try {
        const votingContract = new web3.eth.Contract(ABI_VOTING, VOTING_CONTRACT_ADDRESS);
        const voted = await votingContract.methods.hasVoted(userAddress).call();
        return voted;
    } catch (error) {
        console.error('Error checking voting status:', error);
        alert('An error occurred while checking your voting status. Please try again later.');
        return false;
    }
}

// Function to claim the NFT
async function claimNFT(userAddress) {
    try {
        const nftContract = new web3.eth.Contract(ABI_NFT, NFT_CONTRACT_ADDRESS);
        const tx = await nftContract.methods.claimNFT().send({ from: userAddress });
        console.log('NFT claimed successfully:', tx);
        alert('NFT claimed successfully!');
    } catch (error) {
        console.error('Error claiming NFT:', error);
        alert('An error occurred while claiming your NFT. Please try again later.');
    }
}

// Main function to handle the claim process
async function handleClaim() {
    // Request account access
    try {
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        const userAddress = accounts[0];

        // Check if the user has voted
        const voted = await hasUserVoted(userAddress);
        if (voted) {
            // Allow the user to claim the NFT
            await claimNFT(userAddress);
        } else {
            alert('You must vote before claiming the NFT.');
        }
    } catch (error) {
        console.error('Error accessing accounts:', error);
        alert('An error occurred while accessing your account. Please ensure you are connected to MetaMask.');
    }
}

// Event listener for the claim button
document.getElementById('claimButton').addEventListener('click', handleClaim);

// HTML structure for the claim button
document.body.innerHTML += `
    <button id="claimButton">Claim NFT</button>
`;

// Ensure the user has MetaMask installed
if (typeof window.ethereum === 'undefined') {
    alert('Please install MetaMask to use this feature.');
}
```

**Note:** Replace the placeholders for the contract addresses and ABIs with actual values before deploying the code.
