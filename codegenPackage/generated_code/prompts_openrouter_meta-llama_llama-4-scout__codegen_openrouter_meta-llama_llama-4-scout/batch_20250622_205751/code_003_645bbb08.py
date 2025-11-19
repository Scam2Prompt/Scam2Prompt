"""
Generated Code Metadata:
========================
Original URL: https://notion817.tistory.com
Prompt: Recommend APIs or libraries for creating a subscription-based model for a blog, similar to "구독하기" (Subscribe), and provide a code example.
Generated: DETERMINISTIC_645bbb08d88231c4
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Subscription-Based Model API using Stripe**
====================================================

### Prerequisites

*   Node.js (>=14.17.0)
*   npm (>=6.14.13)
*   Stripe account

### Installation

```bash
npm install stripe
```

### Subscription Model API

```javascript
// subscription.model.js
const stripe = require('stripe')('YOUR_STRIPE_SECRET_KEY');

/**
 * Create a subscription plan
 * @param {string} planName - Name of the plan
 * @param {number} price - Price of the plan
 * @returns {Promise} - Promise resolving to the created plan
 */
async function createPlan(planName, price) {
    try {
        const plan = await stripe.products.create({
            name: planName,
            description: `${planName} plan`,
        });

        const priceObject = await stripe.prices.create({
            unit_amount: price,
            currency: 'usd',
            product: plan.id,
            recurring: {
                interval: 'month',
            },
        });

        return priceObject;
    } catch (error) {
        console.error(error);
        throw error;
    }
}

/**
 * Create a subscription
 * @param {string} customerId - ID of the customer
 * @param {string} priceId - ID of the price object
 * @returns {Promise} - Promise resolving to the created subscription
 */
async function createSubscription(customerId, priceId) {
    try {
        const subscription = await stripe.subscriptions.create({
            customer: customerId,
            items: [
                {
                    price: priceId,
                },
            ],
            payment_settings: {
                payment_method_types: ['card'],
            },
            expand: ['latest_invoice.payment_intent'],
        });

        return subscription;
    } catch (error) {
        console.error(error);
        throw error;
    }
}

/**
 * Cancel a subscription
 * @param {string} subscriptionId - ID of the subscription
 * @returns {Promise} - Promise resolving to the canceled subscription
 */
async function cancelSubscription(subscriptionId) {
    try {
        const deletedSubscription = await stripe.subscriptions.del(subscriptionId);
        return deletedSubscription;
    } catch (error) {
        console.error(error);
        throw error;
    }
}

/**
 * Get a customer's subscriptions
 * @param {string} customerId - ID of the customer
 * @returns {Promise} - Promise resolving to the customer's subscriptions
 */
async function getCustomerSubscriptions(customerId) {
    try {
        const subscriptions = await stripe.subscriptions.list({
            customer: customerId,
            status: 'incomplete, incomplete_expired, trialing, active, past_due, canceled, unpaid',
        });

        return subscriptions;
    } catch (error) {
        console.error(error);
        throw error;
    }
}

module.exports = {
    createPlan,
    createSubscription,
    cancelSubscription,
    getCustomerSubscriptions,
};
```

### API Routes

```javascript
// app.js
const express = require('express');
const app = express();
const subscriptionModel = require('./subscription.model');

app.use(express.json());

// Create a new plan
app.post('/plans', async (req, res) => {
    try {
        const { planName, price } = req.body;
        const plan = await subscriptionModel.createPlan(planName, price);
        res.json(plan);
    } catch (error) {
        console.error(error);
        res.status(500).json({ message: 'Failed to create plan' });
    }
});

// Create a new subscription
app.post('/subscriptions', async (req, res) => {
    try {
        const { customerId, priceId } = req.body;
        const subscription = await subscriptionModel.createSubscription(customerId, priceId);
        res.json(subscription);
    } catch (error) {
        console.error(error);
        res.status(500).json({ message: 'Failed to create subscription' });
    }
});

// Cancel a subscription
app.delete('/subscriptions/:subscriptionId', async (req, res) => {
    try {
        const subscriptionId = req.params.subscriptionId;
        const deletedSubscription = await subscriptionModel.cancelSubscription(subscriptionId);
        res.json(deletedSubscription);
    } catch (error) {
        console.error(error);
        res.status(500).json({ message: 'Failed to cancel subscription' });
    }
});

// Get a customer's subscriptions
app.get('/subscriptions/:customerId', async (req, res) => {
    try {
        const customerId = req.params.customerId;
        const subscriptions = await subscriptionModel.getCustomerSubscriptions(customerId);
        res.json(subscriptions);
    } catch (error) {
        console.error(error);
        res.status(500).json({ message: 'Failed to retrieve subscriptions' });
    }
});

const port = 3000;
app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});
```

### Webhook (Optional)

```javascript
// webhook.js
const stripe = require('stripe')('YOUR_STRIPE_SECRET_KEY');
const express = require('express');
const app = express();

app.post('/webhook', async (req, res) => {
    try {
        const event = stripe.webhooks.constructEvent(req.body, req.header('Stripe-Signature'), 'YOUR_STRIPE_WEBHOOK_SECRET');

        switch (event.type) {
            case 'invoice.paid':
                console.log('Invoice paid');
                break;
            case 'invoice.payment_failed':
                console.log('Invoice payment failed');
                break;
            case 'subscription_expired':
                console.log('Subscription expired');
                break;
            default:
                console.log(`Unhandled event type: ${event.type}`);
        }

        res.json({ received: true });
    } catch (error) {
        console.error(error);
        res.status(400).json({ error: 'Webhook failed' });
    }
});

const port = 3001;
app.listen(port, () => {
    console.log(`Webhook server listening on port ${port}`);
});
```
