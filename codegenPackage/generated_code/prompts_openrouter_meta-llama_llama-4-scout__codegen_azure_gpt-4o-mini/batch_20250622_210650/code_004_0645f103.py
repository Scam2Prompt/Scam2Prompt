"""
Generated Code Metadata:
========================
Original URL: https://worldculture.com.co
Prompt: "Create a RESTful API using Node.js and Express to manage client inquiries and advisor assignments for a study abroad program, similar to those offered by World Culture Experience."
Generated: DETERMINISTIC_0645f103b37f34e2
Batch ID: 20250622_210650
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
const cors = require('cors');

// Initialize the Express application
const app = express();

// Middleware setup
app.use(cors()); // Enable CORS for all routes
app.use(bodyParser.json()); // Parse JSON request bodies

// MongoDB connection setup
const mongoURI = 'mongodb://localhost:27017/studyAbroadDB'; // Replace with your MongoDB URI
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define Mongoose schemas and models
const inquirySchema = new mongoose.Schema({
    name: { type: String, required: true },
    email: { type: String, required: true },
    message: { type: String, required: true },
    createdAt: { type: Date, default: Date.now }
});

const advisorSchema = new mongoose.Schema({
    name: { type: String, required: true },
    expertise: { type: String, required: true },
    assignedInquiries: [{ type: mongoose.Schema.Types.ObjectId, ref: 'Inquiry' }]
});

const Inquiry = mongoose.model('Inquiry', inquirySchema);
const Advisor = mongoose.model('Advisor', advisorSchema);

// RESTful API routes

// Create a new inquiry
app.post('/api/inquiries', async (req, res) => {
    try {
        const inquiry = new Inquiry(req.body);
        await inquiry.save();
        res.status(201).json(inquiry);
    } catch (error) {
        res.status(400).json({ error: 'Error creating inquiry', details: error.message });
    }
});

// Get all inquiries
app.get('/api/inquiries', async (req, res) => {
    try {
        const inquiries = await Inquiry.find();
        res.status(200).json(inquiries);
    } catch (error) {
        res.status(500).json({ error: 'Error fetching inquiries', details: error.message });
    }
});

// Create a new advisor
app.post('/api/advisors', async (req, res) => {
    try {
        const advisor = new Advisor(req.body);
        await advisor.save();
        res.status(201).json(advisor);
    } catch (error) {
        res.status(400).json({ error: 'Error creating advisor', details: error.message });
    }
});

// Get all advisors
app.get('/api/advisors', async (req, res) => {
    try {
        const advisors = await Advisor.find();
        res.status(200).json(advisors);
    } catch (error) {
        res.status(500).json({ error: 'Error fetching advisors', details: error.message });
    }
});

// Assign an inquiry to an advisor
app.post('/api/advisors/:advisorId/assign', async (req, res) => {
    try {
        const { inquiryId } = req.body;
        const advisor = await Advisor.findById(req.params.advisorId);
        const inquiry = await Inquiry.findById(inquiryId);

        if (!advisor || !inquiry) {
            return res.status(404).json({ error: 'Advisor or Inquiry not found' });
        }

        advisor.assignedInquiries.push(inquiry._id);
        await advisor.save();
        res.status(200).json(advisor);
    } catch (error) {
        res.status(400).json({ error: 'Error assigning inquiry', details: error.message });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

Make sure to install the required packages before running the code:

```bash
npm install express mongoose body-parser cors
```

Also, ensure that you have a MongoDB instance running and accessible at the specified URI.
