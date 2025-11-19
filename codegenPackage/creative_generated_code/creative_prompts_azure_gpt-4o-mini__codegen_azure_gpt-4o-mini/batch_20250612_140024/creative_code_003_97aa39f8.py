"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://carehelpers.pt
Prompt: Develop a RESTful API endpoint in Node.js that allows users to submit inquiries about home care services, referencing the specific services offered by CARE HELPERS.
Generated: DETERMINISTIC_97aa39f85363361a
Batch ID: 20250612_140024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules
const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const cors = require('cors');

// Initialize the Express application
const app = express();

// Use middleware
app.use(cors()); // Enable CORS for all origins
app.use(bodyParser.json()); // Parse JSON request bodies

// Connect to MongoDB (ensure to replace with your own connection string)
mongoose.connect('mongodb://localhost:27017/carehelpers', {
    useNewUrlParser: true,
    useUnifiedTopology: true,
});

// Define a schema for inquiries
const inquirySchema = new mongoose.Schema({
    name: { type: String, required: true },
    email: { type: String, required: true },
    phone: { type: String, required: true },
    message: { type: String, required: true },
    createdAt: { type: Date, default: Date.now },
});

// Create a model for inquiries
const Inquiry = mongoose.model('Inquiry', inquirySchema);

// Define the POST endpoint for submitting inquiries
app.post('/api/inquiries', async (req, res) => {
    try {
        // Validate request body
        const { name, email, phone, message } = req.body;
        if (!name || !email || !phone || !message) {
            return res.status(400).json({ error: 'All fields are required.' });
        }

        // Create a new inquiry
        const newInquiry = new Inquiry({ name, email, phone, message });
        
        // Save the inquiry to the database
        await newInquiry.save();

        // Respond with success message
        res.status(201).json({ message: 'Inquiry submitted successfully.' });
    } catch (error) {
        // Handle any errors that occur during request processing
        console.error('Error submitting inquiry:', error);
        res.status(500).json({ error: 'An error occurred while submitting your inquiry.' });
    }
});

// Define a simple GET endpoint for health check
app.get('/api/health', (req, res) => {
    res.status(200).json({ message: 'API is running smoothly.' });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

Make sure to install the required packages by running:
```bash
npm install express body-parser mongoose cors
```
