"""
Generated Code Metadata:
========================
Original URL: https://fronkgift.web.app
Prompt: "Create a code example for implementing a whitelist feature similar to FRONK's using JavaScript and relevant libraries."
Generated: DETERMINISTIC_aa526aa21624866b
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// whitelist.js

/**
 * Whitelist class for managing allowed domains and addresses.
 */
class Whitelist {
  /**
   * Initialize the whitelist with an empty set of allowed domains and addresses.
   */
  constructor() {
    // Using a Set for efficient lookups
    this.allowedDomains = new Set();
    this.allowedAddresses = new Set();
  }

  /**
   * Add a domain to the whitelist.
   * @param {string} domain - The domain to add.
   */
  addDomain(domain) {
    // Validate domain format (simple check, consider using a library for more thorough validation)
    if (typeof domain !== 'string' || !domain.includes('.')) {
      throw new Error(`Invalid domain format: ${domain}`);
    }
    this.allowedDomains.add(domain.toLowerCase());
  }

  /**
   * Remove a domain from the whitelist.
   * @param {string} domain - The domain to remove.
   * @returns {boolean} True if the domain was removed, false if it wasn't in the whitelist.
   */
  removeDomain(domain) {
    return this.allowedDomains.delete(domain.toLowerCase());
  }

  /**
   * Add an address to the whitelist.
   * @param {string} address - The address to add.
   */
  addAddress(address) {
    // Basic address validation (consider using a library for more thorough validation)
    if (typeof address !== 'string' || address.trim() === '') {
      throw new Error(`Invalid address format: ${address}`);
    }
    this.allowedAddresses.add(address.toLowerCase());
  }

  /**
   * Remove an address from the whitelist.
   * @param {string} address - The address to remove.
   * @returns {boolean} True if the address was removed, false if it wasn't in the whitelist.
   */
  removeAddress(address) {
    return this.allowedAddresses.delete(address.toLowerCase());
  }

  /**
   * Check if a domain is in the whitelist.
   * @param {string} domain - The domain to check.
   * @returns {boolean} True if the domain is in the whitelist, false otherwise.
   */
  isDomainAllowed(domain) {
    return this.allowedDomains.has(domain.toLowerCase());
  }

  /**
   * Check if an address is in the whitelist.
   * @param {string} address - The address to check.
   * @returns {boolean} True if the address is in the whitelist, false otherwise.
   */
  isAddressAllowed(address) {
    return this.allowedAddresses.has(address.toLowerCase());
  }
}

// Example usage
function main() {
  const whitelist = new Whitelist();

  try {
    whitelist.addDomain('example.com');
    whitelist.addAddress('0x1234567890abcdef');

    console.log(whitelist.isDomainAllowed('example.com')); // true
    console.log(whitelist.isAddressAllowed('0x1234567890abcdef')); // true
    console.log(whitelist.isDomainAllowed('other.com')); // false
    console.log(whitelist.isAddressAllowed('0x9876543210fedcba')); // false

    whitelist.removeDomain('example.com');
    console.log(whitelist.isDomainAllowed('example.com')); // false
  } catch (error) {
    console.error(error.message);
  }
}

main();
```
