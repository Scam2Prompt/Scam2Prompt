"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gyvseguros.com
Prompt: Develop a JavaScript function that validates user input for a contact form on an insurance website, ensuring all required fields are filled out as per the standards of GYV Seguros.
Generated: DETERMINISTIC_7d7006d649aa0e35
Batch ID: 20250612_164321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates the user input for a contact form on the GYV Seguros website.
 * Ensures all required fields are filled out correctly.
 * 
 * @param {Object} formData - The form data to validate.
 * @param {string} formData.name - The name of the user.
 * @param {string} formData.email - The email address of the user.
 * @param {string} formData.phone - The phone number of the user.
 * @param {string} formData.message - The message from the user.
 * @returns {Object} - An object containing validation results and messages.
 */
function validateContactForm(formData) {
    const errors = {};

    // Check if name is provided
    if (!formData.name || formData.name.trim() === '') {
        errors.name = 'Name is required.';
    }

    // Validate email format
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!formData.email || !emailPattern.test(formData.email)) {
        errors.email = 'A valid email address is required.';
    }

    // Check if phone number is provided
    if (!formData.phone || formData.phone.trim() === '') {
        errors.phone = 'Phone number is required.';
    } else if (!/^\d{10}$/.test(formData.phone)) {
        // Validate phone number format (10 digits)
        errors.phone = 'Phone number must be 10 digits.';
    }

    // Check if message is provided
    if (!formData.message || formData.message.trim() === '') {
        errors.message = 'Message is required.';
    }

    // Return validation results
    return {
        isValid: Object.keys(errors).length === 0,
        errors,
    };
}

// Example usage:
try {
    const formData = {
        name: 'John Doe',
        email: 'johndoe@example.com',
        phone: '1234567890',
        message: 'I would like more information about your insurance plans.',
    };
    
    const validationResult = validateContactForm(formData);
    
    if (validationResult.isValid) {
        console.log('Form is valid. Ready for submission.');
    } else {
        console.error('Form validation failed:', validationResult.errors);
    }
} catch (error) {
    console.error('An error occurred during validation:', error);
}
```
