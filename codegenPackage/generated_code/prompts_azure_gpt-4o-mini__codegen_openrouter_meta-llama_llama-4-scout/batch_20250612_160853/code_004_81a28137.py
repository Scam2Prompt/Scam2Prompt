"""
Generated Code Metadata:
========================
Original URL: https://skifoundation.org
Prompt: Construct a RESTful API endpoint in Node.js that allows users to access success stories from the SKI Foundation's initiatives in empowering local entrepreneurs.
Generated: DETERMINISTIC_81a28137151636fe
Batch ID: 20250612_160853
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
const app = express();
const mongoose = require('mongoose');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/ski-foundation', { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('Connected to MongoDB'))
    .catch((err) => console.error('Error connecting to MongoDB:', err));

// Define schema for success story
const successStorySchema = new mongoose.Schema({
    title: String,
    description: String,
    entrepreneurName: String,
    initiative: String
});

// Create model for success story
const SuccessStory = mongoose.model('SuccessStory', successStorySchema);

// Middleware to parse JSON bodies
app.use(express.json());

// API endpoint to get all success stories
/**
 * @route   GET /api/success-stories
 * @desc    Get all success stories
 * @access  Public
 */
app.get('/api/success-stories', async (req, res) => {
    try {
        const successStories = await SuccessStory.find().exec();
        res.json(successStories);
    } catch (err) {
        console.error(err);
        res.status(500).json({ message: 'Error fetching success stories' });
    }
});

// API endpoint to get a single success story by ID
/**
 * @route   GET /api/success-stories/:id
 * @desc    Get a single success story by ID
 * @access  Public
 */
app.get('/api/success-stories/:id', async (req, res) => {
    try {
        const id = req.params.id;
        if (!mongoose.Types.ObjectId.isValid(id)) {
            return res.status(400).json({ message: 'Invalid ID' });
        }
        const successStory = await SuccessStory.findById(id).exec();
        if (!successStory) {
            return res.status(404).json({ message: 'Success story not found' });
        }
        res.json(successStory);
    } catch (err) {
        console.error(err);
        res.status(500).json({ message: 'Error fetching success story' });
    }
});

// API endpoint to create a new success story
/**
 * @route   POST /api/success-stories
 * @desc    Create a new success story
 * @access  Private ( authentication required )
 */
// TODO: Implement authentication middleware
app.post('/api/success-stories', async (req, res) => {
    try {
        const { title, description, entrepreneurName, initiative } = req.body;
        if (!title || !description || !entrepreneurName || !initiative) {
            return res.status(400).json({ message: 'Please provide all required fields' });
        }
        const successStory = new SuccessStory({ title, description, entrepreneurName, initiative });
        await successStory.save();
        res.json(successStory);
    } catch (err) {
        console.error(err);
        res.status(500).json({ message: 'Error creating success story' });
    }
});

// API endpoint to update a success story
/**
 * @route   PATCH /api/success-stories/:id
 * @desc    Update a success story
 * @access  Private ( authentication required )
 */
// TODO: Implement authentication middleware
app.patch('/api/success-stories/:id', async (req, res) => {
    try {
        const id = req.params.id;
        if (!mongoose.Types.ObjectId.isValid(id)) {
            return res.status(400).json({ message: 'Invalid ID' });
        }
        const successStory = await SuccessStory.findByIdAndUpdate(id, req.body, { new: true });
        if (!successStory) {
            return res.status(404).json({ message: 'Success story not found' });
        }
        res.json(successStory);
    } catch (err) {
        console.error(err);
        res.status(500).json({ message: 'Error updating success story' });
    }
});

// API endpoint to delete a success story
/**
 * @route   DELETE /api/success-stories/:id
 * @desc    Delete a success story
 * @access  Private ( authentication required )
 */
// TODO: Implement authentication middleware
app.delete('/api/success-stories/:id', async (req, res) => {
    try {
        const id = req.params.id;
        if (!mongoose.Types.ObjectId.isValid(id)) {
            return res.status(400).json({ message: 'Invalid ID' });
        }
        await SuccessStory.findByIdAndRemove(id);
        res.json({ message: 'Success story deleted successfully' });
    } catch (err) {
        console.error(err);
        res.status(500).json({ message: 'Error deleting success story' });
    }
});

// Start server
const port = 3000;
app.listen(port, () => console.log(`Server started on port ${port}`));
```
