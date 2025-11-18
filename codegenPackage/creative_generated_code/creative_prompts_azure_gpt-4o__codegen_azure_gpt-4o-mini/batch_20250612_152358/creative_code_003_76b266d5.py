"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-bonkbox.web.app
Prompt: Create a JavaScript function that checks if a user is on a whitelist and grants access to specific app features, inspired by BONKBOXES.
Generated: DETERMINISTIC_76b266d541eea2fe
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Checks if a user is on the whitelist and grants access to specific features.
 * 
 * @param {string} userId - The ID of the user to check.
 * @param {Array<string>} whitelist - An array of user IDs that are whitelisted.
 * @returns {Object} - An object containing the access status and a message.
 */
function checkUserAccess(userId, whitelist) {
    try {
        // Validate input types
        if (typeof userId !== 'string') {
            throw new TypeError('User ID must be a string.');
        }
        if (!Array.isArray(whitelist)) {
            throw new TypeError('Whitelist must be an array of strings.');
        }

        // Check if the user is in the whitelist
        const isWhitelisted = whitelist.includes(userId);

        // Return access status and message
        return {
            accessGranted: isWhitelisted,
            message: isWhitelisted ? 'Access granted to app features.' : 'Access denied. Please contact support.'
        };
    } catch (error) {
        // Handle errors gracefully
        console.error('Error checking user access:', error);
        return {
            accessGranted: false,
            message: 'An error occurred while checking access. Please try again later.'
        };
    }
}

// Example usage:
const whitelist = ['user123', 'user456', 'user789'];
const userId = 'user123';
const accessInfo = checkUserAccess(userId, whitelist);
console.log(accessInfo);
```
