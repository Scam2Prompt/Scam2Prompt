"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metaamaskwallet.github.io
Prompt: Create a step-by-step guide in code to set up multiple MetaMask wallet accounts programmatically, ensuring each account has distinct public and private keys tied to the same seed phrase.
Generated: DETERMINISTIC_23bdb72bcf726997
Batch ID: 20250612_151355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const { ethers } = require("ethers");

/**
 * Function to generate multiple MetaMask wallet accounts using a seed phrase
 * @param {string} seedPhrase - The seed phrase used to derive wallet accounts
 * @param {number} accountCount - The number of accounts to generate
 * @returns {Array} - An array of wallet objects containing addresses and private keys
 * @throws Will throw an error if the seed phrase is invalid or if account count is less than 1
 */
function generateWalletAccounts(seedPhrase, accountCount) {
    // Validate inputs
    if (!seedPhrase || typeof seedPhrase !== 'string') {
        throw new Error('Invalid seed phrase provided. It must be a non-empty string.');
    }
    
    if (accountCount < 1 || !Number.isInteger(accountCount)) {
        throw new Error('Account count must be a positive integer.');
    }

    // Create a wallet from the seed phrase
    const mnemonic = ethers.utils.HDNode.fromMnemonic(seedPhrase);
    const wallets = [];

    // Generate accounts using the seed phrase
    for (let i = 0; i < accountCount; i++) {
        // Derive a new wallet for each account
        const wallet = mnemonic.derivePath(`m/44'/60'/0'/0/${i}`);
        
        // Store wallet information
        wallets.push({
            address: wallet.address,
            privateKey: wallet.privateKey
        });
    }

    return wallets;
}

// Example usage
try {
    const seedPhrase = "test test test test test test test test test test test test"; // Replace with your actual seed phrase
    const accounts = generateWalletAccounts(seedPhrase, 5); // Generate 5 accounts

    // Log the generated wallets
    accounts.forEach((account, index) => {
        console.log(`Account ${index + 1}:`);
        console.log(`Address: ${account.address}`);
        console.log(`Private Key: ${account.privateKey}`);
        console.log('-------------------');
    });
} catch (error) {
    console.error('Error generating wallet accounts:', error.message);
}
```

**Note:** Ensure that you install the `ethers` library by running `npm install ethers` before executing this code.
