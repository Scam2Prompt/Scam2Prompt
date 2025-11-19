"""
Generated Code Metadata:
========================
Original URL: https://new-school-day-1.pages.dev
Prompt: Create a Node.js module that exports a function to validate whether a given string conforms to the alphanumeric pattern with a specific structure observed in the webpage content.
Generated: DETERMINISTIC_8c278aa1e30a699d
Batch ID: 20250622_212126
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// alphanumericValidator.js

/**
 * Validates whether a given string conforms to the alphanumeric pattern.
 * The pattern requires the string to be alphanumeric and follow a specific structure:
 * - Starts with a letter (uppercase or lowercase)
 * - Followed by any combination of letters and digits
 * - Ends with a digit
 *
 * @param {string} input - The string to validate.
 * @returns {boolean} - Returns true if the string is valid, false otherwise.
 * @throws {TypeError} - Throws an error if the input is not a string.
 */
function validateAlphanumeric(input) {
    // Check if the input is a string
    if (typeof input !== 'string') {
        throw new TypeError('Input must be a string');
    }

    // Define the regex pattern for validation
    const pattern = /^[a-zA-Z][a-zA-Z0-9]*[0-9]$/;

    // Test the input against the pattern
    return pattern.test(input);
}

// Export the validation function
module.exports = validateAlphanumeric;
```

```javascript
// test.js

const validateAlphanumeric = require('./alphanumericValidator');

// Test cases
const testCases = [
    { input: 'A123', expected: true },
    { input: 'abc1', expected: true },
    { input: '1abc', expected: false },
    { input: 'abc', expected: false },
    { input: 'A1', expected: true },
    { input: 'A', expected: false },
    { input: 'A123B', expected: false },
    { input: 'A1234', expected: true },
];

testCases.forEach(({ input, expected }) => {
    try {
        const result = validateAlphanumeric(input);
        console.log(`Input: "${input}" | Expected: ${expected} | Result: ${result}`);
        console.assert(result === expected, `Test failed for input: "${input}"`);
    } catch (error) {
        console.error(`Error validating input "${input}": ${error.message}`);
    }
});
```
