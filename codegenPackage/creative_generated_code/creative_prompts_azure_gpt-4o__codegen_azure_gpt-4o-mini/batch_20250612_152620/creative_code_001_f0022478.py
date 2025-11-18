"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scottytheai-def.web.app
Prompt: Generate code to connect a MetaMask wallet to the Scotty AI platform using Web3.js, enabling users to buy $SCOTTY tokens with ETH.
Generated: DETERMINISTIC_f002247874ed485c
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the necessary libraries
import Web3 from 'web3';

// Define the constants for the smart contract
const SCOTTY_CONTRACT_ADDRESS = '0xYourContractAddress'; // Replace with your SCOTTY token contract address
const SCOTTY_ABI = [ /* ABI JSON Array Here */ ]; // Replace with your SCOTTY token contract ABI

// Initialize Web3
const web3 = new Web3(window.ethereum);

// Function to connect to MetaMask
async function connectWallet() {
    if (window.ethereum) {
        try {
            // Request account access
            await window.ethereum.request({ method: 'eth_requestAccounts' });
            console.log('Wallet connected successfully');
        } catch (error) {
            console.error('User denied account access', error);
        }
    } else {
        console.error('MetaMask is not installed. Please install it to use this dApp.');
    }
}

// Function to buy $SCOTTY tokens
async function buyScottyTokens(amountInEther) {
    try {
        // Ensure the user is connected
        const accounts = await web3.eth.getAccounts();
        if (accounts.length === 0) {
            throw new Error('Please connect your MetaMask wallet first.');
        }
        
        const userAddress = accounts[0];
        
        // Convert Ether to Wei
        const amountInWei = web3.utils.toWei(amountInEther.toString(), 'ether');

        // Create contract instance
        const scottyContract = new web3.eth.Contract(SCOTTY_ABI, SCOTTY_CONTRACT_ADDRESS);
        
        // Execute the transaction to buy tokens
        const transaction = await scottyContract.methods.buyTokens().send({
            from: userAddress,
            value: amountInWei,
            gas: 200000 // Estimate gas limit
        });

        console.log('Transaction successful:', transaction);
    } catch (error) {
        console.error('Transaction failed', error);
    }
}

// Event listener for the button to connect wallet
document.getElementById('connectButton').addEventListener('click', connectWallet);

// Event listener for the button to buy tokens
document.getElementById('buyButton').addEventListener('click', () => {
    const amount = document.getElementById('amountInput').value;
    buyScottyTokens(amount);
});
```
