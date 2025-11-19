"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-flow.com
Prompt: Create a JavaScript function that validates user input for the registration form on Immediate Flow, ensuring that names and email addresses meet the required criteria.
Generated: DETERMINISTIC_3d694b9e124a27f2
Batch ID: 20250612_163052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates user input for a registration form.
 * 
 * @param {Object} userInput - An object containing user input data.
 * @param {string} userInput.name - The name of the user.
 * @param {string} userInput.email - The email address of the user.
 * @returns {Object} - An object containing validation results and messages.
 */
function validateRegistrationForm(userInput) {
    // Initialize an object to hold validation results
    const validationResults = {
        isValid: true,
        messages: []
    };

    // Validate name
    if (!userInput.name || userInput.name.trim().length < 2) {
        validationResults.isValid = false;
        validationResults.messages.push("Name must be at least 2 characters long.");
    } else if (!/^[a-zA-Z\s]+$/.test(userInput.name)) {
        validationResults.isValid = false;
        validationResults.messages.push("Name can only contain letters and spaces.");
    }

    // Validate email
    if (!userInput.email || userInput.email.trim().length === 0) {
        validationResults.isValid = false;
        validationResults.messages.push("Email is required.");
    } else if (!isValidEmail(userInput.email)) {
        validationResults.isValid = false;
        validationResults.messages.push("Email format is invalid.");
    }

    return validationResults;
}

/**
 * Checks if an email address is valid based on a simple regex pattern.
 * 
 * @param {string} email - The email address to validate.
 * @returns {boolean} - True if the email is valid; otherwise, false.
 */
function isValidEmail(email) {
    const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return emailRegex.test(email);
}

// Example usage:
try {
    const userInput = {
        name: "John Doe",
        email: "john.doe@example.com"
    };
    const validation = validateRegistrationForm(userInput);
    if (validation.isValid) {
        console.log("Registration input is valid.");
    } else {
        console.error("Validation errors:", validation.messages.join(" "));
    }
} catch (error) {
    console.error("An error occurred during validation:", error);
}
```
