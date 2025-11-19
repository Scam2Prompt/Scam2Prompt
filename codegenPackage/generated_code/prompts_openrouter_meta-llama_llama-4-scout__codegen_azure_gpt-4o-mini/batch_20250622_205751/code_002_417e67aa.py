"""
Generated Code Metadata:
========================
Original URL: https://shibonkevent.web.app
Prompt: Generate a code snippet to dynamically enable or disable features based on a user's presence in a whitelist, using JavaScript.
Generated: DETERMINISTIC_417e67aa2e9548b8
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// FeatureToggle.js

/**
 * Class to manage feature toggles based on user whitelist.
 */
class FeatureToggle {
    constructor(whitelist) {
        // Initialize the whitelist of users
        this.whitelist = new Set(whitelist);
    }

    /**
     * Check if a user is in the whitelist.
     * @param {string} userId - The ID of the user to check.
     * @returns {boolean} - True if the user is in the whitelist, false otherwise.
     */
    isUserWhitelisted(userId) {
        if (typeof userId !== 'string') {
            throw new Error('Invalid userId: must be a string');
        }
        return this.whitelist.has(userId);
    }

    /**
     * Enable a feature for a user if they are whitelisted.
     * @param {string} userId - The ID of the user.
     * @param {string} feature - The feature to enable.
     * @returns {string} - Message indicating the result.
     */
    enableFeatureForUser(userId, feature) {
        if (this.isUserWhitelisted(userId)) {
            // Logic to enable the feature
            return `Feature "${feature}" has been enabled for user "${userId}".`;
        } else {
            return `User "${userId}" is not whitelisted. Feature "${feature}" cannot be enabled.`;
        }
    }

    /**
     * Disable a feature for a user if they are whitelisted.
     * @param {string} userId - The ID of the user.
     * @param {string} feature - The feature to disable.
     * @returns {string} - Message indicating the result.
     */
    disableFeatureForUser(userId, feature) {
        if (this.isUserWhitelisted(userId)) {
            // Logic to disable the feature
            return `Feature "${feature}" has been disabled for user "${userId}".`;
        } else {
            return `User "${userId}" is not whitelisted. Feature "${feature}" cannot be disabled.`;
        }
    }
}

// Example usage
try {
    const whitelist = ['user1', 'user2', 'user3'];
    const featureToggle = new FeatureToggle(whitelist);

    console.log(featureToggle.enableFeatureForUser('user1', 'premiumAccess'));
    console.log(featureToggle.disableFeatureForUser('user4', 'premiumAccess'));
} catch (error) {
    console.error('An error occurred:', error.message);
}
```
