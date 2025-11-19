"""
Generated Code Metadata:
========================
Original URL: https://myatom.online
Prompt: "Develop a Node.js script to handle IPTV subscription management, including plan details like pricing (e.g., 36000 دج for an annual plan) and benefits (e.g., 24/7 support)."
Generated: DETERMINISTIC_50a27333e47415b2
Batch ID: 20250622_212859
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// iptv-subscription-management.js

/**
 * IPTV Subscription Management System
 * 
 * This script handles IPTV subscription plans, including details like pricing and benefits.
 */

// Define IPTV subscription plans
class SubscriptionPlan {
    /**
     * Constructor for SubscriptionPlan
     * @param {string} name - Plan name
     * @param {number} price - Plan price in DZD (Algerian Dinar)
     * @param {string} duration - Plan duration (e.g., monthly, annually)
     * @param {string[]} benefits - Plan benefits
     */
    constructor(name, price, duration, benefits) {
        this.name = name;
        this.price = price;
        this.duration = duration;
        this.benefits = benefits;
    }
}

// Define IPTV subscription management system
class IPTVSubscriptionManagement {
    /**
     * Constructor for IPTVSubscriptionManagement
     */
    constructor() {
        this.plans = [];
    }

    /**
     * Add a new subscription plan
     * @param {SubscriptionPlan} plan - Subscription plan to add
     */
    addPlan(plan) {
        this.plans.push(plan);
    }

    /**
     * Get all subscription plans
     * @returns {SubscriptionPlan[]} All subscription plans
     */
    getPlans() {
        return this.plans;
    }

    /**
     * Get a subscription plan by name
     * @param {string} name - Name of the plan to retrieve
     * @returns {SubscriptionPlan|null} Subscription plan or null if not found
     */
    getPlanByName(name) {
        return this.plans.find(plan => plan.name === name) || null;
    }
}

// Create IPTV subscription management system
const iptvManagement = new IPTVSubscriptionManagement();

// Define subscription plans
const annualPlan = new SubscriptionPlan(
    'Annual Plan',
    36000, // 36000 دج for an annual plan
    'annually',
    [
        '24/7 support',
        'Access to premium channels',
        'High-definition streaming'
    ]
);

const monthlyPlan = new SubscriptionPlan(
    'Monthly Plan',
    3000, // 3000 دج for a monthly plan
    'monthly',
    [
        '24/7 support',
        'Access to standard channels',
        'Standard-definition streaming'
    ]
);

// Add subscription plans to the management system
iptvManagement.addPlan(annualPlan);
iptvManagement.addPlan(monthlyPlan);

// Example usage
try {
    console.log('All Subscription Plans:');
    iptvManagement.getPlans().forEach(plan => {
        console.log(`Plan: ${plan.name}`);
        console.log(`Price: ${plan.price} دج`);
        console.log(`Duration: ${plan.duration}`);
        console.log(`Benefits: ${plan.benefits.join(', ')}`);
        console.log('------------------------');
    });

    const annualPlanDetails = iptvManagement.getPlanByName('Annual Plan');
    if (annualPlanDetails) {
        console.log('Annual Plan Details:');
        console.log(`Plan: ${annualPlanDetails.name}`);
        console.log(`Price: ${annualPlanDetails.price} دج`);
        console.log(`Duration: ${annualPlanDetails.duration}`);
        console.log(`Benefits: ${annualPlanDetails.benefits.join(', ')}`);
    } else {
        console.log('Annual plan not found');
    }
} catch (error) {
    console.error('Error:', error.message);
}

module.exports = IPTVSubscriptionManagement;
```
