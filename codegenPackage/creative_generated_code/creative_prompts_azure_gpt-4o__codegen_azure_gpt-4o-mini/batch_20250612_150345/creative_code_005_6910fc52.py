"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bip32.tools
Prompt: Create a JavaScript application to display and validate BIP32 derivation paths for Bitcoin wallets, including compatibility with BIP44, BIP49, and BIP84, as outlined on https://bip32.tools.
Generated: DETERMINISTIC_6910fc5227891d5e
Batch ID: 20250612_150345
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// bip32-validator.js

/**
 * BIP32 Derivation Path Validator
 * This application validates BIP32 derivation paths for Bitcoin wallets,
 * including compatibility with BIP44, BIP49, and BIP84.
 */

// Function to validate a BIP32 derivation path
function validateBIP32Path(path) {
    const bip32Regex = /^m\/(44'|49'|84')\/\d+'\/\d+'\/\d+'(\/\d+'\/\d+'\/\d+'\/\d+'\/\d+')?$/;

    if (!bip32Regex.test(path)) {
        throw new Error("Invalid BIP32 derivation path format.");
    }

    const parts = path.split('/');
    const purpose = parts[1].replace("'", ""); // Extract purpose
    const coinType = parts[2].replace("'", ""); // Extract coin type

    // Validate purpose and coin type
    if (![44, 49, 84].includes(parseInt(purpose))) {
        throw new Error("Invalid purpose. Allowed values are 44', 49', 84'.");
    }

    if (coinType !== "0") {
        throw new Error("This implementation only supports Bitcoin (coin type: 0).");
    }

    return true; // Return true if validation passes
}

// Example usage of validateBIP32Path
function runValidation() {
    const paths = [
        "m/44'/0'/0'/0",    // BIP44 valid example
        "m/49'/0'/0'/0",    // BIP49 valid example
        "m/84'/0'/0'/0",     // BIP84 valid example
        "m/44'/1'/0'/0",     // Invalid coin type example
        "m/45'/0'/0'/0",     // Invalid purpose example
        "m/44'/0'/0'/x"      // Invalid format example
    ];

    paths.forEach(path => {
        try {
            validateBIP32Path(path);
            console.log(`Path "${path}" is valid.`);
        } catch (error) {
            console.error(`Error validating path "${path}": ${error.message}`);
        }
    });
}

// Execute validation on application start
runValidation();
```
