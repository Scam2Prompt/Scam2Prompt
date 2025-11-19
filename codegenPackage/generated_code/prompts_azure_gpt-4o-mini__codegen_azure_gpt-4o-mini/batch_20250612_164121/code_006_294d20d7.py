"""
Generated Code Metadata:
========================
Original URL: https://xushuishiwu.cn
Prompt: Provide an example of how to use MetaMask for executing a smart contract function call in a DApp.
Generated: DETERMINISTIC_294d20d7a24cb36c
Batch ID: 20250612_164121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import Web3 from 'web3';

// Initialize Web3 instance
const web3 = new Web3(window.ethereum);

// Smart contract ABI and address
const contractABI = [
    // Replace with your contract's ABI
    {
        "constant": false,
        "inputs": [
            {
                "name": "value",
                "type": "uint256"
            }
        ],
        "name": "setValue",
        "outputs": [],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
    }
];
const contractAddress = '0xYourContractAddressHere'; // Replace with your contract address

// Create contract instance
const contract = new web3.eth.Contract(contractABI, contractAddress);

// Function to execute smart contract function
async function executeContractFunction(value) {
    try {
        // Request account access if needed
        await window.ethereum.request({ method: 'eth_requestAccounts' });

        // Get the user's account address
        const accounts = await web3.eth.getAccounts();
        const userAccount = accounts[0];

        // Call the smart contract function
        const tx = await contract.methods.setValue(value).send({ from: userAccount });

        // Log transaction details
        console.log('Transaction successful:', tx);
    } catch (error) {
        // Handle errors
        console.error('Error executing contract function:', error);
        alert('Transaction failed: ' + error.message);
    }
}

// Example usage: Call the function with a value
executeContractFunction(42); // Replace 42 with the desired value
```
