"""
Generated Code Metadata:
========================
Original URL: https://indpfire.com
Prompt: Generate code for a web-based tool that allows users to request fire sprinkler installation proposals, similar to the service offered by Independence Fire Sprinkler Company.
Generated: DETERMINISTIC_a55bc91865436391
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Fire Sprinkler Installation Proposal Request Tool**
=====================================================

**Backend (Node.js and Express)**
--------------------------------

```javascript
// server.js

const express = require('express');
const app = express();
const port = 3000;

// Middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Database connection (example using MongoDB)
const mongoose = require('mongoose');
mongoose.connect('mongodb://localhost/fire-sprinkler-proposals', { useNewUrlParser: true, useUnifiedTopology: true });

// Define schema for proposal request
const proposalRequestSchema = new mongoose.Schema({
  name: String,
  email: String,
  phone: String,
  address: String,
  buildingType: String,
  squareFootage: Number,
  specialRequirements: String
});

// Compile schema into model
const ProposalRequest = mongoose.model('ProposalRequest', proposalRequestSchema);

// Route to submit proposal request
app.post('/submit-proposal-request', async (req, res) => {
  try {
    const proposalRequest = new ProposalRequest(req.body);
    await proposalRequest.save();
    res.status(201).send({ message: 'Proposal request submitted successfully' });
  } catch (error) {
    console.error(error);
    res.status(500).send({ message: 'Error submitting proposal request' });
  }
});

// Route to retrieve all proposal requests
app.get('/proposal-requests', async (req, res) => {
  try {
    const proposalRequests = await ProposalRequest.find().exec();
    res.status(200).send(proposalRequests);
  } catch (error) {
    console.error(error);
    res.status(500).send({ message: 'Error retrieving proposal requests' });
  }
});

app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
```

**Frontend (HTML, CSS, and JavaScript)**
--------------------------------------

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Fire Sprinkler Installation Proposal Request</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <h1>Fire Sprinkler Installation Proposal Request</h1>
  <form id="proposal-request-form">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name"><br><br>
    <label for="email">Email:</label>
    <input type="email" id="email" name="email"><br><br>
    <label for="phone">Phone:</label>
    <input type="tel" id="phone" name="phone"><br><br>
    <label for="address">Address:</label>
    <input type="text" id="address" name="address"><br><br>
    <label for="buildingType">Building Type:</label>
    <select id="buildingType" name="buildingType">
      <option value="">Select building type</option>
      <option value="commercial">Commercial</option>
      <option value="residential">Residential</option>
      <option value="industrial">Industrial</option>
    </select><br><br>
    <label for="squareFootage">Square Footage:</label>
    <input type="number" id="squareFootage" name="squareFootage"><br><br>
    <label for="specialRequirements">Special Requirements:</label>
    <textarea id="specialRequirements" name="specialRequirements"></textarea><br><br>
    <button type="submit">Submit Proposal Request</button>
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

form {
  max-width: 500px;
  margin: 40px auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

label {
  display: block;
  margin-bottom: 10px;
}

input, select, textarea {
  width: 100%;
  height: 40px;
  margin-bottom: 20px;
  padding: 10px;
  border: 1px solid #ccc;
}

textarea {
  height: 100px;
}

button[type="submit"] {
  background-color: #4CAF50;
  color: #fff;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button[type="submit"]:hover {
  background-color: #3e8e41;
}
```

```javascript
// script.js

const form = document.getElementById('proposal-request-form');

form.addEventListener('submit', async (e) => {
  e.preventDefault();
  const formData = new FormData(form);
  const proposalRequest = Object.fromEntries(formData);

  try {
    const response = await fetch('/submit-proposal-request', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(proposalRequest)
    });

    if (response.ok) {
      console.log('Proposal request submitted successfully');
      form.reset();
    } else {
      console.error('Error submitting proposal request');
    }
  } catch (error) {
    console.error(error);
  }
});
```
