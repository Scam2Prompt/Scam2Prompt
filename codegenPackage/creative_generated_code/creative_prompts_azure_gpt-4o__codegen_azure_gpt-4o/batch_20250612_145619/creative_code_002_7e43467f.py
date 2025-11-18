"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethphb.com
Prompt: Generate code to enable JavaScript-based interaction with an Ethereum pledge platform, ensuring proper wallet integration and transaction validation.
Generated: DETERMINISTIC_7e43467fdc127920
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
import Web3 from 'web3'; // Web3.js library
import detectEthereumProvider from '@metamask/detect-provider'; // Detect Ethereum provider

// Initialize Web3 instance
async function initializeWeb3() {
    const provider = await detectEthereumProvider();
    if (provider) {
        return new Web3(provider); // Return Web3 instance using the detected provider
    } else {
        throw new Error('Ethereum provider not found. Please install MetaMask.');
    }
}

// Connect to user's wallet
async function connectWallet() {
    const web3 = await initializeWeb3();
    try {
        // Request access to wallet
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        return accounts[0]; // Return the user's first wallet address
    } catch (error) {
        console.error('Wallet connection error:', error);
        throw new Error('Error connecting to wallet. Please try again.');
    }
}

// Send pledge transaction
async function sendPledgeTransaction(contractAddress, pledgeAmount, userAccount) {
    const web3 = await initializeWeb3();

    try {
        // Validate input values
        if (!web3.utils.isAddress(contractAddress)) {
            throw new Error('Invalid contract address.');
        }
        if (!web3.utils.isAddress(userAccount)) {
            throw new Error('Invalid user account.');
        }
        if (!pledgeAmount || isNaN(pledgeAmount)) {
            throw new Error('Invalid pledge amount.');
        }

        // Convert pledge amount into Wei (smallest denomination of Ether)
        const pledgeAmountInWei = web3.utils.toWei(pledgeAmount.toString(), 'ether');

        // Send transaction to the Ethereum pledge platform
        const transactionHash = await web3.eth.sendTransaction({
            from: userAccount,
            to: contractAddress,
            value: pledgeAmountInWei,
        });

        console.log('Transaction sent successfully. Hash:', transactionHash.transactionHash);
        return transactionHash.transactionHash; // Return transaction hash
    } catch (error) {
        console.error('Transaction error:', error);
        throw new Error('Error sending pledge transaction. Please try again.');
    }
}

// Example usage
async function main() {
    try {
        // Connect to wallet
        const userAccount = await connectWallet();
        console.log('Connected wallet:', userAccount);

        // Define contract address and pledge amount
        const contractAddress = '0xYourContractAddressHere'; // Replace with actual contract address
        const pledgeAmount = 0.1; // Example pledge amount in Ether

        // Send pledge transaction
        const transactionHash = await sendPledgeTransaction(contractAddress, pledgeAmount, userAccount);
        console.log('Transaction completed. Hash:', transactionHash);
    } catch (error) {
        console.error('Error:', error.message);
    }
}

// Run the script
main();
```
