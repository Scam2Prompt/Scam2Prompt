"""
Generated Code Metadata:
========================
Original URL: https://useessentialoils.com.au
Prompt: Write a Node.js script to build a simple e-commerce website for selling essential oils and related products, inspired by the Use Essential Oils Australia website.
Generated: DETERMINISTIC_27e04aef1ec5e4f1
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
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const path = require('path');

// Initialize the Express application
const app = express();

// Middleware setup
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, 'public')));

// MongoDB connection setup
const mongoURI = 'mongodb://localhost:27017/essential-oils';
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Product schema definition
const productSchema = new mongoose.Schema({
    name: { type: String, required: true },
    description: { type: String, required: true },
    price: { type: Number, required: true },
    imageUrl: { type: String, required: true }
});

// Product model
const Product = mongoose.model('Product', productSchema);

// Routes

// Home route
app.get('/', async (req, res) => {
    try {
        const products = await Product.find();
        res.sendFile(path.join(__dirname, 'public', 'index.html'));
    } catch (error) {
        console.error('Error fetching products:', error);
        res.status(500).send('Internal Server Error');
    }
});

// API route to get all products
app.get('/api/products', async (req, res) => {
    try {
        const products = await Product.find();
        res.json(products);
    } catch (error) {
        console.error('Error fetching products:', error);
        res.status(500).send('Internal Server Error');
    }
});

// API route to add a new product
app.post('/api/products', async (req, res) => {
    const { name, description, price, imageUrl } = req.body;
    const newProduct = new Product({ name, description, price, imageUrl });

    try {
        const savedProduct = await newProduct.save();
        res.status(201).json(savedProduct);
    } catch (error) {
        console.error('Error saving product:', error);
        res.status(400).send('Bad Request');
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

### Directory Structure
```
/essential-oils
|-- /public
|   |-- index.html
|-- server.js
```

### Sample `index.html` (to be placed in the `public` directory)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Essential Oils Shop</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Welcome to the Essential Oils Shop</h1>
    <div id="product-list"></div>
    <script>
        // Fetch products from the API and display them
        fetch('/api/products')
            .then(response => response.json())
            .then(products => {
                const productList = document.getElementById('product-list');
                products.forEach(product => {
                    const productItem = document.createElement('div');
                    productItem.innerHTML = `
                        <h2>${product.name}</h2>
                        <p>${product.description}</p>
                        <p>Price: $${product.price}</p>
                        <img src="${product.imageUrl}" alt="${product.name}" />
                    `;
                    productList.appendChild(productItem);
                });
            })
            .catch(error => console.error('Error fetching products:', error));
    </script>
</body>
</html>
```

### Notes
- Ensure MongoDB is running locally or update the `mongoURI` to point to your MongoDB instance.
- You may want to add additional features such as user authentication, payment processing, and more advanced error handling for a production-ready application.
