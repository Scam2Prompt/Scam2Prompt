"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shibonkgo.web.app
Prompt: Provide an example of a whitelist management system using JavaScript, inspired by the Shibonk Gang web app.
Generated: DETERMINISTIC_0c54b72ad4db316a
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

class WhitelistManager {
    constructor() {
        this.whitelist = new Set(); // Using Set to store unique entries
    }

    /**
     * Adds an address to the whitelist.
     * @param {string} address - The address to be added.
     * @throws Will throw an error if the address is not valid.
     */
    addAddress(address) {
        this.validateAddress(address);
        this.whitelist.add(address);
        console.log(`Address ${address} added to the whitelist.`);
    }

    /**
     * Removes an address from the whitelist.
     * @param {string} address - The address to be removed.
     * @throws Will throw an error if the address is not in the whitelist.
     */
    removeAddress(address) {
        this.validateAddress(address);
        if (!this.whitelist.has(address)) {
            throw new Error(`Address ${address} is not in the whitelist.`);
        }
        this.whitelist.delete(address);
        console.log(`Address ${address} removed from the whitelist.`);
    }

    /**
     * Checks if an address is in the whitelist.
     * @param {string} address - The address to check.
     * @returns {boolean} - True if the address is in the whitelist, false otherwise.
     */
    isAddressWhitelisted(address) {
        this.validateAddress(address);
        return this.whitelist.has(address);
    }

    /**
     * Validates the format of the address.
     * @param {string} address - The address to validate.
     * @throws Will throw an error if the address is invalid.
     */
    validateAddress(address) {
        const addressRegex = /^[0-9a-fA-F]{40}$/; // Example regex for Ethereum addresses
        if (!addressRegex.test(address)) {
            throw new Error(`Invalid address format: ${address}`);
        }
    }

    /**
     * Retrieves all whitelisted addresses.
     * @returns {Array} - An array of whitelisted addresses.
     */
    getWhitelistedAddresses() {
        return Array.from(this.whitelist);
    }
}

// Example usage of the WhitelistManager
try {
    const wm = new WhitelistManager();
    wm.addAddress('0x1234567890abcdef1234567890abcdef12345678');
    console.log(wm.isAddressWhitelisted('0x1234567890abcdef1234567890abcdef12345678')); // true
    wm.removeAddress('0x1234567890abcdef1234567890abcdef12345678');
    console.log(wm.getWhitelistedAddresses()); // []
} catch (error) {
    console.error(error.message);
}
```
