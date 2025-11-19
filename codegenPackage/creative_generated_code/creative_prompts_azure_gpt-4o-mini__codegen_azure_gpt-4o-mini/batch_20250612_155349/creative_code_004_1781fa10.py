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
/**
 * Generates an MD5 hash for the given input string.
 * This implementation uses the Crypto API available in modern browsers and Node.js.
 * 
 * @param {string} input - The input string to hash.
 * @returns {Promise<string>} A promise that resolves to the MD5 hash in hexadecimal format.
 * @throws {Error} Throws an error if the input is not a string.
 */
async function md5Hash(input) {
    // Validate input type
    if (typeof input !== 'string') {
        throw new Error('Input must be a string');
    }

    // Encode the input string as a Uint8Array
    const encoder = new TextEncoder();
    const data = encoder.encode(input);

    // Generate the hash using the SubtleCrypto API
    const hashBuffer = await crypto.subtle.digest('MD5', data);

    // Convert the hash buffer to an array of bytes
    const hashArray = Array.from(new Uint8Array(hashBuffer));

    // Convert the byte array to a hexadecimal string
    const hashHex = hashArray.map(b => ('00' + b.toString(16)).slice(-2)).join('');

    return hashHex;
}

// Example usage
md5Hash("Hello, World!")
    .then(hash => console.log(`MD5 hash: ${hash}`))
    .catch(error => console.error(`Error: ${error.message}`));
```
