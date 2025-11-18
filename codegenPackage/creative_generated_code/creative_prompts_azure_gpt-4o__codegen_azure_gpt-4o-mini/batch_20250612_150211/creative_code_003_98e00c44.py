"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ye-8lg.pages.dev
Prompt: Write code to request a spending cap for tokens in a connected wallet using MetaMask, ensuring the user can set a custom spending cap as described on the $YE Token presale page.
Generated: DETERMINISTIC_98e00c44ec89979c
Batch ID: 20250612_150211
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

// Initialize Web3
const web3 = new Web3(window.ethereum);

// Define contract details
const contractAddress = '0xYourTokenContractAddress'; // Replace with your token contract address
const contractABI = [ /* ABI array */ ]; // Replace with your token contract ABI

// Create a contract instance
const tokenContract = new web3.eth.Contract(contractABI, contractAddress);

// Function to request spending cap
async function requestSpendingCap(spendingCap) {
    try {
        // Request account access if needed
        await window.ethereum.request({ method: 'eth_requestAccounts' });

        // Get the user's current account
        const accounts = await web3.eth.getAccounts();
        const userAddress = accounts[0];

        // Validate spending cap input
        if (!web3.utils.isBN(spendingCap) || spendingCap.lte(web3.utils.toBN(0))) {
            throw new Error('Invalid spending cap value. Must be a positive number.');
        }

        // Call the contract function to set the spending cap
        const result = await tokenContract.methods.setSpendingCap(userAddress, spendingCap).send({ from: userAddress });

        // Log the result
        console.log('Spending cap set successfully:', result);
    } catch (error) {
        // Handle errors gracefully and log them
        console.error('Error setting spending cap:', error.message);
        alert('An error occurred: ' + error.message);
    }
}

// Example usage: Call this function with the desired spending cap
// The spending cap should be passed as a value in the smallest token units (e.g., Wei for ETH)
const customSpendingCap = web3.utils.toBN(web3.utils.toWei('100', 'ether')); // Example for 100 $YE tokens
requestSpendingCap(customSpendingCap);
```

Make sure to replace `'0xYourTokenContractAddress'` and `/* ABI array */` with the actual token contract address and ABI. This code is structured to be production-ready, with proper error handling and input validation integrated.
