"""
Generated Code Metadata:
========================
Original URL: https://symbiotic.eu
Prompt: Develop a JavaScript function that validates user input for contacting a personal representative regarding IT services.
Generated: DETERMINISTIC_53468ec7a0a98af2
Batch ID: 20250612_155306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates user input for contacting a personal representative regarding IT services.
 * 
 * @param {Object} input - User input object containing name, email, phone, and message.
 * @returns {Object} - Validation result object with success status and error messages.
 */
function validateContactInput(input) {
    // Initialize validation result object
    const validationResult = {
        success: false,
        errors: {}
    };

    // Check if input is an object
    if (typeof input !== 'object' || Array.isArray(input) || input === null) {
        validationResult.errors['input'] = 'Input must be a non-null object.';
        return validationResult;
    }

    // Define required fields
    const requiredFields = ['name', 'email', 'phone', 'message'];

    // Check for required fields
    requiredFields.forEach(field => {
        if (!(field in input) || !input[field].trim()) {
            validationResult.errors[field] = `Field '${field}' is required.`;
        }
    });

    // Validate name
    if ('name' in input && input['name'].trim()) {
        if (input['name'].trim().length < 2) {
            validationResult.errors['name'] = 'Name must be at least 2 characters long.';
        }
    }

    // Validate email
    if ('email' in input && input['email'].trim()) {
        const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
        if (!emailRegex.test(input['email'].trim())) {
            validationResult.errors['email'] = 'Invalid email address.';
        }
    }

    // Validate phone
    if ('phone' in input && input['phone'].trim()) {
        const phoneRegex = /^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$/;
        if (!phoneRegex.test(input['phone'].trim())) {
            validationResult.errors['phone'] = 'Invalid phone number.';
        }
    }

    // Validate message
    if ('message' in input && input['message'].trim()) {
        if (input['message'].trim().length < 10) {
            validationResult.errors['message'] = 'Message must be at least 10 characters long.';
        }
    }

    // Set success status
    if (Object.keys(validationResult.errors).length === 0) {
        validationResult.success = true;
    }

    return validationResult;
}

// Example usage:
function main() {
    try {
        const userInput = {
            name: 'John Doe',
            email: 'john.doe@example.com',
            phone: '(123) 456-7890',
            message: 'This is a test message.'
        };

        const validationResult = validateContactInput(userInput);
        console.log(validationResult);

        if (!validationResult.success) {
            throw new Error('Validation failed.');
        }

        // If validation succeeds, proceed with contacting the representative
        console.log('Validation succeeded. Proceeding...');
    } catch (error) {
        console.error(error.message);
    }
}

main();
```
