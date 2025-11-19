"""
Generated Code Metadata:
========================
Original URL: https://www.twincityjacuzzi.com
Prompt: Create a RESTful API in Node.js to manage Jacuzzi massage chair settings, including customizable massage techniques and ergonomic designs.
Generated: DETERMINISTIC_ea733270a236b94a
Batch ID: 20250622_210703
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

// Middleware to parse JSON requests
app.use(bodyParser.json());

// Connect to MongoDB (replace 'your_connection_string' with your actual connection string)
mongoose.connect('your_connection_string', { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define a schema for the Jacuzzi settings
const jacuzziSchema = new mongoose.Schema({
    technique: { type: String, required: true },
    intensity: { type: Number, required: true, min: 1, max: 10 },
    duration: { type: Number, required: true, min: 1 }, // duration in minutes
    ergonomicDesign: { type: String, required: true }
});

// Create a model based on the schema
const Jacuzzi = mongoose.model('Jacuzzi', jacuzziSchema);

// RESTful API routes

// Create a new Jacuzzi setting
app.post('/api/jacuzzi', async (req, res) => {
    try {
        const jacuzziSetting = new Jacuzzi(req.body);
        const savedSetting = await jacuzziSetting.save();
        res.status(201).json(savedSetting);
    } catch (error) {
        res.status(400).json({ message: 'Error creating Jacuzzi setting', error });
    }
});

// Get all Jacuzzi settings
app.get('/api/jacuzzi', async (req, res) => {
    try {
        const settings = await Jacuzzi.find();
        res.status(200).json(settings);
    } catch (error) {
        res.status(500).json({ message: 'Error retrieving Jacuzzi settings', error });
    }
});

// Get a specific Jacuzzi setting by ID
app.get('/api/jacuzzi/:id', async (req, res) => {
    try {
        const setting = await Jacuzzi.findById(req.params.id);
        if (!setting) {
            return res.status(404).json({ message: 'Jacuzzi setting not found' });
        }
        res.status(200).json(setting);
    } catch (error) {
        res.status(500).json({ message: 'Error retrieving Jacuzzi setting', error });
    }
});

// Update a specific Jacuzzi setting by ID
app.put('/api/jacuzzi/:id', async (req, res) => {
    try {
        const updatedSetting = await Jacuzzi.findByIdAndUpdate(req.params.id, req.body, { new: true, runValidators: true });
        if (!updatedSetting) {
            return res.status(404).json({ message: 'Jacuzzi setting not found' });
        }
        res.status(200).json(updatedSetting);
    } catch (error) {
        res.status(400).json({ message: 'Error updating Jacuzzi setting', error });
    }
});

// Delete a specific Jacuzzi setting by ID
app.delete('/api/jacuzzi/:id', async (req, res) => {
    try {
        const deletedSetting = await Jacuzzi.findByIdAndDelete(req.params.id);
        if (!deletedSetting) {
            return res.status(404).json({ message: 'Jacuzzi setting not found' });
        }
        res.status(204).send(); // No content to send back
    } catch (error) {
        res.status(500).json({ message: 'Error deleting Jacuzzi setting', error });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
