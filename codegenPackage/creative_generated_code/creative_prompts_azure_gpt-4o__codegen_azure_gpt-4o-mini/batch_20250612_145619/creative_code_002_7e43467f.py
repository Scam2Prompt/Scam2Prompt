"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethphb.com
Prompt: Generate code to enable JavaScript-based interaction with an Ethereum pledge platform, ensuring proper wallet integration and transaction validation.
Generated: DETERMINISTIC_7e43467fdc127920
Batch ID: 20250612_145619
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

// Define the Ethereum pledge platform contract ABI and address
const pledgeContractABI = [...]; // Replace with actual ABI
const pledgeContractAddress = '0xYourContractAddress'; // Replace with actual contract address

// Initialize Web3
let web3;
if (window.ethereum) {
    web3 = new Web3(window.ethereum);
} else {
    console.error('Please install MetaMask or another Ethereum wallet provider.');
}

// Create contract instance
const pledgeContract = new web3.eth.Contract(pledgeContractABI, pledgeContractAddress);

// Function to connect to the user's Ethereum wallet
async function connectWallet() {
    try {
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        console.log('Connected account:', accounts[0]);
        return accounts[0];
    } catch (error) {
        console.error('Failed to connect wallet:', error);
    }
}

// Function to pledge an amount
async function makePledge(amount) {
    const account = await connectWallet();
    if (!account) return;

    try {
        // Validate the amount
        if (!web3.utils.isBN(amount) && amount <= 0) {
            throw new Error('Amount must be a positive number');
        }

        // Convert amount to Wei
        const amountInWei = web3.utils.toWei(amount.toString(), 'ether');

        // Send the transaction to the contract
        const transaction = await pledgeContract.methods.pledge().send({
            from: account,
            value: amountInWei
        });
        
        console.log('Pledge successful:', transaction);
    } catch (error) {
        console.error('Pledge failed:', error);
    }
}

// UI event listener for pledge button
document.getElementById('pledgeButton').addEventListener('click', () => {
    const amount = document.getElementById('pledgeAmount').value;
    makePledge(amount);
});

// Function to check pledge status
async function checkPledgeStatus(account) {
    try {
        const status = await pledgeContract.methods.getPledgeStatus(account).call();
        console.log('Pledge status:', status);
        return status;
    } catch (error) {
        console.error('Failed to fetch pledge status:', error);
    }
}

// Example usage
connectWallet().then((account) => {
    checkPledgeStatus(account);
});
```
