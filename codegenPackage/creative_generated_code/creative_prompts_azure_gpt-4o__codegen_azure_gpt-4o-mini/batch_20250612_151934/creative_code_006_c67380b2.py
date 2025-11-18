"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitsoft360.de
Prompt: Generate code for a JavaScript function that validates domain details and displays them in a user-friendly format.
Generated: DETERMINISTIC_c67380b251254338
Batch ID: 20250612_151934
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates and displays domain details in a user-friendly format.
 * 
 * @param {string} domain - The domain name to validate.
 * @returns {string} A message indicating the validity of the domain and its details.
 */
function validateAndDisplayDomain(domain) {
    // Regular expression for validating domain names
    const domainPattern = /^(?!-)[A-Za-z0-9-]{1,63}(?<!-)(\.[A-Za-z]{2,})+$/;

    // Check if the domain matches the pattern
    if (!domainPattern.test(domain)) {
        return `Invalid domain: "${domain}". Please enter a valid domain name.`;
    }

    // Extract domain details
    const domainParts = domain.split('.');
    const topLevelDomain = domainParts.pop(); // Get the last part as TLD
    const secondLevelDomain = domainParts.join('.'); // Join the rest as SLD

    // Format and display domain details
    const output = `
        Valid Domain: ${domain}
        Second-Level Domain: ${secondLevelDomain}
        Top-Level Domain: ${topLevelDomain}
    `;

    return output.trim();
}

// Example usage
try {
    const domainInput = 'example.com'; // Replace with user input or dynamic value
    const result = validateAndDisplayDomain(domainInput);
    console.log(result);
} catch (error) {
    console.error('An error occurred while validating the domain:', error.message);
}
```
