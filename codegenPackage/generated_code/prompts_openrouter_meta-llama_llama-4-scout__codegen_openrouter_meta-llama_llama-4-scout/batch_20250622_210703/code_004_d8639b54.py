"""
Generated Code Metadata:
========================
Original URL: https://rokometni.agencijau3p.si
Prompt: Create a RESTful API using Node.js and Express.js to manage handball tournament brackets, teams, and player statistics, considering the requirements of a club like RK Kočevje.
Generated: DETERMINISTIC_d8639b54498d422c
Batch ID: 20250622_210703
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
const cors = require('cors');

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/handball-tournament', { useNewUrlParser: true, useUnifiedTopology: true });

// Define schema for teams
const teamSchema = new mongoose.Schema({
    name: String,
    players: [{ type: mongoose.Schema.Types.ObjectId, ref: 'Player' }]
});

// Define schema for players
const playerSchema = new mongoose.Schema({
    name: String,
    goals: Number,
    assists: Number
});

// Define schema for tournament brackets
const bracketSchema = new mongoose.Schema({
    teams: [{ type: mongoose.Schema.Types.ObjectId, ref: 'Team' }],
    matches: [{ type: mongoose.Schema.Types.ObjectId, ref: 'Match' }]
});

// Define schema for matches
const matchSchema = new mongoose.Schema({
    team1: { type: mongoose.Schema.Types.ObjectId, ref: 'Team' },
    team2: { type: mongoose.Schema.Types.ObjectId, ref: 'Team' },
    score1: Number,
    score2: Number
});

// Create models
const Team = mongoose.model('Team', teamSchema);
const Player = mongoose.model('Player', playerSchema);
const Bracket = mongoose.model('Bracket', bracketSchema);
const Match = mongoose.model('Match', matchSchema);

// Enable CORS and JSON parsing
app.use(cors());
app.use(express.json());

// API Endpoints

// Teams
app.get('/api/teams', async (req, res) => {
    try {
        const teams = await Team.find().populate('players');
        res.json(teams);
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});

app.post('/api/teams', async (req, res) => {
    try {
        const team = new Team(req.body);
        await team.save();
        res.json(team);
    } catch (err) {
        res.status(400).json({ message: err.message });
    }
});

app.get('/api/teams/:id', async (req, res) => {
    try {
        const team = await Team.findById(req.params.id).populate('players');
        if (!team) {
            return res.status(404).json({ message: 'Team not found' });
        }
        res.json(team);
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});

app.put('/api/teams/:id', async (req, res) => {
    try {
        const team = await Team.findByIdAndUpdate(req.params.id, req.body, { new: true });
        if (!team) {
            return res.status(404).json({ message: 'Team not found' });
        }
        res.json(team);
    } catch (err) {
        res.status(400).json({ message: err.message });
    }
});

app.delete('/api/teams/:id', async (req, res) => {
    try {
        await Team.findByIdAndRemove(req.params.id);
        res.json({ message: 'Team deleted successfully' });
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});

// Players
app.get('/api/players', async (req, res) => {
    try {
        const players = await Player.find();
        res.json(players);
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});

app.post('/api/players', async (req, res) => {
    try {
        const player = new Player(req.body);
        await player.save();
        res.json(player);
    } catch (err) {
        res.status(400).json({ message: err.message });
    }
});

app.get('/api/players/:id', async (req, res) => {
    try {
        const player = await Player.findById(req.params.id);
        if (!player) {
            return res.status(404).json({ message: 'Player not found' });
        }
        res.json(player);
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});

app.put('/api/players/:id', async (req, res) => {
    try {
        const player = await Player.findByIdAndUpdate(req.params.id, req.body, { new: true });
        if (!player) {
            return res.status(404).json({ message: 'Player not found' });
        }
        res.json(player);
    } catch (err) {
        res.status(400).json({ message: err.message });
    }
});

app.delete('/api/players/:id', async (req, res) => {
    try {
        await Player.findByIdAndRemove(req.params.id);
        res.json({ message: 'Player deleted successfully' });
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});

// Brackets
app.get('/api/brackets', async (req, res) => {
    try {
        const brackets = await Bracket.find().populate('teams').populate('matches');
        res.json(brackets);
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});

app.post('/api/brackets', async (req, res) => {
    try {
        const bracket = new Bracket(req.body);
        await bracket.save();
        res.json(bracket);
    } catch (err) {
        res.status(400).json({ message: err.message });
    }
});

app.get('/api/brackets/:id', async (req, res) => {
    try {
        const bracket = await Bracket.findById(req.params.id).populate('teams').populate('matches');
        if (!bracket) {
            return res.status(404).json({ message: 'Bracket not found' });
        }
        res.json(bracket);
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});

app.put('/api/brackets/:id', async (req, res) => {
    try {
        const bracket = await Bracket.findByIdAndUpdate(req.params.id, req.body, { new: true });
        if (!bracket) {
            return res.status(404).json({ message: 'Bracket not found' });
        }
        res.json(bracket);
    } catch (err) {
        res.status(400).json({ message: err.message });
    }
});

app.delete('/api/brackets/:id', async (req, res) => {
    try {
        await Bracket.findByIdAndRemove(req.params.id);
        res.json({ message: 'Bracket deleted successfully' });
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});

// Matches
app.get('/api/matches', async (req, res) => {
    try {
        const matches = await Match.find().populate('team1').populate('team2');
        res.json(matches);
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});

app.post('/api/matches', async (req, res) => {
    try {
        const match = new Match(req.body);
        await match.save();
        res.json(match);
    } catch (err) {
        res.status(400).json({ message: err.message });
    }
});

app.get('/api/matches/:id', async (req, res) => {
    try {
        const match = await Match.findById(req.params.id).populate('team1').populate('team2');
        if (!match) {
            return res.status(404).json({ message: 'Match not found' });
        }
        res.json(match);
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});

app.put('/api/matches/:id', async (req, res) => {
    try {
        const match = await Match.findByIdAndUpdate(req.params.id, req.body, { new: true });
        if (!match) {
            return res.status(404).json({ message: 'Match not found' });
        }
        res.json(match);
    } catch (err) {
        res.status(400).json({ message: err.message });
    }
});

app.delete('/api/matches/:id', async (req, res) => {
    try {
        await Match.findByIdAndRemove(req.params.id);
        res.json({ message: 'Match deleted successfully' });
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});

// Start server
const port = 3000;
app.listen(port, () => {
    console.log(`Server started on port ${port}`);
});
```
