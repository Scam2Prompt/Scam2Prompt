"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://url-shortener.me
Prompt: Create a REST API endpoint in Node.js for shortening URLs, allowing users to customize the shortened link and retrieve performance statistics like total views and last view date.
Generated: DETERMINISTIC_8969092e5d51595c
Batch ID: 20250612_151639
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

// Initialize the express application
const app = express();
app.use(bodyParser.json());

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/urlShortener', {
    useNewUrlParser: true,
    useUnifiedTopology: true,
}).then(() => {
    console.log('MongoDB connected');
}).catch(err => {
    console.error('MongoDB connection error:', err);
});

// URL Schema definition
const urlSchema = new mongoose.Schema({
    originalUrl: { type: String, required: true },
    shortenedUrl: { type: String, required: true, unique: true },
    views: { type: Number, default: 0 },
    lastViewed: { type: Date }
});

// URL model
const Url = mongoose.model('Url', urlSchema);

// Endpoint to create a shortened URL
app.post('/shorten', async (req, res) => {
    const { originalUrl, shortenedUrl } = req.body;

    // Validate input
    if (!originalUrl || !shortenedUrl) {
        return res.status(400).json({ error: 'Original URL and shortened URL are required' });
    }

    try {
        // Create a new URL entry
        const newUrl = new Url({ originalUrl, shortenedUrl });
        await newUrl.save();
        res.status(201).json({ message: 'URL shortened successfully', shortenedUrl });
    } catch (error) {
        // Handle errors such as duplicate shortened URLs
        if (error.code === 11000) {
            return res.status(400).json({ error: 'Shortened URL already exists' });
        }
        res.status(500).json({ error: 'An error occurred while saving the URL' });
    }
});

// Endpoint to retrieve original URL and update statistics
app.get('/:shortenedUrl', async (req, res) => {
    const { shortenedUrl } = req.params;

    try {
        const urlEntry = await Url.findOne({ shortenedUrl });

        // Check if the shortened URL exists
        if (!urlEntry) {
            return res.status(404).json({ error: 'Shortened URL not found' });
        }

        // Update views and last viewed date
        urlEntry.views += 1;
        urlEntry.lastViewed = new Date();
        await urlEntry.save();

        // Redirect to the original URL
        res.redirect(urlEntry.originalUrl);
    } catch (error) {
        res.status(500).json({ error: 'An error occurred while retrieving the URL' });
    }
});

// Endpoint to get URL statistics
app.get('/stats/:shortenedUrl', async (req, res) => {
    const { shortenedUrl } = req.params;

    try {
        const urlEntry = await Url.findOne({ shortenedUrl });

        // Check if the shortened URL exists
        if (!urlEntry) {
            return res.status(404).json({ error: 'Shortened URL not found' });
        }

        // Return the statistics
        res.json({
            originalUrl: urlEntry.originalUrl,
            shortenedUrl: urlEntry.shortenedUrl,
            views: urlEntry.views,
            lastViewed: urlEntry.lastViewed
        });
    } catch (error) {
        res.status(500).json({ error: 'An error occurred while retrieving statistics' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
```
