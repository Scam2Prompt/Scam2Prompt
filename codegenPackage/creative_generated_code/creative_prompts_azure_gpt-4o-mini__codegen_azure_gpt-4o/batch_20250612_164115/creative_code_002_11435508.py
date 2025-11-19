"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unitedcabinetry.com.au
Prompt: Create a JavaScript function that validates user input for a cabinetry consultation request form, ensuring all required fields are filled out correctly.
Generated: DETERMINISTIC_11435508d7fabacc
Batch ID: 20250612_164115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates user input for a cabinetry consultation request form.
 * Ensures all required fields are filled out and meet basic criteria.
 *
 * @param {Object} formData - The input data from the form.
 * @returns {Object} - An object containing `isValid` (boolean) and `errors` (array of error messages).
 */
function validateConsultationForm(formData) {
    const errors = [];
    
    // Required fields
    const requiredFields = ['name', 'email', 'phone', 'address', 'projectDetails'];

    // Check that all required fields are present and not empty
    requiredFields.forEach(field => {
        if (!formData[field] || formData[field].trim() === '') {
            errors.push(`${field} is required.`);
        }
    });

    // Validate email format
    if (formData.email && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.email)) {
        errors.push('Invalid email format.');
    }

    // Validate phone number (basic check for digits only and length)
    if (formData.phone && !/^\d{10}$/.test(formData.phone)) {
        errors.push('Invalid phone number. It should be 10 digits.');
    }

    // Validate project details minimum length
    if (formData.projectDetails && formData.projectDetails.trim().length < 20) {
        errors.push('Project details must be at least 20 characters long.');
    }
    
    return {
        isValid: errors.length === 0,
        errors: errors
    };
}

// Example usage
const userInput = {
    name: "John Doe",
    email: "john.doe@example.com",
    phone: "1234567890",
    address: "123 Elm Street",
    projectDetails: "Looking to install new kitchen cabinets."
};

const validationResult = validateConsultationForm(userInput);

if (!validationResult.isValid) {
    console.log("Validation Errors:", validationResult.errors);
} else {
    console.log("Form is valid!");
}
```
