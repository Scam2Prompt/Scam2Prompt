"""
Generated Code Metadata:
========================
Original URL: https://polkadots.work
Prompt: "Generate a JavaScript function to URL encode and decode strings using tools similar to those found on コピーツールラボ."
Generated: DETERMINISTIC_4ace32fa2c56c9ae
Batch ID: 20250622_204709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * URL encodes a string, handling special characters and spaces.
 * @param {string} str - The string to be encoded.
 * @returns {string} The URL encoded string.
 * @throws {Error} If the input is not a string.
 */
function urlEncode(str) {
    if (typeof str !== 'string') {
        throw new Error('Input must be a string');
    }
    return encodeURIComponent(str).replace(/[!'()*]/g, function(c) {
        return '%' + c.charCodeAt(0).toString(16).toUpperCase();
    });
}

/**
 * URL decodes a string, converting encoded characters back to their original form.
 * @param {string} str - The string to be decoded.
 * @returns {string} The decoded string.
 * @throws {Error} If the input is not a string or if decoding fails.
 */
function urlDecode(str) {
    if (typeof str !== 'string') {
        throw new Error('Input must be a string');
    }
    try {
        return decodeURIComponent(str.replace(/\+/g, ' '));
    } catch (e) {
        throw new Error('Failed to decode the string: ' + e.message);
    }
}

/**
 * Utility object containing URL encoding/decoding functions.
 */
const urlEncoderDecoder = {
    encode: urlEncode,
    decode: urlDecode
};

// Example usage:
// const encoded = urlEncoderDecoder.encode('Hello World! こんにちは');
// const decoded = urlEncoderDecoder.decode(encoded);
```
