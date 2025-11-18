"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meatsmkluugine.webflow.io
Prompt: Create a script that imports an existing MetaMask wallet using a seed phrase and verifies its successful integration into a web application.
Generated: DETERMINISTIC_3d65a4d76e7c9d46
Batch ID: 20250612_145130
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

// Function to import a MetaMask wallet using a seed phrase
async function importWalletFromSeedPhrase(seedPhrase) {
    try {
        // Validate the seed phrase
        if (!ethers.utils.isValidMnemonic(seedPhrase)) {
            throw new Error('Invalid seed phrase.');
        }

        // Create a wallet instance from the seed phrase
        const wallet = ethers.Wallet.fromMnemonic(seedPhrase);

        // Connect to a provider (e.g., Infura, Alchemy, or local Ethereum node)
        const provider = new ethers.providers.InfuraProvider('mainnet', 'YOUR_INFURA_API_KEY');

        // Connect the wallet to the provider
        const connectedWallet = wallet.connect(provider);

        // Check the wallet address
        const address = connectedWallet.address;

        // Log the successful integration
        console.log(`Wallet imported successfully. Address: ${address}`);

        // Return the connected wallet for further use
        return connectedWallet;
    } catch (error) {
        // Handle errors and log meaningful messages
        console.error('Error importing wallet:', error.message);
        throw error; // Re-throw the error for further handling if necessary
    }
}

// Example usage
(async () => {
    const seedPhrase = 'your seed phrase here'; // Replace with your actual seed phrase
    
    try {
        const wallet = await importWalletFromSeedPhrase(seedPhrase);
        // Now you can use the wallet instance for transactions or to check balances
    } catch (error) {
        // Handle any errors that occurred during wallet import
        console.error('Failed to import wallet:', error);
    }
})();
```

**Note:** Replace `'YOUR_INFURA_API_KEY'` with your actual Infura API key and ensure to never expose private keys or sensitive information in your code.
