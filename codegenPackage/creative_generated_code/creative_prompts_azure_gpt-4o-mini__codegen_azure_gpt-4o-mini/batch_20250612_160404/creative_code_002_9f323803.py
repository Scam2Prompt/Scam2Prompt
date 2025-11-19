"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.iaci.org
Prompt: Create a RESTful API endpoint in Node.js that allows users to submit testimonials for a business association like IACI, including fields for member name, organization, and testimonial text.
Generated: DETERMINISTIC_9f32380394deab95
Batch ID: 20250612_160404
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:${PORT}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
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

// Middleware to parse JSON bodies
app.use(bodyParser.json());

// Connect to MongoDB (replace with your connection string)
mongoose.connect('mongodb://localhost:27017/testimonials', { 
    useNewUrlParser: true, 
    useUnifiedTopology: true 
});

// Define a schema for Testimonials
const testimonialSchema = new mongoose.Schema({
    memberName: { type: String, required: true },
    organization: { type: String, required: true },
    testimonialText: { type: String, required: true },
}, { timestamps: true });

// Create a model for Testimonials
const Testimonial = mongoose.model('Testimonial', testimonialSchema);

// POST endpoint to create a new testimonial
app.post('/api/testimonials', async (req, res) => {
    const { memberName, organization, testimonialText } = req.body;

    // Validate incoming data
    if (!memberName || !organization || !testimonialText) {
        return res.status(400).json({ error: 'All fields are required.' });
    }

    try {
        // Create a new testimonial
        const newTestimonial = new Testimonial({ memberName, organization, testimonialText });
        await newTestimonial.save();

        // Respond with the created testimonial
        res.status(201).json(newTestimonial);
    } catch (error) {
        console.error('Error saving testimonial:', error);
        res.status(500).json({ error: 'Internal Server Error' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});

// Gracefully handle MongoDB connection errors
mongoose.connection.on('error', (err) => {
    console.error('MongoDB connection error:', err);
});

// Close the server on termination
process.on('SIGINT', () => {
    mongoose.connection.close(() => {
        console.log('MongoDB connection closed due to app termination');
        process.exit(0);
    });
});
```
