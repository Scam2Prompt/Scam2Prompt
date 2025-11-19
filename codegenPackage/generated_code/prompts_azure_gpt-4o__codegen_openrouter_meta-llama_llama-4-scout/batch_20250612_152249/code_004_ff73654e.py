"""
Generated Code Metadata:
========================
Original URL: https://ramjiacro.com
Prompt: Develop a web application prototype for a textile company like Ramji Acro, allowing customers to browse yarn types (grey, dyed, mélange) and place orders online.
Generated: DETERMINISTIC_ff73654e03701c34
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Textile Company Web Application Prototype**
=====================================================

**Backend (Node.js, Express.js)**
---------------------------------

```javascript
// server.js

const express = require('express');
const app = express();
const port = 3000;

// Database connection (for demonstration purposes, use a real database in production)
const yarns = [
  { id: 1, type: 'grey', quantity: 100 },
  { id: 2, type: 'dyed', quantity: 50 },
  { id: 3, type: 'mélange', quantity: 200 },
];

// Middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// API Endpoints

// Get all yarn types
app.get('/api/yarns', (req, res) => {
  try {
    res.json(yarns);
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// Get yarn type by ID
app.get('/api/yarns/:id', (req, res) => {
  try {
    const id = parseInt(req.params.id);
    const yarn = yarns.find((y) => y.id === id);
    if (!yarn) {
      res.status(404).json({ message: 'Yarn not found' });
    } else {
      res.json(yarn);
    }
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// Place order
app.post('/api/orders', (req, res) => {
  try {
    const { yarnId, quantity } = req.body;
    const yarn = yarns.find((y) => y.id === parseInt(yarnId));
    if (!yarn) {
      res.status(404).json({ message: 'Yarn not found' });
    } else if (yarn.quantity < quantity) {
      res.status(400).json({ message: 'Insufficient quantity' });
    } else {
      // Update yarn quantity and create order (for demonstration purposes, use a real database in production)
      yarn.quantity -= quantity;
      res.json({ message: 'Order placed successfully' });
    }
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
```

**Frontend (HTML, CSS, JavaScript)**
--------------------------------------

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Textile Company Web Application</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <h1>Yarn Types</h1>
  <ul id="yarn-list"></ul>
  <form id="order-form">
    <label for="yarn-id">Yarn ID:</label>
    <input type="number" id="yarn-id" name="yarnId"><br><br>
    <label for="quantity">Quantity:</label>
    <input type="number" id="quantity" name="quantity"><br><br>
    <button type="submit">Place Order</button>
  </form>

  <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

body {
  font-family: Arial, sans-serif;
}

#yarn-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

#yarn-list li {
  padding: 10px;
  border-bottom: 1px solid #ccc;
}

#yarn-list li:last-child {
  border-bottom: none;
}

#order-form {
  margin-top: 20px;
}
```

```javascript
// script.js

const yarnList = document.getElementById('yarn-list');
const orderForm = document.getElementById('order-form');

// Get all yarn types
fetch('/api/yarns')
  .then((response) => response.json())
  .then((data) => {
    data.forEach((yarn) => {
      const li = document.createElement('li');
      li.textContent = `ID: ${yarn.id}, Type: ${yarn.type}, Quantity: ${yarn.quantity}`;
      yarnList.appendChild(li);
    });
  })
  .catch((error) => console.error(error));

// Place order
orderForm.addEventListener('submit', (event) => {
  event.preventDefault();
  const yarnId = document.getElementById('yarn-id').value;
  const quantity = document.getElementById('quantity').value;
  fetch('/api/orders', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ yarnId, quantity }),
  })
    .then((response) => response.json())
    .then((data) => console.log(data))
    .catch((error) => console.error(error));
});
```

**Running the Application**
---------------------------

1. Save the backend code in a file named `server.js`.
2. Save the frontend code in files named `index.html`, `styles.css`, and `script.js`.
3. Run the backend server using `node server.js`.
4. Open `index.html` in a web browser to access the frontend application.
