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
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const cors = require('cors');

// Initialize Express app
const app = express();

// Middleware
app.use(cors());
app.use(bodyParser.json());

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/carRepairDB', {
    useNewUrlParser: true,
    useUnifiedTopology: true
})
.then(() => console.log('Connected to MongoDB'))
.catch(err => console.error('Could not connect to MongoDB', err));

// Define Service Schema
const serviceSchema = new mongoose.Schema({
    name: {
        type: String,
        required: true,
        minlength: 3,
        maxlength: 50
    },
    description: {
        type: String,
        required: true,
        minlength: 10,
        maxlength: 255
    },
    price: {
        type: Number,
        required: true,
        min: 0
    },
    durationHours: {
        type: Number,
        required: true,
        min: 1
    },
    category: {
        type: String,
        required: true,
        enum: ['engine', 'suspension', 'electrical', 'body']
    },
    createdAt: {
        type: Date,
        default: Date.now
    }
});

// Create Service Model
const Service = mongoose.model('Service', serviceSchema);

// Routes

// GET all services
app.get('/api/services', async (req, res) => {
    try {
        const services = await Service.find().sort('name');
        res.send(services);
    } catch (err) {
        res.status(500).send('Error retrieving services');
    }
});

// GET service by ID
app.get('/api/services/:id', async (req, res) => {
    try {
        const service = await Service.findById(req.params.id);
        if (!service) return res.status(404).send('Service not found');
        res.send(service);
    } catch (err) {
        res.status(500).send('Error retrieving service');
    }
});

// POST new service
app.post('/api/services', async (req, res) => {
    // Validate request
    const { error } = validateService(req.body);
    if (error) return res.status(400).send(error.details[0].message);

    // Create new service
    const service = new Service({
        name: req.body.name,
        description: req.body.description,
        price: req.body.price,
        durationHours: req.body.durationHours,
        category: req.body.category
    });

    try {
        const result = await service.save();
        res.send(result);
    } catch (err) {
        res.status(500).send('Error saving service');
    }
});

// PUT update service
app.put('/api/services/:id', async (req, res) => {
    // Validate request
    const { error } = validateService(req.body);
    if (error) return res.status(400).send(error.details[0].message);

    try {
        const service = await Service.findByIdAndUpdate(req.params.id, {
            name: req.body.name,
            description: req.body.description,
            price: req.body.price,
            durationHours: req.body.durationHours,
            category: req.body.category
        }, { new: true });

        if (!service) return res.status(404).send('Service not found');
        res.send(service);
    } catch (err) {
        res.status(500).send('Error updating service');
    }
});

// DELETE service
app.delete('/api/services/:id', async (req, res) => {
    try {
        const service = await Service.findByIdAndRemove(req.params.id);
        if (!service) return res.status(404).send('Service not found');
        res.send(service);
    } catch (err) {
        res.status(500).send('Error deleting service');
    }
});

// Service validation function
function validateService(service) {
    const schema = Joi.object({
        name: Joi.string().min(3).max(50).required(),
        description: Joi.string().min(10).max(255).required(),
        price: Joi.number().min(0).required(),
        durationHours: Joi.number().min(1).required(),
        category: Joi.string().valid('engine', 'suspension', 'electrical', 'body').required()
    });
    return schema.validate(service);
}

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).send('Something broke!');
});

// Start the server
const port = process.env.PORT || 3000;
app.listen(port, () => console.log(`Server running on port ${port}...`));
```
