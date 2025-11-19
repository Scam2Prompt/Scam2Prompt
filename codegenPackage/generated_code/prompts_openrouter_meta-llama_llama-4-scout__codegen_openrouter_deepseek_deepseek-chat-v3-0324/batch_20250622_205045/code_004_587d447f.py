"""
Generated Code Metadata:
========================
Original URL: https://dxlink.net
Prompt: "Create a RESTful API using Node.js to manage and display DX Link's streaming services for IPTV, movies, and series."
Generated: DETERMINISTIC_587d447fcd6f072b
Batch ID: 20250622_205045
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

// MongoDB connection
mongoose.connect('mongodb://localhost:27017/dxlink', {
  useNewUrlParser: true,
  useUnifiedTopology: true
})
.then(() => console.log('Connected to MongoDB'))
.catch(err => console.error('MongoDB connection error:', err));

// Define Content Schema
const contentSchema = new mongoose.Schema({
  id: { type: String, default: uuidv4, unique: true },
  title: { type: String, required: true },
  description: { type: String },
  type: { type: String, enum: ['IPTV', 'Movie', 'Series'], required: true },
  genre: { type: [String], default: [] },
  releaseYear: { type: Number },
  duration: { type: Number }, // in minutes
  rating: { type: Number, min: 0, max: 10 },
  streamUrl: { type: String, required: true },
  thumbnailUrl: { type: String },
  createdAt: { type: Date, default: Date.now },
  updatedAt: { type: Date, default: Date.now }
});

// Update the updatedAt field before saving
contentSchema.pre('save', function(next) {
  this.updatedAt = Date.now();
  next();
});

// Create Content model
const Content = mongoose.model('Content', contentSchema);

// API Routes

// Health check endpoint
app.get('/api/health', (req, res) => {
  res.status(200).json({ status: 'OK' });
});

// Create new content
app.post('/api/content', async (req, res) => {
  try {
    const content = new Content(req.body);
    await content.save();
    res.status(201).json(content);
  } catch (err) {
    if (err.name === 'ValidationError') {
      res.status(400).json({ error: err.message });
    } else {
      res.status(500).json({ error: 'Internal server error' });
    }
  }
});

// Get all content
app.get('/api/content', async (req, res) => {
  try {
    const { type, genre, limit = 20, page = 1 } = req.query;
    const query = {};
    
    if (type) query.type = type;
    if (genre) query.genre = { $in: genre.split(',') };
    
    const skip = (page - 1) * limit;
    
    const contents = await Content.find(query)
      .skip(skip)
      .limit(parseInt(limit))
      .sort({ createdAt: -1 });
    
    const total = await Content.countDocuments(query);
    
    res.json({
      data: contents,
      pagination: {
        total,
        page: parseInt(page),
        limit: parseInt(limit),
        totalPages: Math.ceil(total / limit)
      }
    });
  } catch (err) {
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Get single content by ID
app.get('/api/content/:id', async (req, res) => {
  try {
    const content = await Content.findOne({ id: req.params.id });
    if (!content) {
      return res.status(404).json({ error: 'Content not found' });
    }
    res.json(content);
  } catch (err) {
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Update content
app.put('/api/content/:id', async (req, res) => {
  try {
    const content = await Content.findOneAndUpdate(
      { id: req.params.id },
      req.body,
      { new: true, runValidators: true }
    );
    
    if (!content) {
      return res.status(404).json({ error: 'Content not found' });
    }
    
    res.json(content);
  } catch (err) {
    if (err.name === 'ValidationError') {
      res.status(400).json({ error: err.message });
    } else {
      res.status(500).json({ error: 'Internal server error' });
    }
  }
});

// Delete content
app.delete('/api/content/:id', async (req, res) => {
  try {
    const content = await Content.findOneAndDelete({ id: req.params.id });
    if (!content) {
      return res.status(404).json({ error: 'Content not found' });
    }
    res.status(204).send();
  } catch (err) {
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Search content
app.get('/api/content/search/:query', async (req, res) => {
  try {
    const query = req.params.query;
    const contents = await Content.find({
      $or: [
        { title: { $regex: query, $options: 'i' } },
        { description: { $regex: query, $options: 'i' } }
      ]
    }).limit(20);
    
    res.json(contents);
  } catch (err) {
    res.status(500).json({ error: 'Internal server error' });
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
