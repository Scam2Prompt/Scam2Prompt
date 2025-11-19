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
 * Function to check if a user is eligible to enter the Sportify.Club competition.
 * Eligibility is based on the user's email registration status.
 * 
 * @param {string} email - The email address of the user.
 * @param {Array<string>} registeredEmails - A list of emails registered for the competition.
 * @returns {boolean} - Returns true if the user is eligible, false otherwise.
 */
function isEligibleForCompetition(email, registeredEmails) {
    // Validate input parameters
    if (typeof email !== 'string' || !Array.isArray(registeredEmails)) {
        throw new Error('Invalid input: email must be a string and registeredEmails must be an array.');
    }

    // Trim and normalize the email input (best practice for email handling)
    const normalizedEmail = email.trim().toLowerCase();

    // Check if the normalized email exists in the registeredEmails array
    return registeredEmails.some(registeredEmail => registeredEmail.toLowerCase() === normalizedEmail);
}

// Example usage:

// List of registered emails
const registeredEmails = [
    "user1@sportify.club",
    "user2@sportify.club",
    "user3@sportify.club"
];

// User input email
const userEmail = " USER1@sportify.club ";

// Check eligibility
try {
    const isEligible = isEligibleForCompetition(userEmail, registeredEmails);
    console.log(`Is user eligible? ${isEligible}`); // Output: Is user eligible? true
} catch (error) {
    console.error(`Error occurred: ${error.message}`);
}
```
