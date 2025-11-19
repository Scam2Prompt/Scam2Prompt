"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fin-flix.me
Prompt: Create a JavaScript function that validates user input for a credit application form, ensuring all fields are filled correctly before submission.
Generated: DETERMINISTIC_dcb9b60c71cb0528
Batch ID: 20250612_164205
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates the user input for a credit application form.
 * Checks that all required fields are filled and that the input
 * values meet the specified criteria (e.g., valid email, phone number).
 * 
 * @param {Object} formData - The user input data from the form.
 * @returns {Object} - An object containing validation results and messages.
 */
function validateCreditApplication(formData) {
    const validationResults = {
        isValid: true,
        messages: []
    };

    // Check for empty fields
    for (const [key, value] of Object.entries(formData)) {
        if (!value) {
            validationResults.isValid = false;
            validationResults.messages.push(`${key} is required.`);
        }
    }

    // Validate email format
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (formData.email && !emailPattern.test(formData.email)) {
        validationResults.isValid = false;
        validationResults.messages.push('Email format is invalid.');
    }

    // Validate phone number format (Assuming US format)
    const phonePattern = /^\(\d{3}\) \d{3}-\d{4}$/;
    if (formData.phone && !phonePattern.test(formData.phone)) {
        validationResults.isValid = false;
        validationResults.messages.push('Phone number must be in the format (XXX) XXX-XXXX.');
    }

    // Validate credit score range
    if (formData.creditScore && (formData.creditScore < 300 || formData.creditScore > 850)) {
        validationResults.isValid = false;
        validationResults.messages.push('Credit score must be between 300 and 850.');
    }

    return validationResults;
}

// Example usage
try {
    const userInput = {
        name: 'John Doe',
        email: 'john.doe@example.com',
        phone: '(123) 456-7890',
        creditScore: 700
    };

    const validation = validateCreditApplication(userInput);
    if (validation.isValid) {
        console.log('Form is valid. Proceeding with submission...');
    } else {
        console.error('Form validation failed:', validation.messages);
    }
} catch (error) {
    console.error('An error occurred during form validation:', error.message);
}
```
