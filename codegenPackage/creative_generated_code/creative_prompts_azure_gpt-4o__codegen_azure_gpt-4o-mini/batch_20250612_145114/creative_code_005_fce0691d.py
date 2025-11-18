"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://collab.host
Prompt: Write a JavaScript function to validate form fields (e.g., name and email) for webinar registration, as seen on the collab.host website.
Generated: DETERMINISTIC_fce0691d0a8ebd31
Batch ID: 20250612_145114
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates form fields for webinar registration.
 * It checks if the name is non-empty and if the email is in a valid format.
 * 
 * @param {string} name - The name of the registrant.
 * @param {string} email - The email of the registrant.
 * @returns {Object} An object containing validation results and messages.
 */
function validateRegistrationForm(name, email) {
    const validationResults = {
        isValid: true,
        messages: []
    };

    // Validate name
    if (!name || name.trim().length === 0) {
        validationResults.isValid = false;
        validationResults.messages.push("Name is required.");
    }

    // Validate email using a regular expression
    const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    if (!email || !emailPattern.test(email)) {
        validationResults.isValid = false;
        validationResults.messages.push("A valid email is required.");
    }

    return validationResults;
}

// Example usage
try {
    const nameInput = "John Doe"; // Replace with actual input
    const emailInput = "john.doe@example.com"; // Replace with actual input

    const validation = validateRegistrationForm(nameInput, emailInput);
    if (!validation.isValid) {
        console.error("Validation errors:", validation.messages);
    } else {
        console.log("Registration details are valid.");
    }
} catch (error) {
    console.error("An error occurred during validation:", error.message);
}
```
