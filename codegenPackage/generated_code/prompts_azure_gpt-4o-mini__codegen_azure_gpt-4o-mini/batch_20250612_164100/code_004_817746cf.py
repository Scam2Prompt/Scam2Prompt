"""
Generated Code Metadata:
========================
Original URL: https://ethervista.co
Prompt: Create a JavaScript code example that subscribes users to updates, similar to the subscription feature on ethervista.co.
Generated: DETERMINISTIC_817746cf592ff153
Batch ID: 20250612_164100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// SubscriptionManager class to handle user subscriptions
class SubscriptionManager {
    constructor() {
        // Initialize an empty array to hold subscribers
        this.subscribers = [];
    }

    /**
     * Subscribe a user to updates
     * @param {string} email - The email address of the user
     * @throws Will throw an error if the email is invalid or already subscribed
     */
    subscribe(email) {
        // Validate the email format
        if (!this.isValidEmail(email)) {
            throw new Error('Invalid email address');
        }

        // Check if the user is already subscribed
        if (this.subscribers.includes(email)) {
            throw new Error('Email is already subscribed');
        }

        // Add the email to the subscribers list
        this.subscribers.push(email);
        console.log(`Successfully subscribed: ${email}`);
    }

    /**
     * Unsubscribe a user from updates
     * @param {string} email - The email address of the user
     * @throws Will throw an error if the email is not found in the subscribers list
     */
    unsubscribe(email) {
        // Check if the user is subscribed
        const index = this.subscribers.indexOf(email);
        if (index === -1) {
            throw new Error('Email not found in subscribers');
        }

        // Remove the email from the subscribers list
        this.subscribers.splice(index, 1);
        console.log(`Successfully unsubscribed: ${email}`);
    }

    /**
     * Validate the email format using a regular expression
     * @param {string} email - The email address to validate
     * @returns {boolean} - True if valid, false otherwise
     */
    isValidEmail(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    }

    /**
     * Get the list of all subscribers
     * @returns {Array} - Array of subscribed email addresses
     */
    getSubscribers() {
        return this.subscribers;
    }
}

// Example usage
try {
    const subscriptionManager = new SubscriptionManager();
    
    // Subscribe users
    subscriptionManager.subscribe('user1@example.com');
    subscriptionManager.subscribe('user2@example.com');

    // Attempt to subscribe an invalid email
    subscriptionManager.subscribe('invalid-email');

} catch (error) {
    console.error(error.message);
}

// Output the current subscribers
console.log('Current Subscribers:', subscriptionManager.getSubscribers());
```
