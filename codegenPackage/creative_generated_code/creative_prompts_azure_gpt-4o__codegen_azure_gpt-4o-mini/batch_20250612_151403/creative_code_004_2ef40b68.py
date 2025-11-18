"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gprobolsa.com
Prompt: Create a REST API endpoint in Node.js that allows businesses to request quotes for eco-friendly promotional products, referencing Grupo ProBolsa's focus on sustainability.
Generated: DETERMINISTIC_2ef40b689f48cff6
Batch ID: 20250612_151403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing required modules
const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const dotenv = require('dotenv');

// Load environment variables from .env file
dotenv.config();

// Initialize Express application
const app = express();

// Middleware for parsing JSON request bodies
app.use(bodyParser.json());

// MongoDB connection setup
mongoose.connect(process.env.MONGODB_URI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define a schema for storing quote requests
const quoteRequestSchema = new mongoose.Schema({
    businessName: { type: String, required: true },
    email: { type: String, required: true },
    productType: { type: String, required: true },
    quantity: { type: Number, required: true },
    ecoFriendly: { type: Boolean, default: true }, // Default to eco-friendly products
    createdAt: { type: Date, default: Date.now }
});

// Create a model from the schema
const QuoteRequest = mongoose.model('QuoteRequest', quoteRequestSchema);

// REST API endpoint to request a quote for eco-friendly products
app.post('/api/quotes', async (req, res) => {
    try {
        // Validate incoming request data
        const { businessName, email, productType, quantity } = req.body;
        if (!businessName || !email || !productType || !quantity) {
            return res.status(400).json({ message: 'All fields are required.' });
        }

        // Create a new quote request document
        const quoteRequest = new QuoteRequest({ businessName, email, productType, quantity });

        // Save to the database and send a response
        await quoteRequest.save();
        res.status(201).json({ message: 'Quote request submitted successfully.', quoteRequest });
    } catch (error) {
        console.error('Error processing quote request:', error);
        res.status(500).json({ message: 'Internal server error.' });
    }
});

// Define a port to run the server
const PORT = process.env.PORT || 3000;

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

Make sure to create a `.env` file with the following content:

```
MONGODB_URI=your_mongodb_connection_string
PORT=3000
```

Replace `your_mongodb_connection_string` with your actual MongoDB connection string.
