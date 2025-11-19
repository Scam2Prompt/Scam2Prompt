"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wairdrop.com
Prompt: Write a JavaScript function to handle email subscriptions effectively, inspired by the Wair Drop website's approach.
Generated: DETERMINISTIC_f6182b75f393f480
Batch ID: 20250612_160113
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Email Subscription Handler
 * This function handles email subscriptions by validating input and
 * simulating the process of adding an email to the subscription list.
 */

class EmailSubscription {
    constructor() {
        // A mock list to store subscribed emails
        this.subscribedEmails = new Set();
    }

    /**
     * Validates the format of the provided email.
     * @param {string} email - The email address to validate.
     * @returns {boolean} - Returns true if the email is valid, false otherwise.
     */
    isValidEmail(email) {
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailPattern.test(email);
    }

    /**
     * Subscribes the user with the provided email address.
     * If the email is already subscribed, it does not add it again.
     * @param {string} email - The email address to subscribe.
     * @returns {string} - Returns a success message or an error message.
     */
    subscribe(email) {
        try {
            // Validate the email format
            if (!this.isValidEmail(email)) {
                throw new Error('Invalid email format.');
            }

            // Check if the email is already subscribed
            if (this.subscribedEmails.has(email)) {
                return 'Email is already subscribed.';
            }

            // Add the email to the subscribed list
            this.subscribedEmails.add(email);
            return 'Successfully subscribed!';
        } catch (error) {
            console.error('Subscription error:', error.message);
            return `Error: ${error.message}`;
        }
    }

    /**
     * Unsubscribes the user with the provided email address.
     * @param {string} email - The email address to unsubscribe.
     * @returns {string} - Returns a success message or an error message.
     */
    unsubscribe(email) {
        try {
            // Validate the email format
            if (!this.isValidEmail(email)) {
                throw new Error('Invalid email format.');
            }

            // Check if the email is subscribed
            if (!this.subscribedEmails.has(email)) {
                return 'Email is not subscribed.';
            }

            // Remove the email from the subscribed list
            this.subscribedEmails.delete(email);
            return 'Successfully unsubscribed!';
        } catch (error) {
            console.error('Unsubscription error:', error.message);
            return `Error: ${error.message}`;
        }
    }

    /**
     * Retrieves the list of currently subscribed emails.
     * @returns {Array<string>} - Returns an array of subscribed emails.
     */
    getSubscribedEmails() {
        return Array.from(this.subscribedEmails);
    }
}

// Example Usage
const subscriptionHandler = new EmailSubscription();
console.log(subscriptionHandler.subscribe('user@example.com')); // Successfully subscribed!
console.log(subscriptionHandler.subscribe('user@example.com')); // Email is already subscribed.
console.log(subscriptionHandler.unsubscribe('user@example.com')); // Successfully unsubscribed!
console.log(subscriptionHandler.unsubscribe('user@example.com')); // Email is not subscribed.
console.log(subscriptionHandler.getSubscribedEmails()); // []
```
