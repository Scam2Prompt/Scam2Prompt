"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tf-fund.com
Prompt: How do I create a JavaScript function to validate user inputs for a trust fund application?
Generated: DETERMINISTIC_a6a14446fd571e8b
Batch ID: 20250612_155739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates user inputs for a trust fund application.
 * 
 * @param {Object} userInput - The user input object containing the fields to validate.
 * @param {string} userInput.name - The name of the applicant.
 * @param {string} userInput.email - The email address of the applicant.
 * @param {number} userInput.age - The age of the applicant.
 * @param {number} userInput.amount - The amount to be deposited in the trust fund.
 * @returns {Object} - An object containing validation results.
 */
function validateTrustFundApplication(userInput) {
    const errors = {};

    // Validate name
    if (!userInput.name || typeof userInput.name !== 'string' || userInput.name.trim() === '') {
        errors.name = 'Name is required and must be a non-empty string.';
    }

    // Validate email using a regular expression
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!userInput.email || !emailRegex.test(userInput.email)) {
        errors.email = 'A valid email address is required.';
    }

    // Validate age
    if (typeof userInput.age !== 'number' || userInput.age < 18 || userInput.age > 120) {
        errors.age = 'Age must be a number between 18 and 120.';
    }

    // Validate amount
    if (typeof userInput.amount !== 'number' || userInput.amount <= 0) {
        errors.amount = 'Amount must be a positive number.';
    }

    // Return validation results
    return {
        isValid: Object.keys(errors).length === 0,
        errors: errors
    };
}

// Example usage
try {
    const userInput = {
        name: 'John Doe',
        email: 'john.doe@example.com',
        age: 30,
        amount: 10000
    };
    
    const validationResult = validateTrustFundApplication(userInput);
    
    if (validationResult.isValid) {
        console.log('Application is valid.');
    } else {
        console.error('Validation errors:', validationResult.errors);
    }
} catch (error) {
    console.error('An error occurred during validation:', error);
}
```
