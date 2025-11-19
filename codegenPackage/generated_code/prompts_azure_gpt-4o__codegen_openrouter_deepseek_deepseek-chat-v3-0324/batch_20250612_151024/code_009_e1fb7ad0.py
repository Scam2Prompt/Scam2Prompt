"""
Generated Code Metadata:
========================
Original URL: https://ion2.pages.dev
Prompt: Recommend privacy-focused methods for handling Ethereum, Cosmos, BSC, and EVM wallet addresses in a web application designed for claiming blockchain-based prizes.
Generated: DETERMINISTIC_e1fb7ad06d8eb5a3
Batch ID: 20250612_151024
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
const { bech32 } = require('bech32');
const { sha3_256 } = require('js-sha3');

/**
 * Validates an Ethereum or EVM-compatible address
 * @param {string} address - The address to validate
 * @returns {boolean} True if valid, false otherwise
 */
function validateEVMAddress(address) {
    try {
        return ethers.utils.isAddress(address);
    } catch (error) {
        console.error('Error validating EVM address:', error);
        return false;
    }
}

/**
 * Validates a Cosmos (Bech32) address
 * @param {string} address - The address to validate
 * @param {string} [prefix='cosmos'] - Expected Bech32 prefix
 * @returns {boolean} True if valid, false otherwise
 */
function validateCosmosAddress(address, prefix = 'cosmos') {
    try {
        const decoded = bech32.decode(address);
        return decoded.prefix === prefix;
    } catch (error) {
        console.error('Error validating Cosmos address:', error);
        return false;
    }
}

/**
 * Validates a BSC address (same as Ethereum but with different prefix)
 * @param {string} address - The address to validate
 * @returns {boolean} True if valid, false otherwise
 */
function validateBSCAddress(address) {
    return validateEVMAddress(address);
}

/**
 * Hashes an address for privacy before storing
 * @param {string} address - The address to hash
 * @returns {string} The hashed address
 */
function hashAddress(address) {
    try {
        return sha3_256(address.toLowerCase());
    } catch (error) {
        console.error('Error hashing address:', error);
        throw new Error('Failed to hash address');
    }
}

/**
 * Normalizes an EVM address to checksum format
 * @param {string} address - The address to normalize
 * @returns {string} The checksum address
 */
function normalizeEVMAddress(address) {
    try {
        return ethers.utils.getAddress(address);
    } catch (error) {
        console.error('Error normalizing EVM address:', error);
        throw new Error('Invalid EVM address format');
    }
}

/**
 * Normalizes a Cosmos address to lowercase
 * @param {string} address - The address to normalize
 * @returns {string} The normalized address
 */
function normalizeCosmosAddress(address) {
    try {
        return address.toLowerCase();
    } catch (error) {
        console.error('Error normalizing Cosmos address:', error);
        throw new Error('Invalid Cosmos address format');
    }
}

/**
 * Determines the blockchain type from the address
 * @param {string} address - The address to check
 * @returns {string} 'ethereum', 'cosmos', 'bsc', or 'unknown'
 */
function detectBlockchainType(address) {
    try {
        if (validateEVMAddress(address)) {
            return 'ethereum';
        } else if (validateCosmosAddress(address)) {
            return 'cosmos';
        } else if (validateBSCAddress(address)) {
            return 'bsc';
        }
        return 'unknown';
    } catch (error) {
        console.error('Error detecting blockchain type:', error);
        return 'unknown';
    }
}

module.exports = {
    validateEVMAddress,
    validateCosmosAddress,
    validateBSCAddress,
    hashAddress,
    normalizeEVMAddress,
    normalizeCosmosAddress,
    detectBlockchainType
};
```
