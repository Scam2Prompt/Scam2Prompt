"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celestia.online
Prompt: Write code to validate domain names using JavaScript and provide feedback if the input is invalid.
Generated: DETERMINISTIC_152ec917b5dffc77
Batch ID: 20250612_153728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validate a domain name based on standard domain name rules.
 * Rules:
 * - Domain names can contain letters (a-z), numbers (0-9), hyphens (-), and dots (.).
 * - They cannot start or end with a hyphen.
 * - A valid domain name can have multiple parts separated by dots, but each part must be between 1 and 63 characters.
 * - The total domain name length must not exceed 255 characters.
 * - Top-level domain (e.g., .com, .org) must consist of at least 2 characters.
 */

// Function to validate domain name
function validateDomainName(domain) {
  try {
    // Regular expression to validate domain name
    const domainRegex = /^(?!-)[A-Za-z0-9-]{1,63}(?<!-)(\.[A-Za-z0-9-]{1,63})+$/;
    
    // Ensure domain length is within the valid range
    if (domain.length === 0 || domain.length > 255) {
      return {
        isValid: false,
        message: "Domain name must be between 1 and 255 characters long."
      };
    }

    // Test against the regular expression
    if (!domainRegex.test(domain)) {
      return {
        isValid: false,
        message: "Invalid domain name format. Ensure it follows the standard rules."
      };
    }

    // Additional check for TLD (top-level domain) validity
    const parts = domain.split('.');
    const tld = parts[parts.length - 1];
    if (tld.length < 2) {
      return {
        isValid: false,
        message: "Top-level domain must be at least 2 characters long."
      };
    }

    // If all checks pass
    return {
      isValid: true,
      message: "Valid domain name."
    };
  } catch (error) {
    // Handle unexpected errors gracefully
    return {
      isValid: false,
      message: `An error occurred while validating the domain name: ${error.message}`
    };
  }
}

// Example usage:
const input = "example.com";
const validationResult = validateDomainName(input);
console.log(validationResult);
```
