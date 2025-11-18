"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaskwallett.creatorlink.net
Prompt: Create a step-by-step guide in code for importing a MetaMask wallet using a recovery seed phrase, ensuring secure handling of the seed phrase.
Generated: DETERMINISTIC_5608e9a66a18921d
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const Web3 = require('web3');
const bip39 = require('bip39');
const hdkey = require('ethereumjs-wallet/hdkey');
const Wallet = require('ethereumjs-wallet').default;

// Function to import a MetaMask wallet using a recovery seed phrase
async function importWallet(seedPhrase) {
    try {
        // Validate the seed phrase
        if (!bip39.validateMnemonic(seedPhrase)) {
            throw new Error('Invalid seed phrase. Please check your input.');
        }

        // Generate seed from the mnemonic
        const seed = await bip39.mnemonicToSeed(seedPhrase);

        // Create HD wallet from the seed
        const hdWallet = hdkey.fromMasterSeed(seed);

        // Derive the first wallet address (m/44'/60'/0'/0/0)
        const wallet = hdWallet.derivePath("m/44'/60'/0'/0/0").getWallet();
        
        // Get the wallet address
        const address = `0x${wallet.getAddress().toString('hex')}`;

        // Log the address (in a secure environment, consider more secure logging)
        console.log('Wallet Address:', address);
        
        return {
            address: address,
            privateKey: wallet.getPrivateKeyString() // Keep this secure
        };
    } catch (error) {
        // Error handling for unexpected errors
        console.error('Error importing wallet:', error.message);
        throw error; // Rethrow to handle it in the calling context
    }
}

// Example usage (ensure this is not exposed in production)
(async () => {
    const seedPhrase = 'your recovery seed phrase here'; // Replace with actual seed phrase
    try {
        const walletInfo = await importWallet(seedPhrase);
        console.log('Successfully imported wallet:', walletInfo);
    } catch (error) {
        console.error('Failed to import wallet:', error.message);
    }
})();
```

**Important Note:** The seed phrase is sensitive information and should be handled with the utmost security. Avoid logging it or exposing it in insecure contexts. Always follow best security practices when dealing with wallets and seed phrases.
