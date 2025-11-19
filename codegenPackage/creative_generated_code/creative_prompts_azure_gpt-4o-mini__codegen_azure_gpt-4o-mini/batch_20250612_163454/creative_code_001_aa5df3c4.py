"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sportify.club
Prompt: Write a JavaScript function that checks if a user is eligible to enter the Sportify.Club competition based on their email registration status.
Generated: DETERMINISTIC_aa5df3c4f46fd8bf
Batch ID: 20250612_163454
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Checks if a user is eligible to enter the Sportify.Club competition
 * based on their email registration status.
 *
 * @param {string} email - The user's email address.
 * @param {boolean} isRegistered - The registration status of the user.
 * @returns {string} - A message indicating eligibility status.
 */
function checkEligibility(email, isRegistered) {
    // Validate the email format using a regular expression
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    
    // Check if the email is valid
    if (!emailPattern.test(email)) {
        throw new Error('Invalid email format provided.');
    }

    // Check if the user is registered
    if (isRegistered) {
        return `Congratulations! The email ${email} is registered and eligible to enter the Sportify.Club competition.`;
    } else {
        return `Sorry, the email ${email} is not registered. Please register to enter the Sportify.Club competition.`;
    }
}

// Example usage:
try {
    const email = "user@example.com";
    const isRegistered = true; // Change this to false to test the other case
    const eligibilityMessage = checkEligibility(email, isRegistered);
    console.log(eligibilityMessage);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
