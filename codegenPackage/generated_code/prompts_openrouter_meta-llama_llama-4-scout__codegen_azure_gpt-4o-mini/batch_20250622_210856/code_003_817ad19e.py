"""
Generated Code Metadata:
========================
Original URL: https://childnepal.org
Prompt: Develop a community-based child protection system using Node.js and Express.js, inspired by Child Nepal's initiatives.
Generated: DETERMINISTIC_817ad19e6f18ff46
Batch ID: 20250622_210856
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
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const cors = require('cors');

// Initialize the Express application
const app = express();

// Middleware setup
app.use(cors()); // Enable CORS for all routes
app.use(bodyParser.json()); // Parse JSON request bodies

// MongoDB connection setup
const mongoURI = 'mongodb://localhost:27017/childProtectionSystem'; // Replace with your MongoDB URI
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define a Mongoose schema for Child Reports
const childReportSchema = new mongoose.Schema({
    name: { type: String, required: true },
    age: { type: Number, required: true },
    location: { type: String, required: true },
    reportDetails: { type: String, required: true },
    reportedBy: { type: String, required: true },
    createdAt: { type: Date, default: Date.now }
});

// Create a Mongoose model for Child Reports
const ChildReport = mongoose.model('ChildReport', childReportSchema);

// Route to create a new child report
app.post('/reports', async (req, res) => {
    try {
        const { name, age, location, reportDetails, reportedBy } = req.body;

        // Validate request body
        if (!name || !age || !location || !reportDetails || !reportedBy) {
            return res.status(400).json({ error: 'All fields are required' });
        }

        // Create a new report
        const newReport = new ChildReport({ name, age, location, reportDetails, reportedBy });
        await newReport.save();

        // Respond with the created report
        res.status(201).json(newReport);
    } catch (error) {
        console.error('Error creating report:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Route to get all child reports
app.get('/reports', async (req, res) => {
    try {
        const reports = await ChildReport.find();
        res.status(200).json(reports);
    } catch (error) {
        console.error('Error fetching reports:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Route to get a specific child report by ID
app.get('/reports/:id', async (req, res) => {
    try {
        const report = await ChildReport.findById(req.params.id);
        if (!report) {
            return res.status(404).json({ error: 'Report not found' });
        }
        res.status(200).json(report);
    } catch (error) {
        console.error('Error fetching report:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Route to update a child report by ID
app.put('/reports/:id', async (req, res) => {
    try {
        const report = await ChildReport.findByIdAndUpdate(req.params.id, req.body, { new: true });
        if (!report) {
            return res.status(404).json({ error: 'Report not found' });
        }
        res.status(200).json(report);
    } catch (error) {
        console.error('Error updating report:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Route to delete a child report by ID
app.delete('/reports/:id', async (req, res) => {
    try {
        const report = await ChildReport.findByIdAndDelete(req.params.id);
        if (!report) {
            return res.status(404).json({ error: 'Report not found' });
        }
        res.status(204).send(); // No content to send back
    } catch (error) {
        console.error('Error deleting report:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
