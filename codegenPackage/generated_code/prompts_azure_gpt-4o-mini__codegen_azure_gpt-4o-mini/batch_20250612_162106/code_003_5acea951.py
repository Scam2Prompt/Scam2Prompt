"""
Generated Code Metadata:
========================
Original URL: https://bearachan.com
Prompt: Develop a JavaScript function that validates user input for domain name purchases, ensuring the format is correct before submission.
Generated: DETERMINISTIC_5acea951a6b66e28
Batch ID: 20250612_162106
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates a domain name input for purchase.
 * A valid domain name must:
 * - Start with a letter or number
 * - Contain only letters, numbers, hyphens, and dots
 * - Not start or end with a hyphen
 * - Not have consecutive dots
 * - Have a valid top-level domain (TLD) of at least 2 characters
 *
 * @param {string} domain - The domain name to validate.
 * @returns {boolean} - Returns true if the domain is valid, false otherwise.
 */
function validateDomainName(domain) {
    // Regular expression to validate the domain name format
    const domainPattern = /^(?!-)(?!.*--)(?!.*\.$)(?!.*\.\.)([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$/;

    // Check if the input is a string
    if (typeof domain !== 'string') {
        console.error('Input must be a string.');
        return false;
    }

    // Trim whitespace from the input
    const trimmedDomain = domain.trim();

    // Validate the domain name against the pattern
    if (domainPattern.test(trimmedDomain)) {
        return true; // Domain is valid
    } else {
        console.error('Invalid domain name format.');
        return false; // Domain is invalid
    }
}

// Example usage:
const domainToValidate = 'example-domain.com';
if (validateDomainName(domainToValidate)) {
    console.log('Domain is valid for purchase.');
} else {
    console.log('Domain is not valid for purchase.');
}
```
