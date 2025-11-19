"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trumpcoins-eth.web.app
Prompt: Create an API endpoint in Node.js to manage customer support inquiries for a collectible coin business, similar to the support offered by Trump Coins.
Generated: DETERMINISTIC_62418f52f511bc00
Batch ID: 20250612_155530
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
const cors = require('cors');

// Initialize the Express application
const app = express();

// Middleware setup
app.use(cors()); // Enable CORS for all routes
app.use(bodyParser.json()); // Parse JSON request bodies

// MongoDB connection setup
const mongoURI = 'mongodb://localhost:27017/coinSupport'; // Replace with your MongoDB URI
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define a Mongoose schema for support inquiries
const inquirySchema = new mongoose.Schema({
    name: { type: String, required: true },
    email: { type: String, required: true },
    message: { type: String, required: true },
    createdAt: { type: Date, default: Date.now }
});

// Create a Mongoose model for the inquiry
const Inquiry = mongoose.model('Inquiry', inquirySchema);

// API endpoint to submit a support inquiry
app.post('/api/inquiries', async (req, res) => {
    try {
        const { name, email, message } = req.body;

        // Validate request data
        if (!name || !email || !message) {
            return res.status(400).json({ error: 'All fields are required' });
        }

        // Create a new inquiry
        const newInquiry = new Inquiry({ name, email, message });
        await newInquiry.save();

        // Respond with the created inquiry
        res.status(201).json(newInquiry);
    } catch (error) {
        console.error('Error creating inquiry:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// API endpoint to get all inquiries
app.get('/api/inquiries', async (req, res) => {
    try {
        const inquiries = await Inquiry.find();
        res.status(200).json(inquiries);
    } catch (error) {
        console.error('Error fetching inquiries:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Start the server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
