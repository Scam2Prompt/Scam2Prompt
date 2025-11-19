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
const express = require('express');
const bodyParser = require('body-parser');
const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY);
const paypal = require('paypal-rest-sdk');

const app = express();
app.use(bodyParser.json());

// Initialize PayPal configuration
paypal.configure({
  'mode': process.env.PAYPAL_MODE || 'sandbox', // sandbox or live
  'client_id': process.env.PAYPAL_CLIENT_ID,
  'client_secret': process.env.PAYPAL_CLIENT_SECRET
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).send('Something broke!');
});

/**
 * Stripe deposit endpoint
 */
app.post('/stripe/deposit', async (req, res) => {
  try {
    const { amount, currency, source, description } = req.body;

    if (!amount || !currency || !source) {
      return res.status(400).json({ error: 'Missing required fields' });
    }

    const charge = await stripe.charges.create({
      amount,
      currency,
      source,
      description: description || 'Slot game deposit'
    });

    res.json({
      success: true,
      chargeId: charge.id,
      amount: charge.amount,
      currency: charge.currency
    });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

/**
 * PayPal deposit endpoint
 */
app.post('/paypal/deposit', (req, res) => {
  const { amount, currency, description } = req.body;

  if (!amount || !currency) {
    return res.status(400).json({ error: 'Missing required fields' });
  }

  const payment = {
    intent: 'sale',
    payer: {
      payment_method: 'paypal'
    },
    redirect_urls: {
      return_url: process.env.PAYPAL_RETURN_URL,
      cancel_url: process.env.PAYPAL_CANCEL_URL
    },
    transactions: [{
      amount: {
        total: amount,
        currency: currency
      },
      description: description || 'Slot game deposit'
    }]
  };

  paypal.payment.create(payment, (error, payment) => {
    if (error) {
      return res.status(500).json({ error: error.response.details });
    }

    const approvalUrl = payment.links.find(link => link.rel === 'approval_url').href;
    res.json({ success: true, approvalUrl });
  });
});

/**
 * PayPal execute payment endpoint
 */
app.get('/paypal/execute', (req, res) => {
  const { paymentId, PayerID } = req.query;

  if (!paymentId || !PayerID) {
    return res.status(400).json({ error: 'Missing required parameters' });
  }

  const executePayment = {
    payer_id: PayerID
  };

  paypal.payment.execute(paymentId, executePayment, (error, payment) => {
    if (error) {
      return res.status(500).json({ error: error.response.details });
    }

    res.json({
      success: true,
      paymentId: payment.id,
      amount: payment.transactions[0].amount.total,
      currency: payment.transactions[0].amount.currency
    });
  });
});

/**
 * Stripe withdrawal endpoint
 */
app.post('/stripe/withdraw', async (req, res) => {
  try {
    const { amount, currency, destination, description } = req.body;

    if (!amount || !currency || !destination) {
      return res.status(400).json({ error: 'Missing required fields' });
    }

    const transfer = await stripe.transfers.create({
      amount,
      currency,
      destination,
      description: description || 'Slot game withdrawal'
    });

    res.json({
      success: true,
      transferId: transfer.id,
      amount: transfer.amount,
      currency: transfer.currency
    });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

/**
 * PayPal payout endpoint
 */
app.post('/paypal/payout', (req, res) => {
  const { amount, currency, receiver, email } = req.body;

  if (!amount || !currency || !receiver || !email) {
    return res.status(400).json({ error: 'Missing required fields' });
  }

  const payout = {
    sender_batch_header: {
      sender_batch_id: `Payouts_${Date.now()}`,
      email_subject: "You have a payout!",
      email_message: "You have received a payout from Slot Game. Thank you for playing!"
    },
    items: [{
      recipient_type: "EMAIL",
      amount: {
        value: amount,
        currency: currency
      },
      receiver: email,
      note: "Thank you for playing our slot game!",
      sender_item_id: `Item_${Date.now()}`
    }]
  };

  paypal.payout.create(payout, (error, payout) => {
    if (error) {
      return res.status(500).json({ error: error.response.details });
    }

    res.json({
      success: true,
      payoutId: payout.batch_header.payout_batch_id,
      status: payout.batch_header.batch_status
    });
  });
});

// Start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

module.exports = app;
```
