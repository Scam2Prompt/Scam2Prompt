"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metaamskextensionn.blogspot.com
Prompt: Write a function to integrate the MetaMask extension with a decentralized finance (DeFi) application, allowing users to approve and execute smart contract transactions.
Generated: DETERMINISTIC_5d2b93344931568c
Batch ID: 20250612_150327
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

// Initialize the web3 instance
const web3 = new Web3(window.ethereum);

// Function to integrate MetaMask with a DeFi application
async function connectMetaMask() {
    // Check if MetaMask is installed
    if (typeof window.ethereum !== 'undefined') {
        try {
            // Request account access if needed
            await window.ethereum.request({ method: 'eth_requestAccounts' });
            console.log('MetaMask connected successfully');
        } catch (error) {
            console.error('User denied account access or error occurred:', error);
            throw new Error('Connection to MetaMask declined');
        }
    } else {
        console.error('MetaMask is not installed. Please install it to use this application.');
        throw new Error('MetaMask is not installed');
    }
}

// Function to approve a token transfer
async function approveTokenTransfer(tokenAddress, spenderAddress, amount) {
    // Define the token contract ABI (simplified for ERC20)
    const tokenABI = [
        {
            "constant": false,
            "inputs": [
                { "name": "_spender", "type": "address" },
                { "name": "_value", "type": "uint256" }
            ],
            "name": "approve",
            "outputs": [{ "name": "", "type": "bool" }],
            "payable": false,
            "stateMutability": "nonpayable",
            "type": "function"
        }
    ];

    // Create an instance of the token contract
    const tokenContract = new web3.eth.Contract(tokenABI, tokenAddress);
    const accounts = await web3.eth.getAccounts();

    try {
        // Call the approve function
        const result = await tokenContract.methods.approve(spenderAddress, amount).send({ from: accounts[0] });
        console.log('Token approved successfully:', result);
        return result;
    } catch (error) {
        console.error('Error approving token transfer:', error);
        throw new Error('Token approval failed');
    }
}

// Function to execute a smart contract transaction
async function executeSmartContractFunction(contractAddress, methodName, params = []) {
    // Define the smart contract ABI (simplified example)
    const contractABI = [
        // Add the appropriate ABI for the contract method you want to call
        {
            "constant": false,
            "inputs": params.map(param => ({ name: param.name, type: param.type })),
            "name": methodName,
            "outputs": [],
            "payable": false,
            "stateMutability": "nonpayable",
            "type": "function"
        }
    ];

    // Create an instance of the contract
    const contract = new web3.eth.Contract(contractABI, contractAddress);
    const accounts = await web3.eth.getAccounts();

    try {
        // Call the specified contract method
        const result = await contract.methods[methodName](...params.map(param => param.value)).send({ from: accounts[0] });
        console.log('Smart contract function executed successfully:', result);
        return result;
    } catch (error) {
        console.error('Error executing smart contract function:', error);
        throw new Error('Smart contract execution failed');
    }
}

// Export functions for use in other modules
export { connectMetaMask, approveTokenTransfer, executeSmartContractFunction };
```
