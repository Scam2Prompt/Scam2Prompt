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
const { sanitize } = require('dompurify');
const { JSDOM } = require('jsdom');

// Configure allowed HTML tags and attributes for classified ads (similar to Kleinanzeigen)
const ALLOWED_TAGS = ['b', 'i', 'u', 'br', 'p', 'ul', 'ol', 'li'];
const ALLOWED_ATTR = [];

/**
 * Validates and sanitizes classified ad input to prevent common web vulnerabilities.
 * @param {Object} adData - The classified ad data to validate and sanitize.
 * @param {string} adData.title - The ad title.
 * @param {string} adData.description - The ad description.
 * @param {number} adData.price - The ad price.
 * @param {string} adData.contactEmail - The contact email.
 * @param {string} [adData.phone] - The contact phone (optional).
 * @returns {Object} - Sanitized ad data with validation errors if any.
 */
function validateAndSanitizeAdInput(adData) {
    const errors = {};
    const sanitizedData = {};

    // Validate and sanitize title
    if (!adData.title || typeof adData.title !== 'string') {
        errors.title = 'Title is required and must be a string';
    } else {
        const trimmedTitle = adData.title.trim();
        if (trimmedTitle.length < 5 || trimmedTitle.length > 100) {
            errors.title = 'Title must be between 5 and 100 characters';
        } else {
            sanitizedData.title = validator.escape(trimmedTitle);
        }
    }

    // Validate and sanitize description
    if (!adData.description || typeof adData.description !== 'string') {
        errors.description = 'Description is required and must be a string';
    } else {
        const trimmedDesc = adData.description.trim();
        if (trimmedDesc.length < 10 || trimmedDesc.length > 2000) {
            errors.description = 'Description must be between 10 and 2000 characters';
        } else {
            // Use DOMPurify to sanitize HTML while allowing basic formatting
            const window = new JSDOM('').window;
            const purify = sanitize(window);
            sanitizedData.description = purify.sanitize(
                trimmedDesc,
                { ALLOWED_TAGS, ALLOWED_ATTR }
            );
        }
    }

    // Validate price
    if (typeof adData.price !== 'number' || adData.price < 0) {
        errors.price = 'Price must be a positive number';
    } else {
        sanitizedData.price = parseFloat(adData.price.toFixed(2));
    }

    // Validate and sanitize email
    if (!adData.contactEmail || typeof adData.contactEmail !== 'string') {
        errors.contactEmail = 'Email is required and must be a string';
    } else {
        const trimmedEmail = adData.contactEmail.trim();
        if (!validator.isEmail(trimmedEmail)) {
            errors.contactEmail = 'Please provide a valid email address';
        } else {
            sanitizedData.contactEmail = trimmedEmail.toLowerCase();
        }
    }

    // Validate and sanitize phone (optional)
    if (adData.phone && typeof adData.phone === 'string') {
        const trimmedPhone = adData.phone.trim();
        if (!validator.isMobilePhone(trimmedPhone, 'any', { strictMode: false })) {
            errors.phone = 'Please provide a valid phone number';
        } else {
            sanitizedData.phone = validator.escape(trimmedPhone);
        }
    }

    return {
        sanitizedData,
        errors: Object.keys(errors).length ? errors : null
    };
}

module.exports = { validateAndSanitizeAdInput };
```
