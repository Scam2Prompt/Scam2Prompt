"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://digielearning.in
Prompt: Write a JavaScript function that allows users to subscribe to the Digielearning service and choose a plan for unlimited access to e-books.
Generated: DETERMINISTIC_cf09035daf3cf329
Batch ID: 20250612_160158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * SubscriptionService class manages user subscriptions to the Digielearning service.
 */
class SubscriptionService {
    constructor() {
        // Initialize an array to store subscribed users
        this.subscribers = [];
        // Define available subscription plans
        this.plans = {
            basic: { price: 10, description: "Basic plan with unlimited e-books." },
            premium: { price: 15, description: "Premium plan with unlimited e-books and additional resources." },
            family: { price: 25, description: "Family plan with unlimited e-books for up to 5 users." }
        };
    }

    /**
     * Subscribe a user to the selected plan.
     * @param {string} userName - The name of the user subscribing.
     * @param {string} plan - The selected subscription plan.
     * @throws {Error} Throws an error if the plan is invalid.
     */
    subscribe(userName, plan) {
        try {
            // Validate user name
            if (!userName || typeof userName !== 'string') {
                throw new Error("Invalid user name. It must be a non-empty string.");
            }

            // Validate plan
            if (!this.plans[plan]) {
                throw new Error(`Invalid plan selected. Available plans: ${Object.keys(this.plans).join(", ")}`);
            }

            // Create a new subscriber object
            const subscriber = {
                userName: userName,
                plan: plan,
                price: this.plans[plan].price,
                subscriptionDate: new Date(),
            };

            // Add subscriber to the list
            this.subscribers.push(subscriber);
            console.log(`Subscription successful for ${userName} to the ${plan} plan.`);
        } catch (error) {
            console.error(`Subscription failed: ${error.message}`);
        }
    }

    /**
     * List all current subscribers.
     * @returns {Array} The array of subscribers.
     */
    listSubscribers() {
        return this.subscribers;
    }
}

// Example usage
const subscriptionService = new SubscriptionService();

// Subscribing users
subscriptionService.subscribe("Alice", "premium");
subscriptionService.subscribe("Bob", "basic");
subscriptionService.subscribe("Charlie", "family");

// Listing all subscribers
console.log(subscriptionService.listSubscribers());
```
