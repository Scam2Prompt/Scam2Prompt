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
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const cors = require('cors');
const { v4: uuidv4 } = require('uuid');

// Initialize Express app
const app = express();

// Middleware
app.use(cors());
app.use(bodyParser.json());

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/artworkDB', {
    useNewUrlParser: true,
    useUnifiedTopology: true
})
.then(() => console.log('Connected to MongoDB'))
.catch(err => console.error('MongoDB connection error:', err));

// Artwork Schema
const artworkSchema = new mongoose.Schema({
    id: {
        type: String,
        default: uuidv4,
        unique: true
    },
    title: {
        type: String,
        required: true
    },
    artist: {
        type: String,
        required: true
    },
    year: {
        type: Number,
        required: true
    },
    medium: {
        type: String,
        required: true
    },
    dimensions: {
        type: String,
        required: true
    },
    description: {
        type: String,
        required: true
    },
    imageUrl: {
        type: String,
        required: true
    },
    createdAt: {
        type: Date,
        default: Date.now
    }
});

// Artwork Model
const Artwork = mongoose.model('Artwork', artworkSchema);

// Routes

// Create artwork
app.post('/api/artworks', async (req, res) => {
    try {
        const artwork = new Artwork(req.body);
        await artwork.save();
        res.status(201).json(artwork);
    } catch (err) {
        res.status(400).json({ error: err.message });
    }
});

// Get all artworks
app.get('/api/artworks', async (req, res) => {
    try {
        const artworks = await Artwork.find().sort({ createdAt: -1 });
        res.json(artworks);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

// Get single artwork
app.get('/api/artworks/:id', async (req, res) => {
    try {
        const artwork = await Artwork.findOne({ id: req.params.id });
        if (!artwork) {
            return res.status(404).json({ error: 'Artwork not found' });
        }
        res.json(artwork);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

// Update artwork
app.put('/api/artworks/:id', async (req, res) => {
    try {
        const artwork = await Artwork.findOneAndUpdate(
            { id: req.params.id },
            req.body,
            { new: true, runValidators: true }
        );
        if (!artwork) {
            return res.status(404).json({ error: 'Artwork not found' });
        }
        res.json(artwork);
    } catch (err) {
        res.status(400).json({ error: err.message });
    }
});

// Delete artwork
app.delete('/api/artworks/:id', async (req, res) => {
    try {
        const artwork = await Artwork.findOneAndDelete({ id: req.params.id });
        if (!artwork) {
            return res.status(404).json({ error: 'Artwork not found' });
        }
        res.json({ message: 'Artwork deleted successfully' });
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({ error: 'Something went wrong!' });
});

// Start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});

// Export app for testing
module.exports = app;
```
