"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meatsmkluugine.webflow.io
Prompt: What steps should I follow to import an existing MetaMask wallet using a seed phrase after installing the browser extension?
Generated: DETERMINISTIC_882eadebc102f7a8
Batch ID: 20250612_155344
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
import { ethers } from 'ethers';

/**
 * Function to import a MetaMask wallet using a seed phrase
 * @param {string} seedPhrase - The seed phrase of the MetaMask wallet
 * @returns {Promise<void>}
 */
async function importMetaMaskWallet(seedPhrase) {
    try {
        // Validate the seed phrase
        if (!seedPhrase || typeof seedPhrase !== 'string') {
            throw new Error('Invalid seed phrase. Please provide a valid seed phrase.');
        }

        // Create a new instance of ethers
        const wallet = ethers.Wallet.fromMnemonic(seedPhrase);

        // Connect to the Ethereum network (you can use a specific provider if required)
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        const signer = wallet.connect(provider);
        
        // Add the wallet to the provider
        await provider.send("eth_requestAccounts", []); // Request account access if needed

        console.log('Wallet imported successfully.');
        console.log('Wallet Address:', wallet.address);

        // Setup web3 instance for further interactions (if needed)
        const web3 = new Web3(provider);

        // Further actions can be performed using web3 or ethers instances
        // Example: const balance = await web3.eth.getBalance(wallet.address);

    } catch (error) {
        console.error('Error importing wallet:', error.message);
    }
}

// Example usage
// Replace with the actual seed phrase you want to import
const seedPhrase = 'your seed phrase here';
importMetaMaskWallet(seedPhrase);
```

> **Note:** Ensure that you replace `'your seed phrase here'` with the actual seed phrase when using this code in a secure environment.
