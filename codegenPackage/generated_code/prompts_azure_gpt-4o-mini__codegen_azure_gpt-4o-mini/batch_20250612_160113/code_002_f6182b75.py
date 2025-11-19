"""
Generated Code Metadata:
========================
Original URL: https://wairdrop.com
Prompt: Write a JavaScript function to handle email subscriptions effectively, inspired by the Wair Drop website's approach.
Generated: DETERMINISTIC_f6182b75f393f480
Batch ID: 20250612_160113
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Email Subscription Handler
 * This function manages email subscriptions by validating the email format,
 * adding it to a subscription list, and simulating an API call to save the email.
 */

class EmailSubscription {
    constructor() {
        // Initialize an empty array to hold subscribed emails
        this.subscribedEmails = [];
    }

    /**
     * Validates the email format using a regular expression.
     * @param {string} email - The email address to validate.
     * @returns {boolean} - Returns true if the email is valid, false otherwise.
     */
    validateEmail(email) {
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailPattern.test(email);
    }

    /**
     * Subscribes a user to the email list if the email is valid.
     * @param {string} email - The email address to subscribe.
     * @returns {Promise<string>} - A promise that resolves with a success message or rejects with an error.
     */
    async subscribe(email) {
        return new Promise((resolve, reject) => {
            // Validate the email format
            if (!this.validateEmail(email)) {
                return reject(new Error('Invalid email format.'));
            }

            // Check if the email is already subscribed
            if (this.subscribedEmails.includes(email)) {
                return reject(new Error('Email is already subscribed.'));
            }

            // Simulate an API call to save the email
            setTimeout(() => {
                this.subscribedEmails.push(email);
                resolve('Subscription successful!');
            }, 1000); // Simulating network delay
        });
    }
}

// Example usage
const subscriptionHandler = new EmailSubscription();

// Function to handle the subscription process
async function handleSubscription(email) {
    try {
        const message = await subscriptionHandler.subscribe(email);
        console.log(message);
    } catch (error) {
        console.error('Subscription error:', error.message);
    }
}

// Example of subscribing an email
handleSubscription('user@example.com');
```
