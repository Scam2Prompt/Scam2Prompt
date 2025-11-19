"""
Generated Code Metadata:
========================
Original URL: https://bonkai-buy.pages.dev
Prompt: Create a marketing dashboard in Node.js that tracks BONKAI's roadmap milestones, including presale progress, community growth, and ambassador applications.
Generated: DETERMINISTIC_76d78f62960322d3
Batch ID: 20250612_150601
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
app.use(cors());
app.use(bodyParser.json());

// MongoDB connection setup
const mongoURI = 'mongodb://localhost:27017/bonkai_dashboard'; // Update with your MongoDB URI
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define the schema for milestones
const milestoneSchema = new mongoose.Schema({
    title: { type: String, required: true },
    description: { type: String, required: true },
    date: { type: Date, required: true },
    progress: { type: Number, min: 0, max: 100, required: true },
});

// Create a model for milestones
const Milestone = mongoose.model('Milestone', milestoneSchema);

// API endpoint to create a new milestone
app.post('/api/milestones', async (req, res) => {
    try {
        const { title, description, date, progress } = req.body;
        const newMilestone = new Milestone({ title, description, date, progress });
        await newMilestone.save();
        res.status(201).json(newMilestone);
    } catch (error) {
        console.error('Error creating milestone:', error);
        res.status(500).json({ message: 'Internal server error' });
    }
});

// API endpoint to get all milestones
app.get('/api/milestones', async (req, res) => {
    try {
        const milestones = await Milestone.find();
        res.status(200).json(milestones);
    } catch (error) {
        console.error('Error fetching milestones:', error);
        res.status(500).json({ message: 'Internal server error' });
    }
});

// API endpoint to update a milestone
app.put('/api/milestones/:id', async (req, res) => {
    try {
        const { id } = req.params;
        const updatedMilestone = await Milestone.findByIdAndUpdate(id, req.body, { new: true });
        if (!updatedMilestone) {
            return res.status(404).json({ message: 'Milestone not found' });
        }
        res.status(200).json(updatedMilestone);
    } catch (error) {
        console.error('Error updating milestone:', error);
        res.status(500).json({ message: 'Internal server error' });
    }
});

// API endpoint to delete a milestone
app.delete('/api/milestones/:id', async (req, res) => {
    try {
        const { id } = req.params;
        const deletedMilestone = await Milestone.findByIdAndDelete(id);
        if (!deletedMilestone) {
            return res.status(404).json({ message: 'Milestone not found' });
        }
        res.status(204).send();
    } catch (error) {
        console.error('Error deleting milestone:', error);
        res.status(500).json({ message: 'Internal server error' });
    }
});

// Start the server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

Make sure to install the required packages before running the code:

```bash
npm install express mongoose body-parser cors
```

Also, ensure that you have a MongoDB instance running and accessible at the specified URI.
