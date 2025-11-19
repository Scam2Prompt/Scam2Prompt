"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usaseoseller.com
Prompt: Develop a Node.js application that tracks the delivery status of purchased services from usaseoseller.com.
Generated: DETERMINISTIC_54d3c3fa19221fb3
Batch ID: 20250612_155332
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const express = require('express'); // Framework for building web apps
const bodyParser = require('body-parser'); // Middleware for parsing JSON requests
const { v4: uuidv4 } = require('uuid'); // For generating unique IDs

// Initialize the app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware for parsing JSON requests
app.use(bodyParser.json());

// In-memory storage for tracking service delivery status
// In a production environment, this would be replaced with a database
const deliveryStatus = {};

/**
 * Endpoint: Create a new service order
 * Method: POST
 * URL: /order
 * Request Body: { "serviceName": "string", "customerName": "string" }
 */
app.post('/order', (req, res) => {
  const { serviceName, customerName } = req.body;

  // Validate input
  if (!serviceName || !customerName) {
    return res.status(400).json({ error: 'Service name and customer name are required.' });
  }

  // Generate a unique order ID
  const orderId = uuidv4();

  // Initialize order status
  deliveryStatus[orderId] = {
    serviceName,
    customerName,
    status: 'Pending', // Default status
    createdAt: new Date(),
  };

  // Respond with the order ID
  res.status(201).json({ orderId, message: 'Order created successfully.' });
});

/**
 * Endpoint: Update the delivery status of an order
 * Method: PUT
 * URL: /order/:orderId
 * Request Body: { "status": "string" }
 */
app.put('/order/:orderId', (req, res) => {
  const { orderId } = req.params;
  const { status } = req.body;

  // Validate input
  if (!status) {
    return res.status(400).json({ error: 'Status is required.' });
  }

  // Check if the order exists
  const order = deliveryStatus[orderId];
  if (!order) {
    return res.status(404).json({ error: 'Order not found.' });
  }

  // Update the order status
  order.status = status;

  // Respond with the updated order details
  res.status(200).json({ orderId, message: 'Order status updated successfully.', order });
});

/**
 * Endpoint: Get the delivery status of an order
 * Method: GET
 * URL: /order/:orderId
 */
app.get('/order/:orderId', (req, res) => {
  const { orderId } = req.params;

  // Check if the order exists
  const order = deliveryStatus[orderId];
  if (!order) {
    return res.status(404).json({ error: 'Order not found.' });
  }

  // Respond with the order details
  res.status(200).json(order);
});

/**
 * Start the server
 */
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

/**
 * Error handling middleware
 * Catches any unhandled errors and responds with a 500 status
 */
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Something went wrong!' });
});
```
