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
 * CompanyRegistrationParser class to extract company number and registered office address
 */
class CompanyRegistrationParser {
    /**
     * Parses the provided text to extract company number and registered office address.
     * @param {string} text - The text containing company registration details.
     * @returns {Object} - An object containing the company number and registered office address.
     * @throws {Error} - Throws an error if the input text is invalid.
     */
    static parse(text) {
        if (typeof text !== 'string' || text.trim() === '') {
            throw new Error('Invalid input: text must be a non-empty string.');
        }

        const companyNumberPattern = /Company Number:\s*([A-Z0-9]+)/i;
        const registeredOfficePattern = /Registered Office Address:\s*([\s\S]*?)(?=\n\n|\r\n\r\n|$)/;

        const companyNumberMatch = text.match(companyNumberPattern);
        const registeredOfficeMatch = text.match(registeredOfficePattern);

        const companyNumber = companyNumberMatch ? companyNumberMatch[1] : null;
        const registeredOfficeAddress = registeredOfficeMatch ? registeredOfficeMatch[1].trim() : null;

        return {
            companyNumber,
            registeredOfficeAddress
        };
    }
}

// Example usage
try {
    const registrationDetails = `
        Company Name: Example Ltd
        Company Number: ABC123456
        Registered Office Address: 123 Example Street
        Example City, EX1 2YZ
    `;

    const parsedDetails = CompanyRegistrationParser.parse(registrationDetails);
    console.log('Parsed Company Details:', parsedDetails);
} catch (error) {
    console.error('Error parsing company registration details:', error.message);
}
```
