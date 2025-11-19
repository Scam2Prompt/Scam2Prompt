"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaskafree.blogspot.com
Prompt: What are the best practices for integrating MetaMask with Ethereum smart contracts?
Generated: DETERMINISTIC_2461eadbc62cd60d
Batch ID: 20250612_161617
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

// Function to initialize Web3 and connect to MetaMask
async function initWeb3() {
    // Check if MetaMask is installed
    if (window.ethereum) {
        // Create a new instance of Web3 using MetaMask's provider
        const web3 = new Web3(window.ethereum);
        
        try {
            // Request account access from the user
            await window.ethereum.request({ method: 'eth_requestAccounts' });
            console.log('MetaMask connected');
            return web3;
        } catch (error) {
            console.error('User denied account access to MetaMask', error);
            throw new Error('Account access denied');
        }
    } else {
        console.error('MetaMask is not installed. Please install it to use this feature.');
        throw new Error('MetaMask not installed');
    }
}

// Function to interact with a smart contract
async function interactWithContract(web3, contractAddress, abi, methodName, params) {
    // Create a contract instance
    const contract = new web3.eth.Contract(abi, contractAddress);
    
    // Get the accounts
    const accounts = await web3.eth.getAccounts();

    try {
        // Call the specified method on the contract
        const result = await contract.methods[methodName](...params).send({ from: accounts[0] });
        console.log('Transaction successful:', result);
        return result;
    } catch (error) {
        console.error('Error interacting with the contract:', error);
        throw new Error('Contract interaction failed');
    }
}

// Example usage (to be called when you want to connect and interact)
(async () => {
    const contractAddress = '0xYourSmartContractAddress';
    const abi = [ /* Your contract ABI */ ];
    
    try {
        const web3 = await initWeb3();
        const result = await interactWithContract(web3, contractAddress, abi, 'yourMethodName', ['param1', 'param2']);
        console.log('Result from contract:', result);
    } catch (error) {
        console.error('An error occurred:', error);
    }
})();
```
