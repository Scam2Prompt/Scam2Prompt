"""
Generated Code Metadata:
========================
Original URL: https://vatangame.games
Prompt: Generate a RESTful API endpoint in Node.js for handling sports betting transactions, including placing bets, retrieving odds, and calculating winnings, inspired by BaxBet's sports betting section.
Generated: DETERMINISTIC_7088e0755194653b
Batch ID: 20250622_211740
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
const bodyParser = require('body-parser');
const { v4: uuidv4 } = require('uuid');

// Initialize the Express application
const app = express();
app.use(bodyParser.json());

// In-memory data storage for bets and odds (for demonstration purposes)
let odds = {
    'football': { 'teamA': 1.5, 'teamB': 2.5 },
    'basketball': { 'teamC': 1.8, 'teamD': 2.0 }
};

let bets = [];

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({ error: 'Something went wrong!' });
});

// Endpoint to retrieve odds
app.get('/api/odds', (req, res) => {
    res.json(odds);
});

// Endpoint to place a bet
app.post('/api/bets', (req, res) => {
    const { sport, team, amount } = req.body;

    // Validate input
    if (!sport || !team || !amount || typeof amount !== 'number') {
        return res.status(400).json({ error: 'Invalid input. Please provide sport, team, and amount.' });
    }

    // Check if the sport and team exist in the odds
    if (!odds[sport] || !odds[sport][team]) {
        return res.status(404).json({ error: 'Sport or team not found.' });
    }

    // Create a new bet
    const bet = {
        id: uuidv4(),
        sport,
        team,
        amount,
        odds: odds[sport][team],
        potentialWinnings: amount * odds[sport][team]
    };

    bets.push(bet);
    res.status(201).json(bet);
});

// Endpoint to calculate winnings
app.post('/api/calculate-winnings', (req, res) => {
    const { betId } = req.body;

    // Validate input
    if (!betId) {
        return res.status(400).json({ error: 'Bet ID is required.' });
    }

    // Find the bet
    const bet = bets.find(b => b.id === betId);
    if (!bet) {
        return res.status(404).json({ error: 'Bet not found.' });
    }

    // Return the potential winnings
    res.json({ betId: bet.id, potentialWinnings: bet.potentialWinnings });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
