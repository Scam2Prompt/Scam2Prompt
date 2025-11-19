"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://danieldefilippi.com
Prompt: Create an API endpoint in Node.js that serves information about Daniel Defilippi's exhibitions and artworks, emphasizing the idea of fragmented life paths.
Generated: DETERMINISTIC_287534117f37065f
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules
const express = require('express');
const cors = require('cors');

// Create an instance of the Express application
const app = express();

// Use middleware
app.use(cors());
app.use(express.json());

// Sample data representing exhibitions and artworks
const exhibitions = [
    {
        id: 1,
        title: 'Fragmented Paths',
        description: 'An exploration of fragmented life paths through various mediums.',
        date: '2023-09-15',
        artworks: [
            {
                id: 1,
                title: 'Echoes of Memory',
                medium: 'Mixed Media',
                year: 2021
            },
            {
                id: 2,
                title: 'Lost Connections',
                medium: 'Oil on Canvas',
                year: 2022
            }
        ]
    },
    {
        id: 2,
        title: 'Reflections of the Self',
        description: 'A series discussing identity and fragmentation.',
        date: '2022-05-20',
        artworks: [
            {
                id: 3,
                title: 'Shattered Mirrors',
                medium: 'Photography',
                year: 2020
            },
            {
                id: 4,
                title: 'The Unseen',
                medium: 'Sculpture',
                year: 2023
            }
        ]
    }
];

// API endpoint to get all exhibitions
app.get('/api/exhibitions', (req, res) => {
    try {
        res.status(200).json(exhibitions);
    } catch (error) {
        console.error('Error fetching exhibitions:', error);
        res.status(500).json({ message: 'Internal Server Error' });
    }
});

// API endpoint to get a specific exhibition by ID
app.get('/api/exhibitions/:id', (req, res) => {
    const exhibitionId = parseInt(req.params.id, 10);
    
    try {
        const exhibition = exhibitions.find(ex => ex.id === exhibitionId);
        
        if (!exhibition) {
            return res.status(404).json({ message: 'Exhibition not found' });
        }
        
        res.status(200).json(exhibition);
    } catch (error) {
        console.error('Error fetching exhibition:', error);
        res.status(500).json({ message: 'Internal Server Error' });
    }
});

// Define the port and start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});

// Export the app for testing purposes
module.exports = app;
```
