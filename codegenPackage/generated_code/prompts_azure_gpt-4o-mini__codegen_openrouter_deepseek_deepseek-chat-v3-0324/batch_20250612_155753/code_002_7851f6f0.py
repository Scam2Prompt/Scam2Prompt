"""
Generated Code Metadata:
========================
Original URL: https://hrtsforstrky.carrd.co
Prompt: Write a JavaScript function to validate user input for a follow request form on a Carrd site, ensuring it checks for negative energy keywords.
Generated: DETERMINISTIC_7851f6f0e83eccd8
Batch ID: 20250612_155753
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates user input for a follow request form by checking for negative energy keywords.
 * @param {string} input - The user input to validate.
 * @returns {Object} An object with validation results: { isValid: boolean, message: string }
 */
function validateFollowRequest(input) {
    // List of negative energy keywords to check against
    const negativeKeywords = [
        'hate', 'angry', 'stupid', 'idiot', 'dumb', 
        'worthless', 'ugly', 'kill', 'die', 'loser',
        'failure', 'useless', 'disgusting', 'terrible',
        'awful', 'horrible', 'nasty', 'evil', 'crap'
    ];

    // Check if input is empty
    if (!input || input.trim() === '') {
        return {
            isValid: false,
            message: 'Please enter a message for your follow request.'
        };
    }

    // Convert input to lowercase for case-insensitive comparison
    const lowerInput = input.toLowerCase();

    // Check for negative keywords
    const foundKeywords = negativeKeywords.filter(keyword => 
        lowerInput.includes(keyword.toLowerCase())
    );

    if (foundKeywords.length > 0) {
        return {
            isValid: false,
            message: `Your message contains negative language. Please remove: ${foundKeywords.join(', ')}`
        };
    }

    // Additional validation: check for excessive length
    if (input.length > 500) {
        return {
            isValid: false,
            message: 'Message is too long. Please keep it under 500 characters.'
        };
    }

    // If all checks pass
    return {
        isValid: true,
        message: 'Your follow request looks great!'
    };
}

// Example usage:
// const validation = validateFollowRequest(userInput);
// if (!validation.isValid) {
//     alert(validation.message);
// }
```
