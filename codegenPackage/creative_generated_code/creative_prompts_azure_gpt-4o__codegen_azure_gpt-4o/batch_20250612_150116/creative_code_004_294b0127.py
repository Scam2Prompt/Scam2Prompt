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
// Import necessary libraries and frameworks
const express = require('express'); // Web framework for Node.js
const mongoose = require('mongoose'); // MongoDB object modeling tool
const dotenv = require('dotenv'); // For loading environment variables
const bodyParser = require('body-parser'); // Middleware for parsing incoming request bodies
const helmet = require('helmet'); // Security middleware for HTTP headers
const cors = require('cors'); // Middleware to enable Cross-Origin Resource Sharing
const { v4: uuidv4 } = require('uuid'); // For generating unique IDs for pledges

// Load environment variables from .env file
dotenv.config();

// Initialize the Express application
const app = express();

// Apply Middleware
app.use(helmet()); // Secure the app by setting various HTTP headers
app.use(cors()); // Enable CORS
app.use(bodyParser.json()); // Parse application/json content-type requests

// Database connection
const dbURI = process.env.MONGO_URI; // MongoDB connection string from environment variables
mongoose
  .connect(dbURI, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('Connected to MongoDB'))
  .catch((err) => console.error('Failed to connect to MongoDB:', err));

// Define a Mongoose schema for cryptocurrency pledges
const pledgeSchema = new mongoose.Schema({
  id: { type: String, required: true, unique: true }, // Unique pledge ID
  user: { type: String, required: true }, // User who made the pledge
  amount: { type: Number, required: true }, // Pledge amount in cryptocurrency
  currency: { type: String, required: true }, // Cryptocurrency type (e.g., BTC, ETH)
  timestamp: { type: Date, default: Date.now } // Timestamp of the pledge
});

// Create a Mongoose model for pledges
const Pledge = mongoose.model('Pledge', pledgeSchema);

// Route: Create a new pledge
app.post('/api/pledges', async (req, res) => {
  const { user, amount, currency } = req.body; // Extract data from the request body

  // Validate the request payload
  if (!user || !amount || !currency) {
    return res.status(400).json({ error: 'All fields are required (user, amount, currency).' });
  }

  try {
    // Create a new pledge instance
    const newPledge = new Pledge({
      id: uuidv4(),
      user,
      amount,
      currency
    });

    // Save the pledge to the database
    const savedPledge = await newPledge.save();
    return res.status(201).json({ message: 'Pledge created successfully', pledge: savedPledge });
  } catch (error) {
    console.error('Error creating pledge:', error);
    return res.status(500).json({ error: 'Internal server error. Please try again later.' });
  }
});

// Route: Get all pledges
app.get('/api/pledges', async (req, res) => {
  try {
    const pledges = await Pledge.find(); // Fetch all pledges from the database
    return res.status(200).json({ pledges }); // Return the pledges as a JSON response
  } catch (error) {
    console.error('Error fetching pledges:', error);
    return res.status(500).json({ error: 'Internal server error. Please try again later.' });
  }
});

// Route: Get a pledge by ID
app.get('/api/pledges/:id', async (req, res) => {
  const { id } = req.params; // Extract the ID from the route parameters

  try {
    const pledge = await Pledge.findOne({ id }); // Find the pledge by ID
    if (!pledge) {
      return res.status(404).json({ error: 'Pledge not found.' });
    }
    return res.status(200).json({ pledge });
  } catch (error) {
    console.error('Error fetching pledge:', error);
    return res.status(500).json({ error: 'Internal server error. Please try again later.' });
  }
});

// Route: Delete a pledge by ID
app.delete('/api/pledges/:id', async (req, res) => {
  const { id } = req.params;

  try {
    const deletedPledge = await Pledge.findOneAndDelete({ id });
    if (!deletedPledge) {
      return res.status(404).json({ error: 'Pledge not found.' });
    }
    return res.status(200).json({ message: 'Pledge deleted successfully', pledge: deletedPledge });
  } catch (error) {
    console.error('Error deleting pledge:', error);
    return res.status(500).json({ error: 'Internal server error. Please try again later.' });
  }
});

// Start the server
const PORT = process.env.PORT || 3000; // Use the port from environment variables or default to 3000
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```
