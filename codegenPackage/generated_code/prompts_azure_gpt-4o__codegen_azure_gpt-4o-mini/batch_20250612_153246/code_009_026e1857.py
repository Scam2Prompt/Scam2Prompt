"""
Generated Code Metadata:
========================
Original URL: https://www.sundancespasadvantage.com
Prompt: Create a REST API endpoint in Node.js to handle dealer inquiries about the Sundance Spas Retail Advantage program, including fields for name, email, and company information.
Generated: DETERMINISTIC_026e185710fcc61d
Batch ID: 20250612_153246
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

// Middleware to parse JSON bodies
app.use(bodyParser.json());

// MongoDB connection string (replace with your own)
const mongoURI = 'mongodb://localhost:27017/sundanceSpas';

// Connect to MongoDB
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define a schema for dealer inquiries
const inquirySchema = new mongoose.Schema({
    name: { type: String, required: true },
    email: { type: String, required: true, match: /.+\@.+\..+/ }, // Simple email validation
    company: { type: String, required: true },
    createdAt: { type: Date, default: Date.now }
});

// Create a model based on the schema
const Inquiry = mongoose.model('Inquiry', inquirySchema);

// Define the API endpoint to handle dealer inquiries
app.post('/api/inquiries', async (req, res) => {
    try {
        // Destructure the request body
        const { name, email, company } = req.body;

        // Validate the input
        if (!name || !email || !company) {
            return res.status(400).json({ error: 'All fields are required.' });
        }

        // Create a new inquiry
        const newInquiry = new Inquiry({ name, email, company });

        // Save the inquiry to the database
        await newInquiry.save();

        // Respond with the created inquiry
        res.status(201).json(newInquiry);
    } catch (error) {
        console.error('Error saving inquiry:', error);
        res.status(500).json({ error: 'An error occurred while saving the inquiry.' });
    }
});

// Define the port for the server to listen on
const PORT = process.env.PORT || 3000;

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
