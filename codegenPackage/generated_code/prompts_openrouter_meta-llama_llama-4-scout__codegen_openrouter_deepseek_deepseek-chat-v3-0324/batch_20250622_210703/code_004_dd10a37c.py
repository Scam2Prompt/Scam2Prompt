"""
Generated Code Metadata:
========================
Original URL: https://huylongagri.com
Prompt: "Create a RESTful API using Node.js to manage coffee orders and shipments for a company like Huy Long Agri."
Generated: DETERMINISTIC_dd10a37c43809ef5
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
const mongoose = require('mongoose');
const cors = require('cors');
const { v4: uuidv4 } = require('uuid');

// Initialize Express app
const app = express();

// Middleware
app.use(cors());
app.use(bodyParser.json());

// MongoDB connection
mongoose.connect('mongodb://localhost:27017/huyLongAgri', {
  useNewUrlParser: true,
  useUnifiedTopology: true
})
.then(() => console.log('Connected to MongoDB'))
.catch(err => console.error('MongoDB connection error:', err));

// Define Mongoose schemas
const orderSchema = new mongoose.Schema({
  orderId: { type: String, default: uuidv4, unique: true },
  customerName: { type: String, required: true },
  coffeeType: { type: String, required: true },
  quantity: { type: Number, required: true, min: 1 },
  orderDate: { type: Date, default: Date.now },
  status: { type: String, enum: ['pending', 'processing', 'shipped', 'delivered'], default: 'pending' },
  pricePerUnit: { type: Number, required: true, min: 0 },
  shippingAddress: { type: String, required: true }
});

const shipmentSchema = new mongoose.Schema({
  shipmentId: { type: String, default: uuidv4, unique: true },
  orderId: { type: String, required: true, ref: 'Order' },
  shippingDate: { type: Date, default: Date.now },
  estimatedDelivery: { type: Date, required: true },
  carrier: { type: String, required: true },
  trackingNumber: { type: String, required: true },
  status: { type: String, enum: ['in-transit', 'delivered', 'returned'], default: 'in-transit' }
});

// Create models
const Order = mongoose.model('Order', orderSchema);
const Shipment = mongoose.model('Shipment', shipmentSchema);

// Helper function for error handling
const handleError = (res, err, statusCode = 500) => {
  console.error(err);
  res.status(statusCode).json({ error: err.message });
};

// Routes for Orders
app.get('/api/orders', async (req, res) => {
  try {
    const orders = await Order.find();
    res.json(orders);
  } catch (err) {
    handleError(res, err);
  }
});

app.get('/api/orders/:id', async (req, res) => {
  try {
    const order = await Order.findOne({ orderId: req.params.id });
    if (!order) return res.status(404).json({ error: 'Order not found' });
    res.json(order);
  } catch (err) {
    handleError(res, err);
  }
});

app.post('/api/orders', async (req, res) => {
  try {
    const newOrder = new Order(req.body);
    const savedOrder = await newOrder.save();
    res.status(201).json(savedOrder);
  } catch (err) {
    handleError(res, err, 400);
  }
});

app.put('/api/orders/:id', async (req, res) => {
  try {
    const updatedOrder = await Order.findOneAndUpdate(
      { orderId: req.params.id },
      req.body,
      { new: true }
    );
    if (!updatedOrder) return res.status(404).json({ error: 'Order not found' });
    res.json(updatedOrder);
  } catch (err) {
    handleError(res, err, 400);
  }
});

app.delete('/api/orders/:id', async (req, res) => {
  try {
    const deletedOrder = await Order.findOneAndDelete({ orderId: req.params.id });
    if (!deletedOrder) return res.status(404).json({ error: 'Order not found' });
    res.json({ message: 'Order deleted successfully' });
  } catch (err) {
    handleError(res, err);
  }
});

// Routes for Shipments
app.get('/api/shipments', async (req, res) => {
  try {
    const shipments = await Shipment.find().populate('orderId');
    res.json(shipments);
  } catch (err) {
    handleError(res, err);
  }
});

app.get('/api/shipments/:id', async (req, res) => {
  try {
    const shipment = await Shipment.findOne({ shipmentId: req.params.id }).populate('orderId');
    if (!shipment) return res.status(404).json({ error: 'Shipment not found' });
    res.json(shipment);
  } catch (err) {
    handleError(res, err);
  }
});

app.post('/api/shipments', async (req, res) => {
  try {
    // Verify the order exists
    const order = await Order.findOne({ orderId: req.body.orderId });
    if (!order) return res.status(404).json({ error: 'Order not found' });

    // Update order status
    await Order.findOneAndUpdate(
      { orderId: req.body.orderId },
      { status: 'shipped' }
    );

    const newShipment = new Shipment(req.body);
    const savedShipment = await newShipment.save();
    res.status(201).json(savedShipment);
  } catch (err) {
    handleError(res, err, 400);
  }
});

app.put('/api/shipments/:id', async (req, res) => {
  try {
    const updatedShipment = await Shipment.findOneAndUpdate(
      { shipmentId: req.params.id },
      req.body,
      { new: true }
    );
    if (!updatedShipment) return res.status(404).json({ error: 'Shipment not found' });
    
    // If status is updated to delivered, update order status
    if (req.body.status === 'delivered') {
      await Order.findOneAndUpdate(
        { orderId: updatedShipment.orderId },
        { status: 'delivered' }
      );
    }
    
    res.json(updatedShipment);
  } catch (err) {
    handleError(res, err, 400);
  }
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Something went wrong!' });
});

// Start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

// Export for testing
module.exports = app;
```
