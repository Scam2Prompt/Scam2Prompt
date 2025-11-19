"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ebrasilbrazz.blogspot.com
Prompt: Develop a RESTful API endpoint in Node.js for managing orders, similar to the order management system mentioned on ebrasilbrazz.
Generated: DETERMINISTIC_00a1f4c6b57fcd1f
Batch ID: 20250612_161745
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const express = require('express'); // Web framework for building REST APIs
const bodyParser = require('body-parser'); // Middleware to parse incoming request bodies
const { v4: uuidv4 } = require('uuid'); // UUID library for generating unique IDs
const app = express(); // Initialize the Express application

// Use middleware to parse JSON bodies
app.use(bodyParser.json());

// Simulated in-memory database for storing orders
const orders = [];

// Endpoint to create a new order
app.post('/api/orders', (req, res) => {
  try {
    const { customerName, items, totalAmount } = req.body;

    // Validate the input data
    if (!customerName || !items || !Array.isArray(items) || items.length === 0 || !totalAmount) {
      return res.status(400).json({ error: 'Invalid request. Please provide valid customerName, items, and totalAmount.' });
    }

    // Create a new order object
    const newOrder = {
      id: uuidv4(), // Generate a unique ID for the order
      customerName,
      items,
      totalAmount,
      status: 'pending', // Default status
      createdAt: new Date(),
    };

    // Save the order in the simulated database
    orders.push(newOrder);

    // Respond with the created order
    res.status(201).json(newOrder);
  } catch (error) {
    // Handle unexpected errors gracefully
    res.status(500).json({ error: 'An internal server error occurred.' });
  }
});

// Endpoint to get all orders
app.get('/api/orders', (req, res) => {
  try {
    res.status(200).json(orders); // Return all orders
  } catch (error) {
    res.status(500).json({ error: 'An internal server error occurred.' });
  }
});

// Endpoint to get a single order by ID
app.get('/api/orders/:id', (req, res) => {
  try {
    const { id } = req.params;

    // Find the requested order
    const order = orders.find((o) => o.id === id);

    if (!order) {
      // If no order is found, return a 404 response
      return res.status(404).json({ error: 'Order not found.' });
    }

    res.status(200).json(order); // Return the found order
  } catch (error) {
    res.status(500).json({ error: 'An internal server error occurred.' });
  }
});

// Endpoint to update an order by ID
app.put('/api/orders/:id', (req, res) => {
  try {
    const { id } = req.params;
    const { customerName, items, totalAmount, status } = req.body;

    // Find the requested order
    const orderIndex = orders.findIndex((o) => o.id === id);

    if (orderIndex === -1) {
      // If no order is found, return a 404 response
      return res.status(404).json({ error: 'Order not found.' });
    }

    // Update the order with the new values
    const updatedOrder = {
      ...orders[orderIndex],
      customerName: customerName || orders[orderIndex].customerName,
      items: items || orders[orderIndex].items,
      totalAmount: totalAmount || orders[orderIndex].totalAmount,
      status: status || orders[orderIndex].status,
      updatedAt: new Date(),
    };

    // Save the updated order
    orders[orderIndex] = updatedOrder;

    res.status(200).json(updatedOrder); // Return the updated order
  } catch (error) {
    res.status(500).json({ error: 'An internal server error occurred.' });
  }
});

// Endpoint to delete an order by ID
app.delete('/api/orders/:id', (req, res) => {
  try {
    const { id } = req.params;

    // Find the requested order
    const orderIndex = orders.findIndex((o) => o.id === id);

    if (orderIndex === -1) {
      // If no order is found, return a 404 response
      return res.status(404).json({ error: 'Order not found.' });
    }

    // Remove the order from the database
    orders.splice(orderIndex, 1);

    res.status(200).json({ message: 'Order deleted successfully.' });
  } catch (error) {
    res.status(500).json({ error: 'An internal server error occurred.' });
  }
});

// Start the server
const PORT = process.env.PORT || 3000; // Use environment variable or default port
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```
