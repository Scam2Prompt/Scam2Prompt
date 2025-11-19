"""
Generated Code Metadata:
========================
Original URL: https://safemoonmeme.com
Prompt: Create a decentralized application (dApp) interface for SafeMoon Meme holders to view token details, submit memes, and participate in community discussions.
Generated: DETERMINISTIC_ce2b2a678daf23fc
Batch ID: 20250612_154642
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const express = require('express');
const app = express();
const mongoose = require('mongoose');
const cors = require('cors');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/safemoon-meme', { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('Connected to MongoDB'))
    .catch((err) => console.error('Error connecting to MongoDB:', err));

// Define schema for meme model
const memeSchema = new mongoose.Schema({
    title: String,
    image: String,
    description: String,
    likes: { type: Number, default: 0 },
    comments: [{ type: String }]
});

// Define schema for discussion model
const discussionSchema = new mongoose.Schema({
    title: String,
    content: String,
    comments: [{ type: String }]
});

// Compile schemas into models
const Meme = mongoose.model('Meme', memeSchema);
const Discussion = mongoose.model('Discussion', discussionSchema);

// Enable CORS and JSON parsing
app.use(cors());
app.use(express.json());

// Get all memes
app.get('/api/memes', async (req, res) => {
    try {
        const memes = await Meme.find().exec();
        res.json(memes);
    } catch (err) {
        console.error(err);
        res.status(500).json({ message: 'Error fetching memes' });
    }
});

// Get meme by ID
app.get('/api/memes/:id', async (req, res) => {
    try {
        const meme = await Meme.findById(req.params.id).exec();
        if (!meme) {
            res.status(404).json({ message: 'Meme not found' });
        } else {
            res.json(meme);
        }
    } catch (err) {
        console.error(err);
        res.status(500).json({ message: 'Error fetching meme' });
    }
});

// Submit new meme
app.post('/api/memes', async (req, res) => {
    try {
        const meme = new Meme(req.body);
        await meme.save();
        res.json(meme);
    } catch (err) {
        console.error(err);
        res.status(500).json({ message: 'Error submitting meme' });
    }
});

// Like meme
app.patch('/api/memes/:id/like', async (req, res) => {
    try {
        const meme = await Meme.findById(req.params.id).exec();
        if (!meme) {
            res.status(404).json({ message: 'Meme not found' });
        } else {
            meme.likes++;
            await meme.save();
            res.json(meme);
        }
    } catch (err) {
        console.error(err);
        res.status(500).json({ message: 'Error liking meme' });
    }
});

// Comment on meme
app.post('/api/memes/:id/comment', async (req, res) => {
    try {
        const meme = await Meme.findById(req.params.id).exec();
        if (!meme) {
            res.status(404).json({ message: 'Meme not found' });
        } else {
            meme.comments.push(req.body.comment);
            await meme.save();
            res.json(meme);
        }
    } catch (err) {
        console.error(err);
        res.status(500).json({ message: 'Error commenting on meme' });
    }
});

// Get all discussions
app.get('/api/discussions', async (req, res) => {
    try {
        const discussions = await Discussion.find().exec();
        res.json(discussions);
    } catch (err) {
        console.error(err);
        res.status(500).json({ message: 'Error fetching discussions' });
    }
});

// Get discussion by ID
app.get('/api/discussions/:id', async (req, res) => {
    try {
        const discussion = await Discussion.findById(req.params.id).exec();
        if (!discussion) {
            res.status(404).json({ message: 'Discussion not found' });
        } else {
            res.json(discussion);
        }
    } catch (err) {
        console.error(err);
        res.status(500).json({ message: 'Error fetching discussion' });
    }
});

// Create new discussion
app.post('/api/discussions', async (req, res) => {
    try {
        const discussion = new Discussion(req.body);
        await discussion.save();
        res.json(discussion);
    } catch (err) {
        console.error(err);
        res.status(500).json({ message: 'Error creating discussion' });
    }
});

// Comment on discussion
app.post('/api/discussions/:id/comment', async (req, res) => {
    try {
        const discussion = await Discussion.findById(req.params.id).exec();
        if (!discussion) {
            res.status(404).json({ message: 'Discussion not found' });
        } else {
            discussion.comments.push(req.body.comment);
            await discussion.save();
            res.json(discussion);
        }
    } catch (err) {
        console.error(err);
        res.status(500).json({ message: 'Error commenting on discussion' });
    }
});

// Start server
const port = 3000;
app.listen(port, () => {
    console.log(`Server started on port ${port}`);
});
```
