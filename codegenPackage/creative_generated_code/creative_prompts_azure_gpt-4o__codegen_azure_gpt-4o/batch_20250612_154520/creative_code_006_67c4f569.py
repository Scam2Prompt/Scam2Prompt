"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dataonmatrix.com
Prompt: Develop a minimum viable product (MVP) for an e-commerce platform using React and MongoDB, as outlined in the custom solutions section of Data on Matrix.
Generated: DETERMINISTIC_67c4f5697ca2dca6
Batch ID: 20250612_154520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

### Backend: Node.js with Express and MongoDB

```javascript
// server.js
const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const cors = require('cors');

// Load environment variables from .env file
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 5000;

// Middleware
app.use(bodyParser.json());
app.use(cors());

// MongoDB Connection
mongoose
  .connect(process.env.MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('MongoDB connected'))
  .catch((err) => console.error(`MongoDB connection error: ${err}`));

// Models
const Product = mongoose.model('Product', new mongoose.Schema({
  name: { type: String, required: true },
  description: { type: String, required: true },
  price: { type: Number, required: true },
  stock: { type: Number, required: true },
}));

// Routes
app.get('/api/products', async (req, res) => {
  try {
    const products = await Product.find();
    res.status(200).json(products);
  } catch (err) {
    res.status(500).json({ error: 'Failed to fetch products' });
  }
});

app.post('/api/products', async (req, res) => {
  try {
    const { name, description, price, stock } = req.body;
    const product = new Product({ name, description, price, stock });
    await product.save();
    res.status(201).json(product);
  } catch (err) {
    res.status(500).json({ error: 'Failed to create product' });
  }
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

---

### Frontend: React

#### React Application File Structure:
```
src/
├── components/
│   ├── ProductList.js
│   ├── ProductForm.js
├── App.js
├── index.js
```

#### `index.js`
```javascript
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import './index.css'; // Basic styles

ReactDOM.render(<App />, document.getElementById('root'));
```

#### `App.js`
```javascript
import React, { useState, useEffect } from 'react';
import ProductList from './components/ProductList';
import ProductForm from './components/ProductForm';

const App = () => {
  const [products, setProducts] = useState([]);

  // Fetch products from the backend
  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const response = await fetch('/api/products');
        const data = await response.json();
        setProducts(data);
      } catch (error) {
        console.error('Error fetching products:', error);
      }
    };
    fetchProducts();
  }, []);

  // Add a new product
  const addProduct = async (product) => {
    try {
      const response = await fetch('/api/products', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(product),
      });
      const newProduct = await response.json();
      setProducts((prevProducts) => [...prevProducts, newProduct]);
    } catch (error) {
      console.error('Error adding product:', error);
    }
  };

  return (
    <div>
      <h1>E-Commerce Platform</h1>
      <ProductForm addProduct={addProduct} />
      <ProductList products={products} />
    </div>
  );
};

export default App;
```

#### `components/ProductList.js`
```javascript
import React from 'react';

const ProductList = ({ products }) => {
  return (
    <div>
      <h2>Product List</h2>
      {products.length === 0 ? (
        <p>No products available</p>
      ) : (
        <ul>
          {products.map((product) => (
            <li key={product._id}>
              <strong>{product.name}</strong>: {product.description} - ${product.price} (Stock: {product.stock})
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default ProductList;
```

#### `components/ProductForm.js`
```javascript
import React, { useState } from 'react';

const ProductForm = ({ addProduct }) => {
  const [formData, setFormData] = useState({
    name: '',
    description: '',
    price: '',
    stock: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const { name, description, price, stock } = formData;

    // Basic validation
    if (!name || !description || !price || !stock) {
      alert('All fields are required.');
      return;
    }

    addProduct({ name, description, price: parseFloat(price), stock: parseInt(stock, 10) });
    setFormData({ name: '', description: '', price: '', stock: '' });
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Add Product</h2>
      <div>
        <label>Name:</label>
        <input type="text" name="name" value={formData.name} onChange={handleChange} required />
      </div>
      <div>
        <label>Description:</label>
        <input type="text" name="description" value={formData.description} onChange={handleChange} required />
      </div>
      <div>
        <label>Price:</label>
        <input type="number" name="price" value={formData.price} onChange={handleChange} required />
      </div>
      <div>
        <label>Stock:</label>
        <input type="number" name="stock" value={formData.stock} onChange={handleChange} required />
      </div>
      <button type="submit">Add Product</button>
    </form>
  );
};

export default ProductForm;
```

---

### `.env`
```
MONGO_URI=<your_mongodb_connection_string>
PORT=5000
```

---

### Notes
- Run `npm install` for dependencies like `express`, `mongoose`, `cors`, and `body-parser` in the backend.
- In the frontend, run `npm install` for dependencies like `react` and `react-dom`.
- Ensure the backend is running on the same origin or use a proxy configuration in the frontend's `package.json`.
