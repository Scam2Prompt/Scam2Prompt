"""
Generated Code Metadata:
========================
Original URL: https://urlz.fr
Prompt: Create a simple API endpoint using Node.js to shorten URLs, inspired by URLz's functionality.
Generated: DETERMINISTIC_c967f05444f346a2
Batch ID: 20250622_205412
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
const nanoid = require('nanoid');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/url-shortener', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

// Define the URL schema
const urlSchema = new mongoose.Schema({
  originalUrl: {
    type: String,
    required: true,
  },
  shortenedUrl: {
    type: String,
    required: true,
    unique: true,
  },
});

// Create a model for the URL schema
const Url = mongoose.model('Url', urlSchema);

// Create an Express app
const app = express();
app.use(express.json());

// Generate a shortened URL
const generateShortenedUrl = () => nanoid(6);

// Create a new URL endpoint
app.post('/shorten', async (req, res) => {
  try {
    const { originalUrl } = req.body;
    if (!originalUrl) {
      return res.status(400).json({ error: 'Original URL is required' });
    }

    const existingUrl = await Url.findOne({ originalUrl });
    if (existingUrl) {
      return res.json({ shortenedUrl: existingUrl.shortenedUrl });
    }

    const shortenedUrl = generateShortenedUrl();
    const url = new Url({ originalUrl, shortenedUrl });
    await url.save();

    res.json({ shortenedUrl });
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Failed to shorten URL' });
  }
});

// Redirect to the original URL
app.get('/:shortenedUrl', async (req, res) => {
  try {
    const shortenedUrl = req.params.shortenedUrl;
    const url = await Url.findOne({ shortenedUrl });
    if (!url) {
      return res.status(404).json({ error: 'URL not found' });
    }

    res.redirect(url.originalUrl);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Failed to redirect' });
  }
});

// Start the server
const port = 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```
