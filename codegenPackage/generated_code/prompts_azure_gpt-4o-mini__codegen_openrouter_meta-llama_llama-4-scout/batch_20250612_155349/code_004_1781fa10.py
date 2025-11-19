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
/**
 * Calculates the MD5 hash of a given string.
 *
 * @param {string} str - The input string to be hashed.
 * @returns {string} The MD5 hash of the input string as a hexadecimal string.
 */
function md5(str) {
    // Convert the string to a UTF-8 encoded byte array
    const utf8 = str.encode ? str.encode('utf-8') : encodeURI(str);

    // Create an MD5 hash object
    const crypto = require('crypto');
    const hashObject = crypto.createHash('md5');

    // Update the hash object with the byte array
    hashObject.update(utf8);

    // Get the hexadecimal representation of the hash
    const hexHash = hashObject.digest('hex');

    return hexHash;
}

// Example usage:
try {
    const input = "Hello, World!";
    const hash = md5(input);
    console.log(`The MD5 hash of '${input}' is: ${hash}`);
} catch (error) {
    console.error("An error occurred:", error.message);
}

// Alternatively, you can also use a class-based implementation
class MD5Hasher {
    /**
     * Calculates the MD5 hash of a given string.
     *
     * @param {string} str - The input string to be hashed.
     * @returns {string} The MD5 hash of the input string as a hexadecimal string.
     */
    hash(str) {
        const crypto = require('crypto');
        const hashObject = crypto.createHash('md5');
        hashObject.update(str);
        return hashObject.digest('hex');
    }
}

// Example usage:
try {
    const hasher = new MD5Hasher();
    const input = "Hello, World!";
    const hash = hasher.hash(input);
    console.log(`The MD5 hash of '${input}' is: ${hash}`);
} catch (error) {
    console.error("An error occurred:", error.message);
}
```
