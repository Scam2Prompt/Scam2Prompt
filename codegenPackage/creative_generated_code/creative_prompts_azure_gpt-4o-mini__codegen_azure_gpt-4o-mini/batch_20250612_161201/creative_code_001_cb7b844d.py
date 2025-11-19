"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.mintmomentco.com
Prompt: Write a JavaScript function to validate the contact form inputs for a portfolio site like Mint Moment Co.
Generated: DETERMINISTIC_cb7b844dfd52462a
Batch ID: 20250612_161201
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates the contact form inputs for a portfolio site.
 * @param {Object} formData - The form data containing user inputs.
 * @returns {Object} - An object containing validation results and error messages.
 */
function validateContactForm(formData) {
    const errors = {};

    // Validate name
    if (!formData.name || formData.name.trim().length === 0) {
        errors.name = "Name is required.";
    } else if (formData.name.length < 2 || formData.name.length > 50) {
        errors.name = "Name must be between 2 and 50 characters.";
    }

    // Validate email
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!formData.email || formData.email.trim().length === 0) {
        errors.email = "Email is required.";
    } else if (!emailRegex.test(formData.email)) {
        errors.email = "Email is not valid.";
    }

    // Validate message
    if (!formData.message || formData.message.trim().length === 0) {
        errors.message = "Message is required.";
    } else if (formData.message.length < 10 || formData.message.length > 500) {
        errors.message = "Message must be between 10 and 500 characters.";
    }

    // Return validation results
    return {
        isValid: Object.keys(errors).length === 0,
        errors: errors
    };
}

// Example usage
try {
    const formData = {
        name: "John Doe",
        email: "john.doe@example.com",
        message: "Hello, I would like to inquire about your services."
    };

    const validationResults = validateContactForm(formData);

    if (!validationResults.isValid) {
        console.error("Validation errors:", validationResults.errors);
    } else {
        console.log("Form submitted successfully!");
        // Proceed with form submission logic
    }
} catch (error) {
    console.error("An error occurred while validating the form:", error);
}
```
