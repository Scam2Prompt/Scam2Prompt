"""
Generated Code Metadata:
========================
Original URL: https://moinulalam.com
Prompt: Write a RESTful API in Node.js for managing a collection of artworks, including endpoints for creating, reading, updating, and deleting artwork records, inspired by the artwork showcased on Moinul Alam's website.
Generated: DETERMINISTIC_95e6611a7b5d527f
Batch ID: 20250622_204958
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
const mongoose = require('mongoose');
const dotenv = require('dotenv');

// Load environment variables
dotenv.config();

// Connect to MongoDB
mongoose.connect(process.env.MONGODB_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

// Define artwork schema
const artworkSchema = new mongoose.Schema({
  title: { type: String, required: true },
  artist: { type: String, required: true },
  year: { type: Number, required: true },
  description: { type: String },
});

// Create artwork model
const Artwork = mongoose.model('Artwork', artworkSchema);

// Initialize Express app
const app = express();
app.use(express.json());

// Get all artworks
app.get('/artworks', async (req, res) => {
  try {
    const artworks = await Artwork.find().exec();
    res.json(artworks);
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// Get artwork by ID
app.get('/artworks/:id', async (req, res) => {
  try {
    const id = req.params.id;
    const artwork = await Artwork.findById(id).exec();
    if (!artwork) {
      res.status(404).json({ message: 'Artwork not found' });
    } else {
      res.json(artwork);
    }
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// Create new artwork
app.post('/artworks', async (req, res) => {
  try {
    const artwork = new Artwork(req.body);
    await artwork.save();
    res.status(201).json(artwork);
  } catch (error) {
    console.error(error);
    if (error.name === 'ValidationError') {
      res.status(400).json({ message: 'Invalid request data' });
    } else {
      res.status(500).json({ message: 'Internal Server Error' });
    }
  }
});

// Update existing artwork
app.put('/artworks/:id', async (req, res) => {
  try {
    const id = req.params.id;
    const artwork = await Artwork.findByIdAndUpdate(id, req.body, {
      new: true,
    }).exec();
    if (!artwork) {
      res.status(404).json({ message: 'Artwork not found' });
    } else {
      res.json(artwork);
    }
  } catch (error) {
    console.error(error);
    if (error.name === 'ValidationError') {
      res.status(400).json({ message: 'Invalid request data' });
    } else {
      res.status(500).json({ message: 'Internal Server Error' });
    }
  }
});

// Delete artwork
app.delete('/artworks/:id', async (req, res) => {
  try {
    const id = req.params.id;
    await Artwork.findByIdAndRemove(id).exec();
    res.status(204).json();
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// Start server
const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```

```javascript
// For running this file 
// node app.js 
// Make sure to install the required packages 
// npm install express mongoose dotenv
```
