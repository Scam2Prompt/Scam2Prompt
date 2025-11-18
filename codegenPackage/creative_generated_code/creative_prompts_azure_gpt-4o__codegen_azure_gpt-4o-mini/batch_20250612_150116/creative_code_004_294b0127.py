"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nodep0.com
Prompt: Suggest tools or frameworks for building a cryptocurrency pledge platform using JavaScript and Node.js.
Generated: DETERMINISTIC_294b012786cf3f7c
Batch ID: 20250612_150116
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const express = require('express'); // Framework for building web applications
const mongoose = require('mongoose'); // MongoDB object modeling tool
const bodyParser = require('body-parser'); // Middleware for parsing request bodies
const cors = require('cors'); // Middleware for enabling CORS
const dotenv = require('dotenv'); // Module for loading environment variables

// Load environment variables from .env file
dotenv.config();

// Initialize express app
const app = express();

// Middleware configuration
app.use(cors()); // Enable CORS for all routes
app.use(bodyParser.json()); // Parse JSON request bodies

// MongoDB connection
mongoose.connect(process.env.MONGODB_URI, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('MongoDB connected'))
  .catch(err => console.error('MongoDB connection error:', err));

// Define a schema for pledges
const pledgeSchema = new mongoose.Schema({
  userId: { type: String, required: true }, // User ID of the pledger
  amount: { type: Number, required: true, min: 0 }, // Amount pledged
  currency: { type: String, required: true }, // Currency type (e.g., BTC, ETH)
  createdAt: { type: Date, default: Date.now } // Timestamp of the pledge
});

// Create a model for the pledge schema
const Pledge = mongoose.model('Pledge', pledgeSchema);

// Route for creating a new pledge
app.post('/pledges', async (req, res) => {
  try {
    const { userId, amount, currency } = req.body; // Destructure request body

    // Validate input data
    if (!userId || !amount || !currency) {
      return res.status(400).json({ error: 'User ID, amount, and currency are required' });
    }

    // Create a new pledge instance
    const pledge = new Pledge({ userId, amount, currency });
    await pledge.save(); // Save pledge to the database

    res.status(201).json(pledge); // Respond with the created pledge
  } catch (error) {
    console.error('Error creating pledge:', error);
    res.status(500).json({ error: 'An error occurred while creating the pledge' }); // Handle server error
  }
});

// Route for retrieving all pledges
app.get('/pledges', async (req, res) => {
  try {
    const pledges = await Pledge.find(); // Fetch all pledges from the database
    res.status(200).json(pledges); // Respond with the list of pledges
  } catch (error) {
    console.error('Error fetching pledges:', error);
    res.status(500).json({ error: 'An error occurred while retrieving pledges' }); // Handle server error
  }
});

// Start the server
const PORT = process.env.PORT || 3000; // Define the port
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`); // Log server start
});
```

Make sure to create an `.env` file in your project root directory and add your MongoDB connection string:

```
MONGODB_URI=mongodb://<username>:<password>@<host>:<port>/<database>
PORT=3000
```
