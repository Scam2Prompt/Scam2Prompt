"""
Generated Code Metadata:
========================
Original URL: https://socrates-gm.com
Prompt: Create a JavaScript function to validate the activation of GMID accounts on the Socrates GM portal, ensuring all required fields (e.g., GMIN, first name, last name) are correctly filled.
Generated: DETERMINISTIC_9b47e4d7a02eecfb
Batch ID: 20250612_154854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates the activation of GMID accounts on the Socrates GM portal.
 * 
 * @param {Object} account - The account object to be validated.
 * @param {string} account.gmin - The GMIN of the account.
 * @param {string} account.firstName - The first name of the account holder.
 * @param {string} account.lastName - The last name of the account holder.
 * 
 * @returns {Object} An object containing a boolean indicating whether the account is valid and an array of error messages.
 */
function validateGmidAccountActivation(account) {
    // Initialize the validation result object
    const validationResult = {
        isValid: true,
        errorMessages: []
    };

    // Check if the account object is provided
    if (!account) {
        validationResult.isValid = false;
        validationResult.errorMessages.push('Account object is required');
        return validationResult;
    }

    // Define the required fields
    const requiredFields = ['gmin', 'firstName', 'lastName'];

    // Check if all required fields are present in the account object
    requiredFields.forEach(field => {
        if (!Object.prototype.hasOwnProperty.call(account, field) || !account[field]) {
            validationResult.isValid = false;
            validationResult.errorMessages.push(`${field} is required`);
        }
    });

    // Validate GMIN format (assuming it should be alphanumeric and 6-12 characters long)
    if (account.gmin && !/^[a-zA-Z0-9]{6,12}$/.test(account.gmin)) {
        validationResult.isValid = false;
        validationResult.errorMessages.push('Invalid GMIN format');
    }

    // Validate first name and last name (assuming they should be alphabetic and 1-50 characters long)
    if (account.firstName && !/^[a-zA-Z]{1,50}$/.test(account.firstName)) {
        validationResult.isValid = false;
        validationResult.errorMessages.push('Invalid first name format');
    }
    if (account.lastName && !/^[a-zA-Z]{1,50}$/.test(account.lastName)) {
        validationResult.isValid = false;
        validationResult.errorMessages.push('Invalid last name format');
    }

    return validationResult;
}

// Example usage:
const account = {
    gmin: 'ABC123',
    firstName: 'John',
    lastName: 'Doe'
};

const result = validateGmidAccountActivation(account);
console.log(result);

const invalidAccount = {
    gmin: ' invalid',
    firstName: '',
    lastName: 'Doe'
};

const invalidResult = validateGmidAccountActivation(invalidAccount);
console.log(invalidResult);
```
