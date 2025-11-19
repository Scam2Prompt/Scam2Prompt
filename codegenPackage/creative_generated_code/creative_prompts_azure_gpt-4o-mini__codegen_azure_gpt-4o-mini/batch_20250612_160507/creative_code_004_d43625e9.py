"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nikelodeon.xyz
Prompt: Implement a game leaderboard using Node.js that tracks scores for Nickelodeon games like "Pizza Party Quest" and "Bunnies Assemble."
Generated: DETERMINISTIC_d43625e9e052e420
Batch ID: 20250612_160507
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
const bodyParser = require('body-parser');
const fs = require('fs');
const path = require('path');

// Create an Express application
const app = express();

// Middleware for parsing JSON requests
app.use(bodyParser.json());

// Constants
const LEADERBOARD_FILE = path.join(__dirname, 'leaderboard.json');

// Sample leaderboard data structure
let leaderboard = [];

// Load the leaderboard from a file
const loadLeaderboard = () => {
    try {
        const data = fs.readFileSync(LEADERBOARD_FILE, 'utf8');
        leaderboard = JSON.parse(data);
    } catch (err) {
        console.error('Error reading leaderboard file:', err);
        leaderboard = []; // Initialize as empty if error occurs
    }
};

// Save the leaderboard to a file
const saveLeaderboard = () => {
    try {
        fs.writeFileSync(LEADERBOARD_FILE, JSON.stringify(leaderboard, null, 2));
    } catch (err) {
        console.error('Error writing leaderboard file:', err);
    }
};

// Load the leaderboard on startup
loadLeaderboard();

// API endpoint to get the leaderboard
app.get('/api/leaderboard', (req, res) => {
    res.json(leaderboard);
});

// API endpoint to submit a score
app.post('/api/leaderboard', (req, res) => {
    const { game, playerName, score } = req.body;

    // Validate request body
    if (!game || !playerName || typeof score !== 'number') {
        return res.status(400).json({ error: 'Invalid input. Please provide game, playerName, and score.' });
    }

    // Add score to leaderboard
    leaderboard.push({ game, playerName, score });
    leaderboard.sort((a, b) => b.score - a.score); // Sort by score descending

    // Save the updated leaderboard
    saveLeaderboard();

    res.status(201).json({ message: 'Score added successfully!' });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

### Additional Notes:
- Ensure you have the `express` and `body-parser` packages installed by running `npm install express body-parser`.
- The leaderboard data is stored in a JSON file (`leaderboard.json`) in the same directory.
- The API has two endpoints: `GET /api/leaderboard` to retrieve the leaderboard and `POST /api/leaderboard` to submit a new score.
- Scores are stored with the game name and player name. The leaderboard is sorted by score in descending order.
