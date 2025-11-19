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
const prompt = require('prompt-sync')();

/**
 * Connects to a Web3 wallet using a 12-word recovery phrase.
 * @returns {Promise<ethers.Wallet>} The connected wallet instance.
 */
async function connectWithRecoveryPhrase() {
    try {
        // Prompt user for the 12-word recovery phrase
        console.log('Please enter your 12-word recovery phrase (separated by spaces):');
        const phrase = prompt({ echo: '*' }); // Hide input for security

        if (!phrase) {
            throw new Error('Recovery phrase cannot be empty.');
        }

        // Split the phrase into words and validate length
        const words = phrase.trim().split(/\s+/);
        if (words.length !== 12) {
            throw new Error('Recovery phrase must be exactly 12 words.');
        }

        // Create wallet from mnemonic
        const wallet = ethers.Wallet.fromMnemonic(phrase);

        console.log('Wallet connected successfully!');
        console.log('Address:', wallet.address);

        return wallet;
    } catch (error) {
        console.error('Error connecting wallet:', error.message);
        throw error;
    }
}

// Example usage
(async () => {
    try {
        const wallet = await connectWithRecoveryPhrase();
        // Additional operations with the wallet can be performed here
    } catch (error) {
        console.error('Failed to connect wallet:', error.message);
    }
})();
```
