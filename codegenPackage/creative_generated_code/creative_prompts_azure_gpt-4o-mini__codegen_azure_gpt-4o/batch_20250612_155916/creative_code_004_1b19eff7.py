"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://haqqnetwork.net
Prompt: How can I create a JavaScript function to validate domain details on the Haqq Network platform?
Generated: DETERMINISTIC_1b19eff7acef8f70
Batch ID: 20250612_155916
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates domain details on the Haqq Network platform.
 * 
 * @param {Object} domainDetails - Object containing domain details to validate.
 * @param {string} domainDetails.domainName - The name of the domain to validate.
 * @param {string} domainDetails.owner - The owner of the domain.
 * @param {string} domainDetails.expiryDate - The expiry date of the domain in ISO format.
 * @returns {Object} - Validation result containing isValid (boolean) and errors (array).
 */
function validateDomainDetails(domainDetails) {
  const validationResult = {
    isValid: true,
    errors: [],
  };

  try {
    // Validate presence and type of domainName
    if (!domainDetails.domainName || typeof domainDetails.domainName !== 'string') {
      validationResult.isValid = false;
      validationResult.errors.push('Invalid domain name. It must be a non-empty string.');
    }

    // Validate domainName format (e.g., matches standard domain patterns)
    const domainNameRegex = /^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    if (domainDetails.domainName && !domainNameRegex.test(domainDetails.domainName)) {
      validationResult.isValid = false;
      validationResult.errors.push('Domain name format is incorrect.');
    }

    // Validate presence and type of owner
    if (!domainDetails.owner || typeof domainDetails.owner !== 'string') {
      validationResult.isValid = false;
      validationResult.errors.push('Invalid owner. It must be a non-empty string.');
    }

    // Validate presence and format of expiryDate
    if (!domainDetails.expiryDate || isNaN(new Date(domainDetails.expiryDate))) {
      validationResult.isValid = false;
      validationResult.errors.push('Invalid expiry date. It must be a valid ISO date string.');
    } else {
      // Ensure expiry date is in the future
      const expiryDate = new Date(domainDetails.expiryDate);
      const currentDate = new Date();
      if (expiryDate <= currentDate) {
        validationResult.isValid = false;
        validationResult.errors.push('Expiry date must be in the future.');
      }
    }
  } catch (error) {
    // Catch unexpected errors and mark validation as invalid
    validationResult.isValid = false;
    validationResult.errors.push(`Unexpected error: ${error.message}`);
  }

  return validationResult;
}

// Example usage
const domainDetails = {
  domainName: 'example.com',
  owner: 'John Doe',
  expiryDate: '2024-12-31T23:59:59.000Z',
};

const result = validateDomainDetails(domainDetails);
console.log(result);
```
