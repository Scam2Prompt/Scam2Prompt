"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appkit-laboratory-ibhc82bf8-reown-com.vercel.app
Prompt: Provide a code implementation for a wallet setup without email using the Ethers library as detailed in the AppKit Lab.
Generated: DETERMINISTIC_1b5b1e86835dd1cd
Batch ID: 20250612_155457
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary packages from the ethers library
const { ethers } = require('ethers');

/**
 * Function to create a new Ethereum wallet without using email.
 * This wallet will be generated using a random mnemonic phrase.
 * @returns {Object} - An object containing the wallet address and mnemonic.
 */
async function createWallet() {
    try {
        // Generate a random mnemonic (BIP39 compatible)
        const mnemonic = ethers.Wallet.createRandom().mnemonic.phrase;

        // Create a wallet instance from the mnemonic
        const wallet = ethers.Wallet.fromMnemonic(mnemonic);

        // Return the wallet address and mnemonic for future use
        return {
            address: wallet.address,
            mnemonic: mnemonic
        };
    } catch (error) {
        console.error("Error creating wallet:", error);
        throw new Error("Failed to create wallet. Please try again.");
    }
}

/**
 * Main function to execute the wallet creation and display the information.
 */
async function main() {
    try {
        const walletInfo = await createWallet();
        console.log("Wallet created successfully!");
        console.log(`Address: ${walletInfo.address}`);
        console.log(`Mnemonic: ${walletInfo.mnemonic}`);
    } catch (error) {
        console.error("An error occurred in the main function:", error.message);
    }
}

// Execute the main function
main();
```
