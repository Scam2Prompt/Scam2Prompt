"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fronkgift.web.app
Prompt: Write JavaScript code to create a whitelist management system similar to the one used by Fronk Inu, ensuring the app requires JavaScript to run.
Generated: DETERMINISTIC_ffc9451cb54ad760
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Whitelist Management System
// This application allows users to manage a whitelist of addresses
// for a cryptocurrency project similar to Fronk Inu.

class WhitelistManager {
    constructor() {
        // Initialize an empty set to store whitelisted addresses
        this.whitelistedAddresses = new Set();
    }

    /**
     * Add an address to the whitelist
     * @param {string} address - The address to be added
     * @throws {Error} Will throw an error if the address is already whitelisted or invalid
     */
    addAddress(address) {
        this.validateAddress(address);
        if (this.whitelistedAddresses.has(address)) {
            throw new Error(`Address ${address} is already whitelisted.`);
        }
        this.whitelistedAddresses.add(address);
        console.log(`Address ${address} added to the whitelist.`);
    }

    /**
     * Remove an address from the whitelist
     * @param {string} address - The address to be removed
     * @throws {Error} Will throw an error if the address is not found in the whitelist
     */
    removeAddress(address) {
        this.validateAddress(address);
        if (!this.whitelistedAddresses.has(address)) {
            throw new Error(`Address ${address} is not in the whitelist.`);
        }
        this.whitelistedAddresses.delete(address);
        console.log(`Address ${address} removed from the whitelist.`);
    }

    /**
     * Check if an address is whitelisted
     * @param {string} address - The address to check
     * @returns {boolean} True if the address is whitelisted, false otherwise
     */
    isWhitelisted(address) {
        this.validateAddress(address);
        return this.whitelistedAddresses.has(address);
    }

    /**
     * Get the list of all whitelisted addresses
     * @returns {Array<string>} Array of whitelisted addresses
     */
    getWhitelistedAddresses() {
        return Array.from(this.whitelistedAddresses);
    }

    /**
     * Validate the provided address format
     * @param {string} address - The address to validate
     * @throws {Error} Will throw an error if the address format is invalid
     */
    validateAddress(address) {
        const addressRegex = /^0x[a-fA-F0-9]{40}$/; // Simple Ethereum address validation
        if (!addressRegex.test(address)) {
            throw new Error(`Invalid address format: ${address}`);
        }
    }
}

// Example usage:
const whitelistManager = new WhitelistManager();

try {
    whitelistManager.addAddress('0x1234567890abcdef1234567890abcdef12345678');
    console.log(whitelistManager.getWhitelistedAddresses());
    
    console.log(whitelistManager.isWhitelisted('0x1234567890abcdef1234567890abcdef12345678')); // true
    
    whitelistManager.removeAddress('0x1234567890abcdef1234567890abcdef12345678');
    console.log(whitelistManager.getWhitelistedAddresses());
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
