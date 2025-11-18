"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://twmassociates.co.za
Prompt: Create a JavaScript function to validate form inputs (e.g., name, email, subject, message) for a consultation request form, similar to the one on the TWM Associates website.
Generated: DETERMINISTIC_276edfffadaed435
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates form inputs for a consultation request form.
 * 
 * @param {Object} formData - An object containing form inputs.
 * @param {string} formData.name - The name of the user.
 * @param {string} formData.email - The email address of the user.
 * @param {string} formData.subject - The subject of the message.
 * @param {string} formData.message - The content of the message.
 * @returns {Object} - An object containing validation results.
 */
function validateFormInputs(formData) {
    const errors = {};

    // Validate name
    if (!formData.name || formData.name.trim().length === 0) {
        errors.name = "Name is required.";
    }

    // Validate email
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!formData.email) {
        errors.email = "Email is required.";
    } else if (!emailRegex.test(formData.email)) {
        errors.email = "Email is invalid.";
    }

    // Validate subject
    if (!formData.subject || formData.subject.trim().length === 0) {
        errors.subject = "Subject is required.";
    }

    // Validate message
    if (!formData.message || formData.message.trim().length === 0) {
        errors.message = "Message is required.";
    } else if (formData.message.length < 10) {
        errors.message = "Message must be at least 10 characters long.";
    }

    // Return validation results
    return {
        isValid: Object.keys(errors).length === 0,
        errors
    };
}

// Example usage:
const formData = {
    name: "John Doe",
    email: "john.doe@example.com",
    subject: "Consultation Request",
    message: "I would like to know more about your services."
};

const validationResult = validateFormInputs(formData);

if (!validationResult.isValid) {
    console.error("Validation failed: ", validationResult.errors);
} else {
    console.log("Validation succeeded!");
}
```
