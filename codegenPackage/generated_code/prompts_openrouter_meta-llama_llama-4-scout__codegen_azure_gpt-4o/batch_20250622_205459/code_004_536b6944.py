"""
Generated Code Metadata:
========================
Original URL: https://pepe2024.space
Prompt: Develop a JavaScript function to validate and format cryptocurrency addresses, specifically for the Pepe 2024 contract address.
Generated: DETERMINISTIC_536b6944cbf9da79
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates and formats a cryptocurrency address for the Pepe 2024 contract.
 * 
 * Pepe 2024 contract addresses are Ethereum-based and must:
 * - Be a valid hexadecimal string.
 * - Start with "0x".
 * - Be exactly 42 characters long (including "0x").
 * 
 * @param {string} address - The cryptocurrency address to validate and format.
 * @returns {string} - The formatted address if valid.
 * @throws {Error} - Throws an error if the address is invalid.
 */
function validateAndFormatPepe2024Address(address) {
    // Ensure the input is a string
    if (typeof address !== 'string') {
        throw new Error('Invalid input: Address must be a string.');
    }

    // Trim any whitespace from the address
    const trimmedAddress = address.trim();

    // Check if the address starts with "0x"
    if (!trimmedAddress.startsWith('0x')) {
        throw new Error('Invalid address: Must start with "0x".');
    }

    // Check if the address is exactly 42 characters long
    if (trimmedAddress.length !== 42) {
        throw new Error('Invalid address: Must be exactly 42 characters long.');
    }

    // Check if the address is a valid hexadecimal string
    const hexPattern = /^0x[a-fA-F0-9]{40}$/;
    if (!hexPattern.test(trimmedAddress)) {
        throw new Error('Invalid address: Must be a valid hexadecimal string.');
    }

    // Return the formatted address (lowercase for consistency)
    return trimmedAddress.toLowerCase();
}

// Example usage:
try {
    const validAddress = validateAndFormatPepe2024Address('0xAbC1234567890Def1234567890ABC1234567890D');
    console.log('Valid Address:', validAddress);
} catch (error) {
    console.error('Error:', error.message);
}
```
