"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://symbiotic.eu
Prompt: Develop a JavaScript function that validates user input for contacting a personal representative regarding IT services.
Generated: DETERMINISTIC_53468ec7a0a98af2
Batch ID: 20250612_155306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates user input for contacting a personal representative regarding IT services.
 * 
 * @param {Object} inputData - The object containing user input data.
 * @param {string} inputData.name - The user's name.
 * @param {string} inputData.email - The user's email address.
 * @param {string} inputData.message - The user's message.
 * @returns {Object} - Returns an object containing validation status and errors (if any).
 */
function validateContactForm(inputData) {
    const errors = [];
    const result = { isValid: true, errors: [] };

    try {
        // Validate name: Must be provided and contain only letters and spaces
        if (!inputData.name || typeof inputData.name !== 'string' || !/^[a-zA-Z\s]+$/.test(inputData.name)) {
            errors.push("Name must be a non-empty string containing only letters and spaces.");
        }

        // Validate email: Must be provided and follow standard email format
        if (!inputData.email || typeof inputData.email !== 'string' || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(inputData.email)) {
            errors.push("Email must be a valid email address.");
        }

        // Validate message: Must be provided and not be empty
        if (!inputData.message || typeof inputData.message !== 'string' || inputData.message.trim() === "") {
            errors.push("Message must be a non-empty string.");
        }

        // Check for validation errors
        if (errors.length > 0) {
            result.isValid = false;
            result.errors = errors;
        }

        return result;
    } catch (error) {
        // Handle unexpected errors gracefully
        console.error("An error occurred during validation:", error);
        return { isValid: false, errors: ["An unexpected error occurred. Please try again."] };
    }
}

// Example usage
const userInput = {
    name: "John Doe",
    email: "john.doe@example.com",
    message: "I am interested in your IT services."
};

const validationResult = validateContactForm(userInput);
if (validationResult.isValid) {
    console.log("Validation successful! User input is valid.");
} else {
    console.log("Validation failed. Errors:", validationResult.errors);
}
```
