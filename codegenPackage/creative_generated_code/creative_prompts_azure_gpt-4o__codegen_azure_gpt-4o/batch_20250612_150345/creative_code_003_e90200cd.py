"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bip32.tools
Prompt: Write a script in Node.js to generate deterministic keys using BIP85 entropy derived from a BIP32 keychain, as explained on https://bip32.tools.
Generated: DETERMINISTIC_e90200cd82d3f9e9
Batch ID: 20250612_150345
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
const bip32 = require('bip32'); // Library for BIP32 key derivation
const bip39 = require('bip39'); // Library for BIP39 mnemonic handling
const crypto = require('crypto'); // Node.js built-in library for cryptographic functions

/**
 * Function to generate deterministic keys using BIP85 entropy derived from a BIP32 keychain.
 * 
 * @param {string} mnemonic - The BIP39 mnemonic phrase to derive the master key.
 * @param {number} index - The derivation index for generating the BIP85 entropy.
 * @param {number} entropyBytes - The number of entropy bytes to generate (e.g., 16, 32).
 * @returns {string} Deterministic key derived from the BIP85 entropy.
 */
function generateBIP85Key(mnemonic, index, entropyBytes) {
    try {
        // Validate the input mnemonic
        if (!bip39.validateMnemonic(mnemonic)) {
            throw new Error('Invalid mnemonic provided.');
        }

        // Convert the mnemonic to a BIP39 seed
        const seed = bip39.mnemonicToSeedSync(mnemonic);

        // Derive the master node from the seed
        const masterNode = bip32.fromSeed(seed);

        // Generate the BIP85 entropy path (e.g., m/83696968'/39'/0'/index)
        const bip85Path = `m/83696968'/39'/0'/${index}`;
        const derivedNode = masterNode.derivePath(bip85Path);

        // Generate entropy from the derived node's private key
        const privateKey = derivedNode.privateKey;

        if (!privateKey) {
            throw new Error('Failed to derive a private key. Ensure the provided mnemonic is valid.');
        }

        // Use HMAC-SHA512 to generate deterministic entropy
        const hmac = crypto.createHmac('sha512', Buffer.from('bip-entropy'));
        hmac.update(privateKey);
        const entropy = hmac.digest();

        // Return the required number of entropy bytes as a hex string
        return entropy.slice(0, entropyBytes).toString('hex');
    } catch (error) {
        console.error('Error generating BIP85 key:', error.message);
        throw error; // Propagate the error for the caller to handle
    }
}

// Example usage
try {
    const mnemonic = 'praise you muffin lion enable neck grocery crumble super myself license ghost'; // Example mnemonic
    const keyIndex = 0; // The index for the derived key
    const entropySize = 16; // Size of entropy in bytes (e.g., 16 bytes = 128 bits)

    const deterministicKey = generateBIP85Key(mnemonic, keyIndex, entropySize);
    console.log('Generated deterministic key:', deterministicKey);
} catch (error) {
    console.error('Failed to generate deterministic key:', error.message);
}

// Note: Replace the example mnemonic with a securely generated mnemonic for production use.
```

### Dependencies
To run this script, ensure you install the required packages:
```bash
npm install bip32 bip39
```

Save the script in a `.js` file and execute it using Node.js. Replace the example mnemonic with your securely generated mnemonic phrase.
