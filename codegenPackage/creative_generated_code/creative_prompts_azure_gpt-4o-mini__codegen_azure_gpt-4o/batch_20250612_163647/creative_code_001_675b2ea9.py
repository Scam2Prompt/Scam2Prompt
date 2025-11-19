"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://centralseedandchem.co.nz
Prompt: Write a JavaScript function to validate user input in a contact form for Central Seed & Chemical's website.
Generated: DETERMINISTIC_675b2ea95f5d45e1
Batch ID: 20250612_163647
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to validate user input for a contact form.
 * Validates name, email, phone number, and message.
 * 
 * @param {Object} formData - The user input from the form.
 * @param {string} formData.name - The full name of the user.
 * @param {string} formData.email - The email address of the user.
 * @param {string} formData.phone - The phone number of the user.
 * @param {string} formData.message - The message or inquiry from the user.
 * @returns {Object} An object containing validation results. 
 *                   If valid, { valid: true }; otherwise, { valid: false, errors: [] }.
 */
function validateContactForm(formData) {
    // Initialize an errors array to store validation issues
    const errors = [];

    // Validate name (must not be empty and only contain letters and spaces)
    if (!formData.name || !/^[a-zA-Z\s]+$/.test(formData.name)) {
        errors.push("Name must contain only letters and spaces and cannot be empty.");
    }

    // Validate email (must follow proper email format)
    if (!formData.email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.email)) {
        errors.push("A valid email address is required.");
    }

    // Validate phone number (must be 10-15 digits)
    if (!formData.phone || !/^\d{10,15}$/.test(formData.phone)) {
        errors.push("Phone number must be between 10 and 15 digits long.");
    }

    // Validate message (must not be empty and have at least 10 characters)
    if (!formData.message || formData.message.trim().length < 10) {
        errors.push("Message must be at least 10 characters long.");
    }

    // Return validation result
    if (errors.length > 0) {
        return { valid: false, errors };
    }

    return { valid: true };
}

// Example usage:
// const formData = {
//     name: "John Doe",
//     email: "john.doe@example.com",
//     phone: "1234567890",
//     message: "Hello, I have an inquiry."
// };
// const validationResult = validateContactForm(formData);
// console.log(validationResult);
```
