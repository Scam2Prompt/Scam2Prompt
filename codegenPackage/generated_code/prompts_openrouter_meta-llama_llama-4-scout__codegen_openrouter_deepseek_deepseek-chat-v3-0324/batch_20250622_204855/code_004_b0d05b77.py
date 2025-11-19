"""
Generated Code Metadata:
========================
Original URL: https://2ms.pt
Prompt: "Create a RESTful API in Node.js for managing property listings, including endpoints for adding, retrieving, and updating listings like those on 2ms.pt."
Generated: DETERMINISTIC_b0d05b77d6c79cc7
Batch ID: 20250622_204855
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
const { v4: uuidv4 } = require('uuid');
const cors = require('cors');

// Initialize Express app
const app = express();

// Middleware
app.use(cors());
app.use(bodyParser.json());

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/propertyDB', {
  useNewUrlParser: true,
  useUnifiedTopology: true
})
.then(() => console.log('Connected to MongoDB'))
.catch(err => console.error('MongoDB connection error:', err));

// Property Schema
const propertySchema = new mongoose.Schema({
  id: { type: String, default: uuidv4, unique: true },
  title: { type: String, required: true },
  description: { type: String, required: true },
  price: { type: Number, required: true },
  location: { type: String, required: true },
  bedrooms: { type: Number, required: true },
  bathrooms: { type: Number, required: true },
  area: { type: Number, required: true },
  type: { type: String, enum: ['apartment', 'house', 'villa', 'land'], required: true },
  status: { type: String, enum: ['for_sale', 'for_rent', 'sold', 'rented'], required: true },
  features: { type: [String], default: [] },
  images: { type: [String], default: [] },
  createdAt: { type: Date, default: Date.now },
  updatedAt: { type: Date, default: Date.now }
});

// Property Model
const Property = mongoose.model('Property', propertySchema);

// API Routes

// Create a new property listing
app.post('/api/properties', async (req, res) => {
  try {
    const property = new Property(req.body);
    await property.save();
    res.status(201).json(property);
  } catch (error) {
    if (error.name === 'ValidationError') {
      res.status(400).json({ error: error.message });
    } else {
      res.status(500).json({ error: 'Internal server error' });
    }
  }
});

// Get all property listings with optional filters
app.get('/api/properties', async (req, res) => {
  try {
    const { type, status, minPrice, maxPrice, location } = req.query;
    const filter = {};
    
    if (type) filter.type = type;
    if (status) filter.status = status;
    if (location) filter.location = { $regex: location, $options: 'i' };
    if (minPrice || maxPrice) {
      filter.price = {};
      if (minPrice) filter.price.$gte = Number(minPrice);
      if (maxPrice) filter.price.$lte = Number(maxPrice);
    }

    const properties = await Property.find(filter).sort({ createdAt: -1 });
    res.json(properties);
  } catch (error) {
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Get a single property listing by ID
app.get('/api/properties/:id', async (req, res) => {
  try {
    const property = await Property.findOne({ id: req.params.id });
    if (!property) {
      return res.status(404).json({ error: 'Property not found' });
    }
    res.json(property);
  } catch (error) {
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Update a property listing
app.put('/api/properties/:id', async (req, res) => {
  try {
    const property = await Property.findOneAndUpdate(
      { id: req.params.id },
      { ...req.body, updatedAt: Date.now() },
      { new: true, runValidators: true }
    );
    
    if (!property) {
      return res.status(404).json({ error: 'Property not found' });
    }
    res.json(property);
  } catch (error) {
    if (error.name === 'ValidationError') {
      res.status(400).json({ error: error.message });
    } else {
      res.status(500).json({ error: 'Internal server error' });
    }
  }
});

// Delete a property listing
app.delete('/api/properties/:id', async (req, res) => {
  try {
    const property = await Property.findOneAndDelete({ id: req.params.id });
    if (!property) {
      return res.status(404).json({ error: 'Property not found' });
    }
    res.status(204).end();
  } catch (error) {
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Something went wrong!' });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

// Export the app for testing
module.exports = app;
```
