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
 * Validates domain details and formats them for display.
 * @param {Object} domainDetails - An object containing domain details.
 * @param {string} domainDetails.name - The domain name (e.g., "example.com").
 * @param {string} domainDetails.owner - The name of the domain owner.
 * @param {string} domainDetails.creationDate - The creation date of the domain in ISO format (e.g., "2023-01-01").
 * @param {string} domainDetails.expirationDate - The expiration date of the domain in ISO format (e.g., "2025-01-01").
 * @returns {string} - A formatted string displaying the validated domain details or an error message if validation fails.
 */
function validateAndDisplayDomainDetails(domainDetails) {
  try {
    // Validate domain details
    if (!domainDetails || typeof domainDetails !== 'object') {
      throw new Error('Domain details must be a valid object.');
    }

    const { name, owner, creationDate, expirationDate } = domainDetails;

    if (!name || typeof name !== 'string' || !/^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/.test(name)) {
      throw new Error('Invalid domain name.');
    }

    if (!owner || typeof owner !== 'string' || owner.trim() === '') {
      throw new Error('Invalid domain owner.');
    }

    if (!creationDate || isNaN(new Date(creationDate).getTime())) {
      throw new Error('Invalid creation date.');
    }

    if (!expirationDate || isNaN(new Date(expirationDate).getTime())) {
      throw new Error('Invalid expiration date.');
    }

    const creationDateObj = new Date(creationDate);
    const expirationDateObj = new Date(expirationDate);

    if (expirationDateObj <= creationDateObj) {
      throw new Error('Expiration date must be after creation date.');
    }

    // Format domain details for display
    const formattedDetails = `
      Domain Details:
      ----------------
      Name: ${name}
      Owner: ${owner}
      Creation Date: ${creationDateObj.toDateString()}
      Expiration Date: ${expirationDateObj.toDateString()}
    `;

    return formattedDetails;

  } catch (error) {
    // Handle errors and provide meaningful feedback
    return `Error: ${error.message}`;
  }
}

// Example usage:
const domain = {
  name: "example.com",
  owner: "John Doe",
  creationDate: "2023-01-01",
  expirationDate: "2025-01-01"
};

console.log(validateAndDisplayDomainDetails(domain));
```
