"""
Generated Code Metadata:
========================
Original URL: https://liketoeatlamb.web.app
Prompt: Create a RESTful API using Node.js to manage a collection of quotes with their translations.
Generated: DETERMINISTIC_953d749dd3787a55
Batch ID: 20250622_204907
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

// Connect to MongoDB (replace 'your_mongo_uri' with your actual MongoDB URI)
mongoose.connect('your_mongo_uri', { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define a schema for quotes
const quoteSchema = new mongoose.Schema({
    text: { type: String, required: true },
    author: { type: String, required: true },
    translations: [{ language: String, text: String }]
});

// Create a model for quotes
const Quote = mongoose.model('Quote', quoteSchema);

// Create a new quote
app.post('/quotes', async (req, res) => {
    try {
        const quote = new Quote(req.body);
        const savedQuote = await quote.save();
        res.status(201).json(savedQuote);
    } catch (error) {
        res.status(400).json({ error: error.message });
    }
});

// Get all quotes
app.get('/quotes', async (req, res) => {
    try {
        const quotes = await Quote.find();
        res.status(200).json(quotes);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// Get a quote by ID
app.get('/quotes/:id', async (req, res) => {
    try {
        const quote = await Quote.findById(req.params.id);
        if (!quote) {
            return res.status(404).json({ error: 'Quote not found' });
        }
        res.status(200).json(quote);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// Update a quote by ID
app.put('/quotes/:id', async (req, res) => {
    try {
        const updatedQuote = await Quote.findByIdAndUpdate(req.params.id, req.body, { new: true, runValidators: true });
        if (!updatedQuote) {
            return res.status(404).json({ error: 'Quote not found' });
        }
        res.status(200).json(updatedQuote);
    } catch (error) {
        res.status(400).json({ error: error.message });
    }
});

// Delete a quote by ID
app.delete('/quotes/:id', async (req, res) => {
    try {
        const deletedQuote = await Quote.findByIdAndDelete(req.params.id);
        if (!deletedQuote) {
            return res.status(404).json({ error: 'Quote not found' });
        }
        res.status(204).send();
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
