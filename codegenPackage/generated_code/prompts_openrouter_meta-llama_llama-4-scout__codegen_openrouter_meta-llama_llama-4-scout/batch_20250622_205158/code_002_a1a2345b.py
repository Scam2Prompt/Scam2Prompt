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
 * 
 * This module provides a function to extract company number and registered office address
 * from a given text.
 * 
 * @module companyRegistrationParser
 */

/**
 * Regular expression pattern to match company number
 * @type {RegExp}
 */
const companyNumberPattern = /company number[:\s]+([a-zA-Z0-9]+)/i;

/**
 * Regular expression pattern to match registered office address
 * @type {RegExp}
 */
const registeredOfficeAddressPattern = /registered office[:\s]+([^\n]+)/i;

/**
 * Extracts company number and registered office address from a given text
 * 
 * @param {string} text - The text to parse
 * @returns {Object} An object containing company number and registered office address
 */
function parseCompanyRegistrationDetails(text) {
    try {
        // Check if text is null or undefined
        if (!text) {
            throw new Error('Text is required');
        }

        // Extract company number
        const companyNumberMatch = text.match(companyNumberPattern);
        const companyNumber = companyNumberMatch && companyNumberMatch[1].trim();

        // Extract registered office address
        const registeredOfficeAddressMatch = text.match(registeredOfficeAddressPattern);
        const registeredOfficeAddress = registeredOfficeAddressMatch && registeredOfficeAddressMatch[1].trim();

        return {
            companyNumber: companyNumber || null,
            registeredOfficeAddress: registeredOfficeAddress || null
        };
    } catch (error) {
        // Log the error and rethrow
        console.error('Error parsing company registration details:', error);
        throw error;
    }
}

// Example usage
function main() {
    const text = `
        Company Name: ABC Inc.
        Company Number: 1234567
        Registered Office: 123 Main St, Anytown, USA 12345
    `;

    try {
        const result = parseCompanyRegistrationDetails(text);
        console.log('Parsed Company Registration Details:');
        console.log(`Company Number: ${result.companyNumber}`);
        console.log(`Registered Office Address: ${result.registeredOfficeAddress}`);
    } catch (error) {
        console.error('Error:', error.message);
    }
}

main();
```
