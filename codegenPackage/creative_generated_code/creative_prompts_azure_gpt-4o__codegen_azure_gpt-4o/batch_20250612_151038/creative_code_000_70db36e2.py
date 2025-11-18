"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://orderly-network.pages.dev
Prompt: Write code using the Orderly SDK to create a custom trading front-end that integrates with the permissionless liquidity layer for Web3 trading.
Generated: DETERMINISTIC_70db36e2f8b0c320
Batch ID: 20250612_151038
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
import OrderlySDK from 'orderly-sdk'; // Ensure you've installed the Orderly SDK via npm or yarn
import dotenv from 'dotenv'; // For environment variable management
import express from 'express'; // Backend framework for API handling
import bodyParser from 'body-parser'; // Parse incoming JSON requests
import cors from 'cors'; // Enable cross-origin requests

// Load environment variables from .env file
dotenv.config();

// Constants
const PORT = process.env.PORT || 3000; // Set the port for the server
const ORDERLY_API_KEY = process.env.ORDERLY_API_KEY; // Your API key for Orderly
const ORDERLY_SECRET_KEY = process.env.ORDERLY_SECRET_KEY; // Your secret key for Orderly

// Initialize the Orderly SDK
const orderlyClient = new OrderlySDK({
  apiKey: ORDERLY_API_KEY,
  secretKey: ORDERLY_SECRET_KEY,
});

// Create and configure the Express app
const app = express();
app.use(cors());
app.use(bodyParser.json());

// Utility function to validate incoming data
const validateInput = (data, requiredFields) => {
  const errors = [];
  requiredFields.forEach((field) => {
    if (!data[field]) {
      errors.push(`Missing field: ${field}`);
    }
  });
  return errors;
};

/**
 * Endpoint: Get available trading pairs
 * Description: Fetches the list of available trading pairs from the Orderly SDK
 */
app.get('/api/trading-pairs', async (req, res) => {
  try {
    const pairs = await orderlyClient.getTradingPairs();
    res.status(200).json({ success: true, data: pairs });
  } catch (error) {
    console.error('Error fetching trading pairs:', error);
    res.status(500).json({ success: false, message: 'Failed to fetch trading pairs' });
  }
});

/**
 * Endpoint: Place an order
 * Description: Allows users to place a trading order via the Orderly SDK
 * Request Body: { pair, side, price, amount }
 */
app.post('/api/place-order', async (req, res) => {
  const requiredFields = ['pair', 'side', 'price', 'amount'];
  const validationErrors = validateInput(req.body, requiredFields);

  if (validationErrors.length > 0) {
    return res.status(400).json({ success: false, errors: validationErrors });
  }

  const { pair, side, price, amount } = req.body;

  try {
    const orderResponse = await orderlyClient.placeOrder({
      pair,
      side,
      price,
      amount,
    });
    res.status(200).json({ success: true, data: orderResponse });
  } catch (error) {
    console.error('Error placing order:', error);
    res.status(500).json({ success: false, message: 'Failed to place order' });
  }
});

/**
 * Endpoint: Cancel an order
 * Description: Cancels an existing order via the Orderly SDK
 * Request Body: { orderId }
 */
app.post('/api/cancel-order', async (req, res) => {
  const requiredFields = ['orderId'];
  const validationErrors = validateInput(req.body, requiredFields);

  if (validationErrors.length > 0) {
    return res.status(400).json({ success: false, errors: validationErrors });
  }

  const { orderId } = req.body;

  try {
    const cancelResponse = await orderlyClient.cancelOrder(orderId);
    res.status(200).json({ success: true, data: cancelResponse });
  } catch (error) {
    console.error('Error cancelling order:', error);
    res.status(500).json({ success: false, message: 'Failed to cancel order' });
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Trading front-end server is running on port ${PORT}`);
});
```

**Notes:**
- Ensure you have installed `orderly-sdk`, `dotenv`, `express`, `body-parser`, and `cors` via npm or yarn.
- Configure a `.env` file to include your `ORDERLY_API_KEY` and `ORDERLY_SECRET_KEY`.
- Further integration or UI components can be developed separately in a front-end framework (e.g., React).
