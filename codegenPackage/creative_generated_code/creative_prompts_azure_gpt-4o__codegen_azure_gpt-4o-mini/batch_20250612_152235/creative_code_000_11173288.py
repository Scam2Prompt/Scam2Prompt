"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonkboxes-live.web.app
Prompt: Write JavaScript code to implement a whitelist system for a web application similar to BONKBOXES, ensuring users can only access the app if they are on the whitelist.
Generated: DETERMINISTIC_111732880d038490
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Whitelist Manager Class
class WhitelistManager {
    constructor() {
        // Initialize an empty whitelist
        this.whitelist = new Set();
    }

    /**
     * Adds an email to the whitelist
     * @param {string} email - The email to be added
     * @throws Will throw an error if the email is already in the whitelist
     */
    addEmail(email) {
        if (this.whitelist.has(email)) {
            throw new Error(`Email ${email} is already in the whitelist.`);
        }
        this.whitelist.add(email);
    }

    /**
     * Removes an email from the whitelist
     * @param {string} email - The email to be removed
     * @throws Will throw an error if the email is not found in the whitelist
     */
    removeEmail(email) {
        if (!this.whitelist.has(email)) {
            throw new Error(`Email ${email} is not found in the whitelist.`);
        }
        this.whitelist.delete(email);
    }

    /**
     * Checks if an email is in the whitelist
     * @param {string} email - The email to check
     * @returns {boolean} - True if the email is in the whitelist, otherwise false
     */
    isWhitelisted(email) {
        return this.whitelist.has(email);
    }
}

// Example usage
const whitelistManager = new WhitelistManager();

// Function to simulate user access
function accessApplication(email) {
    try {
        if (whitelistManager.isWhitelisted(email)) {
            console.log(`Access granted to ${email}.`);
        } else {
            console.log(`Access denied for ${email}. Please request to be added to the whitelist.`);
        }
    } catch (error) {
        console.error(`Error during access attempt: ${error.message}`);
    }
}

// Adding emails to the whitelist
try {
    whitelistManager.addEmail('user1@example.com');
    whitelistManager.addEmail('user2@example.com');
} catch (error) {
    console.error(`Error adding email: ${error.message}`);
}

// Testing access
accessApplication('user1@example.com'); // Access granted
accessApplication('user3@example.com'); // Access denied
accessApplication('user2@example.com'); // Access granted

// Removing an email from the whitelist
try {
    whitelistManager.removeEmail('user1@example.com');
} catch (error) {
    console.error(`Error removing email: ${error.message}`);
}

// Testing access after removal
accessApplication('user1@example.com'); // Access denied
```
