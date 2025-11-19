"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ecolux-btp.com
Prompt: Create a JavaScript function that validates user input for a construction project inquiry form, ensuring fields like name, email, and project details are correctly filled, based on the contact process at ECOLUX.
Generated: DETERMINISTIC_5fa486a4490c3819
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
 * Validates user input fields for a construction project inquiry form.
 * The form includes fields: name, email, and project details.
 * 
 * @param {Object} formData - An object containing form data.
 * @param {string} formData.name - The user's name.
 * @param {string} formData.email - The user's email address.
 * @param {string} formData.projectDetails - Details about the construction project.
 * @returns {Object} - An object with validation result and error messages (if any).
 */
function validateInquiryForm(formData) {
    const errors = {};

    // Validate name (must be at least 2 characters long and contain only letters)
    if (!formData.name || formData.name.trim().length < 2) {
        errors.name = "Name must be at least 2 characters long.";
    } else if (!/^[a-zA-Z\s]+$/.test(formData.name.trim())) {
        errors.name = "Name must contain only letters and spaces.";
    }

    // Validate email (must match basic email format)
    if (!formData.email || formData.email.trim().length === 0) {
        errors.email = "Email is required.";
    } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.email.trim())) {
        errors.email = "Invalid email format.";
    }

    // Validate project details (must be at least 10 characters long)
    if (!formData.projectDetails || formData.projectDetails.trim().length < 10) {
        errors.projectDetails = "Project details must be at least 10 characters long.";
    }

    // Return validation result
    return {
        isValid: Object.keys(errors).length === 0,
        errors: errors
    };
}

// Example usage
const formInput = {
    name: "John Doe",
    email: "john.doe@example.com",
    projectDetails: "Looking to build a modern eco-friendly house."
};

const validationResult = validateInquiryForm(formInput);

if (validationResult.isValid) {
    console.log("Form is valid. Ready for submission.");
} else {
    console.error("Form validation failed:", validationResult.errors);
}
```
