"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://munasimkullakita.org
Prompt: Generate a REST API endpoint in Node.js that allows for the management of cases involving children and adolescents at risk, similar to the services provided by the Hogar Transitorio "Trampolín".
Generated: DETERMINISTIC_2b8b7686d32eb983
Batch ID: 20250612_162051
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
const mongoose = require('mongoose');
const bodyParser = require('body-parser');

// Initialize the express application
const app = express();

// Middleware to parse JSON bodies
app.use(bodyParser.json());

// MongoDB connection URI
const mongoURI = 'mongodb://localhost:27017/trampolin'; // Update with your URI

// Connect to MongoDB
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define a schema for a case
const caseSchema = new mongoose.Schema({
    name: { type: String, required: true },
    age: { type: Number, required: true, min: 0 },
    riskLevel: { type: String, enum: ['low', 'medium', 'high'], required: true },
    description: { type: String, required: true },
    createdAt: { type: Date, default: Date.now }
});

// Create a model for the case
const Case = mongoose.model('Case', caseSchema);

// REST API Endpoints

// Create a new case
app.post('/api/cases', async (req, res) => {
    try {
        const newCase = new Case(req.body);
        const savedCase = await newCase.save();
        res.status(201).json(savedCase);
    } catch (error) {
        res.status(400).json({ message: 'Error creating case', error });
    }
});

// Get all cases
app.get('/api/cases', async (req, res) => {
    try {
        const cases = await Case.find();
        res.status(200).json(cases);
    } catch (error) {
        res.status(500).json({ message: 'Error retrieving cases', error });
    }
});

// Get a case by ID
app.get('/api/cases/:id', async (req, res) => {
    try {
        const caseItem = await Case.findById(req.params.id);
        if (!caseItem) {
            return res.status(404).json({ message: 'Case not found' });
        }
        res.status(200).json(caseItem);
    } catch (error) {
        res.status(500).json({ message: 'Error retrieving case', error });
    }
});

// Update a case by ID
app.put('/api/cases/:id', async (req, res) => {
    try {
        const updatedCase = await Case.findByIdAndUpdate(req.params.id, req.body, { new: true, runValidators: true });
        if (!updatedCase) {
            return res.status(404).json({ message: 'Case not found' });
        }
        res.status(200).json(updatedCase);
    } catch (error) {
        res.status(400).json({ message: 'Error updating case', error });
    }
});

// Delete a case by ID
app.delete('/api/cases/:id', async (req, res) => {
    try {
        const deletedCase = await Case.findByIdAndDelete(req.params.id);
        if (!deletedCase) {
            return res.status(404).json({ message: 'Case not found' });
        }
        res.status(204).send(); // No content to send back
    } catch (error) {
        res.status(500).json({ message: 'Error deleting case', error });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
