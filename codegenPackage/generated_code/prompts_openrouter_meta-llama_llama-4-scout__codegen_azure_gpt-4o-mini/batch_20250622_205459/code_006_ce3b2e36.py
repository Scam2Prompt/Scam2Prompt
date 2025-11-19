"""
Generated Code Metadata:
========================
Original URL: https://metamash.co
Prompt: "Write a Node.js code to build a multi-channel domain knowledge system for a digital agency like Metamash."
Generated: DETERMINISTIC_ce3b2e365751380e
Batch ID: 20250622_205459
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
app.use(cors()); // Enable CORS for all routes
app.use(bodyParser.json()); // Parse JSON request bodies

// MongoDB connection setup
const mongoURI = 'mongodb://localhost:27017/knowledgeSystem'; // Replace with your MongoDB URI
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define a schema for knowledge articles
const articleSchema = new mongoose.Schema({
    title: { type: String, required: true },
    content: { type: String, required: true },
    channel: { type: String, required: true },
    createdAt: { type: Date, default: Date.now }
});

// Create a model for the articles
const Article = mongoose.model('Article', articleSchema);

// Route to create a new article
app.post('/articles', async (req, res) => {
    try {
        const { title, content, channel } = req.body;
        const newArticle = new Article({ title, content, channel });
        await newArticle.save();
        res.status(201).json(newArticle);
    } catch (error) {
        console.error('Error creating article:', error);
        res.status(500).json({ message: 'Internal server error' });
    }
});

// Route to get all articles
app.get('/articles', async (req, res) => {
    try {
        const articles = await Article.find();
        res.status(200).json(articles);
    } catch (error) {
        console.error('Error fetching articles:', error);
        res.status(500).json({ message: 'Internal server error' });
    }
});

// Route to get articles by channel
app.get('/articles/channel/:channel', async (req, res) => {
    try {
        const { channel } = req.params;
        const articles = await Article.find({ channel });
        res.status(200).json(articles);
    } catch (error) {
        console.error('Error fetching articles by channel:', error);
        res.status(500).json({ message: 'Internal server error' });
    }
});

// Route to update an article
app.put('/articles/:id', async (req, res) => {
    try {
        const { id } = req.params;
        const updatedArticle = await Article.findByIdAndUpdate(id, req.body, { new: true });
        if (!updatedArticle) {
            return res.status(404).json({ message: 'Article not found' });
        }
        res.status(200).json(updatedArticle);
    } catch (error) {
        console.error('Error updating article:', error);
        res.status(500).json({ message: 'Internal server error' });
    }
});

// Route to delete an article
app.delete('/articles/:id', async (req, res) => {
    try {
        const { id } = req.params;
        const deletedArticle = await Article.findByIdAndDelete(id);
        if (!deletedArticle) {
            return res.status(404).json({ message: 'Article not found' });
        }
        res.status(204).send(); // No content to send back
    } catch (error) {
        console.error('Error deleting article:', error);
        res.status(500).json({ message: 'Internal server error' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
