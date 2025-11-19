"""
Generated Code Metadata:
========================
Original URL: https://melikataheri.com
Prompt: Create a JavaScript function that validates user input for a registration form for the "Elusive Self-Love" webinar, ensuring it captures necessary details as outlined on Melika Taheri's site.
Generated: DETERMINISTIC_a24616136ba0c683
Batch ID: 20250612_163851
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates user input for the "Elusive Self-Love" webinar registration form.
 * 
 * @param {Object} formData - The user input data from the registration form.
 * @param {string} formData.name - The name of the user.
 * @param {string} formData.email - The email address of the user.
 * @param {string} formData.phone - The phone number of the user.
 * @param {string} formData.age - The age of the user.
 * @returns {Object} - An object containing validation results and messages.
 */
function validateRegistrationForm(formData) {
    const validationResults = {
        isValid: true,
        messages: []
    };

    // Validate name
    if (!formData.name || formData.name.trim().length === 0) {
        validationResults.isValid = false;
        validationResults.messages.push("Name is required.");
    }

    // Validate email
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!formData.email || !emailRegex.test(formData.email)) {
        validationResults.isValid = false;
        validationResults.messages.push("A valid email address is required.");
    }

    // Validate phone number
    const phoneRegex = /^\+?[1-9]\d{1,14}$/; // E.164 format
    if (!formData.phone || !phoneRegex.test(formData.phone)) {
        validationResults.isValid = false;
        validationResults.messages.push("A valid phone number is required.");
    }

    // Validate age
    const age = parseInt(formData.age, 10);
    if (isNaN(age) || age < 18 || age > 120) {
        validationResults.isValid = false;
        validationResults.messages.push("Age must be a number between 18 and 120.");
    }

    return validationResults;
}

// Example usage
try {
    const userInput = {
        name: "John Doe",
        email: "john.doe@example.com",
        phone: "+1234567890",
        age: "30"
    };

    const validation = validateRegistrationForm(userInput);
    if (validation.isValid) {
        console.log("Registration is valid.");
    } else {
        console.error("Validation errors:", validation.messages);
    }
} catch (error) {
    console.error("An error occurred during validation:", error);
}
```
