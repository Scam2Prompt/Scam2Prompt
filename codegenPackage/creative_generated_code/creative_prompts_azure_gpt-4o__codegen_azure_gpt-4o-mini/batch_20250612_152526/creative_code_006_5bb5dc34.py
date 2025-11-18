"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://baazaars.com
Prompt: Write a function in Node.js to integrate PayPal payment processing for discounted products like "Man's Rolex Daytona Panda" and ensure secure transactions.
Generated: DETERMINISTIC_5bb5dc34e55bea39
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
const express = require('express');
const bodyParser = require('body-parser');
const paypal = require('@paypal/checkout-server-sdk');

// Initialize Express app
const app = express();
app.use(bodyParser.json());

// PayPal environment setup
const clientId = 'YOUR_PAYPAL_CLIENT_ID';
const clientSecret = 'YOUR_PAYPAL_CLIENT_SECRET';

// Create a PayPal client
const environment = new paypal.core.SandboxEnvironment(clientId, clientSecret);
const client = new paypal.core.PayPalHttpClient(environment);

// Discounted product details
const discountedProduct = {
    name: "Man's Rolex Daytona Panda",
    price: 2000.00, // Original price
    discount: 0.10, // 10% discount
};

// Calculate discounted price
const calculateDiscountedPrice = (product) => {
    return product.price - (product.price * product.discount);
};

// Create PayPal order
const createPayPalOrder = async (req, res) => {
    const request = new paypal.orders.OrdersCreateRequest();
    const discountedPrice = calculateDiscountedPrice(discountedProduct);

    // Set up the order details
    request.prefer('return=representation');
    request.requestBody({
        intent: 'CAPTURE',
        purchase_units: [{
            amount: {
                currency_code: 'USD',
                value: discountedPrice.toFixed(2),
                breakdown: {
                    item_total: {
                        currency_code: 'USD',
                        value: discountedPrice.toFixed(2),
                    }
                }
            },
            items: [{
                name: discountedProduct.name,
                unit_amount: {
                    currency_code: 'USD',
                    value: discountedPrice.toFixed(2),
                },
                quantity: '1'
            }]
        }]
    });

    try {
        // Call PayPal API to create an order
        const order = await client.execute(request);
        return res.status(200).json({ id: order.result.id });
    } catch (error) {
        console.error("Error creating PayPal order:", error);
        return res.status(500).json({ error: 'Internal server error' });
    }
};

// Capture PayPal order after approval
const capturePayPalOrder = async (req, res) => {
    const orderId = req.params.orderId;
    
    const request = new paypal.orders.OrdersCaptureRequest(orderId);
    request.requestBody({});

    try {
        // Call PayPal API to capture the order
        const capture = await client.execute(request);
        return res.status(200).json(capture.result);
    } catch (error) {
        console.error("Error capturing PayPal order:", error);
        return res.status(500).json({ error: 'Internal server error' });
    }
};

// Define routes
app.post('/api/paypal/create-order', createPayPalOrder);
app.post('/api/paypal/capture-order/:orderId', capturePayPalOrder);

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

**Note:** Replace `'YOUR_PAYPAL_CLIENT_ID'` and `'YOUR_PAYPAL_CLIENT_SECRET'` with your actual PayPal API credentials.
