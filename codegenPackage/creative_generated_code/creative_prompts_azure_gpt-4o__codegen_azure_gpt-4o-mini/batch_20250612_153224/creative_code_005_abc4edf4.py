"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stockyardrefacing.com
Prompt: Develop a REST API in Node.js to manage customer inquiries for cabinet refacing services. Include endpoints for submitting inquiries, retrieving project details, and scheduling consultations.
Generated: DETERMINISTIC_abc4edf41561bf89
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Required dependencies
const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');

// Initialize the Express application
const app = express();

// Middleware to parse incoming JSON requests
app.use(bodyParser.json());

// MongoDB connection string (update with your own credentials)
const mongoURI = 'mongodb://localhost:27017/cabinetRefacing';
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define the Inquiry schema
const inquirySchema = new mongoose.Schema({
    name: { type: String, required: true },
    email: { type: String, required: true },
    message: { type: String, required: true },
    createdAt: { type: Date, default: Date.now },
    projectDetails: { type: String, default: '' },
    consultationScheduled: { type: Boolean, default: false },
    consultationDate: { type: Date, default: null }
});

// Create the Inquiry model
const Inquiry = mongoose.model('Inquiry', inquirySchema);

// Endpoint to submit an inquiry
app.post('/inquiries', async (req, res) => {
    try {
        const { name, email, message } = req.body;

        // Validate request body
        if (!name || !email || !message) {
            return res.status(400).json({ error: 'All fields are required' });
        }

        const newInquiry = new Inquiry({ name, email, message });
        await newInquiry.save();

        res.status(201).json({ message: 'Inquiry submitted successfully', inquiry: newInquiry });
    } catch (error) {
        console.error('Error submitting inquiry:', error);
        res.status(500).json({ error: 'Failed to submit inquiry' });
    }
});

// Endpoint to retrieve project details by ID
app.get('/inquiries/:id', async (req, res) => {
    try {
        const inquiry = await Inquiry.findById(req.params.id);
        if (!inquiry) {
            return res.status(404).json({ error: 'Inquiry not found' });
        }
        res.status(200).json(inquiry);
    } catch (error) {
        console.error('Error retrieving inquiry:', error);
        res.status(500).json({ error: 'Failed to retrieve inquiry' });
    }
});

// Endpoint to schedule a consultation
app.patch('/inquiries/:id/schedule', async (req, res) => {
    try {
        const { consultationDate } = req.body;

        // Validate request body
        if (!consultationDate) {
            return res.status(400).json({ error: 'Consultation date is required' });
        }

        const inquiry = await Inquiry.findByIdAndUpdate(
            req.params.id,
            { consultationScheduled: true, consultationDate: new Date(consultationDate) },
            { new: true }
        );

        if (!inquiry) {
            return res.status(404).json({ error: 'Inquiry not found' });
        }

        res.status(200).json({ message: 'Consultation scheduled', inquiry });
    } catch (error) {
        console.error('Error scheduling consultation:', error);
        res.status(500).json({ error: 'Failed to schedule consultation' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});

```
