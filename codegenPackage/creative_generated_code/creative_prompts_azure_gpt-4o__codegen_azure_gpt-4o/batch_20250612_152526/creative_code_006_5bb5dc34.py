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
// Import dependencies
const paypal = require('@paypal/checkout-server-sdk');
require('dotenv').config(); // For environment variables

// Configure PayPal environment
const environment = new paypal.core.LiveEnvironment(
  process.env.PAYPAL_CLIENT_ID,
  process.env.PAYPAL_CLIENT_SECRET
);
const client = new paypal.core.PayPalHttpClient(environment);

/**
 * Process PayPal payment for discounted products securely.
 * @param {string} productName - Name of the product being purchased.
 * @param {number} originalPrice - Original price of the product.
 * @param {number} discountRate - Discount rate as a percentage (e.g., 20 for 20%).
 * @param {string} currency - Currency code (e.g., 'USD').
 * @returns {Promise<Object>} - Returns PayPal order details or error message.
 */
async function processPayPalPayment(productName, originalPrice, discountRate, currency) {
  try {
    // Validate inputs
    if (!productName || typeof productName !== 'string') {
      throw new Error('Invalid product name.');
    }
    if (originalPrice <= 0 || typeof originalPrice !== 'number') {
      throw new Error('Invalid original price.');
    }
    if (discountRate < 0 || discountRate > 100 || typeof discountRate !== 'number') {
      throw new Error('Invalid discount rate.');
    }
    if (!currency || typeof currency !== 'string') {
      throw new Error('Invalid currency code.');
    }

    // Calculate discounted price
    const discountedPrice = (originalPrice * (100 - discountRate)) / 100;

    // Create PayPal order
    const orderRequest = {
      intent: 'CAPTURE',
      purchase_units: [
        {
          amount: {
            currency_code: currency,
            value: discountedPrice.toFixed(2),
          },
          description: productName,
        },
      ],
    };

    const request = new paypal.orders.OrdersCreateRequest();
    request.requestBody(orderRequest);

    // Execute PayPal order creation
    const response = await client.execute(request);

    // Return PayPal order details
    return {
      status: 'success',
      orderId: response.result.id,
      links: response.result.links,
    };
  } catch (error) {
    // Error handling
    console.error('Error processing PayPal payment:', error.message);
    return {
      status: 'error',
      message: error.message,
    };
  }
}

module.exports = { processPayPalPayment };
```

**Note:** Ensure to set up the `.env` file with `PAYPAL_CLIENT_ID` and `PAYPAL_CLIENT_SECRET` for this code to work securely in production.
