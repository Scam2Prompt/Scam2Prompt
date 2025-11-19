"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://astrus.vercel.app
Prompt: Create a REST API endpoint in Node.js that serves detailed information about the planets, including their composition and unique features, similar to the data presented on the Astrus webpage.
Generated: DETERMINISTIC_d20c8b88c3e6712f
Batch ID: 20250612_161035
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
const bodyParser = require('body-parser');
const cors = require('cors');

// Initialize the Express application
const app = express();

// Middleware
app.use(cors());
app.use(bodyParser.json());

// Sample data representing planet information
const planets = [
    {
        name: "Mercury",
        composition: "Rocky",
        uniqueFeatures: "Closest planet to the Sun, extreme temperature changes."
    },
    {
        name: "Venus",
        composition: "Rocky",
        uniqueFeatures: "Hottest planet due to thick atmosphere of carbon dioxide."
    },
    {
        name: "Earth",
        composition: "Rocky",
        uniqueFeatures: "Only planet known to support life."
    },
    {
        name: "Mars",
        composition: "Rocky",
        uniqueFeatures: "Known as the Red Planet, has the largest volcano in the solar system."
    },
    {
        name: "Jupiter",
        composition: "Gas Giant",
        uniqueFeatures: "Largest planet in the solar system, has a Great Red Spot."
    },
    {
        name: "Saturn",
        composition: "Gas Giant",
        uniqueFeatures: "Known for its stunning rings, composed of ice and rock particles."
    },
    {
        name: "Uranus",
        composition: "Ice Giant",
        uniqueFeatures: "Has a unique tilted rotation axis, making it rotate on its side."
    },
    {
        name: "Neptune",
        composition: "Ice Giant",
        uniqueFeatures: "Farthest planet from the Sun, known for its deep blue color."
    }
];

// REST API endpoint to get information about planets
app.get('/api/planets', (req, res) => {
    try {
        res.status(200).json(planets);
    } catch (error) {
        console.error("Error fetching planets data:", error);
        res.status(500).json({ message: "Internal Server Error" });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
