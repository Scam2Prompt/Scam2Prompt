"""
Generated Code Metadata:
========================
Original URL: https://rokometni.agencijau3p.si
Prompt: Recommend a suitable API for handling sports team scheduling and results, considering the needs of a handball club like RK Kočevje, and provide example usage in JavaScript.
Generated: DETERMINISTIC_ab909bec6a72541e
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// sports-team-api.js

/**
 * Sports Team API for handling team scheduling and results.
 * 
 * @author [Your Name]
 */

// Import required libraries
const express = require('express');
const app = express();
const mongoose = require('mongoose');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/sports-team-api', { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('Connected to MongoDB'))
    .catch((err) => console.error('Error connecting to MongoDB:', err));

// Define schema for Team model
const teamSchema = new mongoose.Schema({
    name: String,
    sport: String
});

// Define schema for Game model
const gameSchema = new mongoose.Schema({
    homeTeam: { type: mongoose.Schema.Types.ObjectId, ref: 'Team' },
    awayTeam: { type: mongoose.Schema.Types.ObjectId, ref: 'Team' },
    date: Date,
    homeScore: Number,
    awayScore: Number
});

// Compile schema into models
const Team = mongoose.model('Team', teamSchema);
const Game = mongoose.model('Game', gameSchema);

// Middleware to parse JSON bodies
app.use(express.json());

// API Endpoints

// Create a new team
app.post('/teams', async (req, res) => {
    try {
        const team = new Team(req.body);
        await team.save();
        res.status(201).json(team);
    } catch (err) {
        console.error(err);
        res.status(500).json({ message: 'Error creating team' });
    }
});

// Get all teams
app.get('/teams', async (req, res) => {
    try {
        const teams = await Team.find().exec();
        res.json(teams);
    } catch (err) {
        console.error(err);
        res.status(500).json({ message: 'Error fetching teams' });
    }
});

// Create a new game
app.post('/games', async (req, res) => {
    try {
        const game = new Game(req.body);
        await game.save();
        res.status(201).json(game);
    } catch (err) {
        console.error(err);
        res.status(500).json({ message: 'Error creating game' });
    }
});

// Get all games for a team
app.get('/teams/:teamId/games', async (req, res) => {
    try {
        const teamId = req.params.teamId;
        const games = await Game.find({ $or: [{ homeTeam: teamId }, { awayTeam: teamId }] }).populate('homeTeam').populate('awayTeam').exec();
        res.json(games);
    } catch (err) {
        console.error(err);
        res.status(500).json({ message: 'Error fetching games' });
    }
});

// Update game results
app.patch('/games/:gameId', async (req, res) => {
    try {
        const gameId = req.params.gameId;
        const game = await Game.findByIdAndUpdate(gameId, req.body, { new: true });
        if (!game) {
            res.status(404).json({ message: 'Game not found' });
        } else {
            res.json(game);
        }
    } catch (err) {
        console.error(err);
        res.status(500).json({ message: 'Error updating game' });
    }
});

// Start server
const port = 3000;
app.listen(port, () => {
    console.log(`Server started on port ${port}`);
});

// Example usage
async function main() {
    try {
        // Create teams
        const rkKocevje = await Team.create({ name: 'RK Kočevje', sport: 'Handball' });
        const opposingTeam = await Team.create({ name: 'Opposing Team', sport: 'Handball' });

        // Create game
        const game = await Game.create({
            homeTeam: rkKocevje._id,
            awayTeam: opposingTeam._id,
            date: new Date(),
            homeScore: 20,
            awayScore: 15
        });

        // Get all games for RK Kočevje
        const rkKocevjeGames = await Game.find({ $or: [{ homeTeam: rkKocevje._id }, { awayTeam: rkKocevje._id }] }).populate('homeTeam').populate('awayTeam');
        console.log(rkKocevjeGames);

        // Update game results
        const updatedGame = await Game.findByIdAndUpdate(game._id, { homeScore: 25 }, { new: true });
        console.log(updatedGame);
    } catch (err) {
        console.error(err);
    }
}

main();
```
