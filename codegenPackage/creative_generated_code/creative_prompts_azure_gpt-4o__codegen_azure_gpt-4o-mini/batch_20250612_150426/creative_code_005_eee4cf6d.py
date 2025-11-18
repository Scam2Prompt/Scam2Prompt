"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chain-list.org
Prompt: Create a JavaScript function that uses ChainList data to validate if a given ChainID corresponds to a supported EVM network, such as ThaiChain 2.0 (ChainID 17).
Generated: DETERMINISTIC_eee4cf6d0089b443
Batch ID: 20250612_150426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * A function to validate if a given ChainID corresponds to a supported EVM network.
 * 
 * @param {number} chainId - The ChainID to validate.
 * @returns {boolean} - Returns true if the ChainID is supported, otherwise false.
 * @throws {TypeError} - Throws an error if the provided chainId is not a number.
 */

// List of supported EVM networks with their ChainIDs
const supportedChains = {
    "ThaiChain 2.0": 17,
    "Ethereum": 1,
    "Binance Smart Chain": 56,
    "Polygon": 137,
    "Avalanche": 43114,
    "Fantom": 250,
    "Arbitrum": 42161,
    // Add more supported chains if needed
};

/**
 * Validates if the provided ChainID is supported.
 * 
 * @param {number} chainId - The ChainID to validate.
 * @returns {boolean} - True if the ChainID is supported, false otherwise.
 */
function isValidChainId(chainId) {
    // Check if chainId is a number
    if (typeof chainId !== 'number') {
        throw new TypeError('The chainId must be a number.');
    }

    // Check if the ChainID exists in the supportedChains object
    return Object.values(supportedChains).includes(chainId);
}

// Example usage:
try {
    const chainIdToValidate = 17; // Example ChainID
    const isSupported = isValidChainId(chainIdToValidate);
    console.log(`ChainID ${chainIdToValidate} is ${isSupported ? 'supported' : 'not supported'}.`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
