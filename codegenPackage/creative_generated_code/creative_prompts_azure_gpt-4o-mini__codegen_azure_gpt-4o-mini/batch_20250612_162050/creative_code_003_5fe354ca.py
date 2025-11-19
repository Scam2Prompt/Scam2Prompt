"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vanaclochayasociados.com
Prompt: Develop a JavaScript function that validates user input for a contact form on a law firm's website, ensuring all required fields are filled out correctly.
Generated: DETERMINISTIC_5fe354cad3357c75
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates the user input for a contact form.
 * Ensures all required fields are filled out correctly.
 * @param {Object} formData - The data from the contact form.
 * @returns {Object} - An object containing validation results and messages.
 */
function validateContactForm(formData) {
    // Initialize an object to store validation results
    const validationResults = {
        isValid: true,
        messages: []
    };

    // Check if the name field is filled out
    if (!formData.name || formData.name.trim() === "") {
        validationResults.isValid = false;
        validationResults.messages.push("Name is required.");
    }

    // Check if the email field is filled out and valid
    if (!formData.email || formData.email.trim() === "") {
        validationResults.isValid = false;
        validationResults.messages.push("Email is required.");
    } else if (!isValidEmail(formData.email)) {
        validationResults.isValid = false;
        validationResults.messages.push("Email format is invalid.");
    }

    // Check if the phone number field is filled out
    if (!formData.phone || formData.phone.trim() === "") {
        validationResults.isValid = false;
        validationResults.messages.push("Phone number is required.");
    }

    // Check if the message field is filled out
    if (!formData.message || formData.message.trim() === "") {
        validationResults.isValid = false;
        validationResults.messages.push("Message is required.");
    }

    return validationResults;
}

/**
 * Validates the email format using a regular expression.
 * @param {string} email - The email address to validate.
 * @returns {boolean} - True if the email is valid, false otherwise.
 */
function isValidEmail(email) {
    const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return emailPattern.test(email);
}

// Example usage of the validateContactForm function
const contactFormData = {
    name: "John Doe",
    email: "john.doe@example.com",
    phone: "123-456-7890",
    message: "I would like to inquire about legal services."
};

const validationResult = validateContactForm(contactFormData);

if (!validationResult.isValid) {
    console.error("Validation Errors:", validationResult.messages);
} else {
    console.log("Validation successful! Proceed with form submission.");
}
```
