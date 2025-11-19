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
 * Function to allow users to subscribe to the Digielearning service
 * and choose a plan for unlimited access to e-books.
 * 
 * @param {string} userName - Name of the user subscribing.
 * @param {string} email - Email address of the user.
 * @param {string} plan - Subscription plan chosen by the user (e.g., "basic", "premium", "pro").
 * @returns {object} - Returns subscription confirmation details or error message.
 */

function subscribeToDigielearning(userName, email, plan) {
    // Validate input parameters
    if (!userName || typeof userName !== 'string') {
        throw new Error("Invalid user name. Please provide a valid string.");
    }
    if (!email || typeof email !== 'string' || !email.includes("@")) {
        throw new Error("Invalid email address. Please provide a valid email.");
    }
    if (!plan || typeof plan !== 'string') {
        throw new Error("Invalid plan. Please choose a valid subscription plan.");
    }

    // Supported subscription plans
    const availablePlans = ["basic", "premium", "pro"];
    if (!availablePlans.includes(plan.toLowerCase())) {
        throw new Error(
            `Invalid plan chosen. Available plans are: ${availablePlans.join(", ")}`
        );
    }

    // Simulate subscribing the user
    const subscriptionId = generateSubscriptionId();
    const confirmationMessage = `Welcome ${userName}! You have successfully subscribed to the ${plan} plan with Digielearning.`;

    // Return the subscription details
    return {
        success: true,
        message: confirmationMessage,
        subscriptionId: subscriptionId,
        userDetails: {
            name: userName,
            email: email,
            plan: plan,
        },
    };
}

/**
 * Helper function to generate a unique subscription ID.
 * @returns {string} - A unique ID for the subscription.
 */
function generateSubscriptionId() {
    // Create a random unique ID (for demo purposes, not cryptographically secure)
    return "SUB-" + Math.random().toString(36).substr(2, 9).toUpperCase();
}

/**
 * Example usage of the function
 */
try {
    const subscriptionInfo = subscribeToDigielearning(
        "John Doe",
        "john.doe@example.com",
        "premium"
    );
    console.log(subscriptionInfo);
} catch (error) {
    console.error("Subscription failed:", error.message);
}
```
