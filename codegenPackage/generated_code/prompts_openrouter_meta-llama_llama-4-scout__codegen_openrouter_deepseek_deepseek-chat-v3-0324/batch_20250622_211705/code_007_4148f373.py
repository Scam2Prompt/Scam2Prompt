"""
Generated Code Metadata:
========================
Original URL: https://receitaslucrativas.digital
Prompt: "Create a simple e-commerce API using Node.js and Express.js to manage sales of luxury crochet products, similar to the ones described in the Receitas Lucrativas course."
Generated: DETERMINISTIC_4148f3738cd8a2b2
Batch ID: 20250622_211705
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
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');

// Initialize Express app
const app = express();

// Apply security middleware
app.use(helmet());
app.use(cors());

// Rate limiting to prevent brute force attacks
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100 // limit each IP to 100 requests per windowMs
});
app.use(limiter);

// Body parser middleware
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Database connection
mongoose.connect('mongodb://localhost:27017/luxury_crochet', {
  useNewUrlParser: true,
  useUnifiedTopology: true
})
.then(() => console.log('MongoDB connected successfully'))
.catch(err => console.error('MongoDB connection error:', err));

// Product Schema
const ProductSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
    trim: true
  },
  description: {
    type: String,
    required: true
  },
  price: {
    type: Number,
    required: true,
    min: 0
  },
  category: {
    type: String,
    required: true,
    enum: ['hats', 'scarves', 'blankets', 'accessories']
  },
  stock: {
    type: Number,
    required: true,
    min: 0
  },
  createdAt: {
    type: Date,
    default: Date.now
  },
  updatedAt: {
    type: Date,
    default: Date.now
  }
});

// Order Schema
const OrderSchema = new mongoose.Schema({
  products: [{
    productId: {
      type: mongoose.Schema.Types.ObjectId,
      ref: 'Product',
      required: true
    },
    quantity: {
      type: Number,
      required: true,
      min: 1
    }
  }],
  totalAmount: {
    type: Number,
    required: true,
    min: 0
  },
  customerName: {
    type: String,
    required: true,
    trim: true
  },
  customerEmail: {
    type: String,
    required: true,
    trim: true
  },
  shippingAddress: {
    type: String,
    required: true
  },
  status: {
    type: String,
    default: 'pending',
    enum: ['pending', 'processing', 'shipped', 'delivered', 'cancelled']
  },
  createdAt: {
    type: Date,
    default: Date.now
  },
  updatedAt: {
    type: Date,
    default: Date.now
  }
});

// Models
const Product = mongoose.model('Product', ProductSchema);
const Order = mongoose.model('Order', OrderSchema);

// API Routes

// Health check endpoint
app.get('/api/health', (req, res) => {
  res.status(200).json({ status: 'OK' });
});

// Product routes
app.route('/api/products')
  // Get all products
  .get(async (req, res) => {
    try {
      const products = await Product.find();
      res.json(products);
    } catch (err) {
      res.status(500).json({ error: 'Failed to fetch products' });
    }
  })
  // Create new product
  .post(async (req, res) => {
    try {
      const product = new Product(req.body);
      await product.save();
      res.status(201).json(product);
    } catch (err) {
      res.status(400).json({ error: 'Failed to create product', details: err.message });
    }
  });

app.route('/api/products/:id')
  // Get single product
  .get(async (req, res) => {
    try {
      const product = await Product.findById(req.params.id);
      if (!product) {
        return res.status(404).json({ error: 'Product not found' });
      }
      res.json(product);
    } catch (err) {
      res.status(500).json({ error: 'Failed to fetch product' });
    }
  })
  // Update product
  .put(async (req, res) => {
    try {
      const product = await Product.findByIdAndUpdate(
        req.params.id,
        { ...req.body, updatedAt: Date.now() },
        { new: true }
      );
      if (!product) {
        return res.status(404).json({ error: 'Product not found' });
      }
      res.json(product);
    } catch (err) {
      res.status(400).json({ error: 'Failed to update product', details: err.message });
    }
  })
  // Delete product
  .delete(async (req, res) => {
    try {
      const product = await Product.findByIdAndDelete(req.params.id);
      if (!product) {
        return res.status(404).json({ error: 'Product not found' });
      }
      res.json({ message: 'Product deleted successfully' });
    } catch (err) {
      res.status(500).json({ error: 'Failed to delete product' });
    }
  });

// Order routes
app.route('/api/orders')
  // Get all orders
  .get(async (req, res) => {
    try {
      const orders = await Order.find().populate('products.productId');
      res.json(orders);
    } catch (err) {
      res.status(500).json({ error: 'Failed to fetch orders' });
    }
  })
  // Create new order
  .post(async (req, res) => {
    try {
      // Validate products and calculate total
      let totalAmount = 0;
      const products = [];
      
      for (const item of req.body.products) {
        const product = await Product.findById(item.productId);
        if (!product) {
          return res.status(404).json({ error: `Product with ID ${item.productId} not found` });
        }
        if (product.stock < item.quantity) {
          return res.status(400).json({ error: `Insufficient stock for product ${product.name}` });
        }
        
        totalAmount += product.price * item.quantity;
        products.push({
          productId: product._id,
          quantity: item.quantity
        });
        
        // Update product stock
        product.stock -= item.quantity;
        await product.save();
      }
      
      const order = new Order({
        ...req.body,
        products,
        totalAmount
      });
      
      await order.save();
      res.status(201).json(order);
    } catch (err) {
      res.status(400).json({ error: 'Failed to create order', details: err.message });
    }
  });

app.route('/api/orders/:id')
  // Get single order
  .get(async (req, res) => {
    try {
      const order = await Order.findById(req.params.id).populate('products.productId');
      if (!order) {
        return res.status(404).json({ error: 'Order not found' });
      }
      res.json(order);
    } catch (err) {
      res.status(500).json({ error: 'Failed to fetch order' });
    }
  })
  // Update order status
  .patch(async (req, res) => {
    try {
      if (!req.body.status) {
        return res.status(400).json({ error: 'Status is required' });
      }
      
      const order = await Order.findByIdAndUpdate(
        req.params.id,
        { status: req.body.status, updatedAt: Date.now() },
        { new: true }
      ).populate('products.productId');
      
      if (!order) {
        return res.status(404).json({ error: 'Order not found' });
      }
      res.json(order);
    } catch (err) {
      res.status(400).json({ error: 'Failed to update order', details: err.message });
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

// Export app for testing
module.exports = app;
```
