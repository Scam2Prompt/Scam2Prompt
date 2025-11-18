"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://expressfinsbk.com
Prompt: Generate code to integrate PayPal and Stripe payment gateways for deposit functionality, as described in the Express Finance Banking system.
Generated: DETERMINISTIC_ee993899b0e5d28c
Batch ID: 20250612_153925
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary packages
const express = require('express');
const bodyParser = require('body-parser');
const paypal = require('@paypal/checkout-server-sdk');
const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY); // Set your Stripe secret key in environment variables

// Initialize Express app
const app = express();
app.use(bodyParser.json());

// PayPal configuration
const environment = new paypal.core.SandboxEnvironment(process.env.PAYPAL_CLIENT_ID, process.env.PAYPAL_CLIENT_SECRET);
const client = new paypal.core.PayPalHttpClient(environment);

// Endpoint to create a PayPal order
app.post('/api/paypal/create-order', async (req, res) => {
    try {
        const request = new paypal.orders.OrdersCreateRequest();
        request.requestBody({
            intent: 'CAPTURE',
            purchase_units: [{
                amount: {
                    currency_code: 'USD',
                    value: req.body.amount, // Amount to be charged
                }
            }]
        });
        
        const order = await client.execute(request);
        res.json({ orderId: order.result.id }); // Send order ID back to client
    } catch (error) {
        console.error('Error creating PayPal order:', error);
        res.status(500).send({ error: 'Failed to create PayPal order' });
    }
});

// Endpoint to capture a PayPal order
app.post('/api/paypal/capture-order', async (req, res) => {
    try {
        const request = new paypal.orders.OrdersCaptureRequest(req.body.orderId);
        request.requestBody({});
        
        const response = await client.execute(request);
        res.json({ order: response.result }); // Send captured order details back to client
    } catch (error) {
        console.error('Error capturing PayPal order:', error);
        res.status(500).send({ error: 'Failed to capture PayPal order' });
    }
});

// Endpoint to create a Stripe payment intent
app.post('/api/stripe/create-payment-intent', async (req, res) => {
    try {
        const paymentIntent = await stripe.paymentIntents.create({
            amount: req.body.amount, // Amount to be charged in cents
            currency: 'usd',
            payment_method_types: ['card'],
        });
        res.json({ clientSecret: paymentIntent.client_secret }); // Send client secret back to client
    } catch (error) {
        console.error('Error creating Stripe payment intent:', error);
        res.status(500).send({ error: 'Failed to create Stripe payment intent' });
    }
});

// Start the server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

Make sure to set the necessary environment variables for `PAYPAL_CLIENT_ID`, `PAYPAL_CLIENT_SECRET`, and `STRIPE_SECRET_KEY` before running the application.
