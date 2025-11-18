"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://panchapakesan.com
Prompt: Create a validation script in JavaScript for a ticket booking form that ensures the "Email Address" is properly formatted, the "Phone Number" contains only digits, and at least one "Preferred Method of Communication" is selected.
Generated: DETERMINISTIC_3f1fcb838e673f27
Batch ID: 20250612_154529
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// TicketBookingFormValidator.js

/**
 * Validates the input fields of a ticket booking form.
 */
class TicketBookingFormValidator {
    /**
     * Validates the email address format.
     * @param {string} email - The email address to validate.
     * @returns {boolean} - True if valid, false otherwise.
     */
    static validateEmail(email) {
        // Regular expression for validating an email address
        const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
        return emailPattern.test(email);
    }

    /**
     * Validates the phone number to ensure it contains only digits.
     * @param {string} phone - The phone number to validate.
     * @returns {boolean} - True if valid, false otherwise.
     */
    static validatePhone(phone) {
        // Regular expression to match only digits
        const phonePattern = /^\d+$/;
        return phonePattern.test(phone);
    }

    /**
     * Validates that at least one preferred method of communication is selected.
     * @param {Array} methods - An array of selected communication methods.
     * @returns {boolean} - True if at least one method is selected, false otherwise.
     */
    static validateCommunicationMethod(methods) {
        return methods.length > 0; // Checks if the array has at least one item
    }

    /**
     * Validates the entire ticket booking form.
     * @param {Object} formData - The form data object containing email, phone, and methods.
     * @returns {Object} - An object containing validation results and messages.
     */
    static validateForm(formData) {
        const validationResults = {
            isValid: true,
            errors: []
        };

        // Validate email
        if (!this.validateEmail(formData.email)) {
            validationResults.isValid = false;
            validationResults.errors.push("Invalid email format.");
        }

        // Validate phone number
        if (!this.validatePhone(formData.phone)) {
            validationResults.isValid = false;
            validationResults.errors.push("Phone number must contain only digits.");
        }

        // Validate preferred communication methods
        if (!this.validateCommunicationMethod(formData.communicationMethods)) {
            validationResults.isValid = false;
            validationResults.errors.push("At least one preferred method of communication must be selected.");
        }

        return validationResults;
    }
}

// Example usage
const formData = {
    email: "test@example.com",
    phone: "1234567890",
    communicationMethods: ["email"] // Can be empty or contain selected methods
};

const validationResult = TicketBookingFormValidator.validateForm(formData);

// Output validation results
if (validationResult.isValid) {
    console.log("Form is valid!");
} else {
    console.error("Validation errors:", validationResult.errors);
}
```
