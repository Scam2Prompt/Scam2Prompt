"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mystrikingly.com
Prompt: Provide code to integrate Stripe payment processing into a Strikingly-built e-commerce site.
Generated: DETERMINISTIC_7334f2477a897640
Batch ID: 20250612_154752
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://js.stripe.com/v3/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * This is an example integration of Stripe payment processing with a Strikingly-built e-commerce site.
 * It assumes you are using a server-side language (Node.js with Express) to handle payment processing securely.
 * Do not expose sensitive keys or logic directly in the client-side code.
 */

const express = require('express');
const bodyParser = require('body-parser');
const stripe = require('stripe')('your_stripe_secret_key'); // Replace with your actual Stripe secret key

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware to parse JSON payloads
app.use(bodyParser.json());

// Endpoint to create a Stripe Payment Intent
app.post('/create-payment-intent', async (req, res) => {
  try {
    // Extract payment details from the request body
    const { amount, currency } = req.body;

    // Validate the request data
    if (!amount || !currency) {
      return res.status(400).json({ error: 'Missing required payment parameters: amount or currency' });
    }

    // Create a payment intent with the specified amount and currency
    const paymentIntent = await stripe.paymentIntents.create({
      amount, // Amount in the smallest currency unit (e.g., cents for USD)
      currency,
      automatic_payment_methods: {
        enabled: true, // Enable automatic payment method handling
      },
    });

    // Respond with the client secret key to complete the payment on the client-side
    res.status(200).json({ clientSecret: paymentIntent.client_secret });
  } catch (error) {
    console.error('Error creating payment intent:', error.message);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Serve the application
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

/**
 * To use this server-side script:
 * 1. Deploy it to a secure server (e.g., AWS, Heroku, or similar).
 * 2. On your Strikingly site, set up a custom "Order Now" button with an onClick event 
 *    that sends the payment details (amount, currency) to this server's `/create-payment-intent` endpoint.
 * 3. Have the client-side code use Stripe.js to handle the payment using the `clientSecret` returned by this endpoint.
 * 
 * Client-side example:
 * 
 * <script src="https://js.stripe.com/v3/"></script>
 * <script>
 *   const stripe = Stripe('your_stripe_publishable_key'); // Replace with your actual Stripe publishable key
 *
 *   async function pay() {
 *     const response = await fetch('/create-payment-intent', {
 *       method: 'POST',
 *       headers: { 'Content-Type': 'application/json' },
 *       body: JSON.stringify({ amount: 1000, currency: 'usd' }) // Replace with actual payment details
 *     });
 *     
 *     const data = await response.json();
 *     const clientSecret = data.clientSecret;
 *
 *     const result = await stripe.confirmPayment({
 *       clientSecret,
 *       payment_method: {
 *         card: stripe.elements().create('card'), // Replace with actual card details
 *       },
 *     });
 *     
 *     if (result.error) {
 *       alert(`Payment failed: ${result.error.message}`);
 *     } else {
 *       alert('Payment successful!');
 *     }
 *   }
 * </script>
 */
```
