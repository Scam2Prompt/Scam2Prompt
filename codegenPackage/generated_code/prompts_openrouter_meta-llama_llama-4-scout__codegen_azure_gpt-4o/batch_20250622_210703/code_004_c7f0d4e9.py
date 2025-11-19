"""
Generated Code Metadata:
========================
Original URL: https://breakthroughstudio.in
Prompt: Develop a community support system using Node.js and Express.js that connects suspension training enthusiasts, similar to Breakthrough Studio's community approach.
Generated: DETERMINISTIC_c7f0d4e9a792f57c
Batch ID: 20250622_210703
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
const mongoose = require('mongoose');
const dotenv = require('dotenv');

// Load environment variables from .env file
dotenv.config();

// Initialize Express app
const app = express();

// Middleware for parsing JSON requests
app.use(bodyParser.json());

// Connect to MongoDB database
mongoose
  .connect(process.env.MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('Connected to MongoDB'))
  .catch((err) => {
    console.error('Database connection error:', err.message);
    process.exit(1); // Exit process if database connection fails
  });

// Define Mongoose schema and model for community members
const memberSchema = new mongoose.Schema({
  name: { type: String, required: true },
  email: { type: String, required: true, unique: true },
  interests: { type: [String], required: true },
  joinedAt: { type: Date, default: Date.now },
});

const Member = mongoose.model('Member', memberSchema);

// Route: Get all community members
app.get('/members', async (req, res) => {
  try {
    const members = await Member.find();
    res.status(200).json(members);
  } catch (err) {
    console.error('Error fetching members:', err.message);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Route: Add a new community member
app.post('/members', async (req, res) => {
  try {
    const { name, email, interests } = req.body;

    // Validate request body
    if (!name || !email || !interests || !Array.isArray(interests)) {
      return res.status(400).json({ error: 'Invalid request data' });
    }

    const newMember = new Member({ name, email, interests });
    await newMember.save();
    res.status(201).json(newMember);
  } catch (err) {
    console.error('Error adding member:', err.message);
    if (err.code === 11000) {
      // Handle duplicate email error
      res.status(400).json({ error: 'Email already exists' });
    } else {
      res.status(500).json({ error: 'Internal server error' });
    }
  }
});

// Route: Update a community member's information
app.put('/members/:id', async (req, res) => {
  try {
    const { id } = req.params;
    const { name, email, interests } = req.body;

    // Validate request body
    if (!name || !email || !interests || !Array.isArray(interests)) {
      return res.status(400).json({ error: 'Invalid request data' });
    }

    const updatedMember = await Member.findByIdAndUpdate(
      id,
      { name, email, interests },
      { new: true, runValidators: true }
    );

    if (!updatedMember) {
      return res.status(404).json({ error: 'Member not found' });
    }

    res.status(200).json(updatedMember);
  } catch (err) {
    console.error('Error updating member:', err.message);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Route: Delete a community member
app.delete('/members/:id', async (req, res) => {
  try {
    const { id } = req.params;

    const deletedMember = await Member.findByIdAndDelete(id);

    if (!deletedMember) {
      return res.status(404).json({ error: 'Member not found' });
    }

    res.status(200).json({ message: 'Member deleted successfully' });
  } catch (err) {
    console.error('Error deleting member:', err.message);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Route: Search for members by interest
app.get('/members/search', async (req, res) => {
  try {
    const { interest } = req.query;

    if (!interest) {
      return res.status(400).json({ error: 'Interest query parameter is required' });
    }

    const members = await Member.find({ interests: interest });
    res.status(200).json(members);
  } catch (err) {
    console.error('Error searching members:', err.message);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```

### Notes:
- Ensure you have a `.env` file with `MONGO_URI` and `PORT` defined.
- Install required dependencies: `npm install express body-parser mongoose dotenv`.
- This code is production-ready, with proper error handling and validation.
