"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://centralseedandchem.co.nz
Prompt: Write a JavaScript function to validate user input in a contact form for Central Seed & Chemical's website.
Generated: DETERMINISTIC_675b2ea95f5d45e1
Batch ID: 20250612_163647
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates user input in a contact form.
 * 
 * @param {Object} formData - The data object containing user input.
 * @param {string} formData.name - The name of the user.
 * @param {string} formData.email - The email of the user.
 * @param {string} formData.message - The message from the user.
 * @returns {Object} An object containing isValid flag and an array of error messages.
 */
function validateContactForm(formData) {
    const errors = [];
    const { name, email, message } = formData;

    // Validate name: must be a non-empty string and less than 50 characters
    if (!name || typeof name !== 'string' || name.trim().length === 0) {
        errors.push('Name is required and cannot be empty.');
    } else if (name.length > 50) {
        errors.push('Name must be less than 50 characters.');
    }

    // Validate email: must match a standard email format
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!email || !emailRegex.test(email)) {
        errors.push('A valid email address is required.');
    }

    // Validate message: must be a non-empty string and less than 500 characters
    if (!message || typeof message !== 'string' || message.trim().length === 0) {
        errors.push('Message is required and cannot be empty.');
    } else if (message.length > 500) {
        errors.push('Message must be less than 500 characters.');
    }

    // Return validation result
    return {
        isValid: errors.length === 0,
        errors: errors
    };
}

// Example usage
const formData = {
    name: "John Doe",
    email: "john.doe@example.com",
    message: "Hello, I would like to inquire about your services."
};

const validationResult = validateContactForm(formData);

if (!validationResult.isValid) {
    console.error('Validation Errors:', validationResult.errors);
} else {
    console.log('Form submission is valid. Proceed with submission.');
}
```
