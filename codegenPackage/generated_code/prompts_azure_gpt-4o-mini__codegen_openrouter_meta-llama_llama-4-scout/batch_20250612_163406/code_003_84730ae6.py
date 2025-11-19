"""
Generated Code Metadata:
========================
Original URL: https://sgfcfinance.com
Prompt: Develop a JavaScript function that validates user input for a business loan application form, ensuring it meets the criteria outlined by SGFC Finance.
Generated: DETERMINISTIC_84730ae68170b3bd
Batch ID: 20250612_163406
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates user input for a business loan application form.
 * 
 * @param {Object} formData - The user input data from the form.
 * @param {string} formData.businessName - The name of the business.
 * @param {string} formData.businessType - The type of business.
 * @param {number} formData.annualRevenue - The annual revenue of the business.
 * @param {number} formData loanAmount - The loan amount being requested.
 * @param {string} formData.contactName - The name of the contact person.
 * @param {string} formData.contactEmail - The email of the contact person.
 * @param {string} formData.contactPhone - The phone number of the contact person.
 * 
 * @returns {Object} An object containing a boolean indicating whether the input is valid and an array of error messages.
 */

// Constants for validation criteria
const SGFC_FINANCE_CRITERIA = {
    businessNameMinLength: 2,
    businessNameMaxLength: 255,
    businessTypeMinLength: 2,
    businessTypeMaxLength: 255,
    annualRevenueMin: 0,
    loanAmountMin: 0,
    contactNameMinLength: 2,
    contactNameMaxLength: 255,
    contactEmailRegex: /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/,
    contactPhoneRegex: /^\d{3}-\d{3}-\d{4}$/,
};

function validateLoanApplication(formData) {
    try {
        // Check if formData is an object
        if (typeof formData !== 'object' || Array.isArray(formData) || formData === null) {
            throw new Error('Form data must be an object');
        }

        // Initialize error messages array
        let errorMessages = [];

        // Validate business name
        if (!formData.businessName || formData.businessName.length < SGFC_FINANCE_CRITERIA.businessNameMinLength 
            || formData.businessName.length > SGFC_FINANCE_CRITERIA.businessNameMaxLength) {
            errorMessages.push('Business name must be between 2 and 255 characters');
        }

        // Validate business type
        if (!formData.businessType || formData.businessType.length < SGFC_FINANCE_CRITERIA.businessTypeMinLength 
            || formData.businessType.length > SGFC_FINANCE_CRITERIA.businessTypeMaxLength) {
            errorMessages.push('Business type must be between 2 and 255 characters');
        }

        // Validate annual revenue
        if (typeof formData.annualRevenue !== 'number' || formData.annualRevenue < SGFC_FINANCE_CRITERIA.annualRevenueMin) {
            errorMessages.push('Annual revenue must be a number greater than or equal to 0');
        }

        // Validate loan amount
        if (typeof formData.loanAmount !== 'number' || formData.loanAmount < SGFC_FINANCE_CRITERIA.loanAmountMin) {
            errorMessages.push('Loan amount must be a number greater than or equal to 0');
        }

        // Validate contact name
        if (!formData.contactName || formData.contactName.length < SGFC_FINANCE_CRITERIA.contactNameMinLength 
            || formData.contactName.length > SGFC_FINANCE_CRITERIA.contactNameMaxLength) {
            errorMessages.push('Contact name must be between 2 and 255 characters');
        }

        // Validate contact email
        if (!SGFC_FINANCE_CRITERIA.contactEmailRegex.test(formData.contactEmail)) {
            errorMessages.push('Contact email must be a valid email address');
        }

        // Validate contact phone
        if (!SGFC_FINANCE_CRITERIA.contactPhoneRegex.test(formData.contactPhone)) {
            errorMessages.push('Contact phone must be in the format XXX-XXX-XXXX');
        }

        // Return validation result
        return {
            isValid: errorMessages.length === 0,
            errorMessages: errorMessages,
        };
    } catch (error) {
        // Log and rethrow the error
        console.error('Error validating loan application:', error);
        throw error;
    }
}

// Example usage:
let formData = {
    businessName: 'Example Business',
    businessType: 'Example Type',
    annualRevenue: 100000,
    loanAmount: 50000,
    contactName: 'John Doe',
    contactEmail: 'john.doe@example.com',
    contactPhone: '123-456-7890',
};

let validationResult = validateLoanApplication(formData);
console.log(validationResult);
```
