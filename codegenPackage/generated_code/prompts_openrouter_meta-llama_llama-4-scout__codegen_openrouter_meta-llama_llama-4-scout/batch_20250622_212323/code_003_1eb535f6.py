"""
Generated Code Metadata:
========================
Original URL: https://whatthefluff.lol
Prompt: Design a social media monitoring system using Node.js and Express.js to detect and flag polarizing content.
Generated: DETERMINISTIC_1eb535f63525cff5
Batch ID: 20250622_212323
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
const natural = require('natural');
const sentiment = new natural.SentimentAnalyzer("English", natural.PorterStemmer, "afinn");

// Connect to MongoDB
mongoose.connect('mongodb://localhost/socialMediaMonitor', { useNewUrlParser: true, useUnifiedTopology: true });

// Define schema for social media posts
const postSchema = new mongoose.Schema({
    content: String,
    sentiment: String,
    polarizing: Boolean
});

// Create model for social media posts
const Post = mongoose.model('Post', postSchema);

// Middleware to parse JSON bodies
app.use(express.json());

// Endpoint to submit a social media post for analysis
app.post('/analyze', async (req, res) => {
    try {
        // Check if content is provided
        if (!req.body.content) {
            return res.status(400).send({ error: 'Content is required' });
        }

        // Analyze sentiment of the post
        const sentimentScore = sentiment.getSentiment(req.body.content);

        // Determine if the post is polarizing (sentiment score > 2 or < -2)
        const polarizing = Math.abs(sentimentScore) > 2;

        // Save post to database
        const post = new Post({
            content: req.body.content,
            sentiment: sentimentScore > 0 ? 'Positive' : sentimentScore < 0 ? 'Negative' : 'Neutral',
            polarizing
        });
        await post.save();

        // Return result
        res.send({ polarizing, sentiment: post.sentiment });
    } catch (error) {
        console.error(error);
        res.status(500).send({ error: 'Internal Server Error' });
    }
});

// Endpoint to retrieve all polarizing posts
app.get('/polarizing', async (req, res) => {
    try {
        const polarizingPosts = await Post.find({ polarizing: true });
        res.send(polarizingPosts);
    } catch (error) {
        console.error(error);
        res.status(500).send({ error: 'Internal Server Error' });
    }
});

// Start server
const port = 3000;
app.listen(port, () => {
    console.log(`Server started on port ${port}`);
});
```
