"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maskatiyasgroup.com
Prompt: Create a REST API endpoint in Node.js that allows users to submit inquiries about mobile LCDs from Maskatiyas Group, including details on their Gold Touch and Golden Crown brands.
Generated: DETERMINISTIC_e4dd93f931d0e0fd
Batch ID: 20250612_161700
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

// Create an instance of the Express application
const app = express();

// Middleware to parse JSON bodies
app.use(bodyParser.json());

// MongoDB connection string (update with your actual connection string)
const mongoURI = 'mongodb://localhost:27017/maskatiyasdb';

// Connect to MongoDB
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define a schema for inquiries
const inquirySchema = new mongoose.Schema({
    name: { type: String, required: true },
    email: { type: String, required: true, match: /.+\@.+\..+/ },
    phone: { type: String, required: true },
    brand: { type: String, required: true, enum: ['Gold Touch', 'Golden Crown'] },
    message: { type: String, required: true }
});

// Create a model from the schema
const Inquiry = mongoose.model('Inquiry', inquirySchema);

// REST API endpoint to submit inquiries
app.post('/api/inquiries', async (req, res) => {
    try {
        // Destructure the request body
        const { name, email, phone, brand, message } = req.body;

        // Validate that all required fields are provided
        if (!name || !email || !phone || !brand || !message) {
            return res.status(400).json({ error: 'All fields are required.' });
        }

        // Create a new inquiry
        const newInquiry = new Inquiry({ name, email, phone, brand, message });

        // Save the inquiry to the database
        await newInquiry.save();

        // Respond with success
        return res.status(201).json({ message: 'Inquiry submitted successfully.' });
    } catch (error) {
        console.error('Error submitting inquiry:', error);
        return res.status(500).json({ error: 'An error occurred while submitting the inquiry.' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
