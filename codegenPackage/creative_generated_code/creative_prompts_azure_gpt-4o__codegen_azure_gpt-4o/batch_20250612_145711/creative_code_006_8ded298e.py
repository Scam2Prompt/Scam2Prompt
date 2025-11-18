"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://servchains.com
Prompt: Develop a Node.js application to facilitate partnerships with servchains.com, including sponsor and affiliate marketing partnership options.
Generated: DETERMINISTIC_8ded298e7bf07604
Batch ID: 20250612_145711
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing required modules
const express = require('express'); // Web framework
const bodyParser = require('body-parser'); // Middleware to parse request bodies
const dotenv = require('dotenv'); // Manage environment variables

// Load environment variables from .env file
dotenv.config();

// Initialize the Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware setup
app.use(bodyParser.json()); // Parse JSON request bodies

// In-memory storage for partnerships (in production, replace with a database)
const partnerships = [];

// Data validation utility
const validatePartnershipData = (data) => {
  const { type, name, email, details } = data;
  if (!type || !name || !email || !details) {
    return 'All fields (type, name, email, details) are required.';
  }
  if (!['sponsor', 'affiliate'].includes(type)) {
    return "Type must be either 'sponsor' or 'affiliate'.";
  }
  return null;
};

// Route: Health check
app.get('/health', (req, res) => {
  res.status(200).json({ status: 'OK', message: 'API is healthy.' });
});

// Route: Submit a new partnership request
app.post('/partnerships', (req, res) => {
  try {
    const { type, name, email, details } = req.body;

    // Validate incoming data
    const validationError = validatePartnershipData(req.body);
    if (validationError) {
      return res.status(400).json({ error: validationError });
    }

    // Create partnership object
    const newPartnership = {
      id: partnerships.length + 1, // Simple ID generation (use UUID for production)
      type,
      name,
      email,
      details,
      createdAt: new Date(),
    };

    // Store the new partnership
    partnerships.push(newPartnership);

    // Send success response
    res.status(201).json({
      message: 'Partnership request submitted successfully.',
      partnership: newPartnership,
    });
  } catch (error) {
    // Handle unexpected errors
    console.error('Error submitting partnership request:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// Route: Get all partnership requests
app.get('/partnerships', (req, res) => {
  try {
    res.status(200).json({ partnerships });
  } catch (error) {
    // Handle unexpected errors
    console.error('Error fetching partnerships:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// Route: Get a specific partnership request by ID
app.get('/partnerships/:id', (req, res) => {
  try {
    const partnershipId = parseInt(req.params.id, 10);

    if (isNaN(partnershipId)) {
      return res.status(400).json({ error: 'Invalid partnership ID.' });
    }

    const partnership = partnerships.find((p) => p.id === partnershipId);

    if (!partnership) {
      return res.status(404).json({ error: 'Partnership not found.' });
    }

    res.status(200).json({ partnership });
  } catch (error) {
    // Handle unexpected errors
    console.error('Error fetching partnership by ID:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// Route: Delete a specific partnership request by ID
app.delete('/partnerships/:id', (req, res) => {
  try {
    const partnershipId = parseInt(req.params.id, 10);

    if (isNaN(partnershipId)) {
      return res.status(400).json({ error: 'Invalid partnership ID.' });
    }

    const partnershipIndex = partnerships.findIndex((p) => p.id === partnershipId);

    if (partnershipIndex === -1) {
      return res.status(404).json({ error: 'Partnership not found.' });
    }

    partnerships.splice(partnershipIndex, 1);

    res.status(200).json({ message: 'Partnership request deleted successfully.' });
  } catch (error) {
    // Handle unexpected errors
    console.error('Error deleting partnership by ID:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```

Save this file as `server.js`, and make sure to install the required dependencies (`express`, `body-parser`, and `dotenv`) before running it. Create a `.env` file to specify the `PORT` if needed.
