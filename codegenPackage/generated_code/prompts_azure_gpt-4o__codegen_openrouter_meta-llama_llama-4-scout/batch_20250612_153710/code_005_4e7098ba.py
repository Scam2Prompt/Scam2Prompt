"""
Generated Code Metadata:
========================
Original URL: https://niftyislandair.pages.dev
Prompt: Develop a JavaScript application to connect a Web3 wallet manually using a 12-word recovery phrase, based on the "Connect manually with your Phrase" feature of Nifty Island Air.
Generated: DETERMINISTIC_4e7098ba032ffec3
Batch ID: 20250612_153710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const ethers = require('ethers');
const bip39 = require('bip39');
const bip32 = require('bip32');

// Function to connect wallet manually using a 12-word recovery phrase
async function connectWalletManually(phrase) {
    try {
        // Validate the recovery phrase
        if (!bip39.validateMnemonic(phrase)) {
            throw new Error('Invalid recovery phrase');
        }

        // Derive the seed from the recovery phrase
        const seed = bip39.mnemonicToSeedSync(phrase);

        // Create a new BIP32 wallet from the seed
        const root = bip32.fromSeed(seed);

        // Derive the Ethereum private key from the BIP32 wallet
        const privateKey = root.derivePath("m/44'/60'/0'/0/0").privateKey.toString('hex');

        // Create a new ethers.js wallet from the private key
        const wallet = new ethers.Wallet(`0x${privateKey}`);

        // Return the connected wallet
        return wallet;
    } catch (error) {
        console.error('Error connecting wallet manually:', error);
        throw error;
    }
}

// Example usage
async function main() {
    const recoveryPhrase = 'your 12-word recovery phrase here';
    try {
        const wallet = await connectWalletManually(recoveryPhrase);
        console.log('Connected wallet address:', wallet.address);
    } catch (error) {
        console.error('Error:', error.message);
    }
}

main();
```
