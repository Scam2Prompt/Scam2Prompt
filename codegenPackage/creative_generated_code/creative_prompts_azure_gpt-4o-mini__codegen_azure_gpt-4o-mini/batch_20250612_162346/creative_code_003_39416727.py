"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://myrolandclaim.org
Prompt: Create a JavaScript function that validates user input for registering in the Roland Consumer Claim, ensuring it meets the eligibility criteria.
Generated: DETERMINISTIC_394167273cd28858
Batch ID: 20250612_162346
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates user input for registering in the Roland Consumer Claim.
 *
 * @param {Object} userInput - The user input object containing registration details.
 * @param {string} userInput.name - The name of the user.
 * @param {string} userInput.email - The email address of the user.
 * @param {string} userInput.claimNumber - The claim number associated with the user.
 * @param {string} userInput.productPurchased - The product name purchased by the user.
 * @returns {Object} - An object containing 'isValid' boolean and 'errors' array with validation messages.
 */
function validateRegistration(userInput) {
    const errors = [];
    let isValid = true;

    // Validate name
    if (!userInput.name || userInput.name.trim().length === 0) {
        errors.push("Name is required.");
        isValid = false;
    }

    // Validate email
    if (!userInput.email || !isValidEmail(userInput.email)) {
        errors.push("Valid email is required.");
        isValid = false;
    }

    // Validate claim number
    if (!userInput.claimNumber || !/^\d{5}$/.test(userInput.claimNumber)) {
        errors.push("Claim number must be a 5-digit number.");
        isValid = false;
    }

    // Validate product purchased
    if (!userInput.productPurchased || userInput.productPurchased.trim().length === 0) {
        errors.push("Product purchased is required.");
        isValid = false;
    }

    return {
        isValid,
        errors
    };
}

/**
 * Validates email format using a regular expression.
 *
 * @param {string} email - The email address to validate.
 * @returns {boolean} - True if the email format is valid, otherwise false.
 */
function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

// Example usage:
const userInput = {
    name: "John Doe",
    email: "johndoe@example.com",
    claimNumber: "12345",
    productPurchased: "Roland Synthesizer"
};

const validationResult = validateRegistration(userInput);

if (validationResult.isValid) {
    console.log("Registration is valid.");
} else {
    console.error("Registration errors:", validationResult.errors);
}
```
