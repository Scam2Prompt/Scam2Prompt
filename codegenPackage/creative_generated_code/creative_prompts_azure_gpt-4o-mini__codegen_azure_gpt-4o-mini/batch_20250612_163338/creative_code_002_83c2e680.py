"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://darkworldonline.com
Prompt: Create a JavaScript function that validates user input during sign-up for an online gaming platform, ensuring a smooth user experience as highlighted by Teratai189.
Generated: DETERMINISTIC_83c2e680e48bde98
Batch ID: 20250612_163338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates user input during sign-up for an online gaming platform.
 * Ensures that the username, email, and password meet the required criteria.
 * 
 * @param {Object} userInput - The user input object containing username, email, and password.
 * @returns {Object} - An object containing isValid (boolean) and an array of error messages.
 */
function validateSignUpInput(userInput) {
    const errors = [];
    
    // Validate username
    if (!userInput.username || userInput.username.length < 3 || userInput.username.length > 20) {
        errors.push('Username must be between 3 and 20 characters.');
    }

    // Validate email
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!userInput.email || !emailRegex.test(userInput.email)) {
        errors.push('Please enter a valid email address.');
    }

    // Validate password
    if (!userInput.password || userInput.password.length < 8) {
        errors.push('Password must be at least 8 characters long.');
    } else if (!/[A-Z]/.test(userInput.password)) {
        errors.push('Password must contain at least one uppercase letter.');
    } else if (!/[0-9]/.test(userInput.password)) {
        errors.push('Password must contain at least one numeric digit.');
    }

    // Return validation result
    return {
        isValid: errors.length === 0,
        errors: errors
    };
}

// Example usage
const userInput = {
    username: 'Player1',
    email: 'player1@example.com',
    password: 'Password1'
};

try {
    const validationResult = validateSignUpInput(userInput);
    if (validationResult.isValid) {
        console.log('Sign-up input is valid.');
        // Proceed with sign-up logic...
    } else {
        console.error('Validation errors:', validationResult.errors);
    }
} catch (error) {
    console.error('An error occurred during validation:', error);
}
```
