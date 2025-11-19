"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://travelobay.com
Prompt: Create a function in JavaScript that allows users to register on R7 Casino, including input validation for email and password strength.
Generated: DETERMINISTIC_9ebb978d64daa3c0
Batch ID: 20250612_155233
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to register a user on R7 Casino.
 * Validates user input for email format and password strength.
 * Stores user data if validation passes.
 * 
 * @param {string} email - User's email address.
 * @param {string} password - User's chosen password.
 * @returns {object} - Returns success message or error details.
 */
function registerUser(email, password) {
    // Regular expression for validating email format
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    // Regular expression for validating password strength
    // Password must be at least 8 characters long and include
    // at least one uppercase letter, one lowercase letter, one number, and one special character.
    const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{8,}$/;

    // Validate email format
    if (!emailRegex.test(email)) {
        return {
            success: false,
            error: "Invalid email format. Please provide a valid email address."
        };
    }

    // Validate password strength
    if (!passwordRegex.test(password)) {
        return {
            success: false,
            error: "Weak password. Password must be at least 8 characters long and include one uppercase letter, one lowercase letter, one number, and one special character."
        };
    }

    // Simulated user database (in a real application, this would involve database interaction)
    const userDatabase = [];

    // Check if email already exists in the database
    const userExists = userDatabase.some(user => user.email === email);

    if (userExists) {
        return {
            success: false,
            error: "Email is already registered. Please use a different email address."
        };
    }

    // Register the user
    const newUser = {
        email: email,
        password: password // Note: In production, passwords should be hashed using a library like bcrypt.
    };

    userDatabase.push(newUser);

    return {
        success: true,
        message: "Registration successful. Welcome to R7 Casino!"
    };
}

// Example usage:
const result = registerUser("test@example.com", "StrongP@ssw0rd!");
console.log(result);
```
