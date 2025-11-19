"""
Generated Code Metadata:
========================
Original URL: https://villasdeloix.com
Prompt: "Create a RESTful API in Node.js to manage villa listings, including endpoints for adding, retrieving, and updating villa information, similar to what is displayed on Villas de Loix."
Generated: DETERMINISTIC_c75c973c3eb97980
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
const mongoose = require('mongoose');
const bodyParser = require('body-parser');

// Initialize the Express application
const app = express();

// Middleware to parse JSON requests
app.use(bodyParser.json());

// Connect to MongoDB (replace with your own connection string)
mongoose.connect('mongodb://localhost:27017/villaListings', {
    useNewUrlParser: true,
    useUnifiedTopology: true,
})
.then(() => console.log('MongoDB connected'))
.catch(err => console.error('MongoDB connection error:', err));

// Define a Villa schema
const villaSchema = new mongoose.Schema({
    name: { type: String, required: true },
    location: { type: String, required: true },
    price: { type: Number, required: true },
    description: { type: String, required: true },
    amenities: { type: [String], required: true },
});

// Create a Villa model
const Villa = mongoose.model('Villa', villaSchema);

// Endpoint to add a new villa
app.post('/villas', async (req, res) => {
    try {
        const villa = new Villa(req.body);
        await villa.save();
        res.status(201).json(villa);
    } catch (error) {
        res.status(400).json({ message: 'Error adding villa', error });
    }
});

// Endpoint to retrieve all villas
app.get('/villas', async (req, res) => {
    try {
        const villas = await Villa.find();
        res.status(200).json(villas);
    } catch (error) {
        res.status(500).json({ message: 'Error retrieving villas', error });
    }
});

// Endpoint to retrieve a villa by ID
app.get('/villas/:id', async (req, res) => {
    try {
        const villa = await Villa.findById(req.params.id);
        if (!villa) {
            return res.status(404).json({ message: 'Villa not found' });
        }
        res.status(200).json(villa);
    } catch (error) {
        res.status(500).json({ message: 'Error retrieving villa', error });
    }
});

// Endpoint to update a villa by ID
app.put('/villas/:id', async (req, res) => {
    try {
        const villa = await Villa.findByIdAndUpdate(req.params.id, req.body, { new: true, runValidators: true });
        if (!villa) {
            return res.status(404).json({ message: 'Villa not found' });
        }
        res.status(200).json(villa);
    } catch (error) {
        res.status(400).json({ message: 'Error updating villa', error });
    }
});

// Endpoint to delete a villa by ID
app.delete('/villas/:id', async (req, res) => {
    try {
        const villa = await Villa.findByIdAndDelete(req.params.id);
        if (!villa) {
            return res.status(404).json({ message: 'Villa not found' });
        }
        res.status(204).send();
    } catch (error) {
        res.status(500).json({ message: 'Error deleting villa', error });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
