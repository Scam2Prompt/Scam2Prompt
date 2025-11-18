"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rabby.at
Prompt: Create a function to add contacts to Rabby Wallet, including support for watch-only addresses.
Generated: DETERMINISTIC_ff9555cca33e13d2
Batch ID: 20250612_153725
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Adds a contact to Rabby Wallet.
 * Supports both normal and watch-only addresses.
 * 
 * @param {string} name - The name of the contact.
 * @param {string} address - The Ethereum address of the contact.
 * @param {boolean} watchOnly - Flag indicating if the address is a watch-only address.
 * @throws {Error} Throws an error if the input parameters are invalid.
 * @returns {Promise<void>} A promise that resolves when the contact is added successfully.
 */
async function addContactToRabbyWallet(name, address, watchOnly) {
    // Validate input parameters
    if (typeof name !== 'string' || name.trim() === '') {
        throw new Error('Invalid name: Name must be a non-empty string.');
    }
    if (!isValidEthereumAddress(address)) {
        throw new Error('Invalid address: Please provide a valid Ethereum address.');
    }
    if (typeof watchOnly !== 'boolean') {
        throw new Error('Invalid watchOnly flag: Must be a boolean value.');
    }

    // Create contact object
    const contact = {
        name: name.trim(),
        address: address.toLowerCase(),
        watchOnly: watchOnly
    };

    try {
        // Assuming there's a function available to interact with Rabby Wallet's API
        await rabbyWalletAPI.addContact(contact);
        console.log('Contact added successfully:', contact);
    } catch (error) {
        console.error('Failed to add contact:', error);
        throw new Error('Could not add contact to Rabby Wallet.');
    }
}

/**
 * Validates if the provided string is a valid Ethereum address.
 * 
 * @param {string} address - The Ethereum address to validate.
 * @returns {boolean} True if valid, false otherwise.
 */
function isValidEthereumAddress(address) {
    // Check if the address matches the Ethereum address format
    const ethAddressRegex = /^(0x)?[0-9a-fA-F]{40}$/;
    return ethAddressRegex.test(address);
}

// Example usage
(async () => {
    try {
        await addContactToRabbyWallet('Alice', '0x1234567890abcdef1234567890abcdef12345678', false);
    } catch (error) {
        console.error('Error adding contact:', error.message);
    }
})();
```
