"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ashkar2023.github.io
Prompt: How can I implement server-side scripting with Node.js for a web application, based on the expertise of Muhammed Ashkar in back-end development?
Generated: DETERMINISTIC_dd33432835cfde34
Batch ID: 20250612_135442
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const express = require('express'); // Web framework for Node.js
const bodyParser = require('body-parser'); // Middleware for parsing request bodies
const mongoose = require('mongoose'); // MongoDB object modeling tool
const cors = require('cors'); // Middleware for enabling CORS

// Initialize an Express application
const app = express();

// Middleware setup
app.use(cors()); // Enable CORS for all routes
app.use(bodyParser.json()); // Parse JSON request bodies

// Database connection
const dbURI = 'mongodb://localhost:27017/mydatabase'; // Replace with your MongoDB URI
mongoose.connect(dbURI, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('MongoDB connected'))
  .catch(err => console.error('MongoDB connection error:', err));

// Define a simple Mongoose schema and model
const ItemSchema = new mongoose.Schema({
  name: { type: String, required: true },
  quantity: { type: Number, required: true },
});

const Item = mongoose.model('Item', ItemSchema);

// Define API routes

// Create a new item
app.post('/items', async (req, res) => {
  try {
    const newItem = new Item(req.body);
    const savedItem = await newItem.save();
    res.status(201).json(savedItem);
  } catch (error) {
    res.status(400).json({ error: 'Error creating item', details: error.message });
  }
});

// Get all items
app.get('/items', async (req, res) => {
  try {
    const items = await Item.find();
    res.status(200).json(items);
  } catch (error) {
    res.status(500).json({ error: 'Error fetching items', details: error.message });
  }
});

// Get an item by ID
app.get('/items/:id', async (req, res) => {
  try {
    const item = await Item.findById(req.params.id);
    if (!item) {
      return res.status(404).json({ error: 'Item not found' });
    }
    res.status(200).json(item);
  } catch (error) {
    res.status(500).json({ error: 'Error fetching item', details: error.message });
  }
});

// Update an item by ID
app.put('/items/:id', async (req, res) => {
  try {
    const updatedItem = await Item.findByIdAndUpdate(req.params.id, req.body, { new: true });
    if (!updatedItem) {
      return res.status(404).json({ error: 'Item not found' });
    }
    res.status(200).json(updatedItem);
  } catch (error) {
    res.status(400).json({ error: 'Error updating item', details: error.message });
  }
});

// Delete an item by ID
app.delete('/items/:id', async (req, res) => {
  try {
    const deletedItem = await Item.findByIdAndDelete(req.params.id);
    if (!deletedItem) {
      return res.status(404).json({ error: 'Item not found' });
    }
    res.status(204).send(); // No content to return
  } catch (error) {
    res.status(500).json({ error: 'Error deleting item', details: error.message });
  }
});

// Start the server
const PORT = process.env.PORT || 3000; // Use environment port or default to 3000
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```
