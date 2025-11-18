"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://link-gleam.pages.dev
Prompt: Create a function in Node.js to validate email addresses and social media logins for participants entering a Gleam-hosted giveaway like Katana Inu x Baby Doge.
Generated: DETERMINISTIC_48080fb435560df7
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// emailValidator.js

/**
 * A simple email validation function using a regular expression.
 * @param {string} email - The email address to validate.
 * @returns {boolean} - Returns true if the email is valid, otherwise false.
 */
function validateEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

/**
 * A function to validate social media login handles.
 * This example assumes handles for Twitter, Instagram, and Facebook.
 * @param {string} handle - The social media handle to validate.
 * @param {string} platform - The platform for which to validate the handle.
 * @returns {boolean} - Returns true if the handle is valid, otherwise false.
 */
function validateSocialMediaHandle(handle, platform) {
    let handleRegex;

    switch (platform.toLowerCase()) {
        case 'twitter':
            handleRegex = /^@([A-Za-z0-9_]{1,15})$/; // Twitter handles start with '@' and can be up to 15 characters long
            break;
        case 'instagram':
            handleRegex = /^([A-Za-z0-9._]{1,30})$/; // Instagram handles can be up to 30 characters long
            break;
        case 'facebook':
            handleRegex = /^([A-Za-z0-9.]{5,})$/; // Facebook handles can start with letters/numbers and must be at least 5 characters
            break;
        default:
            throw new Error('Unsupported platform. Supported platforms are: Twitter, Instagram, Facebook.');
    }

    return handleRegex.test(handle);
}

/**
 * Main function to validate participant data for a giveaway.
 * @param {string} email - The email address of the participant.
 * @param {string} handle - The social media handle of the participant.
 * @param {string} platform - The social media platform (Twitter, Instagram, Facebook).
 * @returns {Object} - An object containing the validation results.
 */
function validateParticipant(email, handle, platform) {
    try {
        const emailValid = validateEmail(email);
        const socialMediaValid = validateSocialMediaHandle(handle, platform);

        return {
            emailValid: emailValid,
            socialMediaValid: socialMediaValid
        };
    } catch (error) {
        console.error('Error in validation:', error.message);
        return {
            emailValid: false,
            socialMediaValid: false,
            error: error.message
        };
    }
}

// Example usage
const participantData = {
    email: 'example@test.com',
    handle: '@exampleUser',
    platform: 'Twitter'
};

const validationResults = validateParticipant(participantData.email, participantData.handle, participantData.platform);
console.log('Validation Results:', validationResults);

module.exports = {
    validateEmail,
    validateSocialMediaHandle,
    validateParticipant
};
```
