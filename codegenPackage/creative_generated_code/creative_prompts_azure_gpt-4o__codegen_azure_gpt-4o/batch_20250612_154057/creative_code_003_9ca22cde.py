"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.hypersteakin.site
Prompt: Create a JavaScript function to manage registrations for the HyperSteakin Gaming Summit, including options for selecting pass types (Digital Pass or Berlin Experience) and validating user inputs.
Generated: DETERMINISTIC_9ca22cdef7163357
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to manage registrations for the HyperSteakin Gaming Summit.
 * Allows users to select pass types and validates user inputs.
 * 
 * Pass Types:
 * - Digital Pass
 * - Berlin Experience
 * 
 * Input validation includes:
 * - Required fields (name, email, pass type)
 * - Valid email format
 */

// Registration function
function registerForSummit(name, email, passType) {
    // Available pass types
    const validPassTypes = ["Digital Pass", "Berlin Experience"];

    try {
        // Validate inputs
        validateInputs(name, email, passType, validPassTypes);

        // Simulate registration process (could be replaced with a database call)
        const registrationDetails = {
            name,
            email,
            passType,
            registrationDate: new Date().toISOString(),
        };

        console.log("Registration successful!", registrationDetails);
        return registrationDetails; // Return details for further processing if needed
    } catch (error) {
        console.error("Registration failed:", error.message);
        return { success: false, message: error.message };
    }
}

/**
 * Validates user inputs for the registration process.
 * @param {string} name - User's name
 * @param {string} email - User's email address
 * @param {string} passType - Type of pass selected
 * @param {string[]} validPassTypes - List of valid pass types
 * @throws {Error} Throws validation error if inputs are invalid
 */
function validateInputs(name, email, passType, validPassTypes) {
    // Check if name is provided
    if (!name || typeof name !== "string") {
        throw new Error("Name is required and must be a string.");
    }

    // Check if email is provided and has a valid format
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!email || !emailRegex.test(email)) {
        throw new Error("A valid email address is required.");
    }

    // Check if pass type is valid
    if (!validPassTypes.includes(passType)) {
        throw new Error(`Pass type must be one of the following: ${validPassTypes.join(", ")}.`);
    }
}

// Example usage
registerForSummit("John Doe", "john.doe@example.com", "Berlin Experience");
```
