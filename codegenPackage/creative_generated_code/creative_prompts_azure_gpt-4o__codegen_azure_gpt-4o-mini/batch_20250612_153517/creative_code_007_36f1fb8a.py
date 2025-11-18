"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bridge-satoshivm.pages.dev
Prompt: Write a script to connect a MetaMask wallet and approve spending of tSAVM for bridging operations on the SatoshiVM Testnet.
Generated: DETERMINISTIC_36f1fb8a8899543f
Batch ID: 20250612_153517
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

// Define the contract address and ABI for the tSAVM token
const TSAVM_CONTRACT_ADDRESS = '0xYourTSAVMContractAddress';
const TSAVM_ABI = [
    // Only including necessary ABI elements for approve function
    "function approve(address spender, uint256 amount) external returns (bool)"
];

// Initialize web3 provider
const web3 = new Web3(window.ethereum);

// Function to connect to MetaMask
async function connectMetaMask() {
    if (window.ethereum) {
        try {
            // Request account access
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            const account = accounts[0];
            console.log('Connected account:', account);
            return account;
        } catch (error) {
            console.error('User denied account access or error occurred:', error);
            throw new Error('MetaMask connection failed');
        }
    } else {
        console.error('MetaMask is not installed');
        throw new Error('MetaMask is required');
    }
}

// Function to approve spending of tSAVM tokens
async function approveTSAVM(spenderAddress, amount) {
    try {
        const account = await connectMetaMask();
        
        // Create contract instance
        const tsavmContract = new web3.eth.Contract(TSAVM_ABI, TSAVM_CONTRACT_ADDRESS);
        
        // Estimate gas for the approve transaction
        const gasEstimate = await tsavmContract.methods.approve(spenderAddress, amount).estimateGas({ from: account });
        
        // Send the transaction
        const transaction = await tsavmContract.methods.approve(spenderAddress, amount).send({
            from: account,
            gas: gasEstimate
        });

        console.log('Approval successful:', transaction);
        return transaction;
    } catch (error) {
        console.error('Approval transaction failed:', error);
        throw new Error('Approval failed');
    }
}

// Example usage
(async () => {
    const spenderAddress = '0xYourSpenderAddress'; // Replace with the address that will spend the tokens
    const amount = web3.utils.toWei('100', 'ether'); // Amount of tSAVM to approve (example: 100 tSAVM)

    try {
        const transaction = await approveTSAVM(spenderAddress, amount);
        console.log('Transaction details:', transaction);
    } catch (error) {
        console.error('Error in approval process:', error);
    }
})();
```

Make sure to replace `'0xYourTSAVMContractAddress'` and `'0xYourSpenderAddress'` with the actual contract address and spender address before running the script.
