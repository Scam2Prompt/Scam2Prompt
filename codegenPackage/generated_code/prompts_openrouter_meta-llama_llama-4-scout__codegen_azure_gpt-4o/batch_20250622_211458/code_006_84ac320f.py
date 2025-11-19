"""
Generated Code Metadata:
========================
Original URL: https://ether-pool.org
Prompt: Write a Node.js function to validate and sanitize user input for classified ads to prevent common web vulnerabilities, using best practices from platforms like Kleinanzeigen.
Generated: DETERMINISTIC_84ac320fc5c710dd
Batch ID: 20250622_211458
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
const validator = require('validator');

/**
 * Validates and sanitizes user input for classified ads.
 * Prevents common web vulnerabilities such as XSS, SQL injection, etc.
 * 
 * @param {Object} input - The user input object containing classified ad details.
 * @returns {Object} - Sanitized and validated input object or throws an error if validation fails.
 */
function validateAndSanitizeInput(input) {
    // Ensure input is an object
    if (typeof input !== 'object' || input === null) {
        throw new Error('Invalid input: Input must be an object.');
    }

    // Define allowed fields and their validation rules
    const rules = {
        title: {
            required: true,
            maxLength: 100,
            sanitize: (value) => validator.escape(value.trim())
        },
        description: {
            required: true,
            maxLength: 1000,
            sanitize: (value) => validator.escape(value.trim())
        },
        price: {
            required: true,
            validate: (value) => validator.isFloat(value.toString(), { min: 0 }),
            sanitize: (value) => parseFloat(value)
        },
        email: {
            required: true,
            validate: (value) => validator.isEmail(value),
            sanitize: (value) => validator.normalizeEmail(value)
        },
        phone: {
            required: false,
            validate: (value) => validator.isMobilePhone(value, 'any'),
            sanitize: (value) => value.trim()
        }
    };

    const sanitizedInput = {};

    // Validate and sanitize each field
    for (const field in rules) {
        const rule = rules[field];
        const value = input[field];

        // Check if the field is required and missing
        if (rule.required && (value === undefined || value === null || value === '')) {
            throw new Error(`Invalid input: ${field} is required.`);
        }

        // If the field is optional and not provided, skip validation/sanitization
        if (!rule.required && (value === undefined || value === null || value === '')) {
            continue;
        }

        // Validate the field if a validation function is provided
        if (rule.validate && !rule.validate(value)) {
            throw new Error(`Invalid input: ${field} is not valid.`);
        }

        // Sanitize the field if a sanitization function is provided
        sanitizedInput[field] = rule.sanitize ? rule.sanitize(value) : value;
    }

    return sanitizedInput;
}

module.exports = validateAndSanitizeInput;

// Example usage:
// const input = {
//     title: "<script>alert('XSS')</script>",
//     description: "This is a great product!",
//     price: "19.99",
//     email: "user@example.com",
//     phone: "+1234567890"
// };
// try {
//     const sanitizedInput = validateAndSanitizeInput(input);
//     console.log(sanitizedInput);
// } catch (error) {
//     console.error(error.message);
// }
```
