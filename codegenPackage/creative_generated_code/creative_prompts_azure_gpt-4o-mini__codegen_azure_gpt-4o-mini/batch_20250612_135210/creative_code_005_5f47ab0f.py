"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wap.xushuishiwu.cn
Prompt: Write a code snippet that demonstrates how to interact with a smart contract using the MetaMask wallet.
Generated: DETERMINISTIC_5f47ab0f6dcd5f0d
Batch ID: 20250612_135210
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing necessary libraries
import Web3 from 'web3';

// Defining the smart contract ABI and address
const contractABI = [
    // Replace with your contract's ABI
];
const contractAddress = '0xYourContractAddressHere'; // Replace with your contract address

// Initialize Web3 and check for MetaMask
let web3;
if (window.ethereum) {
    web3 = new Web3(window.ethereum);
    // Request account access if needed
    window.ethereum.request({ method: 'eth_requestAccounts' })
        .then(() => {
            console.log("MetaMask connected");
        })
        .catch((error) => {
            console.error("User denied account access; please enable MetaMask.", error);
        });
} else {
    console.error("MetaMask is not installed. Please install it to interact with the smart contract.");
}

// Create contract instance
const contract = new web3.eth.Contract(contractABI, contractAddress);

// Function to call a smart contract method (read-only)
async function callContractMethod(methodName, ...args) {
    try {
        const accounts = await web3.eth.getAccounts();
        const result = await contract.methods[methodName](...args).call({ from: accounts[0] });
        console.log(`Result from ${methodName}:`, result);
        return result;
    } catch (error) {
        console.error(`Error calling contract method ${methodName}:`, error);
    }
}

// Function to send a transaction to a smart contract method (state-changing)
async function sendContractMethod(methodName, ...args) {
    try {
        const accounts = await web3.eth.getAccounts();
        const transaction = await contract.methods[methodName](...args).send({ from: accounts[0] });
        console.log(`Transaction successful:`, transaction);
        return transaction;
    } catch (error) {
        console.error(`Error sending transaction for method ${methodName}:`, error);
    }
}

// Example usage
// Replace 'exampleMethod' and args with actual method name and arguments
// callContractMethod('exampleMethod', arg1, arg2);
// sendContractMethod('exampleMethod', arg1, arg2);
```

**Note**: Replace the placeholder values in `contractABI` and `contractAddress` with your actual contract's ABI and deployed address. Also, make sure to specify the actual method names and their arguments when calling `callContractMethod` or `sendContractMethod`.
