"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://teamadver.com
Prompt: Write a code snippet for a custom website that integrates SEO-friendly features and e-commerce capabilities, inspired by Team Adver's web development services.
Generated: DETERMINISTIC_cd94a0f93944d46d
Batch ID: 20250612_160526
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:${PORT}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Below is a clean, runnable, and production-ready code snippet for a custom website integrating SEO-friendly features and e-commerce capabilities in Node.js using Express.js, MongoDB, and EJS templates.

```javascript
// Import required modules
const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const helmet = require('helmet'); // For improving security
const compression = require('compression'); // For performance optimization

// Initialize the Express app
const app = express();

// Middleware setup
app.use(bodyParser.urlencoded({ extended: true })); // Parse form data
app.use(bodyParser.json()); // Parse JSON payloads
app.use(helmet()); // Enhance security by setting HTTP headers
app.use(compression()); // Compress HTTP responses for faster delivery
app.use(express.static('public')); // Serve static files like CSS and images

// Set the view engine to EJS for dynamic HTML rendering
app.set('view engine', 'ejs');

// Database connection (MongoDB)
mongoose
  .connect('mongodb://localhost:27017/ecommerceDB', {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  })
  .then(() => console.log('Connected to MongoDB'))
  .catch((err) => console.error('Database connection error:', err));

// Define the product schema and model
const productSchema = new mongoose.Schema({
  name: { type: String, required: true },
  description: { type: String, required: true },
  price: { type: Number, required: true },
  category: { type: String, required: true },
  seoTitle: { type: String, required: true },
  seoDescription: { type: String, required: true },
});

const Product = mongoose.model('Product', productSchema);

// SEO-friendly route for rendering product pages
app.get('/product/:id', async (req, res) => {
  try {
    const product = await Product.findById(req.params.id);
    if (!product) {
      return res.status(404).render('404', { message: 'Product not found' });
    }

    res.render('product', {
      product,
      seoTitle: product.seoTitle,
      seoDescription: product.seoDescription,
    });
  } catch (error) {
    console.error(error);
    res.status(500).render('error', { message: 'Internal Server Error' });
  }
});

// Route to display all products (with sorting and pagination)
app.get('/shop', async (req, res) => {
  try {
    const { category, sortBy, page = 1, limit = 10 } = req.query;

    const filters = category ? { category } : {};
    const sortOptions = sortBy ? { [sortBy]: 1 } : { name: 1 };

    const products = await Product.find(filters)
      .sort(sortOptions)
      .skip((page - 1) * limit)
      .limit(parseInt(limit));

    res.render('shop', { products, page: parseInt(page) });
  } catch (error) {
    console.error(error);
    res.status(500).render('error', { message: 'Internal Server Error' });
  }
});

// Route to add new products (Admin/Developer use case)
app.post('/admin/add-product', async (req, res) => {
  try {
    const { name, description, price, category, seoTitle, seoDescription } = req.body;

    const newProduct = new Product({
      name,
      description,
      price,
      category,
      seoTitle,
      seoDescription,
    });

    await newProduct.save();
    res.status(201).send({ message: 'Product added successfully!' });
  } catch (error) {
    console.error(error);
    res.status(400).send({ message: 'Error adding product', error });
  }
});

// Default error-handling middleware
app.use((req, res) => {
  res.status(404).render('404', { message: 'Page not found' });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});

/* 
Directory Structure:
  - public/
      - css/
      - images/
  - views/
      - shop.ejs
      - product.ejs
      - 404.ejs
      - error.ejs
*/
```

The code includes best practices for error handling, security, and SEO considerations while enabling dynamic rendering of e-commerce product pages.
