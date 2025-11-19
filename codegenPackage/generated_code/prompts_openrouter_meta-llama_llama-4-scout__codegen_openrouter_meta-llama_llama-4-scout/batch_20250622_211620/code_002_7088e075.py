"""
Generated Code Metadata:
========================
Original URL: https://jadobet.org
Prompt: Generate a RESTful API endpoint in Node.js for handling sports betting transactions, including placing bets, retrieving odds, and calculating winnings, inspired by BaxBet's sports betting section.
Generated: DETERMINISTIC_7088e0755194653b
Batch ID: 20250622_211620
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
const app = express();
const mongoose = require('mongoose');
const { validate } = require('joi');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/baxbet', { useNewUrlParser: true, useUnifiedTopology: true });

// Define schema for bets
const betSchema = new mongoose.Schema({
    userId: { type: String, required: true },
    sport: { type: String, required: true },
    event: { type: String, required: true },
    betType: { type: String, required: true },
    stake: { type: Number, required: true },
    odds: { type: Number, required: true },
    status: { type: String, default: 'pending' },
    winnings: { type: Number, default: 0 },
});

// Define schema for odds
const oddsSchema = new mongoose.Schema({
    sport: { type: String, required: true },
    event: { type: String, required: true },
    betType: { type: String, required: true },
    odds: { type: Number, required: true },
});

// Create models
const Bet = mongoose.model('Bet', betSchema);
const Odds = mongoose.model('Odds', oddsSchema);

// Define Joi schema for validating requests
const betSchemaValidation = Joi.object({
    userId: Joi.string().required(),
    sport: Joi.string().required(),
    event: Joi.string().required(),
    betType: Joi.string().required(),
    stake: Joi.number().required(),
    odds: Joi.number().required(),
});

const oddsSchemaValidation = Joi.object({
    sport: Joi.string().required(),
    event: Joi.string().required(),
    betType: Joi.string().required(),
    odds: Joi.number().required(),
});

// Middleware to parse JSON bodies
app.use(express.json());

// Endpoint to place a bet
app.post('/bets', async (req, res) => {
    try {
        // Validate request body
        const { error } = validate(req.body, betSchemaValidation);
        if (error) {
            return res.status(400).send({ message: 'Invalid request data', error });
        }

        // Check if odds exist for the event
        const odds = await Odds.findOne({ sport: req.body.sport, event: req.body.event, betType: req.body.betType });
        if (!odds) {
            return res.status(404).send({ message: 'Odds not found for this event' });
        }

        // Create a new bet
        const bet = new Bet(req.body);
        await bet.save();

        res.send({ message: 'Bet placed successfully', bet });
    } catch (error) {
        console.error(error);
        res.status(500).send({ message: 'Internal Server Error' });
    }
});

// Endpoint to retrieve odds for an event
app.get('/odds/:sport/:event/:betType', async (req, res) => {
    try {
        const odds = await Odds.findOne({ sport: req.params.sport, event: req.params.event, betType: req.params.betType });
        if (!odds) {
            return res.status(404).send({ message: 'Odds not found for this event' });
        }
        res.send({ odds: odds.odds });
    } catch (error) {
        console.error(error);
        res.status(500).send({ message: 'Internal Server Error' });
    }
});

// Endpoint to calculate winnings for a bet
app.patch('/bets/:id/calculate-winnings', async (req, res) => {
    try {
        const bet = await Bet.findById(req.params.id);
        if (!bet) {
            return res.status(404).send({ message: 'Bet not found' });
        }

        // Calculate winnings
        const winnings = bet.stake * bet.odds;
        bet.winnings = winnings;
        bet.status = 'settled';
        await bet.save();

        res.send({ message: 'Winnings calculated successfully', winnings });
    } catch (error) {
        console.error(error);
        res.status(500).send({ message: 'Internal Server Error' });
    }
});

// Endpoint to create/update odds
app.post('/odds', async (req, res) => {
    try {
        // Validate request body
        const { error } = validate(req.body, oddsSchemaValidation);
        if (error) {
            return res.status(400).send({ message: 'Invalid request data', error });
        }

        // Check if odds already exist for the event
        const existingOdds = await Odds.findOne({ sport: req.body.sport, event: req.body.event, betType: req.body.betType });
        if (existingOdds) {
            existingOdds.odds = req.body.odds;
            await existingOdds.save();
            return res.send({ message: 'Odds updated successfully', odds: existingOdds });
        }

        // Create new odds
        const odds = new Odds(req.body);
        await odds.save();

        res.send({ message: 'Odds created successfully', odds });
    } catch (error) {
        console.error(error);
        res.status(500).send({ message: 'Internal Server Error' });
    }
});

// Start server
const port = 3000;
app.listen(port, () => {
    console.log(`Server started on port ${port}`);
});
```
