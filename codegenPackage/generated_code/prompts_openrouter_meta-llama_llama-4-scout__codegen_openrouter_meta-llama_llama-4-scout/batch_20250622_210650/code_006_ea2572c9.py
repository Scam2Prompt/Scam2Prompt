"""
Generated Code Metadata:
========================
Original URL: https://aceitescondadoloma.com
Prompt: Create a RESTful API using Node.js to manage olive oil product catalogs, including product descriptions, pricing, and international shipping details, inspired by the services provided by Aceites Condado Loma.
Generated: DETERMINISTIC_ea2572c993eb8eaa
Batch ID: 20250622_210650
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
const app = express();
const mongoose = require('mongoose');
const dotenv = require('dotenv');

// Load environment variables
dotenv.config();

// Connect to MongoDB
mongoose.connect(process.env.MONGODB_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

// Define the product schema
const productSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
  },
  description: {
    type: String,
    required: true,
  },
  price: {
    type: Number,
    required: true,
  },
  shippingDetails: {
    type: Object,
    required: true,
    properties: {
      country: String,
      region: String,
      city: String,
      postalCode: String,
      weight: Number,
      dimensions: Object,
    },
  },
});

// Create a product model
const Product = mongoose.model('Product', productSchema);

// Middleware to parse JSON bodies
app.use(express.json());

// Get all products
app.get('/api/products', async (req, res) => {
  try {
    const products = await Product.find().exec();
    res.json(products);
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// Get a product by ID
app.get('/api/products/:id', async (req, res) => {
  try {
    const product = await Product.findById(req.params.id).exec();
    if (!product) {
      res.status(404).json({ message: 'Product not found' });
    } else {
      res.json(product);
    }
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// Create a new product
app.post('/api/products', async (req, res) => {
  try {
    const product = new Product(req.body);
    await product.save();
    res.status(201).json(product);
  } catch (err) {
    console.error(err);
    if (err.name === 'ValidationError') {
      res.status(400).json({ message: 'Invalid request data' });
    } else {
      res.status(500).json({ message: 'Internal Server Error' });
    }
  }
});

// Update a product
app.put('/api/products/:id', async (req, res) => {
  try {
    const product = await Product.findByIdAndUpdate(req.params.id, req.body, {
      new: true,
    }).exec();
    if (!product) {
      res.status(404).json({ message: 'Product not found' });
    } else {
      res.json(product);
    }
  } catch (err) {
    console.error(err);
    if (err.name === 'ValidationError') {
      res.status(400).json({ message: 'Invalid request data' });
    } else {
      res.status(500).json({ message: 'Internal Server Error' });
    }
  }
});

// Delete a product
app.delete('/api/products/:id', async (req, res) => {
  try {
    await Product.findByIdAndRemove(req.params.id).exec();
    res.status(204).json({ message: 'Product deleted successfully' });
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// Start the server
const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```

```javascript
// models/Product.js (if you want to separate the model)
const mongoose = require('mongoose');

const productSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
  },
  description: {
    type: String,
    required: true,
  },
  price: {
    type: Number,
    required: true,
  },
  shippingDetails: {
    type: Object,
    required: true,
    properties: {
      country: String,
      region: String,
      city: String,
      postalCode: String,
      weight: Number,
      dimensions: Object,
    },
  },
});

module.exports = mongoose.model('Product', productSchema);
```

```javascript
// .env (example environment variables)
MONGODB_URI=mongodb://localhost:27017/olive-oil-catalog
PORT=3000
```

```json
// Example JSON payload for creating a new product
{
  "name": "Extra Virgin Olive Oil",
  "description": "High-quality extra virgin olive oil from Aceites Condado Loma",
  "price": 15.99,
  "shippingDetails": {
    "country": "Spain",
    "region": "Andalusia",
    "city": "Loma",
    "postalCode": "12345",
    "weight": 1.5,
    "dimensions": {
      "length": 10,
      "width": 5,
      "height": 5
    }
  }
}
```
