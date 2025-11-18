"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.gnosis-safe.io
Prompt: Write a code snippet using the Safe{CORE} SDK to integrate a modular Smart Account with ERC-4337 functionality into a decentralized application (dApp).
Generated: DETERMINISTIC_ea29f0e9257e20cc
Batch ID: 20250612_151232
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules from the Safe{CORE} SDK
import { SafeFactory, SafeAccountConfig } from '@safe-global/safe-core-sdk';
import { ethers } from 'ethers';

// Initialize Ethereum provider (MetaMask or other wallet)
const provider = new ethers.providers.Web3Provider(window.ethereum);

// Define the Smart Account configuration
const safeAccountConfig: SafeAccountConfig = {
    owners: ['0xYourEthereumAddress1', '0xYourEthereumAddress2'], // List of owners
    threshold: 2, // Number of required confirmations for transactions
};

// Function to create a new Smart Account
async function createSmartAccount() {
    try {
        // Request account access if needed
        await provider.send("eth_requestAccounts", []);

        // Create a SafeFactory instance
        const safeFactory = await SafeFactory.create({ ethAdapter: new EthersAdapter({ ethers, signer: provider.getSigner() }) });

        // Create a new Smart Account
        const safeSdk = await safeFactory.deploySafe(safeAccountConfig);
        console.log(`New Smart Account created at: ${safeSdk.getAddress()}`);
        
        return safeSdk;
    } catch (error) {
        console.error("Failed to create Smart Account:", error);
    }
}

// Function to integrate ERC-4337 functionality
async function integrateERC4337(safeSdk) {
    try {
        // Implement ERC-4337 integration logic here
        // Example: prepare a transaction
        const transaction = {
            to: '0xRecipientAddress',
            value: ethers.utils.parseEther('0.01'), // Amount to send
            data: '0x', // Add data if required
        };

        const txResponse = await safeSdk.getTransactionManager().createTransaction(transaction);
        console.log("Transaction prepared:", txResponse);

        // Optionally, execute the transaction
        const txHash = await safeSdk.executeTransaction(txResponse);
        console.log(`Transaction executed successfully. Hash: ${txHash}`);
    } catch (error) {
        console.error("Failed to integrate ERC-4337 functionality:", error);
    }
}

// Main function to run the dApp
(async () => {
    const safeSdk = await createSmartAccount();
    if (safeSdk) {
        await integrateERC4337(safeSdk);
    }
})();
```

**Note:** Remember to replace placeholder addresses with actual Ethereum addresses and ensure the necessary dependencies (`@safe-global/safe-core-sdk`, `ethers`) are installed before running the code. This code provides a basic structure and should be tailored to fit the specific use case of your decentralized application.
