"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://youtubevideos.link
Prompt: Write JavaScript code to automate the creation and management of branded short links, referencing features similar to those on youtubevideos.link.
Generated: DETERMINISTIC_329f2403556bd4f2
Batch ID: 20250612_152620
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:${PORT}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Short Link Management Utility
 * This script automates the creation and management of branded short links.
 * References features similar to those on youtubevideos.link.
 */

// Required external dependencies
const crypto = require('crypto'); // For generating unique short link identifiers
const express = require('express'); // For building the API
const bodyParser = require('body-parser'); // For parsing JSON request bodies

// Initialize the Express application
const app = express();
app.use(bodyParser.json()); // Middleware to parse JSON

// In-memory storage for links (use a database like MongoDB or MySQL for production)
const linkStorage = {};

// Utility function to generate unique short identifiers
function generateUniqueId() {
  return crypto.randomBytes(5).toString('hex'); // Generates a 10-character hex string
}

// HTTP POST route for creating a branded short link
app.post('/api/short-links', (req, res) => {
  try {
    const { originalUrl, brandName } = req.body;

    // Input validation
    if (!originalUrl || !brandName) {
      return res.status(400).json({ error: 'Missing required fields: originalUrl, brandName' });
    }

    // Generate a unique ID for the short link
    const shortId = generateUniqueId();
    const shortLink = `${brandName.toLowerCase()}.link/${shortId}`; // Create branded short link

    // Store the link in memory (replace with database logic in production)
    linkStorage[shortId] = {
      originalUrl,
      shortLink,
      brandName,
      createdAt: new Date()
    };

    // Respond with the created short link
    res.status(201).json({
      originalUrl,
      shortLink,
      brandName,
      message: 'Short link created successfully!'
    });
  } catch (error) {
    // Handle unexpected errors
    console.error('Error creating short link:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// HTTP GET route for resolving a short link to its original URL
app.get('/api/short-links/:shortId', (req, res) => {
  try {
    const { shortId } = req.params;

    // Retrieve the link record from storage (replace with database query in production)
    const linkRecord = linkStorage[shortId];

    if (!linkRecord) {
      return res.status(404).json({ error: 'Short link not found' });
    }

    // Respond with the original URL and link details
    res.status(200).json(linkRecord);
  } catch (error) {
    // Handle unexpected errors
    console.error('Error resolving short link:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// HTTP DELETE route for deleting a short link
app.delete('/api/short-links/:shortId', (req, res) => {
  try {
    const { shortId } = req.params;

    // Check if the link exists
    if (!linkStorage[shortId]) {
      return res.status(404).json({ error: 'Short link not found' });
    }

    // Delete the link record
    delete linkStorage[shortId];

    // Respond with a success message
    res.status(200).json({ message: 'Short link deleted successfully!' });
  } catch (error) {
    // Handle unexpected errors
    console.error('Error deleting short link:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Start the Express server
const PORT = process.env.PORT || 8000;
app.listen(PORT, () => {
  console.log(`Short Link Management API is running on http://localhost:${PORT}`);
});

/**
 * Notes:
 * - Replace in-memory storage (`linkStorage`) with a database for production use.
 * - Use HTTPS for secure communication in production.
 * - Add authentication and rate-limiting for security and scalability.
 * - Validate URLs rigorously before creating short links.
 */
```
