"""
Generated Code Metadata:
========================
Original URL: https://ablakvaros.hu.ablak-nyilaszaro.hu
Prompt: "Create a RESTful API using Node.js to manage orders for window and door installations, including endpoints for calculating costs and scheduling installations."
Generated: DETERMINISTIC_751ae2dfa94be0b9
Batch ID: 20250622_210703
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
const { v4: uuidv4 } = require('uuid');
const cors = require('cors');

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Enable CORS and JSON body parsing
app.use(cors());
app.use(bodyParser.json());

// In-memory database for orders
let orders = [];

// Product pricing configuration
const PRODUCT_PRICES = {
  window: {
    standard: 200,
    premium: 350
  },
  door: {
    standard: 500,
    premium: 800
  }
};

// Installation scheduling configuration
const INSTALLATION_SLOTS = {
  morning: '9:00 AM - 12:00 PM',
  afternoon: '1:00 PM - 4:00 PM',
  evening: '5:00 PM - 8:00 PM'
};

// Helper function to validate order data
const validateOrderData = (data) => {
  if (!data.customerName || typeof data.customerName !== 'string') {
    throw new Error('Invalid customer name');
  }
  if (!data.address || typeof data.address !== 'string') {
    throw new Error('Invalid address');
  }
  if (!data.products || !Array.isArray(data.products) || data.products.length === 0) {
    throw new Error('Invalid products');
  }
  if (!data.installationDate || !(new Date(data.installationDate) instanceof Date) || isNaN(new Date(data.installationDate).getTime())) {
    throw new Error('Invalid installation date');
  }
  if (!data.installationSlot || !INSTALLATION_SLOTS[data.installationSlot]) {
    throw new Error('Invalid installation slot');
  }

  for (const product of data.products) {
    if (!product.type || !PRODUCT_PRICES[product.type]) {
      throw new Error(`Invalid product type: ${product.type}`);
    }
    if (!product.quality || !PRODUCT_PRICES[product.type][product.quality]) {
      throw new Error(`Invalid product quality: ${product.quality}`);
    }
    if (!product.quantity || typeof product.quantity !== 'number' || product.quantity <= 0) {
      throw new Error(`Invalid quantity for product: ${product.type}`);
    }
  }
};

// Calculate total cost for an order
const calculateTotalCost = (products) => {
  return products.reduce((total, product) => {
    return total + (PRODUCT_PRICES[product.type][product.quality] * product.quantity);
  }, 0);
};

// Check if installation slot is available
const isSlotAvailable = (date, slot) => {
  return !orders.some(order => 
    order.installationDate === date && 
    order.installationSlot === slot &&
    order.status !== 'cancelled'
  );
};

// API Endpoints

// Create a new order
app.post('/api/orders', (req, res) => {
  try {
    validateOrderData(req.body);
    
    const { installationDate, installationSlot } = req.body;
    if (!isSlotAvailable(installationDate, installationSlot)) {
      return res.status(400).json({ error: 'Installation slot is not available' });
    }

    const order = {
      id: uuidv4(),
      ...req.body,
      totalCost: calculateTotalCost(req.body.products),
      status: 'pending',
      createdAt: new Date().toISOString()
    };

    orders.push(order);
    res.status(201).json(order);
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});

// Get all orders
app.get('/api/orders', (req, res) => {
  res.json(orders);
});

// Get order by ID
app.get('/api/orders/:id', (req, res) => {
  const order = orders.find(o => o.id === req.params.id);
  if (!order) {
    return res.status(404).json({ error: 'Order not found' });
  }
  res.json(order);
});

// Update order status
app.patch('/api/orders/:id/status', (req, res) => {
  const { status } = req.body;
  const validStatuses = ['pending', 'confirmed', 'completed', 'cancelled'];
  
  if (!validStatuses.includes(status)) {
    return res.status(400).json({ error: 'Invalid status' });
  }

  const orderIndex = orders.findIndex(o => o.id === req.params.id);
  if (orderIndex === -1) {
    return res.status(404).json({ error: 'Order not found' });
  }

  orders[orderIndex].status = status;
  res.json(orders[orderIndex]);
});

// Calculate cost without creating an order
app.post('/api/calculate-cost', (req, res) => {
  try {
    if (!req.body.products || !Array.isArray(req.body.products) || req.body.products.length === 0) {
      throw new Error('Invalid products');
    }

    for (const product of req.body.products) {
      if (!product.type || !PRODUCT_PRICES[product.type]) {
        throw new Error(`Invalid product type: ${product.type}`);
      }
      if (!product.quality || !PRODUCT_PRICES[product.type][product.quality]) {
        throw new Error(`Invalid product quality: ${product.quality}`);
      }
      if (!product.quantity || typeof product.quantity !== 'number' || product.quantity <= 0) {
        throw new Error(`Invalid quantity for product: ${product.type}`);
      }
    }

    const totalCost = calculateTotalCost(req.body.products);
    res.json({ totalCost });
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});

// Get available installation slots for a date
app.get('/api/available-slots/:date', (req, res) => {
  try {
    const date = req.params.date;
    if (!(new Date(date) instanceof Date) || isNaN(new Date(date).getTime())) {
      throw new Error('Invalid date');
    }

    const availableSlots = Object.keys(INSTALLATION_SLOTS).filter(slot => 
      isSlotAvailable(date, slot)
    );

    res.json({ 
      date, 
      availableSlots: availableSlots.map(slot => ({
        slot,
        time: INSTALLATION_SLOTS[slot]
      })) 
    });
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Something went wrong!' });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

// Export app for testing
module.exports = app;
```
