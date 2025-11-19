"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensea.ru
Prompt: Develop a REST API endpoint in Node.js that allows users to place orders for diving equipment, including payment processing and delivery options.
Generated: DETERMINISTIC_dd98ee99a3a9c315
Batch ID: 20250612_135046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const express = require('express');        // Web server framework
const bodyParser = require('body-parser'); // Middleware to parse JSON requests
const stripe = require('stripe')('your-stripe-api-key'); // Stripe for payment processing

// Initialize the Express application
const app = express();
const port = process.env.PORT || 3000;

// Middleware to parse incoming JSON requests
app.use(bodyParser.json());

// Mock database for diving equipment and orders
const divingEquipment = [
    { id: 1, name: "Diving Suit", price: 150 },
    { id: 2, name: "Oxygen Tank", price: 200 },
    { id: 3, name: "Diving Mask", price: 50 },
];

const orders = [];

// POST /order - Place an order
app.post('/order', async (req, res) => {
    try {
        const { items, deliveryOption, paymentToken } = req.body;

        // Validate request body
        if (!items || !Array.isArray(items) || items.length === 0) {
            return res.status(400).json({ error: 'Invalid items list.' });
        }
        if (!deliveryOption || typeof deliveryOption !== 'string') {
            return res.status(400).json({ error: 'Delivery option is required and must be a string.' });
        }
        if (!paymentToken || typeof paymentToken !== 'string') {
            return res.status(400).json({ error: 'Payment token is required.' });
        }

        // Calculate total order cost
        let totalCost = 0;
        items.forEach(item => {
            const product = divingEquipment.find(equip => equip.id === item.id);
            if (product) {
                totalCost += product.price * (item.quantity || 1);
            }
        });

        // Add delivery cost (mock logic for delivery option)
        const deliveryCost = deliveryOption === 'standard' ? 10 : 20;
        totalCost += deliveryCost;

        // Process payment using Stripe
        const payment = await stripe.paymentIntents.create({
            amount: totalCost * 100, // Stripe requires amount in cents
            currency: 'usd',
            payment_method: paymentToken,
            confirm: true,
        });

        // Save order to mock database
        const newOrder = {
            id: orders.length + 1,
            items,
            deliveryOption,
            totalCost,
            paymentId: payment.id,
            status: 'Processing',
        };
        orders.push(newOrder);

        // Respond with order confirmation
        res.status(201).json({
            message: 'Order placed successfully.',
            order: newOrder,
        });
    } catch (error) {
        console.error('Error placing order:', error);

        // Handle Stripe or other errors
        if (error.type === 'StripeCardError') {
            return res.status(402).json({ error: 'Payment failed. Card was declined.' });
        }
        res.status(500).json({ error: 'An error occurred while placing the order.' });
    }
});

// GET /equipment - Retrieve available diving equipment
app.get('/equipment', (req, res) => {
    res.status(200).json({ equipment: divingEquipment });
});

// GET /orders - Retrieve all orders
app.get('/orders', (req, res) => {
    res.status(200).json({ orders });
});

// Start the Express server
app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
```
