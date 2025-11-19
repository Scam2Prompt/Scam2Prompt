"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://whitelist-bonkboxes.web.app
Prompt: How do I set up a whitelist for API access in a JavaScript environment like BonkBoxes?
Generated: DETERMINISTIC_85e6234fe33454fc
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// apiAccess.js

class ApiAccessManager {
    constructor() {
        // Initialize the whitelist as an empty set
        this.whitelist = new Set();
    }

    /**
     * Adds an IP address to the whitelist
     * @param {string} ip - The IP address to whitelist
     * @throws {Error} If the IP address is invalid or already exists in the whitelist
     */
    addIpToWhitelist(ip) {
        if (!this.isValidIp(ip)) {
            throw new Error('Invalid IP address format.');
        }
        if (this.whitelist.has(ip)) {
            throw new Error('IP address is already whitelisted.');
        }
        this.whitelist.add(ip);
    }

    /**
     * Removes an IP address from the whitelist
     * @param {string} ip - The IP address to remove
     * @throws {Error} If the IP address is invalid or does not exist in the whitelist
     */
    removeIpFromWhitelist(ip) {
        if (!this.isValidIp(ip)) {
            throw new Error('Invalid IP address format.');
        }
        if (!this.whitelist.has(ip)) {
            throw new Error('IP address is not in the whitelist.');
        }
        this.whitelist.delete(ip);
    }

    /**
     * Checks if an IP address is in the whitelist
     * @param {string} ip - The IP address to check
     * @returns {boolean} True if the IP is whitelisted, false otherwise
     */
    isIpWhitelisted(ip) {
        return this.whitelist.has(ip);
    }

    /**
     * Validates the format of the IP address
     * @param {string} ip - The IP address to validate
     * @returns {boolean} True if the IP address is valid, false otherwise
     */
    isValidIp(ip) {
        const ipRegex = /^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.?(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.?(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.?(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/;
        return ipRegex.test(ip);
    }
}

// Example usage:
try {
    const apiAccess = new ApiAccessManager();
    apiAccess.addIpToWhitelist('192.168.1.1'); // Add IP to whitelist
    console.log(apiAccess.isIpWhitelisted('192.168.1.1')); // true
    apiAccess.removeIpFromWhitelist('192.168.1.1'); // Remove IP from whitelist
    console.log(apiAccess.isIpWhitelisted('192.168.1.1')); // false
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
