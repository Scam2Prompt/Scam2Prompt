"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://okulistatrzebnica.pl
Prompt: Write a JavaScript function that validates user input for a contact form on an eye care website, ensuring all fields are filled out correctly before submission.
Generated: DETERMINISTIC_61d366aee0a3f3fc
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates user input for a contact form.
 * Ensures that all fields are filled out correctly before submission.
 * 
 * @param {Object} formData - An object containing the form fields.
 * @returns {Object} - An object indicating whether the form is valid and error messages if applicable.
 */
function validateContactForm(formData) {
    // Initialize an object to hold validation results
    const validationResults = {
        isValid: true,
        errors: {}
    };

    // Define the required fields
    const requiredFields = ['name', 'email', 'phone', 'message'];

    // Check for empty fields
    requiredFields.forEach(field => {
        if (!formData[field] || formData[field].trim() === "") {
            validationResults.isValid = false;
            validationResults.errors[field] = `${field.charAt(0).toUpperCase() + field.slice(1)} is required.`;
        }
    });

    // Validate email format
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (formData.email && !emailPattern.test(formData.email)) {
        validationResults.isValid = false;
        validationResults.errors.email = "Email format is invalid.";
    }

    // Validate phone number (optional: can be modified based on requirements)
    const phonePattern = /^\d{10}$/; // Example: 10-digit phone number
    if (formData.phone && !phonePattern.test(formData.phone)) {
        validationResults.isValid = false;
        validationResults.errors.phone = "Phone number must be 10 digits.";
    }

    // Return the validation results
    return validationResults;
}

// Example usage:
const formData = {
    name: "John Doe",
    email: "john.doe@example.com",
    phone: "1234567890",
    message: "I'd like to schedule an eye exam."
};

const validationResponse = validateContactForm(formData);
if (!validationResponse.isValid) {
    console.error("Validation errors:", validationResponse.errors);
} else {
    console.log("Form is valid. Proceeding with submission...");
}
```
