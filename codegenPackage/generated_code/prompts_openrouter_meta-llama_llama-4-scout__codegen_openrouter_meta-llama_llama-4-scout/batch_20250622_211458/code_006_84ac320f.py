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
/**
 * Validates and sanitizes user input for classified ads.
 * 
 * @param {object} input - User input data.
 * @param {string} input.title - Title of the ad.
 * @param {string} input.description - Description of the ad.
 * @param {string} input.category - Category of the ad.
 * @param {string} input.location - Location of the ad.
 * @param {string} input.price - Price of the ad.
 * 
 * @returns {object} Sanitized and validated input data.
 * 
 * @throws {Error} If any input field is invalid or missing.
 */

function validateAndSanitizeAdInput(input) {
    // Check if input is an object
    if (typeof input !== 'object' || Array.isArray(input) || input === null) {
        throw new Error('Input must be an object');
    }

    // Define allowed categories
    const allowedCategories = ['electronics', 'furniture', 'clothing', 'other'];

    // Define validation and sanitization rules
    const validationRules = {
        title: {
            required: true,
            maxLength: 100,
            trim: true,
            escape: true,
        },
        description: {
            required: true,
            maxLength: 1000,
            trim: true,
            escape: true,
        },
        category: {
            required: true,
            in: allowedCategories,
        },
        location: {
            required: true,
            maxLength: 200,
            trim: true,
            escape: true,
        },
        price: {
            required: true,
            numeric: true,
            min: 0,
        },
    };

    // Validate and sanitize input data
    const sanitizedInput = {};
    for (const field in validationRules) {
        if (!Object.prototype.hasOwnProperty.call(input, field)) {
            if (validationRules[field].required) {
                throw new Error(`Missing required field: ${field}`);
            } else {
                continue;
            }
        }

        let value = input[field];
        if (validationRules[field].trim) {
            value = String(value).trim();
        }

        if (validationRules[field].escape) {
            value = String(value).replace(/&/g, '&amp;')
                .replace(/</g, '&lt;')
                .replace(/>/g, '&gt;')
                .replace(/"/g, '&quot;')
                .replace(/'/g, '&#x27;');
        }

        if (validationRules[field].maxLength && value.length > validationRules[field].maxLength) {
            throw new Error(`Field ${field} exceeds maximum length of ${validationRules[field].maxLength} characters`);
        }

        if (validationRules[field].in && !validationRules[field].in.includes(value)) {
            throw new Error(`Field ${field} must be one of ${validationRules[field].in.join(', ')}`);
        }

        if (validationRules[field].numeric && isNaN(Number(value)) || validationRules[field].min && Number(value) < validationRules[field].min) {
            throw new Error(`Field ${field} must be a number greater than or equal to ${validationRules[field].min}`);
        }

        sanitizedInput[field] = value;
    }

    return sanitizedInput;
}

// Example usage:
try {
    const userInput = {
        title: 'Test Ad',
        description: 'This is a test ad.',
        category: 'electronics',
        location: 'New York',
        price: '100',
    };

    const sanitizedInput = validateAndSanitizeAdInput(userInput);
    // Use sanitizedInput
    // For demonstration purposes, print it:
    console.log(sanitizedInput);
} catch (error) {
    console.error(error.message);
}
```
