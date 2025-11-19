"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.propertyshare.net
Prompt: Develop a RESTful API endpoint in Node.js that accepts property submissions for qualification and sale, inspired by the processes outlined on Property Share.
Generated: DETERMINISTIC_8909637b81b60e17
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');

// Initialize the Express application
const app = express();

// Use body-parser to handle JSON requests
app.use(bodyParser.json());

// Connect to MongoDB (ensure MongoDB is running)
mongoose.connect('mongodb://localhost:27017/propertyShare', {
    useNewUrlParser: true,
    useUnifiedTopology: true,
}).then(() => {
    console.log('Connected to MongoDB');
}).catch(err => {
    console.error('MongoDB connection error:', err);
});

// Define the property schema
const propertySchema = new mongoose.Schema({
    title: {
        type: String,
        required: true,
    },
    description: {
        type: String,
        required: true,
    },
    price: {
        type: Number,
        required: true,
    },
    location: {
        type: String,
        required: true,
    },
    submittedAt: {
        type: Date,
        default: Date.now,
    },
});

// Create the property model
const Property = mongoose.model('Property', propertySchema);

// POST endpoint to submit a property for qualification and sale
app.post('/api/properties', async (req, res) => {
    const { title, description, price, location } = req.body;

    // Validate incoming data
    if (!title || !description || !price || !location) {
        return res.status(400).json({ error: 'All fields are required.' });
    }

    try {
        // Create a new property instance
        const newProperty = new Property({ title, description, price, location });

        // Save the property to the database
        await newProperty.save();

        // Respond with the created property
        res.status(201).json(newProperty);
    } catch (error) {
        console.error('Error saving property:', error);
        res.status(500).json({ error: 'Internal server error.' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
