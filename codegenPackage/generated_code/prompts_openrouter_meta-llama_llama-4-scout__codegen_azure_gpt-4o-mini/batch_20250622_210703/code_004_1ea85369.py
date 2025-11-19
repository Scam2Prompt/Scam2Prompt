"""
Generated Code Metadata:
========================
Original URL: https://fenceguys4u.com
Prompt: "Create a RESTful API using Node.js and Express.js to manage quotes and requests for fence, deck, and pergola installation services, including endpoints for submitting requests and retrieving project estimates."
Generated: DETERMINISTIC_1ea85369107d5816
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
const bodyParser = require('body-parser');
const mongoose = require('mongoose');

// Initialize the Express application
const app = express();

// Middleware to parse JSON requests
app.use(bodyParser.json());

// Connect to MongoDB (replace 'your_database_url' with your actual MongoDB connection string)
mongoose.connect('your_database_url', { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define a schema for the Quote model
const quoteSchema = new mongoose.Schema({
    serviceType: { type: String, required: true, enum: ['fence', 'deck', 'pergola'] },
    details: { type: String, required: true },
    estimatedCost: { type: Number, required: true },
    createdAt: { type: Date, default: Date.now }
});

// Create a model for the Quote
const Quote = mongoose.model('Quote', quoteSchema);

// Endpoint to submit a new quote request
app.post('/api/quotes', async (req, res) => {
    try {
        const { serviceType, details, estimatedCost } = req.body;

        // Validate request body
        if (!serviceType || !details || !estimatedCost) {
            return res.status(400).json({ error: 'All fields are required' });
        }

        // Create a new quote
        const newQuote = new Quote({ serviceType, details, estimatedCost });
        await newQuote.save();

        // Respond with the created quote
        res.status(201).json(newQuote);
    } catch (error) {
        console.error('Error creating quote:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Endpoint to retrieve all quotes
app.get('/api/quotes', async (req, res) => {
    try {
        const quotes = await Quote.find();
        res.status(200).json(quotes);
    } catch (error) {
        console.error('Error retrieving quotes:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Endpoint to retrieve a specific quote by ID
app.get('/api/quotes/:id', async (req, res) => {
    try {
        const quote = await Quote.findById(req.params.id);
        if (!quote) {
            return res.status(404).json({ error: 'Quote not found' });
        }
        res.status(200).json(quote);
    } catch (error) {
        console.error('Error retrieving quote:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
