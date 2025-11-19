"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bolehshop.id
Prompt: Create a JavaScript function that validates user input for a lottery registration form, inspired by the user-friendly design of HONGTOGEL.
Generated: DETERMINISTIC_838acd80887fd02b
Batch ID: 20250612_164238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates user input for a lottery registration form.
 * Ensures the input meets specified criteria:
 * - Name: non-empty and only letters
 * - Age: must be a number between 18 and 99
 * - Email: valid email format
 * - Phone: valid phone number (10-15 digits)
 * 
 * @param {Object} userInput - The user input object containing registration details.
 * @returns {Object} result - An object indicating success or failure and errors if any.
 */
function validateLotteryRegistration(userInput) {
    // Initialize the result object
    const result = {
        isValid: true,
        errors: []
    };

    // Validate Name
    if (!userInput.name || !/^[a-zA-Z\s]+$/.test(userInput.name)) {
        result.isValid = false;
        result.errors.push("Name must be a non-empty string containing only letters.");
    }

    // Validate Age
    if (typeof userInput.age !== 'number' || userInput.age < 18 || userInput.age > 99) {
        result.isValid = false;
        result.errors.push("Age must be a number between 18 and 99.");
    }

    // Validate Email
    if (!userInput.email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(userInput.email)) {
        result.isValid = false;
        result.errors.push("Email must be a valid email format.");
    }

    // Validate Phone
    if (!userInput.phone || !/^\d{10,15}$/.test(userInput.phone)) {
        result.isValid = false;
        result.errors.push("Phone number must be between 10 and 15 digits.");
    }

    return result;
}

// Example usage:
const userRegistration = {
    name: "John Doe",
    age: 25,
    email: "john.doe@example.com",
    phone: "1234567890"
};

const validationResult = validateLotteryRegistration(userRegistration);
if (validationResult.isValid) {
    console.log("Registration is valid.");
} else {
    console.log("Registration failed with the following errors:");
    console.error(validationResult.errors);
}
```
