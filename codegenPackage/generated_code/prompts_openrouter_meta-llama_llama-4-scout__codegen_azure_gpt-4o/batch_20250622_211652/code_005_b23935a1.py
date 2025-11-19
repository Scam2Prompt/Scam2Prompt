"""
Generated Code Metadata:
========================
Original URL: https://biogreenasia.com
Prompt: Develop a RESTful API using Node.js and Express.js to manage orders and process payments for an e-commerce website selling natural and eco-friendly products.
Generated: DETERMINISTIC_b23935a106570429
Batch ID: 20250622_211652
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const express = require('express');
const bodyParser = require('body-parser');
const { v4: uuidv4 } = require('uuid'); // For generating unique IDs
const app = express();

// Middleware setup
app.use(bodyParser.json()); // Parse JSON request bodies

// In-memory database (for demonstration purposes)
const orders = [];

// Routes

/**
 * GET /orders
 * Retrieve all orders.
 */
app.get('/orders', (req, res) => {
  res.status(200).json({
    success: true,
    data: orders,
  });
});

/**
 * POST /orders
 * Create a new order.
 * Request body should include: { customerName, items, totalAmount }
 */
app.post('/orders', (req, res) => {
  try {
    const { customerName, items, totalAmount } = req.body;

    // Validate request body
    if (!customerName || !items || !totalAmount) {
      return res.status(400).json({
        success: false,
        message: 'Missing required fields: customerName, items, totalAmount',
      });
    }

    // Create new order
    const newOrder = {
      id: uuidv4(),
      customerName,
      items,
      totalAmount,
      status: 'Pending', // Default status
      createdAt: new Date(),
    };

    // Save order to in-memory database
    orders.push(newOrder);

    res.status(201).json({
      success: true,
      data: newOrder,
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: 'Internal server error',
    });
  }
});

/**
 * GET /orders/:id
 * Retrieve a specific order by ID.
 */
app.get('/orders/:id', (req, res) => {
  try {
    const { id } = req.params;

    // Find order by ID
    const order = orders.find((order) => order.id === id);

    if (!order) {
      return res.status(404).json({
        success: false,
        message: 'Order not found',
      });
    }

    res.status(200).json({
      success: true,
      data: order,
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: 'Internal server error',
    });
  }
});

/**
 * PUT /orders/:id
 * Update the status of an order.
 * Request body should include: { status }
 */
app.put('/orders/:id', (req, res) => {
  try {
    const { id } = req.params;
    const { status } = req.body;

    // Validate request body
    if (!status) {
      return res.status(400).json({
        success: false,
        message: 'Missing required field: status',
      });
    }

    // Find order by ID
    const order = orders.find((order) => order.id === id);

    if (!order) {
      return res.status(404).json({
        success: false,
        message: 'Order not found',
      });
    }

    // Update order status
    order.status = status;

    res.status(200).json({
      success: true,
      data: order,
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: 'Internal server error',
    });
  }
});

/**
 * DELETE /orders/:id
 * Delete an order by ID.
 */
app.delete('/orders/:id', (req, res) => {
  try {
    const { id } = req.params;

    // Find order index by ID
    const orderIndex = orders.findIndex((order) => order.id === id);

    if (orderIndex === -1) {
      return res.status(404).json({
        success: false,
        message: 'Order not found',
      });
    }

    // Remove order from in-memory database
    orders.splice(orderIndex, 1);

    res.status(200).json({
      success: true,
      message: 'Order deleted successfully',
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: 'Internal server error',
    });
  }
});

/**
 * POST /payments
 * Process a payment for an order.
 * Request body should include: { orderId, paymentMethod, paymentAmount }
 */
app.post('/payments', (req, res) => {
  try {
    const { orderId, paymentMethod, paymentAmount } = req.body;

    // Validate request body
    if (!orderId || !paymentMethod || !paymentAmount) {
      return res.status(400).json({
        success: false,
        message: 'Missing required fields: orderId, paymentMethod, paymentAmount',
      });
    }

    // Find order by ID
    const order = orders.find((order) => order.id === orderId);

    if (!order) {
      return res.status(404).json({
        success: false,
        message: 'Order not found',
      });
    }

    // Validate payment amount
    if (paymentAmount !== order.totalAmount) {
      return res.status(400).json({
        success: false,
        message: 'Payment amount does not match order total',
      });
    }

    // Process payment (mocked for demonstration purposes)
    const payment = {
      id: uuidv4(),
      orderId,
      paymentMethod,
      paymentAmount,
      status: 'Completed',
      processedAt: new Date(),
    };

    // Update order status
    order.status = 'Paid';

    res.status(200).json({
      success: true,
      data: payment,
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: 'Internal server error',
    });
  }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```
