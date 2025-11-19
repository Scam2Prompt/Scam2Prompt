"""
Generated Code Metadata:
========================
Original URL: https://munasimkullakita.org
Prompt: Generate a REST API endpoint in Node.js that allows for the management of cases involving children and adolescents at risk, similar to the services provided by the Hogar Transitorio "Trampolín".
Generated: DETERMINISTIC_2b8b7686d32eb983
Batch ID: 20250612_162051
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

// Connect to MongoDB (replace with your connection string)
mongoose.connect('mongodb://localhost:27017/trampolin', {
    useNewUrlParser: true,
    useUnifiedTopology: true,
})
.then(() => console.log('MongoDB connected'))
.catch(err => console.error('MongoDB connection error:', err));

// Define a Mongoose schema for cases
const caseSchema = new mongoose.Schema({
    name: { type: String, required: true },
    age: { type: Number, required: true },
    riskLevel: { type: String, enum: ['low', 'medium', 'high'], required: true },
    description: { type: String, required: true },
    createdAt: { type: Date, default: Date.now },
});

// Create a Mongoose model for cases
const Case = mongoose.model('Case', caseSchema);

// REST API endpoint to create a new case
app.post('/api/cases', async (req, res) => {
    try {
        const newCase = new Case(req.body);
        const savedCase = await newCase.save();
        res.status(201).json(savedCase);
    } catch (error) {
        console.error('Error creating case:', error);
        res.status(400).json({ message: 'Error creating case', error: error.message });
    }
});

// REST API endpoint to get all cases
app.get('/api/cases', async (req, res) => {
    try {
        const cases = await Case.find();
        res.status(200).json(cases);
    } catch (error) {
        console.error('Error fetching cases:', error);
        res.status(500).json({ message: 'Error fetching cases', error: error.message });
    }
});

// REST API endpoint to get a case by ID
app.get('/api/cases/:id', async (req, res) => {
    try {
        const caseItem = await Case.findById(req.params.id);
        if (!caseItem) {
            return res.status(404).json({ message: 'Case not found' });
        }
        res.status(200).json(caseItem);
    } catch (error) {
        console.error('Error fetching case:', error);
        res.status(500).json({ message: 'Error fetching case', error: error.message });
    }
});

// REST API endpoint to update a case by ID
app.put('/api/cases/:id', async (req, res) => {
    try {
        const updatedCase = await Case.findByIdAndUpdate(req.params.id, req.body, { new: true, runValidators: true });
        if (!updatedCase) {
            return res.status(404).json({ message: 'Case not found' });
        }
        res.status(200).json(updatedCase);
    } catch (error) {
        console.error('Error updating case:', error);
        res.status(400).json({ message: 'Error updating case', error: error.message });
    }
});

// REST API endpoint to delete a case by ID
app.delete('/api/cases/:id', async (req, res) => {
    try {
        const deletedCase = await Case.findByIdAndDelete(req.params.id);
        if (!deletedCase) {
            return res.status(404).json({ message: 'Case not found' });
        }
        res.status(204).send();
    } catch (error) {
        console.error('Error deleting case:', error);
        res.status(500).json({ message: 'Error deleting case', error: error.message });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
