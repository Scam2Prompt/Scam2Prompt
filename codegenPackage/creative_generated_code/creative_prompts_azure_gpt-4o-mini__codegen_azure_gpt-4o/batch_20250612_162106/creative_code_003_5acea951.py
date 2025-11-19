"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bearachan.com
Prompt: Develop a JavaScript function that validates user input for domain name purchases, ensuring the format is correct before submission.
Generated: DETERMINISTIC_5acea951a6b66e28
Batch ID: 20250612_162106
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates a domain name for purchase.
 * A valid domain name:
 * - Can only contain alphanumeric characters, hyphens, and periods.
 * - Must start and end with an alphanumeric character.
 * - Cannot contain consecutive periods or hyphens.
 * - Must be 2 to 63 characters long.
 * 
 * @param {string} domainName - The domain name to validate.
 * @returns {Object} - Returns an object with `isValid` (boolean) and `message` (string).
 */
function validateDomainName(domainName) {
  // Regular expression for domain name validation
  const domainRegex = /^[a-zA-Z0-9]([a-zA-Z0-9.-]*[a-zA-Z0-9])?$/;
  const maxLength = 63; // Maximum allowed length for a domain name
  const minLength = 2; // Minimum allowed length for a domain name
  
  try {
    // Check if domain name is empty
    if (!domainName || typeof domainName !== 'string') {
      return { isValid: false, message: "Domain name is required and must be a string." };
    }
    
    // Check the length of the domain name
    if (domainName.length < minLength || domainName.length > maxLength) {
      return { isValid: false, message: `Domain name must be between ${minLength} and ${maxLength} characters.` };
    }
    
    // Check the format using the regex
    if (!domainRegex.test(domainName)) {
      return {
        isValid: false,
        message: "Domain name contains invalid characters or format. It must only contain alphanumeric characters, hyphens, and periods, and cannot start or end with hyphens or periods."
      };
    }
    
    // Check for consecutive periods or hyphens
    if (/[\.-]{2,}/.test(domainName)) {
      return { isValid: false, message: "Domain name cannot contain consecutive periods or hyphens." };
    }
    
    // If all checks pass
    return { isValid: true, message: "Domain name is valid." };
  } catch (error) {
    // Handle unexpected errors
    return { isValid: false, message: `An error occurred during validation: ${error.message}` };
  }
}

// Example usage
const result = validateDomainName("example-domain.com");
console.log(result); // { isValid: true, message: "Domain name is valid." }
```
