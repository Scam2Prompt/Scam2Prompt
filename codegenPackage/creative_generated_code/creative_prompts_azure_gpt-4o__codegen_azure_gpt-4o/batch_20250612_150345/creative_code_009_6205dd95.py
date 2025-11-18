"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bip32.tools
Prompt: Implement a JavaScript function to convert a BIP39 mnemonic phrase into a BIP85 subkey and display its details, as described on https://bip32.tools.
Generated: DETERMINISTIC_6205dd9570b8aff0
Batch ID: 20250612_150345
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
// Install dependencies with npm: bip39, bip85
const bip39 = require('bip39'); // Used for mnemonic phrase validation
const bip85 = require('bip85'); // Used for BIP85 subkey derivation

/**
 * Function to convert a BIP39 mnemonic phrase into a BIP85 subkey and display its details.
 * @param {string} mnemonic - The BIP39 mnemonic phrase.
 * @param {number} index - The index for the BIP85 derivation path.
 * @returns {object} - Returns an object containing the subkey and its details.
 */
function generateBIP85Subkey(mnemonic, index) {
  try {
    // Validate the mnemonic phrase
    if (!bip39.validateMnemonic(mnemonic)) {
      throw new Error('Invalid BIP39 mnemonic phrase.');
    }

    // Generate seed from the mnemonic using BIP39
    const seed = bip39.mnemonicToSeedSync(mnemonic);

    // Initialize the BIP85 library with the seed
    const bip85Instance = new bip85.BIP85(seed);

    // Derive the subkey using BIP85 at the specified index
    const subkey = bip85Instance.deriveBIP39(12, index); // Example: 12-word mnemonic subkey

    // Return subkey details
    return {
      mnemonic: subkey.mnemonic,
      index: index,
    };
  } catch (error) {
    // Handle errors and display meaningful messages
    console.error('Error generating BIP85 subkey:', error.message);
    return null;
  }
}

// Example usage
const mnemonicPhrase =
  'abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about'; // Replace with your own mnemonic
const derivationIndex = 0; // Replace with desired index

const result = generateBIP85Subkey(mnemonicPhrase, derivationIndex);
if (result) {
  console.log('BIP85 Subkey Details:', result);
} else {
  console.log('Failed to generate subkey.');
}

// Export the function (optional, for module usage)
module.exports = generateBIP85Subkey;
```
