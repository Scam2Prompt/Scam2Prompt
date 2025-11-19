"""
Generated Code Metadata:
========================
Original URL: https://dataonmatrix.com
Prompt: Develop a minimum viable product (MVP) for an e-commerce platform using React and MongoDB, as outlined in the custom solutions section of Data on Matrix.
Generated: DETERMINISTIC_67c4f5697ca2dca6
Batch ID: 20250612_154520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**E-Commerce Platform MVP**
==========================

### Backend (Node.js, Express, MongoDB)

**models/Product.js**
```javascript
const mongoose = require('mongoose');

const productSchema = new mongoose.Schema({
  name: String,
  description: String,
  price: Number,
  image: String
});

module.exports = mongoose.model('Product', productSchema);
```

**models/User.js**
```javascript
const mongoose = require('mongoose');
const bcrypt = require('bcrypt');

const userSchema = new mongoose.Schema({
  email: String,
  password: String,
  name: String,
  role: { type: String, enum: ['admin', 'customer'] }
});

userSchema.pre('save', async function(next) {
  if (this.isNew || this.isModified('password')) {
    this.password = await bcrypt.hash(this.password, 10);
  }
  next();
});

module.exports = mongoose.model('User', userSchema);
```

**routes/auth.js**
```javascript
const express = require('express');
const router = express.Router();
const User = require('../models/User');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');

router.post('/register', async (req, res) => {
  try {
    const { email, password, name } = req.body;
    const user = new User({ email, password, name, role: 'customer' });
    await user.save();
    res.json({ message: 'User created successfully' });
  } catch (error) {
    res.status(400).json({ message: error.message });
  }
});

router.post('/login', async (req, res) => {
  try {
    const { email, password } = req.body;
    const user = await User.findOne({ email });
    if (!user) {
      return res.status(401).json({ message: 'Invalid credentials' });
    }
    const isValidPassword = await bcrypt.compare(password, user.password);
    if (!isValidPassword) {
      return res.status(401).json({ message: 'Invalid credentials' });
    }
    const token = jwt.sign({ userId: user._id }, process.env.SECRET_KEY, {
      expiresIn: '1h'
    });
    res.json({ token });
  } catch (error) {
    res.status(400).json({ message: error.message });
  }
});

module.exports = router;
```

**routes/products.js**
```javascript
const express = require('express');
const router = express.Router();
const Product = require('../models/Product');

router.get('/', async (req, res) => {
  try {
    const products = await Product.find();
    res.json(products);
  } catch (error) {
    res.status(400).json({ message: error.message });
  }
});

router.post('/', async (req, res) => {
  try {
    const product = new Product(req.body);
    await product.save();
    res.json({ message: 'Product created successfully' });
  } catch (error) {
    res.status(400).json({ message: error.message });
  }
});

module.exports = router;
```

**app.js**
```javascript
const express = require('express');
const app = express();
const mongoose = require('mongoose');
const authRoutes = require('./routes/auth');
const productRoutes = require('./routes/products');

mongoose.connect('mongodb://localhost/ecommerce', {
  useNewUrlParser: true,
  useUnifiedTopology: true
});

app.use(express.json());
app.use('/api/auth', authRoutes);
app.use('/api/products', productRoutes);

app.listen(3001, () => {
  console.log('Server listening on port 3001');
});
```

### Frontend (React)

**components/Product.js**
```javascript
import React from 'react';

const Product = ({ product }) => {
  return (
    <div>
      <h2>{product.name}</h2>
      <p>{product.description}</p>
      <p>Price: ${product.price}</p>
      <img src={product.image} alt={product.name} />
    </div>
  );
};

export default Product;
```

**components/ProductList.js**
```javascript
import React, { useState, useEffect } from 'react';
import Product from './Product';

const ProductList = () => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    fetch('/api/products')
      .then(response => response.json())
      .then(data => setProducts(data));
  }, []);

  return (
    <div>
      <h1>Product List</h1>
      {products.map(product => (
        <Product key={product._id} product={product} />
      ))}
    </div>
  );
};

export default ProductList;
```

**components/Login.js**
```javascript
import React, { useState } from 'react';

const Login = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await fetch('/api/auth/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, password })
      });
      const data = await response.json();
      if (data.token) {
        localStorage.setItem('token', data.token);
      }
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Email:
        <input type="email" value={email} onChange={(event) => setEmail(event.target.value)} />
      </label>
      <br />
      <label>
        Password:
        <input type="password" value={password} onChange={(event) => setPassword(event.target.value)} />
      </label>
      <br />
      <button type="submit">Login</button>
    </form>
  );
};

export default Login;
```

**App.js**
```javascript
import React from 'react';
import ProductList from './components/ProductList';
import Login from './components/Login';

const App = () => {
  return (
    <div>
      <ProductList />
      <Login />
    </div>
  );
};

export default App;
```

**index.js**
```javascript
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
```
