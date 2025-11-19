"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://superiortitlemontana.com
Prompt: Develop a JavaScript function that validates user input in the property information request form on the Superior Title Montana website.
Generated: DETERMINISTIC_1985f8b9f2fd5379
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
 * Validates user input for the property information request form.
 * Ensures that all required fields are filled out correctly.
 * 
 * @param {Object} formData - The data object containing user input from the form.
 * @returns {Object} - An object containing validation results. 
 *                     { isValid: boolean, errors: Array<string> }
 */
function validatePropertyInfoRequest(formData) {
    const errors = [];
    
    // Check for empty fields
    if (!formData.name || formData.name.trim() === "") {
        errors.push("Name is required.");
    }
    
    if (!formData.email || formData.email.trim() === "") {
        errors.push("Email is required.");
    } else if (!validateEmail(formData.email)) {
        errors.push("Email format is invalid.");
    }
    
    if (!formData.phone || formData.phone.trim() === "") {
        errors.push("Phone number is required.");
    } else if (!validatePhone(formData.phone)) {
        errors.push("Phone number format is invalid.");
    }
    
    if (!formData.propertyAddress || formData.propertyAddress.trim() === "") {
        errors.push("Property address is required.");
    }
    
    // Return validation result
    return {
        isValid: errors.length === 0,
        errors: errors
    };
}

/**
 * Validates the format of an email address.
 * 
 * @param {string} email - The email address to validate.
 * @returns {boolean} - True if the email format is valid, false otherwise.
 */
function validateEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

/**
 * Validates the format of a phone number.
 * 
 * @param {string} phone - The phone number to validate.
 * @returns {boolean} - True if the phone number format is valid, false otherwise.
 */
function validatePhone(phone) {
    const phoneRegex = /^\+?[1-9]\d{1,14}$/; // E.164 format
    return phoneRegex.test(phone);
}

// Example usage:
const formData = {
    name: "John Doe",
    email: "john.doe@example.com",
    phone: "+1234567890",
    propertyAddress: "123 Main St, Anytown, MT"
};

const validationResult = validatePropertyInfoRequest(formData);
if (!validationResult.isValid) {
    console.error("Validation errors:", validationResult.errors);
} else {
    console.log("Validation successful!");
}
```
