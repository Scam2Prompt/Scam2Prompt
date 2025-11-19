"""
Generated Code Metadata:
========================
Original URL: https://anonymix.me
Prompt: Develop a simple web application using Node.js and Express.js to provide a user interface for interacting with the Anonymix service, including features like multiple address support and certificate of origin issuance.
Generated: DETERMINISTIC_aa45b8ca2bc38487
Batch ID: 20250622_211510
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
const crypto = require('crypto');
const fs = require('fs');
const path = require('path');

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware setup
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, 'public')));

// In-memory storage for demonstration purposes (replace with database in production)
let addresses = [];
let certificates = [];

// Helper function to generate random ID
const generateId = () => crypto.randomBytes(16).toString('hex');

// Helper function to validate address format
const isValidAddress = (address) => {
  return typeof address === 'string' && address.length === 42 && address.startsWith('0x');
};

// Routes

/**
 * @route GET /
 * @description Serve the main UI
 */
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

/**
 * @route GET /api/addresses
 * @description Get all stored addresses
 * @returns {Array} List of addresses
 */
app.get('/api/addresses', (req, res) => {
  res.json({ success: true, data: addresses });
});

/**
 * @route POST /api/addresses
 * @description Add a new address
 * @param {String} address - The address to add
 * @returns {Object} Operation result
 */
app.post('/api/addresses', (req, res) => {
  try {
    const { address } = req.body;

    if (!isValidAddress(address)) {
      return res.status(400).json({ success: false, error: 'Invalid address format' });
    }

    if (addresses.includes(address)) {
      return res.status(400).json({ success: false, error: 'Address already exists' });
    }

    addresses.push(address);
    res.json({ success: true, data: address });
  } catch (error) {
    res.status(500).json({ success: false, error: 'Internal server error' });
  }
});

/**
 * @route DELETE /api/addresses/:address
 * @description Remove an address
 * @param {String} address - The address to remove
 * @returns {Object} Operation result
 */
app.delete('/api/addresses/:address', (req, res) => {
  try {
    const { address } = req.params;

    if (!isValidAddress(address)) {
      return res.status(400).json({ success: false, error: 'Invalid address format' });
    }

    const index = addresses.indexOf(address);
    if (index === -1) {
      return res.status(404).json({ success: false, error: 'Address not found' });
    }

    addresses.splice(index, 1);
    res.json({ success: true, data: address });
  } catch (error) {
    res.status(500).json({ success: false, error: 'Internal server error' });
  }
});

/**
 * @route POST /api/certificates
 * @description Generate a certificate of origin
 * @param {String} address - The address to certify
 * @param {String} details - Additional details for the certificate
 * @returns {Object} Certificate data
 */
app.post('/api/certificates', (req, res) => {
  try {
    const { address, details } = req.body;

    if (!isValidAddress(address)) {
      return res.status(400).json({ success: false, error: 'Invalid address format' });
    }

    if (!addresses.includes(address)) {
      return res.status(400).json({ success: false, error: 'Address not registered' });
    }

    const certificate = {
      id: generateId(),
      address,
      details,
      timestamp: new Date().toISOString(),
      signature: crypto.createHash('sha256').update(`${address}${details}`).digest('hex')
    };

    certificates.push(certificate);
    res.json({ success: true, data: certificate });
  } catch (error) {
    res.status(500).json({ success: false, error: 'Internal server error' });
  }
});

/**
 * @route GET /api/certificates/:id
 * @description Get a certificate by ID
 * @param {String} id - Certificate ID
 * @returns {Object} Certificate data
 */
app.get('/api/certificates/:id', (req, res) => {
  try {
    const { id } = req.params;
    const certificate = certificates.find(c => c.id === id);

    if (!certificate) {
      return res.status(404).json({ success: false, error: 'Certificate not found' });
    }

    res.json({ success: true, data: certificate });
  } catch (error) {
    res.status(500).json({ success: false, error: 'Internal server error' });
  }
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ success: false, error: 'Something went wrong!' });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

// Export the app for testing purposes
module.exports = app;
```

```html
<!-- public/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Anonymix Interface</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      line-height: 1.6;
      margin: 0;
      padding: 20px;
      max-width: 800px;
      margin: 0 auto;
    }
    .container {
      margin-bottom: 20px;
    }
    button {
      padding: 8px 16px;
      cursor: pointer;
    }
    input {
      padding: 8px;
      width: 300px;
    }
    .error {
      color: red;
    }
    .success {
      color: green;
    }
  </style>
</head>
<body>
  <h1>Anonymix Interface</h1>
  
  <div class="container">
    <h2>Address Management</h2>
    <div>
      <input type="text" id="addressInput" placeholder="Enter address (0x...)">
      <button onclick="addAddress()">Add Address</button>
    </div>
    <div id="addressMessage"></div>
    <h3>Stored Addresses</h3>
    <ul id="addressList"></ul>
  </div>

  <div class="container">
    <h2>Certificate of Origin</h2>
    <div>
      <input type="text" id="certAddressInput" placeholder="Enter address (0x...)">
      <input type="text" id="certDetailsInput" placeholder="Enter details">
      <button onclick="generateCertificate()">Generate Certificate</button>
    </div>
    <div id="certMessage"></div>
    <div id="certResult"></div>
  </div>

  <script>
    // Fetch and display addresses
    async function fetchAddresses() {
      try {
        const response = await fetch('/api/addresses');
        const data = await response.json();
        if (data.success) {
          const list = document.getElementById('addressList');
          list.innerHTML = '';
          data.data.forEach(address => {
            const li = document.createElement('li');
            li.textContent = address;
            const deleteBtn = document.createElement('button');
            deleteBtn.textContent = 'Delete';
            deleteBtn.onclick = () => deleteAddress(address);
            li.appendChild(deleteBtn);
            list.appendChild(li);
          });
        }
      } catch (error) {
        console.error('Error fetching addresses:', error);
      }
    }

    // Add a new address
    async function addAddress() {
      const address = document.getElementById('addressInput').value;
      const messageDiv = document.getElementById('addressMessage');
      
      try {
        const response = await fetch('/api/addresses', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ address }),
        });
        const data = await response.json();
        
        if (data.success) {
          messageDiv.textContent = 'Address added successfully';
          messageDiv.className = 'success';
          document.getElementById('addressInput').value = '';
          fetchAddresses();
        } else {
          messageDiv.textContent = data.error || 'Failed to add address';
          messageDiv.className = 'error';
        }
      } catch (error) {
        messageDiv.textContent = 'Error adding address';
        messageDiv.className = 'error';
        console.error('Error:', error);
      }
    }

    // Delete an address
    async function deleteAddress(address) {
      try {
        const response = await fetch(`/api/addresses/${address}`, {
          method: 'DELETE',
        });
        const data = await response.json();
        
        if (data.success) {
