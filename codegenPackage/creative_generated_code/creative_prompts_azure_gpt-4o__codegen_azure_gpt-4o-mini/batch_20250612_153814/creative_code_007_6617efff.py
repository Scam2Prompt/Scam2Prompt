"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask.meta.electrosil14.com
Prompt: Explain how to use MetaMask with Web3.js to interact with a deployed smart contract on Ethereum.
Generated: DETERMINISTIC_6617efffe887428e
Batch ID: 20250612_153814
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing required libraries
import Web3 from 'web3';

// Check if MetaMask is installed and enabled
if (typeof window.ethereum !== 'undefined') {
    console.log('MetaMask is installed!');
} else {
    console.error('MetaMask is not installed. Please install it to use this application.');
}

// Initialize Web3 instance
const web3 = new Web3(window.ethereum);

// Define the smart contract ABI and address
const contractABI = [
    // Add the ABI of your smart contract here
];

const contractAddress = '0xYourContractAddressHere'; // Replace with your deployed contract address

// Create a contract instance
const contract = new web3.eth.Contract(contractABI, contractAddress);

// Function to request account access from MetaMask
async function requestAccount() {
    try {
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        console.log('Account access granted.');
    } catch (error) {
        console.error('Error accessing account:', error);
    }
}

// Function to interact with the smart contract
async function interactWithContract() {
    try {
        // Request account access
        await requestAccount();

        // Get the user's Ethereum account
        const accounts = await web3.eth.getAccounts();
        const userAccount = accounts[0];

        // Example: Call a read function from the contract
        const result = await contract.methods.yourReadFunction().call({ from: userAccount });
        console.log('Data from contract:', result);

        // Example: Call a write function from the contract
        const txReceipt = await contract.methods.yourWriteFunction(/* parameters */)
            .send({ from: userAccount, gas: 3000000 });
        console.log('Transaction successful:', txReceipt);
    } catch (error) {
        console.error('Error interacting with contract:', error);
    }
}

// Call the function to interact with the contract
interactWithContract();
```
