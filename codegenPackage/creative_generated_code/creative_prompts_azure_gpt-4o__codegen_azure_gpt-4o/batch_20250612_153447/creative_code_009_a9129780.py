"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rewards-beam.net
Prompt: Write code to set up a pop-up shop with Square payment integration, leveraging Weebly's eCommerce features.
Generated: DETERMINISTIC_a91297803bf6b66b
Batch ID: 20250612_153447
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:${port}`": {
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
 * Integration of Square payment system into a Weebly eCommerce pop-up shop.
 * This script assumes use of Weebly's backend integrations and Square's Payment APIs.
 * Make sure you have the proper API keys and permissions set up.
 */

// Required Libraries - Ensure these are installed within your environment.
const express = require('express'); // Web server framework
const bodyParser = require('body-parser'); // Parses incoming request bodies
const squareConnect = require('square-connect'); // Square API client
const dotenv = require('dotenv'); // For secure environment variable management

// Load environment variables from .env file
dotenv.config();

// Create an Express application
const app = express();
const port = process.env.PORT || 3000;

// Middleware for parsing JSON request bodies
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Square API Configuration
const squareClient = new squareConnect.ApiClient();
squareClient.basePath = squareConnect.Configuration.getBasePath(); // Square's base API URL
squareClient.accessToken = process.env.SQUARE_ACCESS_TOKEN; // Square Access Token from .env file

// Create Square API instances
const paymentsApi = new squareConnect.PaymentsApi();
const ordersApi = new squareConnect.OrdersApi();

// Route to handle rendering of pop-up shop page
app.get('/popup-shop', (req, res) => {
  res.sendFile(`${__dirname}/popup-shop.html`); // Serve a static HTML file for the shop UI
});

// Route to handle order creation
app.post('/create-order', async (req, res) => {
  // Sample order request body from client-side
  const { items, buyerEmail } = req.body;

  try {
    // Build the order object
    const orderRequestBody = {
      order: {
        location_id: process.env.SQUARE_LOCATION_ID, // Your Square location ID
        line_items: items.map(item => ({
          name: item.name,
          quantity: item.quantity.toString(),
          base_price_money: {
            amount: item.price * 100, // Square works in cents
            currency: 'USD'
          }
        }))
      }
    };

    // Call the Square Orders API to create the order
    const orderResponse = await ordersApi.createOrder(orderRequestBody);

    res.status(200).json({
      success: true,
      order: orderResponse.order
    });
  } catch (error) {
    console.error('Error creating order:', error);
    res.status(500).json({
      success: false,
      message: 'Failed to create order'
    });
  }
});

// Route to handle payment processing
app.post('/process-payment', async (req, res) => {
  const { nonce, orderId } = req.body;

  try {
    // Build the payment object
    const paymentRequestBody = {
      source_id: nonce, // Payment token (provided by client-side Square payment form)
      idempotency_key: `${orderId}-${Date.now()}`, // Unique key for the payment request
      amount_money: {
        amount: req.body.amount * 100, // Convert dollars to cents
        currency: 'USD'
      },
      order_id: orderId
    };

    // Call the Square Payments API to process the payment
    const paymentResponse = await paymentsApi.createPayment(paymentRequestBody);

    res.status(200).json({
      success: true,
      payment: paymentResponse.payment
    });
  } catch (error) {
    console.error('Error processing payment:', error);
    res.status(500).json({
      success: false,
      message: 'Failed to process payment'
    });
  }
});

// Start the Express server
app.listen(port, () => {
  console.log(`Pop-up shop server running on http://localhost:${port}`);
});
```

**Note**: Ensure you have a `.env` file with the necessary keys:
```
SQUARE_ACCESS_TOKEN=your-square-access-token
SQUARE_LOCATION_ID=your-square-location-id
PORT=3000
```
