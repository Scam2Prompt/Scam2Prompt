"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paxfulcn.com
Prompt: Create a JavaScript function that calculates a hash using the MD5 algorithm, similar to the hex_md5 function mentioned in the content.
Generated: DETERMINISTIC_1781fa1008f03c95
Batch ID: 20250612_155349
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the crypto module for hashing
const crypto = require('crypto');

/**
 * Generates an MD5 hash from the input string.
 * 
 * @param {string} input - The string to hash.
 * @returns {string} - The resulting MD5 hash in hexadecimal format.
 * @throws {Error} - Throws an error if the input is not a string or is empty.
 */
function calculateMD5Hash(input) {
    // Validate the input
    if (typeof input !== 'string' || input.trim() === '') {
        throw new Error('Input must be a non-empty string.');
    }

    // Create an MD5 hash using the crypto module
    const hash = crypto.createHash('md5');
    hash.update(input);

    // Return the hash in hexadecimal format
    return hash.digest('hex');
}

// Example Usage:
// Uncomment the lines below to test the function
// try {
//     const result = calculateMD5Hash('Hello World');
//     console.log('MD5 Hash:', result); // Expected: fc3ff98e8c6a0d3087d515c0473f8677
// } catch (error) {
//     console.error('Error:', error.message);
// }

module.exports = calculateMD5Hash; // Export the function for use in other files
```
