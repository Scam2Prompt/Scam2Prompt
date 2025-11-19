"""
Generated Code Metadata:
========================
Original URL: https://financialrecoverysolutions.co.uk
Prompt: Create a JavaScript function that validates user input for a claim submission form based on the requirements outlined by Financial Recovery Solutions for mis-sold bank accounts.
Generated: DETERMINISTIC_4cb61ba8e0121d28
Batch ID: 20250612_155322
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates user input for a claim submission form based on Financial Recovery Solutions requirements.
 * @param {Object} formData - The form data to validate.
 * @param {string} formData.fullName - User's full name.
 * @param {string} formData.email - User's email address.
 * @param {string} formData.phone - User's phone number.
 * @param {string} formData.accountNumber - Bank account number.
 * @param {string} formData.sortCode - Bank sort code.
 * @param {string} formData.bankName - Name of the bank.
 * @param {Date} formData.accountOpenedDate - Date when account was opened.
 * @param {string} formData.claimReason - Reason for the claim.
 * @param {boolean} formData.termsAgreed - Whether terms are agreed.
 * @returns {Object} - Validation result with isValid flag and errors object.
 */
function validateClaimForm(formData) {
    const errors = {};
    const currentDate = new Date();
    const minDate = new Date();
    minDate.setFullYear(currentDate.getFullYear() - 20); // Accounts older than 20 years not accepted

    // Validate full name (required, at least 2 words, max 100 chars)
    if (!formData.fullName || formData.fullName.trim().length === 0) {
        errors.fullName = 'Full name is required';
    } else if (formData.fullName.trim().split(/\s+/).length < 2) {
        errors.fullName = 'Please enter your full name (first and last name)';
    } else if (formData.fullName.length > 100) {
        errors.fullName = 'Full name must be less than 100 characters';
    }

    // Validate email (required, valid format)
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!formData.email || formData.email.trim().length === 0) {
        errors.email = 'Email is required';
    } else if (!emailRegex.test(formData.email)) {
        errors.email = 'Please enter a valid email address';
    }

    // Validate phone (required, UK format)
    const phoneRegex = /^(\+44|0)[1-9]\d{8,9}$/;
    if (!formData.phone || formData.phone.trim().length === 0) {
        errors.phone = 'Phone number is required';
    } else if (!phoneRegex.test(formData.phone.replace(/\s+/g, ''))) {
        errors.phone = 'Please enter a valid UK phone number';
    }

    // Validate account number (required, 8 digits)
    const accountNumberRegex = /^\d{8}$/;
    if (!formData.accountNumber || formData.accountNumber.trim().length === 0) {
        errors.accountNumber = 'Account number is required';
    } else if (!accountNumberRegex.test(formData.accountNumber)) {
        errors.accountNumber = 'Account number must be 8 digits';
    }

    // Validate sort code (required, format 00-00-00 or 000000)
    const sortCodeRegex = /^(\d{2}-\d{2}-\d{2}|\d{6})$/;
    if (!formData.sortCode || formData.sortCode.trim().length === 0) {
        errors.sortCode = 'Sort code is required';
    } else if (!sortCodeRegex.test(formData.sortCode)) {
        errors.sortCode = 'Sort code must be in format 00-00-00 or 000000';
    }

    // Validate bank name (required, at least 2 chars)
    if (!formData.bankName || formData.bankName.trim().length === 0) {
        errors.bankName = 'Bank name is required';
    } else if (formData.bankName.trim().length < 2) {
        errors.bankName = 'Bank name must be at least 2 characters';
    }

    // Validate account opened date (required, not in future, not older than 20 years)
    if (!formData.accountOpenedDate) {
        errors.accountOpenedDate = 'Account opened date is required';
    } else {
        const openedDate = new Date(formData.accountOpenedDate);
        if (isNaN(openedDate.getTime())) {
            errors.accountOpenedDate = 'Invalid date format';
        } else if (openedDate > currentDate) {
            errors.accountOpenedDate = 'Date cannot be in the future';
        } else if (openedDate < minDate) {
            errors.accountOpenedDate = 'Account must be less than 20 years old';
        }
    }

    // Validate claim reason (required, at least 20 chars)
    if (!formData.claimReason || formData.claimReason.trim().length === 0) {
        errors.claimReason = 'Claim reason is required';
    } else if (formData.claimReason.trim().length < 20) {
        errors.claimReason = 'Claim reason must be at least 20 characters';
    }

    // Validate terms agreement (must be true)
    if (!formData.termsAgreed) {
        errors.termsAgreed = 'You must agree to the terms and conditions';
    }

    return {
        isValid: Object.keys(errors).length === 0,
        errors: errors
    };
}

// Example usage:
// const validationResult = validateClaimForm(formData);
// if (!validationResult.isValid) {
//     // Handle errors
//     console.log(validationResult.errors);
// }
```
