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

// Initialize the Express application
const app = express();

// Middleware setup
app.use(cors()); // Enable CORS for all routes
app.use(bodyParser.json()); // Parse JSON request bodies

// MongoDB connection setup
const mongoURI = 'mongodb://localhost:27017/dxlink'; // Replace with your MongoDB URI
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define a schema for streaming services
const streamingServiceSchema = new mongoose.Schema({
    title: { type: String, required: true },
    type: { type: String, enum: ['IPTV', 'Movie', 'Series'], required: true },
    description: { type: String },
    releaseDate: { type: Date },
    rating: { type: Number, min: 0, max: 10 }
});

// Create a model for streaming services
const StreamingService = mongoose.model('StreamingService', streamingServiceSchema);

// RESTful API routes

// Get all streaming services
app.get('/api/services', async (req, res) => {
    try {
        const services = await StreamingService.find();
        res.status(200).json(services);
    } catch (error) {
        res.status(500).json({ message: 'Error retrieving services', error });
    }
});

// Get a single streaming service by ID
app.get('/api/services/:id', async (req, res) => {
    try {
        const service = await StreamingService.findById(req.params.id);
        if (!service) {
            return res.status(404).json({ message: 'Service not found' });
        }
        res.status(200).json(service);
    } catch (error) {
        res.status(500).json({ message: 'Error retrieving service', error });
    }
});

// Create a new streaming service
app.post('/api/services', async (req, res) => {
    const { title, type, description, releaseDate, rating } = req.body;
    const newService = new StreamingService({ title, type, description, releaseDate, rating });

    try {
        const savedService = await newService.save();
        res.status(201).json(savedService);
    } catch (error) {
        res.status(400).json({ message: 'Error creating service', error });
    }
});

// Update an existing streaming service
app.put('/api/services/:id', async (req, res) => {
    try {
        const updatedService = await StreamingService.findByIdAndUpdate(req.params.id, req.body, { new: true });
        if (!updatedService) {
            return res.status(404).json({ message: 'Service not found' });
        }
        res.status(200).json(updatedService);
    } catch (error) {
        res.status(400).json({ message: 'Error updating service', error });
    }
});

// Delete a streaming service
app.delete('/api/services/:id', async (req, res) => {
    try {
        const deletedService = await StreamingService.findByIdAndDelete(req.params.id);
        if (!deletedService) {
            return res.status(404).json({ message: 'Service not found' });
        }
        res.status(204).send(); // No content to send back
    } catch (error) {
        res.status(500).json({ message: 'Error deleting service', error });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
