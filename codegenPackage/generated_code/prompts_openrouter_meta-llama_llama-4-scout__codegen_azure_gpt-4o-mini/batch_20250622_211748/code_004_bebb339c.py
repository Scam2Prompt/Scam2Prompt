"""
Generated Code Metadata:
========================
Original URL: https://www.atletismomg.org.br
Prompt: Create a RESTful API in Node.js to manage certifications and records for athletes and teams, similar to the Certidões FMA and Recordes Estaduais sections on the website.
Generated: DETERMINISTIC_bebb339cde72b3c6
Batch ID: 20250622_211748
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

// Initialize the Express application
const app = express();

// Middleware to parse JSON requests
app.use(bodyParser.json());

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/athleteCertifications', {
    useNewUrlParser: true,
    useUnifiedTopology: true,
})
.then(() => console.log('MongoDB connected'))
.catch(err => console.error('MongoDB connection error:', err));

// Define a schema for certifications
const certificationSchema = new mongoose.Schema({
    athleteName: { type: String, required: true },
    teamName: { type: String, required: true },
    certificationType: { type: String, required: true },
    dateIssued: { type: Date, default: Date.now },
});

// Create a model for certifications
const Certification = mongoose.model('Certification', certificationSchema);

// RESTful API routes

// Create a new certification
app.post('/certifications', async (req, res) => {
    try {
        const certification = new Certification(req.body);
        await certification.save();
        res.status(201).json(certification);
    } catch (error) {
        res.status(400).json({ message: 'Error creating certification', error });
    }
});

// Get all certifications
app.get('/certifications', async (req, res) => {
    try {
        const certifications = await Certification.find();
        res.status(200).json(certifications);
    } catch (error) {
        res.status(500).json({ message: 'Error fetching certifications', error });
    }
});

// Get a certification by ID
app.get('/certifications/:id', async (req, res) => {
    try {
        const certification = await Certification.findById(req.params.id);
        if (!certification) {
            return res.status(404).json({ message: 'Certification not found' });
        }
        res.status(200).json(certification);
    } catch (error) {
        res.status(500).json({ message: 'Error fetching certification', error });
    }
});

// Update a certification by ID
app.put('/certifications/:id', async (req, res) => {
    try {
        const certification = await Certification.findByIdAndUpdate(req.params.id, req.body, { new: true, runValidators: true });
        if (!certification) {
            return res.status(404).json({ message: 'Certification not found' });
        }
        res.status(200).json(certification);
    } catch (error) {
        res.status(400).json({ message: 'Error updating certification', error });
    }
});

// Delete a certification by ID
app.delete('/certifications/:id', async (req, res) => {
    try {
        const certification = await Certification.findByIdAndDelete(req.params.id);
        if (!certification) {
            return res.status(404).json({ message: 'Certification not found' });
        }
        res.status(204).send();
    } catch (error) {
        res.status(500).json({ message: 'Error deleting certification', error });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
