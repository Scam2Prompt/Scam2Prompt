"""
Generated Code Metadata:
========================
Original URL: https://1111-967.pages.dev
Prompt: Create a REST API endpoint in Node.js that allows users to submit their personal success stories, reflecting the lessons from Andrew Tate's "Lessons from Fighting" section.
Generated: DETERMINISTIC_59e3c8bbb065f1b6
Batch ID: 20250612_161616
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

// Middleware to parse JSON bodies
app.use(bodyParser.json());

// Connect to MongoDB (replace with your own connection string)
mongoose.connect('mongodb://localhost:27017/successStories', {
    useNewUrlParser: true,
    useUnifiedTopology: true,
})
.then(() => console.log('MongoDB connected'))
.catch(err => console.error('MongoDB connection error:', err));

// Define a schema for success stories
const successStorySchema = new mongoose.Schema({
    title: { type: String, required: true },
    content: { type: String, required: true },
    author: { type: String, required: true },
    createdAt: { type: Date, default: Date.now }
});

// Create a model based on the schema
const SuccessStory = mongoose.model('SuccessStory', successStorySchema);

// Define a POST endpoint to submit success stories
app.post('/api/success-stories', async (req, res) => {
    try {
        // Validate request body
        const { title, content, author } = req.body;
        if (!title || !content || !author) {
            return res.status(400).json({ error: 'Title, content, and author are required.' });
        }

        // Create a new success story
        const newStory = new SuccessStory({ title, content, author });
        await newStory.save();

        // Respond with the created story
        res.status(201).json(newStory);
    } catch (error) {
        console.error('Error saving success story:', error);
        res.status(500).json({ error: 'An error occurred while saving the story.' });
    }
});

// Define a GET endpoint to retrieve all success stories
app.get('/api/success-stories', async (req, res) => {
    try {
        const stories = await SuccessStory.find();
        res.status(200).json(stories);
    } catch (error) {
        console.error('Error retrieving success stories:', error);
        res.status(500).json({ error: 'An error occurred while retrieving stories.' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
