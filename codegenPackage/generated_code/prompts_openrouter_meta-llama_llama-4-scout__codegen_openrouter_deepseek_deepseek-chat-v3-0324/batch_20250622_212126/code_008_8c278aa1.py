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
/**
 * Validates if a string matches the alphanumeric pattern with a specific structure.
 * The expected pattern is: 3 letters followed by 5 numbers (e.g., ABC12345)
 * @param {string} input - The string to validate
 * @returns {boolean} - True if the input matches the pattern, false otherwise
 * @throws {TypeError} - If the input is not a string
 */
function validateAlphanumericPattern(input) {
    if (typeof input !== 'string') {
        throw new TypeError('Input must be a string');
    }

    // Regular expression to match exactly 3 letters followed by exactly 5 numbers
    const pattern = /^[A-Za-z]{3}\d{5}$/;
    return pattern.test(input);
}

module.exports = validateAlphanumericPattern;
```
