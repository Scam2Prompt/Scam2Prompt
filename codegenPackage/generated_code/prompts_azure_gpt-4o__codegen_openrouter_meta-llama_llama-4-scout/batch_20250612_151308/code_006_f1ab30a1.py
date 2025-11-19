"""
Generated Code Metadata:
========================
Original URL: https://poolz.uk
Prompt: Create a web application that integrates a pool design gallery and allows users to customize pool designs based on their property and budget, inspired by Poolz's custom design service.
Generated: DETERMINISTIC_f1ab30a17c9c0c60
Batch ID: 20250612_151308
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Pool Design Gallery Web Application**
=====================================

**Backend (Node.js, Express.js)**
--------------------------------

```javascript
// server.js
const express = require('express');
const app = express();
const port = 3000;
const mongoose = require('mongoose');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/pool-designs', { useNewUrlParser: true, useUnifiedTopology: true });

// Define pool design schema
const poolDesignSchema = new mongoose.Schema({
  name: String,
  image: String,
  width: Number,
  length: Number,
  depth: Number,
  features: [{ type: String }]
});

// Define user schema
const userSchema = new mongoose.Schema({
  name: String,
  email: String,
  budget: Number,
  propertySize: Number
});

// Create models
const PoolDesign = mongoose.model('PoolDesign', poolDesignSchema);
const User = mongoose.model('User', userSchema);

// Middleware
app.use(express.json());
app.use(express.static('public'));

// API Endpoints
app.get('/api/pool-designs', async (req, res) => {
  try {
    const poolDesigns = await PoolDesign.find();
    res.json(poolDesigns);
  } catch (err) {
    res.status(500).json({ message: 'Error fetching pool designs' });
  }
});

app.post('/api/users', async (req, res) => {
  try {
    const user = new User(req.body);
    await user.save();
    res.json(user);
  } catch (err) {
    res.status(400).json({ message: 'Error creating user' });
  }
});

app.post('/api/customize-pool-design', async (req, res) => {
  try {
    const { userId, poolDesignId, budget, propertySize } = req.body;
    const user = await User.findById(userId);
    const poolDesign = await PoolDesign.findById(poolDesignId);

    if (!user || !poolDesign) {
      return res.status(404).json({ message: 'User or pool design not found' });
    }

    // Customize pool design based on user input
    const customizedPoolDesign = {
      ...poolDesign.toJSON(),
      width: poolDesign.width * (propertySize / 100),
      length: poolDesign.length * (budget / 10000)
    };

    res.json(customizedPoolDesign);
  } catch (err) {
    res.status(500).json({ message: 'Error customizing pool design' });
  }
});

// Start server
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```

**Frontend (HTML, CSS, JavaScript)**
------------------------------------

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Pool Design Gallery</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <h1>Pool Design Gallery</h1>
  <div class="pool-designs">
    <!-- Display pool designs -->
  </div>
  <form id="customize-pool-design-form">
    <label for="user-name">Name:</label>
    <input type="text" id="user-name" name="name"><br><br>
    <label for="user-email">Email:</label>
    <input type="email" id="user-email" name="email"><br><br>
    <label for="user-budget">Budget:</label>
    <input type="number" id="user-budget" name="budget"><br><br>
    <label for="user-property-size">Property Size:</label>
    <input type="number" id="user-property-size" name="propertySize"><br><br>
    <select id="pool-design-select" name="poolDesignId">
      <!-- Populate pool design options -->
    </select><br><br>
    <button id="customize-pool-design-btn">Customize Pool Design</button>
  </form>
  <div id="customized-pool-design">
    <!-- Display customized pool design -->
  </div>

  <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */
body {
  font-family: Arial, sans-serif;
}

.pool-designs {
  display: flex;
  flex-wrap: wrap;
}

.pool-design {
  margin: 20px;
  width: 200px;
  height: 150px;
  border: 1px solid #ccc;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

#customize-pool-design-form {
  margin-top: 20px;
}

#customized-pool-design {
  margin-top: 20px;
}
```

```javascript
// script.js
const poolDesignsContainer = document.querySelector('.pool-designs');
const customizePoolDesignForm = document.getElementById('customize-pool-design-form');
const customizedPoolDesignContainer = document.getElementById('customized-pool-design');

// Fetch pool designs from API
fetch('/api/pool-designs')
  .then(response => response.json())
  .then(poolDesigns => {
    poolDesigns.forEach(poolDesign => {
      const poolDesignHTML = `
        <div class="pool-design">
          <h2>${poolDesign.name}</h2>
          <img src="${poolDesign.image}" alt="${poolDesign.name}">
        </div>
      `;
      poolDesignsContainer.insertAdjacentHTML('beforeend', poolDesignHTML);
    });
  })
  .catch(error => console.error(error));

// Handle customize pool design form submission
customizePoolDesignForm.addEventListener('submit', async (event) => {
  event.preventDefault();

  const userName = document.getElementById('user-name').value;
  const userEmail = document.getElementById('user-email').value;
  const userBudget = document.getElementById('user-budget').value;
  const userPropertySize = document.getElementById('user-property-size').value;
  const poolDesignId = document.getElementById('pool-design-select').value;

  try {
    // Create user
    const userResponse = await fetch('/api/users', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name: userName, email: userEmail, budget: userBudget, propertySize: userPropertySize })
    });
    const user = await userResponse.json();

    // Customize pool design
    const customizePoolDesignResponse = await fetch('/api/customize-pool-design', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ userId: user._id, poolDesignId, budget: userBudget, propertySize: userPropertySize })
    });
    const customizedPoolDesign = await customizePoolDesignResponse.json();

    // Display customized pool design
    const customizedPoolDesignHTML = `
      <h2>Customized Pool Design</h2>
      <p>Name: ${customizedPoolDesign.name}</p>
      <p>Width: ${customizedPoolDesign.width}</p>
      <p>Length: ${customizedPoolDesign.length}</p>
    `;
    customizedPoolDesignContainer.innerHTML = customizedPoolDesignHTML;
  } catch (error) {
    console.error(error);
  }
});
```
