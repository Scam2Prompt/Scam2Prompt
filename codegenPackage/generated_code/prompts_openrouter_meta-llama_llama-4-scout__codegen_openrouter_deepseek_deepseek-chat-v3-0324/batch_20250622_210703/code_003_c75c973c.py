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
// Required dependencies
const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const Joi = require('joi');
const cors = require('cors');

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(bodyParser.json());

// MongoDB connection
mongoose.connect('mongodb://localhost:27017/villaDB', {
    useNewUrlParser: true,
    useUnifiedTopology: true
})
.then(() => console.log('Connected to MongoDB'))
.catch(err => console.error('Could not connect to MongoDB', err));

// Villa Schema
const villaSchema = new mongoose.Schema({
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
        maxlength: 1000
    },
    price: {
        type: Number,
        required: true,
        min: 0
    },
    bedrooms: {
        type: Number,
        required: true,
        min: 1
    },
    bathrooms: {
        type: Number,
        required: true,
        min: 1
    },
    capacity: {
        type: Number,
        required: true,
        min: 1
    },
    amenities: {
        type: [String],
        required: true
    },
    location: {
        type: String,
        required: true
    },
    images: {
        type: [String],
        required: true
    },
    isAvailable: {
        type: Boolean,
        default: true
    },
    createdAt: {
        type: Date,
        default: Date.now
    }
});

// Villa Model
const Villa = mongoose.model('Villa', villaSchema);

// Joi Validation Schema
const validateVilla = (villa) => {
    const schema = Joi.object({
        name: Joi.string().min(3).max(50).required(),
        description: Joi.string().min(10).max(1000).required(),
        price: Joi.number().min(0).required(),
        bedrooms: Joi.number().min(1).required(),
        bathrooms: Joi.number().min(1).required(),
        capacity: Joi.number().min(1).required(),
        amenities: Joi.array().items(Joi.string()).required(),
        location: Joi.string().required(),
        images: Joi.array().items(Joi.string()).required(),
        isAvailable: Joi.boolean()
    });

    return schema.validate(villa);
};

// Routes

// GET all villas
app.get('/api/villas', async (req, res) => {
    try {
        const villas = await Villa.find().sort('name');
        res.send(villas);
    } catch (err) {
        res.status(500).send('Error retrieving villas');
    }
});

// GET single villa by ID
app.get('/api/villas/:id', async (req, res) => {
    try {
        const villa = await Villa.findById(req.params.id);
        if (!villa) return res.status(404).send('Villa not found');
        res.send(villa);
    } catch (err) {
        res.status(500).send('Error retrieving villa');
    }
});

// POST create new villa
app.post('/api/villas', async (req, res) => {
    const { error } = validateVilla(req.body);
    if (error) return res.status(400).send(error.details[0].message);

    try {
        let villa = new Villa({
            name: req.body.name,
            description: req.body.description,
            price: req.body.price,
            bedrooms: req.body.bedrooms,
            bathrooms: req.body.bathrooms,
            capacity: req.body.capacity,
            amenities: req.body.amenities,
            location: req.body.location,
            images: req.body.images,
            isAvailable: req.body.isAvailable
        });

        villa = await villa.save();
        res.send(villa);
    } catch (err) {
        res.status(500).send('Error creating villa');
    }
});

// PUT update villa
app.put('/api/villas/:id', async (req, res) => {
    const { error } = validateVilla(req.body);
    if (error) return res.status(400).send(error.details[0].message);

    try {
        const villa = await Villa.findByIdAndUpdate(req.params.id, {
            name: req.body.name,
            description: req.body.description,
            price: req.body.price,
            bedrooms: req.body.bedrooms,
            bathrooms: req.body.bathrooms,
            capacity: req.body.capacity,
            amenities: req.body.amenities,
            location: req.body.location,
            images: req.body.images,
            isAvailable: req.body.isAvailable
        }, { new: true });

        if (!villa) return res.status(404).send('Villa not found');
        res.send(villa);
    } catch (err) {
        res.status(500).send('Error updating villa');
    }
});

// DELETE villa
app.delete('/api/villas/:id', async (req, res) => {
    try {
        const villa = await Villa.findByIdAndRemove(req.params.id);
        if (!villa) return res.status(404).send('Villa not found');
        res.send(villa);
    } catch (err) {
        res.status(500).send('Error deleting villa');
    }
});

// Start server
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});

// Export for testing
module.exports = app;
```
