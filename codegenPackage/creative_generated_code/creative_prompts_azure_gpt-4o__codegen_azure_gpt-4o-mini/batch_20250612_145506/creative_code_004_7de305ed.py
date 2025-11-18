"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://floki.icu
Prompt: Write code using the MetaMask API to prompt users to connect their wallet and claim FLOKI INU rewards.
Generated: DETERMINISTIC_7de305edbecafb30
Batch ID: 20250612_145506
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

// Define the contract ABI and address (replace with actual values)
const contractABI = [
    // Add the ABI details of the FLOKI INU contract
];
const contractAddress = '0xYourContractAddress'; // Replace with actual contract address

// Initialize Web3
let web3;

// Function to check if MetaMask is installed
const isMetaMaskInstalled = () => {
    return Boolean(window.ethereum && window.ethereum.isMetaMask);
};

// Function to connect to MetaMask
const connectWallet = async () => {
    if (!isMetaMaskInstalled()) {
        alert('MetaMask not detected. Please install it to use this feature.');
        return;
    }

    try {
        // Request account access if needed
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        return accounts[0]; // Return the first account address
    } catch (error) {
        console.error('User denied account access or error occurred:', error);
        alert('Could not connect to your wallet. Please try again.');
        return null;
    }
};

// Function to claim FLOKI INU rewards
const claimRewards = async (account) => {
    if (!web3) {
        web3 = new Web3(window.ethereum);
    }

    const contract = new web3.eth.Contract(contractABI, contractAddress);

    try {
        // Call the claim function on the contract
        const tx = await contract.methods.claimRewards().send({ from: account });
        console.log('Transaction successful:', tx);
        alert('Rewards claimed successfully!');
    } catch (error) {
        console.error('Error claiming rewards:', error);
        alert('An error occurred while claiming rewards. Please check the console for details.');
    }
};

// Main function to handle wallet connection and claiming rewards
const handleClaimRewards = async () => {
    const account = await connectWallet();
    if (account) {
        await claimRewards(account);
    }
};

// Add event listener to a button (replace 'claimButton' with your button ID)
document.getElementById('claimButton').addEventListener('click', handleClaimRewards);
```
