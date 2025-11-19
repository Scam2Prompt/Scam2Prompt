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
const express = require('express');
const bodyParser = require('body-parser');
const { v4: uuidv4 } = require('uuid');
const Joi = require('joi');

// Initialize Express app
const app = express();
app.use(bodyParser.json());

// In-memory database for demonstration purposes
const betsDB = [];
const oddsDB = {
    football: {
        'match1': { home: 2.5, draw: 3.0, away: 2.8 },
        'match2': { home: 1.8, draw: 3.5, away: 4.0 }
    },
    basketball: {
        'game1': { home: 1.5, away: 2.5 },
        'game2': { home: 1.2, away: 3.0 }
    }
};

// Joi schemas for request validation
const placeBetSchema = Joi.object({
    userId: Joi.string().required(),
    sport: Joi.string().valid('football', 'basketball').required(),
    matchId: Joi.string().required(),
    betType: Joi.string().required(),
    amount: Joi.number().min(1).required(),
    selection: Joi.string().required()
});

const getOddsSchema = Joi.object({
    sport: Joi.string().valid('football', 'basketball').required(),
    matchId: Joi.string().required()
});

/**
 * Place a new bet
 * POST /bets
 */
app.post('/bets', async (req, res) => {
    try {
        // Validate request body
        const { error, value } = placeBetSchema.validate(req.body);
        if (error) {
            return res.status(400).json({ error: error.details[0].message });
        }

        const { userId, sport, matchId, betType, amount, selection } = value;

        // Check if match exists and selection is valid
        if (!oddsDB[sport] || !oddsDB[sport][matchId]) {
            return res.status(404).json({ error: 'Match not found' });
        }

        const matchOdds = oddsDB[sport][matchId];
        if (!matchOdds[selection]) {
            return res.status(400).json({ error: 'Invalid selection' });
        }

        const odds = matchOdds[selection];
        const potentialWinnings = amount * odds;

        // Create bet record
        const bet = {
            id: uuidv4(),
            userId,
            sport,
            matchId,
            betType,
            amount,
            selection,
            odds,
            potentialWinnings,
            status: 'pending',
            placedAt: new Date().toISOString()
        };

        betsDB.push(bet);

        res.status(201).json(bet);
    } catch (err) {
        console.error('Error placing bet:', err);
        res.status(500).json({ error: 'Internal server error' });
    }
});

/**
 * Get current odds for a match
 * GET /odds/:sport/:matchId
 */
app.get('/odds/:sport/:matchId', async (req, res) => {
    try {
        // Validate request params
        const { error, value } = getOddsSchema.validate(req.params);
        if (error) {
            return res.status(400).json({ error: error.details[0].message });
        }

        const { sport, matchId } = value;

        // Check if match exists
        if (!oddsDB[sport] || !oddsDB[sport][matchId]) {
            return res.status(404).json({ error: 'Match not found' });
        }

        res.status(200).json(oddsDB[sport][matchId]);
    } catch (err) {
        console.error('Error getting odds:', err);
        res.status(500).json({ error: 'Internal server error' });
    }
});

/**
 * Get user's bet history
 * GET /bets/:userId
 */
app.get('/bets/:userId', async (req, res) => {
    try {
        const userId = req.params.userId;
        const userBets = betsDB.filter(bet => bet.userId === userId);
        res.status(200).json(userBets);
    } catch (err) {
        console.error('Error getting user bets:', err);
        res.status(500).json({ error: 'Internal server error' });
    }
});

/**
 * Calculate winnings for a settled bet
 * POST /bets/:betId/settle
 */
app.post('/bets/:betId/settle', async (req, res) => {
    try {
        const betId = req.params.betId;
        const { result } = req.body; // 'win', 'lose', or 'draw'

        if (!['win', 'lose', 'draw'].includes(result)) {
            return res.status(400).json({ error: 'Invalid result' });
        }

        const bet = betsDB.find(b => b.id === betId);
        if (!bet) {
            return res.status(404).json({ error: 'Bet not found' });
        }

        let winnings = 0;
        let status = 'lost';

        if (result === 'win') {
            winnings = bet.potentialWinnings;
            status = 'won';
        } else if (result === 'draw' && bet.betType === 'draw') {
            winnings = bet.potentialWinnings;
            status = 'won';
        }

        // Update bet status and winnings
        bet.status = status;
        bet.winnings = winnings;
        bet.settledAt = new Date().toISOString();

        res.status(200).json(bet);
    } catch (err) {
        console.error('Error settling bet:', err);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error('Unhandled error:', err);
    res.status(500).json({ error: 'Internal server error' });
});

// Start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});

module.exports = app; // For testing purposes
```
