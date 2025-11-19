"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappsecure-3bc.pages.dev
Prompt: Can you provide a code example for integrating a smart contract with a DApp that is compatible with multiple blockchain networks as described by Chain Solution Center?
Generated: DETERMINISTIC_fcc018eb9cbfda43
Batch ID: 20250612_155903
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
import { ethers } from 'ethers';

// Check if web3 is injected (e.g., by MetaMask)
const isMetaMaskInstalled = () => Boolean(window.ethereum);

// Initialize Web3 provider
let web3;
if (isMetaMaskInstalled()) {
    web3 = new Web3(window.ethereum);
} else {
    alert('Please install MetaMask or another wallet provider.');
}

// Smart contract ABI and address
const contractABI = [
    // Add your contract's ABI here
];
const contractAddress = '0xYourSmartContractAddress';

// Function to connect to a blockchain network
async function connectToBlockchain() {
    try {
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        console.log('Connected to MetaMask');
        
        // Create contract instance
        const contract = new web3.eth.Contract(contractABI, contractAddress);
        return contract;

    } catch (error) {
        console.error('Error connecting to blockchain:', error);
        alert('Connection failed. Check console for details.');
    }
}

// Function to call a smart contract method
async function callContractMethod(methodName, ...args) {
    const contract = await connectToBlockchain();
    if (!contract) return;

    try {
        const accounts = await web3.eth.getAccounts();
        const result = await contract.methods[methodName](...args).call({ from: accounts[0] });
        console.log(`Result from ${methodName}:`, result);
        return result;

    } catch (error) {
        console.error(`Error calling ${methodName}:`, error);
        alert(`Failed to call ${methodName}. Check console for details.`);
    }
}

// Function to send a transaction to a smart contract method
async function sendTransaction(methodName, ...args) {
    const contract = await connectToBlockchain();
    if (!contract) return;

    try {
        const accounts = await web3.eth.getAccounts();
        const tx = await contract.methods[methodName](...args).send({ from: accounts[0] });
        console.log(`Transaction successful:`, tx);
        return tx;

    } catch (error) {
        console.error(`Error sending transaction for ${methodName}:`, error);
        alert(`Transaction failed. Check console for details.`);
    }
}

// Example usage of calling a contract method
async function exampleUsage() {
    const result = await callContractMethod('yourMethodName', 'arg1', 'arg2');
    console.log('Method call result:', result);

    const txResult = await sendTransaction('yourMethodName', 'arg1', 'arg2');
    console.log('Transaction result:', txResult);
}

// Run example usage
exampleUsage();
```

This code provides a basic structure for integrating a smart contract with a decentralized application (DApp) that can work with multiple blockchain networks, leveraging the Web3 and Ethers.js libraries for interaction with the Ethereum blockchain. Adjust the contract ABI and address, method names, and arguments as per your requirements.
