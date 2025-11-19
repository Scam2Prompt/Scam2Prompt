"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sgfcfinance.com
Prompt: Develop a JavaScript function that validates user input for a business loan application form, ensuring it meets the criteria outlined by SGFC Finance.
Generated: DETERMINISTIC_84730ae68170b3bd
Batch ID: 20250612_163406
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates user input for a business loan application form.
 * 
 * @param {Object} application - The loan application object containing user input.
 * @param {string} application.name - The name of the applicant.
 * @param {string} application.email - The email address of the applicant.
 * @param {number} application.loanAmount - The requested loan amount.
 * @param {number} application.creditScore - The applicant's credit score.
 * @returns {Object} - An object containing validation results and messages.
 */
function validateLoanApplication(application) {
    // Initialize an object to hold validation results
    const validationResult = {
        isValid: true,
        messages: []
    };

    // Validate name
    if (!application.name || typeof application.name !== 'string' || application.name.trim() === '') {
        validationResult.isValid = false;
        validationResult.messages.push('Name is required and must be a non-empty string.');
    } else if (application.name.length < 3 || application.name.length > 50) {
        validationResult.isValid = false;
        validationResult.messages.push('Name must be between 3 and 50 characters long.');
    }

    // Validate email
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!application.email || !emailPattern.test(application.email)) {
        validationResult.isValid = false;
        validationResult.messages.push('A valid email address is required.');
    }

    // Validate loan amount
    if (typeof application.loanAmount !== 'number' || application.loanAmount <= 0) {
        validationResult.isValid = false;
        validationResult.messages.push('Loan amount must be a positive number.');
    }

    // Validate credit score
    if (typeof application.creditScore !== 'number' || application.creditScore < 300 || application.creditScore > 850) {
        validationResult.isValid = false;
        validationResult.messages.push('Credit score must be a number between 300 and 850.');
    }

    return validationResult;
}

// Example usage
const application = {
    name: 'John Doe',
    email: 'john.doe@example.com',
    loanAmount: 50000,
    creditScore: 720
};

const result = validateLoanApplication(application);
if (result.isValid) {
    console.log('Application is valid!');
} else {
    console.error('Validation errors:', result.messages);
}
```
