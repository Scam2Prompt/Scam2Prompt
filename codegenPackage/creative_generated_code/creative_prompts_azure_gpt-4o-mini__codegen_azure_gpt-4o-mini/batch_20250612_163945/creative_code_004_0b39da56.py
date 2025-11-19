"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connectsync.org
Prompt: Create an example of a JavaScript function that handles user subscriptions for updates as described on Connect Sync.
Generated: DETERMINISTIC_0b39da56ae5ae24d
Batch ID: 20250612_163945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * User Subscription Handler
 * This function manages user subscriptions for receiving updates.
 * It allows users to subscribe and unsubscribe, storing their preferences.
 */
class SubscriptionService {
    constructor() {
        // Store subscriptions in a Set for uniqueness
        this.subscribers = new Set();
    }

    /**
     * Subscribe a user for updates
     * @param {string} userEmail - The email of the user to subscribe
     * @throws {Error} If the email format is invalid or the user is already subscribed
     */
    subscribe(userEmail) {
        this.validateEmail(userEmail);

        if (this.subscribers.has(userEmail)) {
            throw new Error('User is already subscribed.');
        }

        this.subscribers.add(userEmail);
        console.log(`User ${userEmail} subscribed successfully.`);
    }

    /**
     * Unsubscribe a user from updates
     * @param {string} userEmail - The email of the user to unsubscribe
     * @throws {Error} If the user is not subscribed
     */
    unsubscribe(userEmail) {
        if (!this.subscribers.has(userEmail)) {
            throw new Error('User is not subscribed.');
        }

        this.subscribers.delete(userEmail);
        console.log(`User ${userEmail} unsubscribed successfully.`);
    }

    /**
     * Validate email format
     * @param {string} email - The email to validate
     * @throws {Error} If the email format is invalid
     */
    validateEmail(email) {
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailPattern.test(email)) {
            throw new Error('Invalid email format.');
        }
    }

    /**
     * Get all subscribed users
     * @returns {Array<string>} - List of subscribed user emails
     */
    getSubscribers() {
        return Array.from(this.subscribers);
    }
}

// Example usage
try {
    const subscriptionService = new SubscriptionService();
    
    // Subscribe users
    subscriptionService.subscribe('user1@example.com');
    subscriptionService.subscribe('user2@example.com');

    // Attempt to subscribe again
    subscriptionService.subscribe('user1@example.com'); // Should throw an error

} catch (error) {
    console.error(error.message);
}
```
