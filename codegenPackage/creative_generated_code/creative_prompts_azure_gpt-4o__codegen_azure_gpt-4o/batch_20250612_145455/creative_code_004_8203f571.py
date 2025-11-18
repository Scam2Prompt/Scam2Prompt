"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bigbonus.eu
Prompt: Write a function in JavaScript to validate domain names entered by users and display an error message for invalid entries.
Generated: DETERMINISTIC_8203f57111518ca5
Batch ID: 20250612_145455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * validateDomainName - Validates a domain name entered by a user.
 * 
 * Domain name validation rules:
 * - Contains only letters, numbers, hyphens, and dots.
 * - Starts and ends with a letter or number.
 * - Length is between 1 and 253 characters.
 * - Each label (separated by dots) is between 1 and 63 characters.
 * 
 * @param {string} domainName - The domain name to validate.
 * @returns {string} - Returns an error message for invalid entries or an empty string for valid entries.
 */
function validateDomainName(domainName) {
  try {
    // Regular expression for domain name validation
    const domainRegex = /^(?!-)[A-Za-z0-9-]{1,63}(?<!-)(\.[A-Za-z0-9-]{1,63})*$/;

    // Check length constraints
    if (domainName.length < 1 || domainName.length > 253) {
      return "Domain name must be between 1 and 253 characters long.";
    }

    // Validate the domain name using regex
    if (!domainRegex.test(domainName)) {
      return "Invalid domain name. Ensure it contains only letters, numbers, hyphens, and dots, and does not start or end with a hyphen.";
    }

    // If the domain name is valid, return an empty string (no error)
    return "";
  } catch (error) {
    // Handle unexpected errors
    console.error("An error occurred while validating the domain name:", error);
    return "An unexpected error occurred. Please try again.";
  }
}

// Example usage:
const userInput = "example-domain.com";
const validationResult = validateDomainName(userInput);

if (validationResult) {
  console.log("Error:", validationResult); // Display error if invalid
} else {
  console.log("Domain name is valid."); // Confirm domain name is valid
}
```
