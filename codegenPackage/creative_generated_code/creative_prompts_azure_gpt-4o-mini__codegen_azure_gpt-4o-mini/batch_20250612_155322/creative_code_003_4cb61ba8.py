"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://financialrecoverysolutions.co.uk
Prompt: Create a JavaScript function that validates user input for a claim submission form based on the requirements outlined by Financial Recovery Solutions for mis-sold bank accounts.
Generated: DETERMINISTIC_4cb61ba8e0121d28
Batch ID: 20250612_155322
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates user input for a claim submission form based on Financial Recovery Solutions guidelines.
 * 
 * @param {Object} formData - The data entered by the user in the claim submission form.
 * @param {string} formData.name - The name of the claimant.
 * @param {string} formData.email - The email address of the claimant.
 * @param {string} formData.accountNumber - The account number of the mis-sold bank account.
 * @param {string} formData.claimDetails - Details regarding the claim.
 * @returns {Object} - An object containing the validation results.
 */
function validateClaimSubmission(formData) {
    const errors = {};

    // Check if name is provided and is a valid string
    if (!formData.name || typeof formData.name !== 'string' || formData.name.trim() === '') {
        errors.name = 'Name is required and cannot be empty.';
    }

    // Validate email format
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!formData.email || typeof formData.email !== 'string' || !emailRegex.test(formData.email)) {
        errors.email = 'A valid email address is required.';
    }

    // Check if account number is provided and is a valid format (e.g., numeric)
    const accountNumberRegex = /^\d{8,12}$/; // Assuming account number is 8 to 12 digits long
    if (!formData.accountNumber || typeof formData.accountNumber !== 'string' || !accountNumberRegex.test(formData.accountNumber)) {
        errors.accountNumber = 'Account number must be between 8 and 12 digits.';
    }

    // Check if claim details are provided
    if (!formData.claimDetails || typeof formData.claimDetails !== 'string' || formData.claimDetails.trim() === '') {
        errors.claimDetails = 'Claim details are required and cannot be empty.';
    }

    // Return validation results
    return {
        isValid: Object.keys(errors).length === 0,
        errors: errors
    };
}

// Example usage:
try {
    const formData = {
        name: 'John Doe',
        email: 'john.doe@example.com',
        accountNumber: '12345678',
        claimDetails: 'Details of the mis-sold account...'
    };

    const validationResult = validateClaimSubmission(formData);
    if (!validationResult.isValid) {
        console.log('Validation errors:', validationResult.errors);
    } else {
        console.log('Claim submission is valid.');
    }
} catch (error) {
    console.error('An error occurred during validation:', error);
}
```
