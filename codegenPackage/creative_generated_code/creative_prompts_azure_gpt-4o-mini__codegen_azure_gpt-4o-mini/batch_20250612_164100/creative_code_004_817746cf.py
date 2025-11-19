"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethervista.co
Prompt: Create a JavaScript code example that subscribes users to updates, similar to the subscription feature on ethervista.co.
Generated: DETERMINISTIC_817746cf592ff153
Batch ID: 20250612_164100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Subscription Manager Class
class SubscriptionManager {
    constructor() {
        // This will hold the subscribers' email addresses
        this.subscribers = new Set();
    }

    /**
     * Subscribe a user to updates
     * @param {string} email - The email address of the user to subscribe
     * @throws {Error} If the email is invalid or already subscribed
     */
    subscribe(email) {
        this.validateEmail(email);
        
        if (this.subscribers.has(email)) {
            throw new Error('Email is already subscribed.');
        }

        this.subscribers.add(email);
        console.log(`Successfully subscribed: ${email}`);
    }

    /**
     * Unsubscribe a user from updates
     * @param {string} email - The email address of the user to unsubscribe
     * @throws {Error} If the email is not found in the subscribers
     */
    unsubscribe(email) {
        if (!this.subscribers.has(email)) {
            throw new Error('Email not found in subscribers.');
        }

        this.subscribers.delete(email);
        console.log(`Successfully unsubscribed: ${email}`);
    }

    /**
     * Validate the provided email format
     * @param {string} email - The email address to validate
     * @throws {Error} If the email format is invalid
     */
    validateEmail(email) {
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

        if (!emailPattern.test(email)) {
            throw new Error('Invalid email format.');
        }
    }

    /**
     * Send updates to all subscribers
     * @param {string} message - The message to send to subscribers
     */
    sendUpdates(message) {
        this.subscribers.forEach(email => {
            // Simulate sending an email
            console.log(`Sending update to ${email}: ${message}`);
        });
    }
}

// Example usage of SubscriptionManager
const subscriptionManager = new SubscriptionManager();

try {
    subscriptionManager.subscribe('user@example.com');
    subscriptionManager.subscribe('user2@example.com');
    subscriptionManager.sendUpdates('New updates are available!');
    subscriptionManager.unsubscribe('user@example.com');
    subscriptionManager.sendUpdates('Check out the latest updates!');
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
