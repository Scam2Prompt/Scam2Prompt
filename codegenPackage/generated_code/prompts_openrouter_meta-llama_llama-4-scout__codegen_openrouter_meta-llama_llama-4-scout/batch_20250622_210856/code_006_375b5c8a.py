"""
Generated Code Metadata:
========================
Original URL: https://republik.pages.dev
Prompt: Implement a simple payment gateway using Stripe or PayPal to handle deposits and withdrawals for a slot gaming site, and provide an example code in Node.js.
Generated: DETERMINISTIC_375b5c8a81a32788
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// payment-gateway.js

// Import required libraries
const stripe = require('stripe')('sk_test_...'); // Replace with your Stripe secret key
const paypal = require('paypal-rest-sdk');
const express = require('express');
const app = express();
app.use(express.json());

// Configure PayPal
paypal.configure({
  'mode': 'sandbox', // Change to 'live' for production
  'client_id': 'YOUR_PAYPAL_CLIENT_ID',
  'client_secret': 'YOUR_PAYPAL_CLIENT_SECRET'
});

// Stripe payment gateway
class StripePaymentGateway {
  /**
   * Create a Stripe customer
   * @param {string} email - Customer email
   * @returns {Promise} - Stripe customer object
   */
  async createCustomer(email) {
    try {
      const customer = await stripe.customers.create({ email });
      return customer;
    } catch (err) {
      throw new Error(`Error creating Stripe customer: ${err.message}`);
    }
  }

  /**
   * Make a deposit using Stripe
   * @param {string} customerId - Stripe customer ID
   * @param {number} amount - Deposit amount
   * @returns {Promise} - Stripe payment intent object
   */
  async makeDeposit(customerId, amount) {
    try {
      const paymentIntent = await stripe.paymentIntents.create({
        amount,
        currency: 'usd',
        payment_method_types: ['card'],
        customer: customerId
      });
      return paymentIntent;
    } catch (err) {
      throw new Error(`Error making deposit: ${err.message}`);
    }
  }

  /**
   * Make a withdrawal using Stripe
   * @param {string} customerId - Stripe customer ID
   * @param {number} amount - Withdrawal amount
   * @returns {Promise} - Stripe payout object
   */
  async makeWithdrawal(customerId, amount) {
    try {
      const payout = await stripe.payouts.create({
        amount,
        currency: 'usd',
        customer: customerId
      });
      return payout;
    } catch (err) {
      throw new Error(`Error making withdrawal: ${err.message}`);
    }
  }
}

// PayPal payment gateway
class PayPalPaymentGateway {
  /**
   * Create a PayPal payment
   * @param {string} email - Customer email
   * @param {number} amount - Payment amount
   * @returns {Promise} - PayPal payment object
   */
  async createPayment(email, amount) {
    try {
      const payment = await paypal.payment.create({
        "intent": "sale",
        "payer": {
          "payment_method": "paypal"
        },
        "redirect_urls": {
          "return_url": "/payment/success",
          "cancel_url": "/payment/cancel"
        },
        "transactions": [{
          "amount": {
            "currency": "USD",
            "total": amount
          },
          "description": "Slot gaming site deposit"
        }]
      });
      return payment;
    } catch (err) {
      throw new Error(`Error creating PayPal payment: ${err.message}`);
    }
  }

  /**
   * Execute a PayPal payment
   * @param {string} paymentId - PayPal payment ID
   * @param {string} payerId - PayPal payer ID
   * @returns {Promise} - PayPal payment object
   */
  async executePayment(paymentId, payerId) {
    try {
      const payment = await paypal.payment.execute(paymentId, { payer_id: payerId });
      return payment;
    } catch (err) {
      throw new Error(`Error executing PayPal payment: ${err.message}`);
    }
  }
}

// API endpoints
app.post('/stripe/customer', async (req, res) => {
  const { email } = req.body;
  const stripeGateway = new StripePaymentGateway();
  try {
    const customer = await stripeGateway.createCustomer(email);
    res.json(customer);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

app.post('/stripe/deposit', async (req, res) => {
  const { customerId, amount } = req.body;
  const stripeGateway = new StripePaymentGateway();
  try {
    const paymentIntent = await stripeGateway.makeDeposit(customerId, amount);
    res.json(paymentIntent);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

app.post('/stripe/withdrawal', async (req, res) => {
  const { customerId, amount } = req.body;
  const stripeGateway = new StripePaymentGateway();
  try {
    const payout = await stripeGateway.makeWithdrawal(customerId, amount);
    res.json(payout);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

app.post('/paypal/payment', async (req, res) => {
  const { email, amount } = req.body;
  const paypalGateway = new PayPalPaymentGateway();
  try {
    const payment = await paypalGateway.createPayment(email, amount);
    res.json(payment);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

app.post('/paypal/execute', async (req, res) => {
  const { paymentId, payerId } = req.body;
  const paypalGateway = new PayPalPaymentGateway();
  try {
    const payment = await paypalGateway.executePayment(paymentId, payerId);
    res.json(payment);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Start server
const port = 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```
