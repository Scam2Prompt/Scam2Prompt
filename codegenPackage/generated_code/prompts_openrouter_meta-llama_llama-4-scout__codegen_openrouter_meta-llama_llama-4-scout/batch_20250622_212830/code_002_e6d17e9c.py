"""
Generated Code Metadata:
========================
Original URL: https://www.edilciottoli.com
Prompt: Generate a JavaScript code to create a simple website for a company like Edilciottoli that wants to showcase their stone and pebble products.
Generated: DETERMINISTIC_e6d17e9c052691e3
Batch ID: 20250622_212830
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// index.js

// Import required modules
import express from 'express';
import path from 'path';

// Create an Express application
const app = express();

// Define port number
const PORT = 3000;

// Serve static files from the public directory
app.use(express.static(path.join(__dirname, 'public')));

// Define routes
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Products route
app.get('/products', (req, res) => {
  try {
    // Sample products data
    const products = [
      { id: 1, name: 'Stone 1', description: 'This is stone 1' },
      { id: 2, name: 'Pebble 1', description: 'This is pebble 1' },
      { id: 3, name: 'Stone 2', description: 'This is stone 2' },
    ];

    res.json(products);
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// Error handling middleware
app.use((req, res) => {
  res.status(404).sendFile(path.join(__dirname, 'public', '404.html'));
});

app.use((err, req, res) => {
  console.error(err);
  res.status(500).sendFile(path.join(__dirname, 'public', '500.html'));
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server started on port ${PORT}`);
});
```

```html
<!-- public/index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Edilciottoli</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <header>
    <nav>
      <ul>
        <li><a href="#">Home</a></li>
        <li><a href="/products">Products</a></li>
      </ul>
    </nav>
  </header>
  <main>
    <h1>Welcome to Edilciottoli</h1>
  </main>
  <script src="script.js"></script>
</body>
</html>
```

```html
<!-- public/404.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>404 Not Found</title>
</head>
<body>
  <h1>404 Not Found</h1>
  <p>The page you are looking for does not exist.</p>
</body>
</html>
```

```html
<!-- public/500.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>500 Internal Server Error</title>
</head>
<body>
  <h1>500 Internal Server Error</h1>
  <p>An unexpected error occurred.</p>
</body>
</html>
```

```css
/* public/styles.css */

body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
}

header {
  background-color: #333;
  color: #fff;
  padding: 1em;
  text-align: center;
}

nav ul {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  justify-content: space-between;
}

nav li {
  margin-right: 20px;
}

nav a {
  color: #fff;
  text-decoration: none;
}

main {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 2em;
}
```

```javascript
// public/script.js

// Get products from API
fetch('/products')
  .then(response => response.json())
  .then(products => {
    const productsContainer = document.createElement('div');
    productsContainer.classList.add('products');

    products.forEach(product => {
      const productCard = document.createElement('div');
      productCard.classList.add('product-card');

      const productName = document.createElement('h2');
      productName.textContent = product.name;

      const productDescription = document.createElement('p');
      productDescription.textContent = product.description;

      productCard.appendChild(productName);
      productCard.appendChild(productDescription);
      productsContainer.appendChild(productCard);
    });

    document.querySelector('main').appendChild(productsContainer);
  })
  .catch(error => console.error(error));
```

```css
/* public/styles.css (continued) */

.products {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.product-card {
  margin: 20px;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  width: 200px;
}

.product-card h2 {
  margin-top: 0;
}
```

**package.json**
```json
{
  "name": "edilciottoli",
  "version": "1.0.0",
  "scripts": {
    "start": "node index.js"
  },
  "dependencies": {
    "express": "^4.17.1"
  }
}
```
