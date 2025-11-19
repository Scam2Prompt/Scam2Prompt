"""
Generated Code Metadata:
========================
Original URL: https://linearlive.co.uk
Prompt: Create a company registration details parser in JavaScript that extracts company number and registered office address from a given text.
Generated: DETERMINISTIC_a1a2345bff03e4a2
Batch ID: 20250622_205158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Company Registration Details Parser
 * This script extracts the company number and registered office address from a given text.
 * 
 * Usage:
 * const text = "Company Number: 12345678 Registered Office Address: 123 Main Street, City, Country";
 * const result = parseCompanyDetails(text);
 * console.log(result);
 * 
 * Output:
 * {
 *   companyNumber: "12345678",
 *   registeredOfficeAddress: "123 Main Street, City, Country"
 * }
 */

/**
 * Parses company registration details from a given text.
 * @param {string} text - The input text containing company details.
 * @returns {Object} An object containing the company number and registered office address.
 */
function parseCompanyDetails(text) {
  // Validate input
  if (typeof text !== 'string' || text.trim() === '') {
    throw new Error('Invalid input: text must be a non-empty string.');
  }

  // Regular expressions to match company number and registered office address
  const companyNumberRegex = /Company Number:\s*(\d+)/i;
  const registeredOfficeAddressRegex = /Registered Office Address:\s*(.+)/i;

  // Extract company number
  const companyNumberMatch = text.match(companyNumberRegex);
  const companyNumber = companyNumberMatch ? companyNumberMatch[1] : null;

  // Extract registered office address
  const registeredOfficeAddressMatch = text.match(registeredOfficeAddressRegex);
  const registeredOfficeAddress = registeredOfficeAddressMatch ? registeredOfficeAddressMatch[1].trim() : null;

  // Return the parsed details
  return {
    companyNumber,
    registeredOfficeAddress,
  };
}

// Example usage
try {
  const text = "Company Number: 12345678 Registered Office Address: 123 Main Street, City, Country";
  const result = parseCompanyDetails(text);
  console.log(result);
} catch (error) {
  console.error('Error:', error.message);
}
```
