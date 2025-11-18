"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonkai-buy.pages.dev
Prompt: Create a marketing dashboard in Node.js that tracks BONKAI's roadmap milestones, including presale progress, community growth, and ambassador applications.
Generated: DETERMINISTIC_76d78f62960322d3
Batch ID: 20250612_150601
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

// Create an instance of the Express app
const app = express();

// Middleware setup
app.use(bodyParser.json());

// MongoDB connection string
const mongoURI = 'mongodb://localhost:27017/bonkai-dashboard';

// Connect to MongoDB
mongoose.connect(mongoURI, {
    useNewUrlParser: true,
    useUnifiedTopology: true
})
.then(() => {
    console.log('MongoDB connected successfully');
})
.catch(err => {
    console.error('MongoDB connection error:', err);
});

// Define a Mongoose schema for Roadmap Milestones
const milestoneSchema = new mongoose.Schema({
    title: { type: String, required: true },
    description: { type: String, required: true },
    date: { type: Date, required: true },
    progress: { type: Number, min: 0, max: 100, required: true },
});

// Create a Mongoose model
const Milestone = mongoose.model('Milestone', milestoneSchema);

// Route to add a new milestone
app.post('/milestones', async (req, res) => {
    try {
        const { title, description, date, progress } = req.body;
        const newMilestone = new Milestone({ title, description, date, progress });
        await newMilestone.save();
        res.status(201).json(newMilestone);
    } catch (error) {
        console.error('Error creating milestone:', error);
        res.status(500).json({ error: 'Internal Server Error' });
    }
});

// Route to get all milestones
app.get('/milestones', async (req, res) => {
    try {
        const milestones = await Milestone.find();
        res.status(200).json(milestones);
    } catch (error) {
        console.error('Error fetching milestones:', error);
        res.status(500).json({ error: 'Internal Server Error' });
    }
});

// Route to update a milestone by ID
app.put('/milestones/:id', async (req, res) => {
    try {
        const { id } = req.params;
        const updatedMilestone = await Milestone.findByIdAndUpdate(id, req.body, { new: true });
        if (!updatedMilestone) {
            return res.status(404).json({ error: 'Milestone not found' });
        }
        res.status(200).json(updatedMilestone);
    } catch (error) {
        console.error('Error updating milestone:', error);
        res.status(500).json({ error: 'Internal Server Error' });
    }
});

// Route to delete a milestone by ID
app.delete('/milestones/:id', async (req, res) => {
    try {
        const { id } = req.params;
        const deletedMilestone = await Milestone.findByIdAndDelete(id);
        if (!deletedMilestone) {
            return res.status(404).json({ error: 'Milestone not found' });
        }
        res.status(204).send();
    } catch (error) {
        console.error('Error deleting milestone:', error);
        res.status(500).json({ error: 'Internal Server Error' });
    }
});

// Start the application server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
