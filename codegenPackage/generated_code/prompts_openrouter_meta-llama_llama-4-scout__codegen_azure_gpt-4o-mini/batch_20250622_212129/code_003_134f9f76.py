"""
Generated Code Metadata:
========================
Original URL: https://buttholecoin.dev
Prompt: Create a basic roadmap tracker using JavaScript and a database to monitor progress on the Butthole Coin project's milestones.
Generated: DETERMINISTIC_134f9f761ffed14e
Batch ID: 20250622_212129
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary modules
const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');

// Initialize the Express application
const app = express();
app.use(bodyParser.json());

// Connect to MongoDB database
mongoose.connect('mongodb://localhost:27017/buttholeCoin', {
    useNewUrlParser: true,
    useUnifiedTopology: true,
})
.then(() => console.log('MongoDB connected'))
.catch(err => console.error('MongoDB connection error:', err));

// Define a schema for milestones
const milestoneSchema = new mongoose.Schema({
    title: { type: String, required: true },
    description: { type: String, required: true },
    dueDate: { type: Date, required: true },
    completed: { type: Boolean, default: false },
});

// Create a model for milestones
const Milestone = mongoose.model('Milestone', milestoneSchema);

// Route to create a new milestone
app.post('/milestones', async (req, res) => {
    try {
        const { title, description, dueDate } = req.body;
        const newMilestone = new Milestone({ title, description, dueDate });
        await newMilestone.save();
        res.status(201).json(newMilestone);
    } catch (error) {
        console.error('Error creating milestone:', error);
        res.status(500).json({ message: 'Error creating milestone' });
    }
});

// Route to get all milestones
app.get('/milestones', async (req, res) => {
    try {
        const milestones = await Milestone.find();
        res.status(200).json(milestones);
    } catch (error) {
        console.error('Error fetching milestones:', error);
        res.status(500).json({ message: 'Error fetching milestones' });
    }
});

// Route to update a milestone
app.put('/milestones/:id', async (req, res) => {
    try {
        const { id } = req.params;
        const updatedMilestone = await Milestone.findByIdAndUpdate(id, req.body, { new: true });
        if (!updatedMilestone) {
            return res.status(404).json({ message: 'Milestone not found' });
        }
        res.status(200).json(updatedMilestone);
    } catch (error) {
        console.error('Error updating milestone:', error);
        res.status(500).json({ message: 'Error updating milestone' });
    }
});

// Route to delete a milestone
app.delete('/milestones/:id', async (req, res) => {
    try {
        const { id } = req.params;
        const deletedMilestone = await Milestone.findByIdAndDelete(id);
        if (!deletedMilestone) {
            return res.status(404).json({ message: 'Milestone not found' });
        }
        res.status(204).send();
    } catch (error) {
        console.error('Error deleting milestone:', error);
        res.status(500).json({ message: 'Error deleting milestone' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
