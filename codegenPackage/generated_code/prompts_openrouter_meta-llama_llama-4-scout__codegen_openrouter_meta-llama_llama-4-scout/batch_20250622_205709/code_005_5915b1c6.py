"""
Generated Code Metadata:
========================
Original URL: https://mechanics.ae
Prompt: Develop a RESTful API using Node.js to handle car repair service requests, including creating, reading, updating, and deleting (CRUD) services like car engine repair and suspension repair.
Generated: DETERMINISTIC_5915b1c64bd07e17
Batch ID: 20250622_205709
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
const app = express();
const mongoose = require('mongoose');
const port = 3000;

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/car-repair', { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('Connected to MongoDB'))
    .catch((err) => console.error('Error connecting to MongoDB:', err));

// Define schema for car repair services
const serviceSchema = new mongoose.Schema({
    name: { type: String, required: true },
    description: { type: String, required: true },
    price: { type: Number, required: true }
});

// Create model for car repair services
const Service = mongoose.model('Service', serviceSchema);

// Middleware to parse JSON bodies
app.use(express.json());

// Create a new car repair service
app.post('/services', async (req, res) => {
    try {
        const service = new Service(req.body);
        await service.save();
        res.status(201).json(service);
    } catch (err) {
        res.status(400).json({ message: 'Error creating service', error: err });
    }
});

// Get all car repair services
app.get('/services', async (req, res) => {
    try {
        const services = await Service.find();
        res.json(services);
    } catch (err) {
        res.status(500).json({ message: 'Error getting services', error: err });
    }
});

// Get a car repair service by ID
app.get('/services/:id', async (req, res) => {
    try {
        const id = req.params.id;
        const service = await Service.findById(id);
        if (!service) {
            res.status(404).json({ message: 'Service not found' });
        } else {
            res.json(service);
        }
    } catch (err) {
        res.status(400).json({ message: 'Error getting service', error: err });
    }
});

// Update a car repair service
app.put('/services/:id', async (req, res) => {
    try {
        const id = req.params.id;
        const service = await Service.findByIdAndUpdate(id, req.body, { new: true });
        if (!service) {
            res.status(404).json({ message: 'Service not found' });
        } else {
            res.json(service);
        }
    } catch (err) {
        res.status(400).json({ message: 'Error updating service', error: err });
    }
});

// Delete a car repair service
app.delete('/services/:id', async (req, res) => {
    try {
        const id = req.params.id;
        await Service.findByIdAndRemove(id);
        res.status(204).json({ message: 'Service deleted successfully' });
    } catch (err) {
        res.status(400).json({ message: 'Error deleting service', error: err });
    }
});

// Start server
app.listen(port, () => {
    console.log(`Server started on port ${port}`);
});
```
