"""
Generated Code Metadata:
========================
Original URL: https://filmdailyweb.com
Prompt: Write a Node.js application to fetch and display the latest news articles from a database or API, inspired by the diverse articles on Film Daily Web.
Generated: DETERMINISTIC_5d9176a075fbceaa
Batch ID: 20250622_210655
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://newsapi.org/v2/top-headlines": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
const express = require('express');
const axios = require('axios');
const mongoose = require('mongoose');
const cors = require('cors');
require('dotenv').config();

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 5000;

// Middleware
app.use(cors());
app.use(express.json());

// Database connection
mongoose.connect(process.env.MONGODB_URI, {
    useNewUrlParser: true,
    useUnifiedTopology: true
})
.then(() => console.log('Connected to MongoDB'))
.catch(err => console.error('MongoDB connection error:', err));

// Article Schema
const articleSchema = new mongoose.Schema({
    title: { type: String, required: true },
    description: { type: String, required: true },
    url: { type: String, required: true },
    publishedAt: { type: Date, default: Date.now },
    source: { type: String, required: true },
    imageUrl: { type: String }
});

const Article = mongoose.model('Article', articleSchema);

// Fetch news from external API
async function fetchNewsFromAPI() {
    try {
        const response = await axios.get('https://newsapi.org/v2/top-headlines', {
            params: {
                country: 'us',
                category: 'entertainment',
                apiKey: process.env.NEWS_API_KEY
            }
        });

        const articles = response.data.articles.map(article => ({
            title: article.title,
            description: article.description,
            url: article.url,
            publishedAt: new Date(article.publishedAt),
            source: article.source.name,
            imageUrl: article.urlToImage
        }));

        // Save to database
        await Article.insertMany(articles);
        console.log('News articles fetched and saved successfully');
    } catch (error) {
        console.error('Error fetching news:', error.message);
    }
}

// Routes
app.get('/api/news', async (req, res) => {
    try {
        const articles = await Article.find().sort({ publishedAt: -1 }).limit(20);
        res.json(articles);
    } catch (error) {
        console.error('Error fetching articles:', error.message);
        res.status(500).json({ error: 'Internal server error' });
    }
});

app.get('/api/news/refresh', async (req, res) => {
    try {
        await fetchNewsFromAPI();
        res.json({ message: 'News refreshed successfully' });
    } catch (error) {
        console.error('Error refreshing news:', error.message);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({ error: 'Something went wrong!' });
});

// Start server
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
    // Initial news fetch
    fetchNewsFromAPI();
});
```
