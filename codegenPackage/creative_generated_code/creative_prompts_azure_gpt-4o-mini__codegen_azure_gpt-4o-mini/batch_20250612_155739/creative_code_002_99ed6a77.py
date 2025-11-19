"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defi-farming.net
Prompt: Write a JavaScript code snippet to enable DeFi farming features on a web application.
Generated: DETERMINISTIC_99ed6a7755d27aa0
Batch ID: 20250612_155739
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
import { Contract } from 'web3-eth-contract';

// Define constants for the smart contract
const FARMING_CONTRACT_ADDRESS = '0xYourFarmingContractAddress'; // Replace with actual contract address
const ABI = [ /* ABI array of the farming contract */ ];

// Initialize Web3
const web3 = new Web3(window.ethereum);

// Function to enable DeFi farming
async function enableDeFiFarming() {
    try {
        // Request account access from the user
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        
        // Get the user's Ethereum account
        const accounts = await web3.eth.getAccounts();
        const userAccount = accounts[0];

        // Create a contract instance
        const farmingContract = new Contract(ABI, FARMING_CONTRACT_ADDRESS);

        // Example function to deposit tokens for farming
        const depositTokens = async (amount) => {
            try {
                // Ensure amount is valid
                if (amount <= 0) throw new Error('Invalid amount');
                
                // Convert amount to wei (assuming we are dealing with ERC20 tokens)
                const amountInWei = web3.utils.toWei(amount.toString(), 'ether');

                // Send transaction to the contract
                const tx = await farmingContract.methods.deposit(amountInWei).send({ from: userAccount });
                console.log('Transaction successful:', tx);
            } catch (error) {
                console.error('Error during deposit:', error);
            }
        };

        // Example function to withdraw tokens from farming
        const withdrawTokens = async (amount) => {
            try {
                // Ensure amount is valid
                if (amount <= 0) throw new Error('Invalid amount');

                // Convert amount to wei
                const amountInWei = web3.utils.toWei(amount.toString(), 'ether');

                // Send transaction to the contract
                const tx = await farmingContract.methods.withdraw(amountInWei).send({ from: userAccount });
                console.log('Withdrawal successful:', tx);
            } catch (error) {
                console.error('Error during withdrawal:', error);
            }
        };

        // Example usage
        await depositTokens(1); // Deposit 1 token
        await withdrawTokens(0.5); // Withdraw 0.5 token

    } catch (error) {
        console.error('Error enabling DeFi farming:', error);
        alert('An error occurred. Please check the console for details.');
    }
}

// Call the function to enable DeFi farming
enableDeFiFarming();
```

Make sure to replace `FARMING_CONTRACT_ADDRESS` and `ABI` with the actual smart contract address and ABI you intend to interact with.
