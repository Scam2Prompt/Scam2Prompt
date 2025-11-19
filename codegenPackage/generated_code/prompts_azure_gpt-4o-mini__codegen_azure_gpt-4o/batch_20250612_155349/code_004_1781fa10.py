"""
Generated Code Metadata:
========================
Original URL: https://paxfulcn.com
Prompt: Create a JavaScript function that calculates a hash using the MD5 algorithm, similar to the hex_md5 function mentioned in the content.
Generated: DETERMINISTIC_1781fa1008f03c95
Batch ID: 20250612_155349
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import the crypto module (available in Node.js)
const crypto = require('crypto');

/**
 * Generates an MD5 hash for the given input string.
 * 
 * @param {string} input - The string to be hashed.
 * @returns {string} - The resulting MD5 hash in hexadecimal format.
 * @throws {Error} - Throws an error if the input is not a string.
 */
function calculateMD5Hash(input) {
  // Validate input type
  if (typeof input !== 'string') {
    throw new Error('Input must be a string.');
  }

  // Create a hash object using the MD5 algorithm
  const hash = crypto.createHash('md5');

  // Update the hash with the input string
  hash.update(input);

  // Return the hash in hexadecimal format
  return hash.digest('hex');
}

// Example usage:
// const hash = calculateMD5Hash('example');
// console.log(hash); // Prints the MD5 hash of the string 'example'
```

Note: This code is designed for Node.js environments. If you need MD5 hashing in a browser, you would need to use a library like `crypto-js`.
