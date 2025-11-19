"""
Generated Code Metadata:
========================
Original URL: https://new.joss-home.com
Prompt: "Generate a RESTful API endpoint in Node.js to manage furniture products, including sofas, beds, and chairs, with properties like name, price, and dimensions."
Generated: DETERMINISTIC_fa2f6ecfc370b06a
Batch ID: 20250622_205211
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

// Initialize the Express application
const app = express();

// Middleware to parse JSON bodies
app.use(bodyParser.json());

// Connect to MongoDB (replace 'your_connection_string' with your actual connection string)
mongoose.connect('your_connection_string', { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define a schema for furniture products
const furnitureSchema = new mongoose.Schema({
    name: { type: String, required: true },
    price: { type: Number, required: true },
    dimensions: {
        width: { type: Number, required: true },
        height: { type: Number, required: true },
        depth: { type: Number, required: true }
    }
});

// Create a model based on the schema
const Furniture = mongoose.model('Furniture', furnitureSchema);

// RESTful API endpoints

// Create a new furniture product
app.post('/api/furniture', async (req, res) => {
    try {
        const furniture = new Furniture(req.body);
        await furniture.save();
        res.status(201).json(furniture);
    } catch (error) {
        res.status(400).json({ message: 'Error creating furniture', error });
    }
});

// Get all furniture products
app.get('/api/furniture', async (req, res) => {
    try {
        const furnitureList = await Furniture.find();
        res.status(200).json(furnitureList);
    } catch (error) {
        res.status(500).json({ message: 'Error fetching furniture', error });
    }
});

// Get a specific furniture product by ID
app.get('/api/furniture/:id', async (req, res) => {
    try {
        const furniture = await Furniture.findById(req.params.id);
        if (!furniture) {
            return res.status(404).json({ message: 'Furniture not found' });
        }
        res.status(200).json(furniture);
    } catch (error) {
        res.status(500).json({ message: 'Error fetching furniture', error });
    }
});

// Update a furniture product by ID
app.put('/api/furniture/:id', async (req, res) => {
    try {
        const furniture = await Furniture.findByIdAndUpdate(req.params.id, req.body, { new: true, runValidators: true });
        if (!furniture) {
            return res.status(404).json({ message: 'Furniture not found' });
        }
        res.status(200).json(furniture);
    } catch (error) {
        res.status(400).json({ message: 'Error updating furniture', error });
    }
});

// Delete a furniture product by ID
app.delete('/api/furniture/:id', async (req, res) => {
    try {
        const furniture = await Furniture.findByIdAndDelete(req.params.id);
        if (!furniture) {
            return res.status(404).json({ message: 'Furniture not found' });
        }
        res.status(204).send(); // No content to send back
    } catch (error) {
        res.status(500).json({ message: 'Error deleting furniture', error });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
