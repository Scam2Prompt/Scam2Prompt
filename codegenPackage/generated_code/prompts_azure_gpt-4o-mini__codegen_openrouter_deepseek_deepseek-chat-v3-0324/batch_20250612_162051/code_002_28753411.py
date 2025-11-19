"""
Generated Code Metadata:
========================
Original URL: https://danieldefilippi.com
Prompt: Create an API endpoint in Node.js that serves information about Daniel Defilippi's exhibitions and artworks, emphasizing the idea of fragmented life paths.
Generated: DETERMINISTIC_287534117f37065f
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(bodyParser.json());

// Sample data for Daniel Defilippi's exhibitions and artworks
const exhibitionsData = [
    {
        id: 1,
        title: "Fragmented Memories",
        year: 2018,
        description: "An exploration of disjointed personal histories through mixed media installations.",
        location: "Modern Art Gallery, New York",
        fragments: [
            "Broken mirror series",
            "Fragmented timeline projection",
            "Scattered memory objects"
        ]
    },
    {
        id: 2,
        title: "Paths Not Taken",
        year: 2020,
        description: "Interactive exhibit showcasing parallel life possibilities through digital interfaces.",
        location: "Contemporary Arts Center, Berlin",
        fragments: [
            "Digital decision trees",
            "Alternative life projections",
            "Interactive path selection"
        ]
    }
];

const artworksData = [
    {
        id: 1,
        title: "Shattered Journey",
        year: 2017,
        medium: "Mixed media on canvas",
        description: "A visual representation of life's unpredictable turns and fractures.",
        fragments: 12,
        exhibitionId: 1
    },
    {
        id: 2,
        title: "Parallel Shadows",
        year: 2019,
        medium: "Digital projection",
        description: "Interactive artwork showing simultaneous life possibilities as shadow projections.",
        fragments: 8,
        exhibitionId: 2
    }
];

// API Endpoints

/**
 * GET /api/exhibitions
 * Returns all exhibitions
 */
app.get('/api/exhibitions', (req, res) => {
    try {
        res.status(200).json(exhibitionsData);
    } catch (error) {
        console.error('Error fetching exhibitions:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

/**
 * GET /api/exhibitions/:id
 * Returns a specific exhibition by ID
 */
app.get('/api/exhibitions/:id', (req, res) => {
    try {
        const id = parseInt(req.params.id);
        const exhibition = exhibitionsData.find(e => e.id === id);
        
        if (!exhibition) {
            return res.status(404).json({ error: 'Exhibition not found' });
        }
        
        res.status(200).json(exhibition);
    } catch (error) {
        console.error('Error fetching exhibition:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

/**
 * GET /api/artworks
 * Returns all artworks
 */
app.get('/api/artworks', (req, res) => {
    try {
        res.status(200).json(artworksData);
    } catch (error) {
        console.error('Error fetching artworks:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

/**
 * GET /api/artworks/:id
 * Returns a specific artwork by ID
 */
app.get('/api/artworks/:id', (req, res) => {
    try {
        const id = parseInt(req.params.id);
        const artwork = artworksData.find(a => a.id === id);
        
        if (!artwork) {
            return res.status(404).json({ error: 'Artwork not found' });
        }
        
        res.status(200).json(artwork);
    } catch (error) {
        console.error('Error fetching artwork:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

/**
 * GET /api/exhibitions/:id/artworks
 * Returns all artworks for a specific exhibition
 */
app.get('/api/exhibitions/:id/artworks', (req, res) => {
    try {
        const id = parseInt(req.params.id);
        const exhibitionArtworks = artworksData.filter(a => a.exhibitionId === id);
        
        if (exhibitionArtworks.length === 0) {
            return res.status(404).json({ error: 'No artworks found for this exhibition' });
        }
        
        res.status(200).json(exhibitionArtworks);
    } catch (error) {
        console.error('Error fetching exhibition artworks:', error);
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
});

module.exports = app; // For testing purposes
```
