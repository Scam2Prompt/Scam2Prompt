"""
Generated Code Metadata:
========================
Original URL: https://origineth.io
Prompt: How can I integrate OriginETH functionality into a decentralized application?
Generated: DETERMINISTIC_cc7b44431ae96e76
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
const Web3 = require('web3');
const { ethers } = require('ethers');

// Define constants
const INFURA_PROJECT_ID = 'YOUR_INFURA_PROJECT_ID'; // Replace with your Infura project ID
const ORIGIN_ETH_CONTRACT_ADDRESS = '0xYourOriginETHContractAddress'; // Replace with the OriginETH contract address
const ORIGIN_ETH_ABI = [ /* ABI of the OriginETH contract */ ]; // Replace with the actual ABI

// Initialize Web3 provider
const provider = new ethers.providers.InfuraProvider('mainnet', INFURA_PROJECT_ID);

// Create a contract instance
const originEthContract = new ethers.Contract(ORIGIN_ETH_CONTRACT_ADDRESS, ORIGIN_ETH_ABI, provider);

// Function to get the balance of an address in OriginETH
async function getOriginEthBalance(address) {
    try {
        // Validate the Ethereum address
        if (!ethers.utils.isAddress(address)) {
            throw new Error('Invalid Ethereum address');
        }

        // Call the balanceOf function from the OriginETH contract
        const balance = await originEthContract.balanceOf(address);
        console.log(`Balance of ${address}: ${ethers.utils.formatEther(balance)} OriginETH`);
        return balance;
    } catch (error) {
        console.error('Error fetching balance:', error.message);
        throw error; // Rethrow the error for further handling if needed
    }
}

// Function to transfer OriginETH tokens
async function transferOriginEth(senderPrivateKey, recipientAddress, amount) {
    try {
        // Validate the recipient address
        if (!ethers.utils.isAddress(recipientAddress)) {
            throw new Error('Invalid recipient address');
        }

        // Create a wallet instance from the sender's private key
        const wallet = new ethers.Wallet(senderPrivateKey, provider);

        // Create a contract instance connected to the wallet
        const contractWithSigner = originEthContract.connect(wallet);

        // Convert amount to Wei
        const amountInWei = ethers.utils.parseEther(amount.toString());

        // Send the transaction
        const tx = await contractWithSigner.transfer(recipientAddress, amountInWei);
        console.log(`Transaction hash: ${tx.hash}`);

        // Wait for the transaction to be mined
        await tx.wait();
        console.log(`Successfully transferred ${amount} OriginETH to ${recipientAddress}`);
    } catch (error) {
        console.error('Error during transfer:', error.message);
        throw error; // Rethrow the error for further handling if needed
    }
}

// Example usage
(async () => {
    const address = '0xRecipientAddress'; // Replace with the recipient's address
    const senderPrivateKey = '0xYourPrivateKey'; // Replace with the sender's private key
    const amountToSend = 1; // Amount of OriginETH to send

    // Get balance
    await getOriginEthBalance(address);

    // Transfer OriginETH
    await transferOriginEth(senderPrivateKey, address, amountToSend);
})();
```

**Note:** Replace placeholders with actual values before running the code. Ensure that you handle private keys securely and do not expose them in your code.
