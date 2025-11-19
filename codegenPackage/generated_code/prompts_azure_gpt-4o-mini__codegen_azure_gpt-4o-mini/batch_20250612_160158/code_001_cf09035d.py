"""
Generated Code Metadata:
========================
Original URL: https://digielearning.in
Prompt: Write a JavaScript function that allows users to subscribe to the Digielearning service and choose a plan for unlimited access to e-books.
Generated: DETERMINISTIC_cf09035daf3cf329
Batch ID: 20250612_160158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * SubscriptionService class to manage user subscriptions to the Digielearning service.
 */
class SubscriptionService {
    constructor() {
        // Available subscription plans
        this.plans = {
            basic: { price: 9.99, description: "Basic plan with unlimited access to e-books." },
            premium: { price: 19.99, description: "Premium plan with unlimited access to e-books and exclusive content." },
            family: { price: 29.99, description: "Family plan for up to 4 users with unlimited access to e-books." }
        };
        // Store subscriptions
        this.subscriptions = [];
    }

    /**
     * Subscribe a user to a selected plan.
     * @param {string} userName - The name of the user subscribing.
     * @param {string} plan - The selected subscription plan.
     * @throws Will throw an error if the plan is not valid.
     */
    subscribe(userName, plan) {
        // Validate input
        if (!userName || typeof userName !== 'string') {
            throw new Error("Invalid user name. It must be a non-empty string.");
        }
        if (!this.plans[plan]) {
            throw new Error(`Invalid plan selected. Available plans are: ${Object.keys(this.plans).join(', ')}`);
        }

        // Create subscription object
        const subscription = {
            userName: userName,
            plan: plan,
            price: this.plans[plan].price,
            dateSubscribed: new Date()
        };

        // Add subscription to the list
        this.subscriptions.push(subscription);
        console.log(`User ${userName} subscribed to the ${plan} plan.`);
    }

    /**
     * Get the list of all subscriptions.
     * @returns {Array} - Array of subscription objects.
     */
    getSubscriptions() {
        return this.subscriptions;
    }

    /**
     * Get details of a specific plan.
     * @param {string} plan - The plan to retrieve details for.
     * @returns {Object} - Details of the specified plan.
     * @throws Will throw an error if the plan is not valid.
     */
    getPlanDetails(plan) {
        if (!this.plans[plan]) {
            throw new Error(`Invalid plan selected. Available plans are: ${Object.keys(this.plans).join(', ')}`);
        }
        return this.plans[plan];
    }
}

// Example usage
try {
    const subscriptionService = new SubscriptionService();
    subscriptionService.subscribe("Alice", "premium");
    console.log(subscriptionService.getSubscriptions());
    console.log(subscriptionService.getPlanDetails("basic"));
} catch (error) {
    console.error("Error:", error.message);
}
```
